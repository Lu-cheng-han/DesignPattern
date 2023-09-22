class CommandState:
    def process(self, context, command_object):
        pass

class TakePicCommandState(CommandState):
    def process(self, context, command_object):
        # 处理 TakePicCommand 并提取属性
        context.set_properties(command_object.well_1_r, command_object.well_1_g, ...)
        context.transition_to(AreaCommandState())  # 切换到处理 AreaCommand 的状态

class AreaCommandState(CommandState):
    def process(self, context, command_object):
        # 处理 AreaCommand 并提取属性
        context.set_properties(command_object.area_1_x, command_object.area_1_y, ...)
        context.transition_to(HeatingStateCommandState())  # 切换到处理 HeatingStateCommand 的状态

class HeatingStateCommandState(CommandState):
    def process(self, context, command_object):
        # 处理 HeatingStateCommand 并提取属性
        context.set_properties(command_object.heat_state, ...)
        # 可以根据需要继续切换到其他状态

class MyClass:
    def __init__(self):
        self.state = None
        self.properties = {}

    def set_properties(self, **kwargs):
        self.properties.update(kwargs)

    def transition_to(self, state):
        self.state = state

    def set_initial_property(self, request):
        command_object = request.command
        if isinstance(command_object, TakePicCommand):
            self.transition_to(TakePicCommandState())
        elif isinstance(command_object, AreaCommand):
            self.transition_to(AreaCommandState())
        elif isinstance(command_object, HeatingStateCommand):
            self.transition_to(HeatingStateCommandState())

        # 处理命令
        self.state.process(self, command_object)
