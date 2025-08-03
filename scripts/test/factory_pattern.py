


class Command():
    def capture_component_image(self) -> None:
        NotImplemented

# A.py
class MayaCommand(Command):
    def capture_component_image(self) -> None:
        cmds.import_image()

# B.py
class MaxCommand(Command):
    def capture_component_image(self) -> None:
        maxUtil.import_thumnail()

# C.py
class UnrealCommand(Command):
    def capture_component_image(self) -> None:
        un5.import_resource()


class AssetPreviewerController():
    def capture_component_image111(self, dcc_type :str) -> None:
        toolkit_obj = None
        if dcc_type == "MAYA":
            import A
            toolkit_obj = A.MayaCommand()
        elif dcc_type == "MAX":
            import B
            toolkit_obj = B.MaxCommand()
        else: # unreal
            import C
            toolkit_obj = C.UnrealCommand()
            
        toolkit_obj.capture_component_image()


# -----------------------------------------------------------------------
import maya.cmds as cmds
class AssetPreviewerController():
    def capture_component_image111(self, dcc_type :str) -> None:
        if dcc_type == "MAYA":
            cmds.import_image()
        elif dcc_type == "MAX":
            maxUtil.import_thumnail()
        else: # unreal
            un5.import_resource()


# 절차지향 언어           / 객체지향언어
# 절차지향 방식, 프로그래밍 / 객체지향언어 방식, 프로그래밍

# C                       C, C++, python ... class 개념을 가지고있는 언어들

