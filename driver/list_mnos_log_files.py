from datetime import datetime
from pathlib import Path

from .list_log_files import ListLogFiles
from .model import Path_Is_Not_Folder_Error


class ListMnosLogFiles(ListLogFiles):
    """
    获取当天Mnos文件中指定日期文件下的文件信息
    默认是获取当天日期文件信息
        instance= ListMnosLogFiles（）
    也可以指定日期
        instance= ListMnosLogFiles（_date="2023-09-05"）
    获取所有日志名，若不存在返回None
        instance.get_all_log_files()
    获取已保存的所有文件夹名，若不存在返回None
        instance.get_all_sub_folders()
    """

    def __init__(self,
                 target_folder: Path = Path(r"/var/log/MnOS"),
                 _date: str = None):
        super().__init__(target_folder)
        self.__date = _date
        self.__path = self.__get_path()

    def __get_path(self) -> Path:
        if self.__date:
            path = super().path / self.__date
        else:
            path = super().path / datetime.now().strftime("%Y-%m-%d")
        if not path.exists():
            raise Path_Is_Not_Folder_Error(f"目标路径<{path}>不存在")
        if path.is_file():
            raise Path_Is_Not_Folder_Error(f"目标路径<{path}>不是文件夹")
        return path

    @property
    def path(self) -> Path:
        return self.__path

    @property
    def date(self) -> str:
        return self.__date
