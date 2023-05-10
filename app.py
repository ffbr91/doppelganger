#!/usr/bin/env python3

import sys
import os
import hashlib

from collections import defaultdict

from PySide6 import QtWidgets
from PySide6.QtWidgets import (QFileDialog, QInputDialog, QDialog, QDialogButtonBox, QListWidgetItem, QTreeWidgetItem,
                               QLineEdit, QAbstractItemView, QVBoxLayout, QListWidget, QLabel)
from PySide6.QtCore import (Qt, QRunnable, Signal, Slot, QThreadPool, QObject)

from ui.main_ui import Ui_MainWindow

class FileHasher():
    @staticmethod
    def sha256(file_path):
        """
        Return tuple of sha256sum and file path
        """

        def read_chunks(file_handle, chunk_size=4096):
            """
            Return chunk read from file handle
            """
            while True:
                chunk = file_handle.read(chunk_size)
                if not chunk:
                    return
                yield chunk

        #print(f'Hashing {file_path}...')
        with open(file_path, 'rb') as f:
            sha256 = hashlib.sha256()
            for chunk in read_chunks(f):
                sha256.update(chunk)

        return (sha256.hexdigest(), file_path)

class WorkerSignals(QObject):
    """
    Signals emitted by workers
    """
    result = Signal(tuple)
    finished = Signal()

class Worker(QRunnable):
    """
    Generic workers
    """

    def __init__(self, func, *args, **kwargs):
        """
        Setup a worker with a function and its args and kwargs
        """
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        """
        Execute function with args and kwargs and emit signals when done
        """
        result = self.func(*self.args, **self.kwargs)
        self.signals.result.emit(result)
        self.signals.finished.emit()

