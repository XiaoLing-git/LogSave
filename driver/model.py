from enum import Enum
from typing import List


class Label(str, Enum):
    Navi_Plan = "导航规划"
    Navi_Control = "导航控制"
    CornerLoad = "经典Corner"
    NewCornerLoad = "一步Corner"
    AttachLoad = "经典Attach"
    NewAttachLoad = "一步Attach"
    StackLoad = "经典堆叠"
    Chassis_Control = "底盘控制"
    Fork_Control = "货叉控制"
    Fixed_Brake = "定点刹车"
    Lift_To_Bottom = "一降到底"
    Integration = "集成测试"
    VPS_Test = "VPS测试"
    Options = "其他测试"

    @classmethod
    def get_all_type(cls) -> List:
        return [
            cls.Options,
            cls.Navi_Plan,
            cls.Navi_Control,
            cls.CornerLoad,
            cls.NewCornerLoad,
            cls.AttachLoad,
            cls.NewAttachLoad,
            cls.StackLoad,
            cls.Chassis_Control,
            cls.Fork_Control,
            cls.Lift_To_Bottom,
            cls.Integration,
            cls.VPS_Test
        ]


class Path_Is_Not_Folder_Error(Exception):
    def __int__(self, msg):
        self.msg = msg

    def __repr__(self):
        return f"{self.__class__} <<{self.msg}>>"
