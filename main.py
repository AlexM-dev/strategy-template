"""
Точка входа в стратегию
"""

from strategy_bridge.processors import RobotCommandsSender, VisionDetectionsCollector
from strategy_bridge.processors.referee_commands_collector import (
    RefereeCommandsCollector,
)
from strategy_bridge.runner import Runner

import bridge.processors.const as const
import bridge.processors.strategy as strategy
from bridge.processors.python_controller import SSLController
from bridge.processors.robot_command_sink import CommandSink
from bridge.processors.field_creator import FieldCreator
from bridge.processors.drawing_processor import Drawer

if __name__ == "__main__":

    # config.init_logging("./logs")

    # TODO: Move list of processors to config
    PROCESSORS = [
        VisionDetectionsCollector(processing_pause=0.001),
        RefereeCommandsCollector(processing_pause=0.001),
        FieldCreator(processing_pause=0.01),
        SSLController(
            ally_color=const.COLOR,
            # should_debug=True,
            processing_pause=const.Ts,
            reduce_pause_on_process_time=True,
            dbg_game_status=strategy.GameStates.RUN,
            dbg_state=strategy.States.ATTACK,
        ),
        SSLController(
            ally_color=const.Color.YELLOW,
            # should_debug=True,
            processing_pause=const.Ts,
            reduce_pause_on_process_time=True,
            dbg_game_status=strategy.GameStates.RUN,
            dbg_state=strategy.States.ATTACK,
        ),
        Drawer(),
        CommandSink(processing_pause=0.001),  # , should_debug=True
        RobotCommandsSender(processing_pause=0.001),
    ]

    RUNNER = Runner(processors=PROCESSORS)
    RUNNER.run()