class RemoveSelectedDialog(QDialog):
    """
    Custom dialog to show list of files to be removed
    """
    def __init__(self, selected):
        super().__init__()

        self.setWindowTitle("Remove selected")

        self.selected = selected

        QBtn = QDialogButtonBox.Yes | QDialogButtonBox.No

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(QLabel('Are you sure you want to remove the following files?'))

        list_remove = QListWidget()
        for path in selected:
            list_remove.addItem(QListWidgetItem(path))

        list_remove.setSelectionMode(QAbstractItemView.NoSelection)

        self.layout.addWidget(list_remove)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def accept(self):
        """
        Remove files if 'Yes' was selected
        """
        for file_path in self.selected:
            os.remove(file_path)

        return super().accept()

    def reject(self) -> None:
        return super().reject()

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Setup MainWindow
        """
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.thread_pool = QThreadPool()

        self.hashes = {}
        self.hash_progress = 0

        self.candidates = []

        self.setWindowTitle('Doppelganger')

        self.button_path_add.clicked.connect(self.onButtonPathAddClicked)
        self.button_path_remove.clicked.connect(self.onButtonPathRemoveClicked)
        self.button_path_remove.setEnabled(False)
        self.list_paths.itemSelectionChanged.connect(self.onListPathsItemSelectionChanged)

        self.button_ext_add.clicked.connect(self.onButtonExtAddClicked)
        self.button_ext_remove.clicked.connect(self.onButtonExtRemoveClicked)
        self.button_ext_remove.setEnabled(False)
        self.list_extensions.itemSelectionChanged.connect(self.onListExtensionsItemSelectionChanged)

        self.button_find_duplicates.clicked.connect(self.onButtonFindDuplicatesClicked)

        self.tree_duplicates.itemSelectionChanged.connect(self.onTreeItemSelectionChanged)
        self.tree_duplicates.setSelectionMode(QAbstractItemView.ExtendedSelection)

        self.button_select_same.clicked.connect(self.onButtonSelectSameClicked)
        self.button_select_same.setEnabled(False)

        self.button_remove_selected.clicked.connect(self.onButtonRemoveSelectedClicked)
        self.button_remove_selected.setEnabled(False)

        self.progressbar_hashes.setVisible(False)

    def onButtonPathAddClicked(self):
        """
        Add selected path to list if not already exists
        """
        path_dialog = QFileDialog()
        path_dialog.setFileMode(QFileDialog.Directory)

        if path_dialog.exec():
            path = path_dialog.selectedFiles()[0]
            if not self.list_paths.findItems(path, Qt.MatchFlag.MatchExactly):
                self.list_paths.addItem(QListWidgetItem(path))

    def onButtonPathRemoveClicked(self):
        """
        Remove selected path from list
        """
        for item in self.list_paths.selectedItems():
            self.list_paths.takeItem(self.list_paths.row(item))

    def onListPathsItemSelectionChanged(self):
        """
        Enable/disable button_path_remove
        """
        self.button_path_remove.setEnabled(len(self.list_paths.selectedItems()) > 0)

    def onButtonExtRemoveClicked(self):
        """
        Remove selected extension from list
        """
        for item in self.list_extensions.selectedItems():
            self.list_extensions.takeItem(self.list_extensions.row(item))

    def onButtonExtAddClicked(self):
        """
        Add extension to list and possibly prepend a '.'
        """
        text, ok = QInputDialog().getText(self, 'Add file extension', 'Extension (.jpg, .mp4, ...)',
                                          QLineEdit.EchoMode.Normal, None)
        if ok and text:
            if not text.startswith('.'):
                text = f'.{text}'
            if not self.list_extensions.findItems(text, Qt.MatchFlag.MatchExactly):
                self.list_extensions.addItem(QListWidgetItem(text))

    def onListExtensionsItemSelectionChanged(self):
        """
        Enable/disable button_ext_remove
        """
        self.button_ext_remove.setEnabled(len(self.list_extensions.selectedItems()) > 0)

    def onButtonSelectSameClicked(self):
        """
        Select files with same parent directory
        """
        search_dir = os.path.dirname(self.tree_duplicates.selectedItems()[0].text(0))
        for i in range(self.tree_duplicates.topLevelItemCount()):
            for j in range(self.tree_duplicates.topLevelItem(i).childCount()):
                child_dir = os.path.dirname(self.tree_duplicates.topLevelItem(i).child(j).text(0))
                self.tree_duplicates.topLevelItem(i).child(j).setSelected(search_dir == child_dir)


    def onButtonRemoveSelectedClicked(self):
        """
        Remove selected files
        """
        selected = [item.text(0) for item in self.tree_duplicates.selectedItems()]
        if RemoveSelectedDialog(selected).exec():
            self.button_find_duplicates.click()

    def getCandidates(self):
        """
        Evaluate duplicate candidates
        """
        file_paths = []
        file_sizes = defaultdict(list)

        # Get all the file paths
        root_paths = [self.list_paths.item(x).text() for x in range(self.list_paths.count())]
        extensions = [self.list_extensions.item(x).text() for x in range(self.list_extensions.count())]

        for root_path in root_paths:
            for root, _, files in os.walk(root_path):
                for name in files:
                    if extensions:
                        if not os.path.splitext(name)[1].lower() in extensions.lower():
                            continue

                    file_path = os.path.join(root, name)
                    if os.path.islink(file_path):
                        continue

                    file_paths.append(file_path)

        # Filter out same paths
        file_paths = list(set(file_paths))

        # Setup a dictionary of { 'file_size': [ file_paths ] }
        for file_path in file_paths:
            size = os.path.getsize(file_path)
            if not size in file_sizes:
                file_sizes[size] = []
            file_sizes[size].append(file_path)

        # Filter out files with a unique file size
        for files in filter(lambda files: len(files) > 1, file_sizes.values()):
            self.candidates.extend(files)

    def onCandidatesReceived(self):
        """
        Callback when getCandidates returns
        """
        if not self.candidates:
            self.edit_possible_duplicates.setText('0')
            self.button_find_duplicates.setEnabled(True)
            self.progressbar_hashes.setVisible(False)
            return

        self.edit_possible_duplicates.setText(f'{len(self.candidates)}')

        # Setup threads for calculating each file hash
        for candidate in self.candidates:
            worker = Worker(FileHasher.sha256, candidate)
            worker.signals.result.connect(self.onFileHasherResult)
            self.thread_pool.start(worker)

    def onButtonFindDuplicatesClicked(self):
        # Reset UI
        self.button_find_duplicates.setEnabled(False)
        self.progressbar_hashes.setVisible(True)
        self.progressbar_hashes.setValue(0)
        self.edit_possible_duplicates.setText('')
        self.edit_num_duplicates.setText('')
        self.edit_size_duplicates.setText('')
        self.tree_duplicates.clear()

        # Reset variables
        self.candidates.clear()
        self.hashes.clear()
        self.hash_progress = 0

        # Search possible duplicates
        worker = Worker(self.getCandidates)
        worker.signals.finished.connect(self.onCandidatesReceived)
        self.thread_pool.start(worker)

    def onTreeItemSelectionChanged(self):
        """
        Show/hide button_remove_selected
        """
        num_selected = len(self.tree_duplicates.selectedItems())
        self.button_remove_selected.setEnabled(num_selected > 0)

        if num_selected == 0:
            self.button_select_same.setEnabled(False)
        elif num_selected == 1:
            basename = os.path.basename(os.path.dirname(self.tree_duplicates.selectedItems()[0].text(0)))
            self.button_select_same.setEnabled(basename != '')
        else:
            # Enable button_select_same when all files are in the same directory
            parent_dirs = []
            for item in self.tree_duplicates.selectedItems():
                parent_dirs.append(os.path.basename(os.path.dirname(item.text(0))))

            self.button_select_same.setEnabled(all(directory == parent_dirs[0] for directory in parent_dirs))

    def hashingDone(self):
        """
        Callback when all files have been hashed
        """
        self.button_find_duplicates.setEnabled(True)
        self.progressbar_hashes.setVisible(False)

        items = []

        number_of_duplicates = 0
        size_of_duplicates = 0

        # Fill QTreeWidget with duplicates
        for _, files in self.hashes.items():
            if len(files) == 1:
                continue

            file_name = os.path.basename(files[0])
            file_size_b = os.path.getsize(files[0])
            file_size_mb = file_size_b / 1000000

            number_of_duplicates = number_of_duplicates + 1
            size_of_duplicates = size_of_duplicates + file_size_mb

            file_item = QTreeWidgetItem([file_name, f'{file_size_mb: .1f} MB'])
            for file_path in files:
                path_item = QTreeWidgetItem([file_path, None])
                file_item.addChild(path_item)

            items.append(file_item)

        self.tree_duplicates.insertTopLevelItems(0, items)
        items = [self.tree_duplicates.topLevelItem(i) for i in range(self.tree_duplicates.topLevelItemCount())]
        for item in items:
            item.setExpanded(True)
        self.tree_duplicates.resizeColumnToContents(0)

        self.edit_num_duplicates.setText(f'{number_of_duplicates}')
        self.edit_size_duplicates.setText(f'{size_of_duplicates: .1f} MB')

    def onFileHasherResult(self, result):
        """
        Callback when file hash calculated
        """
        # Append hash and path to hashes dict
        file_hash, file_path = result
        if not file_hash in self.hashes:
            self.hashes[file_hash] = []

        self.hashes[file_hash].append(file_path)

        self.hash_progress = self.hash_progress + 1
        self.progressbar_hashes.setValue(int((self.hash_progress / len(self.candidates)) * 100))

        if self.hash_progress == len(self.candidates):
            # All files hashed
            self.hashingDone()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()