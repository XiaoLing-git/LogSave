from pathlib import Path
from typing import Union, List

from .model import Path_Is_Not_Folder_Error


class ListLogFiles:
    """
    显示指定路径下的文件名
    """

    def __init__(self, target_folder: Path):
        self.__path = target_folder
        self.__assert_path_is_folder()

    @property
    def path(self):
        return self.__path

    def get_all_log_files(self) -> Union[List[str], None]:
        result = []
        items = self.path.iterdir()
        for item in items:
            if item.is_file() and item.name.endswith("log"):
                result.append(item.name)
        if len(result) == 0:
            return None
        return result.copy()

    def get_all_sub_folders(self) -> Union[List[str], None]:
        result = []
        items = self.path.iterdir()
        for item in items:
            if item.is_dir():
                result.append(item.name)
        if len(result) == 0:
            return None
        return result.copy()

    def __assert_path_is_folder(self) -> None:
        if not self.__path.exists():
            raise Path_Is_Not_Folder_Error("目标路径不存在")
        if self.__path.is_file():
            raise Path_Is_Not_Folder_Error("目标路径不是文件夹")
