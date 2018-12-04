from enum import Enum


class Type:
    CAR = 0


class RadType(Enum):
    OUTER = 0
    PRIMITIVE = 1


class CONST:
    # int constants
    COUNT_INC = 1
    COUNT_DEC = 1
    INITIALIZE_ZERO = 0
    INITIALIZE_ONE = 1
    OBJECT_CREATION_DELAY = 50
    ROAD_LANE = 9
    UPDATE_FRAME_TIME_DELAY = 1
    TRUE = 1
    FALSE = 0
    FIRST_LANE = 0
    LAST_LANE = 8

    # double constants
    ACCELERATION = 0.01

    # string constants
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
    NEW_LINE = "\n"
    GRAPH_OUTPUT_LOCATION = '\Tools\GraphInput.txt'
    FRAME_SIZE = "fullscreen"
    FULL_SCREEN = '-fullscreen'
    TITLE = "Self Driving Simulator"


class COLOUR:
    # colour constants
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    WHITE = "white"


