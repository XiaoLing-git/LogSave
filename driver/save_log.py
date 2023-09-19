import os
import shutil
from datetime import datetime
from pathlib import Path
from typing import List

from .utils import assert_target_existed


class SaveLog:
    def __init__(self,
                 target_files: List[Path],
                 label: str,
                 name: str,
                 storage_path: Path):
        self.__target_files = target_files
        self.__assert_target_files_existed()

        self.__label = label
        self.__name = name
        self.__storage_path = self.__create_storage_folder(storage_path)

    def __build(self):
        for file in self.__target_files:
            shutil.move(str(file), str(self.__storage_path))

    @classmethod
    def run(cls,
            target_files: List[Path],
            label: str,
            name: str,
            storage_path: Path):
        _instance = cls(target_files, label, name, storage_path)
        _instance.__build()

    def __create_storage_folder(self, storage_path: Path) -> Path:
        _t = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = storage_path / f"{_t}_{self.__label}_{self.__name}"
        if not path.exists():
            os.makedirs(str(path))
        return path

    def __assert_target_files_existed(self):
        for p in self.__target_files:
            assert_target_existed(p)