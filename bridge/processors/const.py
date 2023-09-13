##################################################
# GAME SETTING CONSTS
GK = 5
ENEMY_GK = 5
IS_SIMULATOR_USED = 1
CAMERAS_COUNT: int = 4
MAX_BALLS_IN_CAMERA: int = 64
MAX_BALLS_IN_FIELD: int = CAMERAS_COUNT * MAX_BALLS_IN_CAMERA
BALL_PACKET_SIZE: int = 3
SIDE = 1 #1 if our goal on plus coords on X. -1 if our goal on minus coords on X.

ROBOTS_MAX_COUNT: int = 32
TEAM_ROBOTS_MAX_COUNT: int = ROBOTS_MAX_COUNT // 2
SINGLE_ROBOT_PACKET_SIZE = 5
ROBOT_TEAM_PACKET_SIZE: int = SINGLE_ROBOT_PACKET_SIZE * TEAM_ROBOTS_MAX_COUNT

GEOMETRY_PACKET_SIZE: int = 2
##################################################

##################################################
# ROBOT SETTING CONSTS
MAX_SPEED = 30
MAX_SPEED_R = 7
ACCELERATION = 3
BASE_KICKER_VOLTAGE = 15.0
##################################################

