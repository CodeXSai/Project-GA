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
    DELAY_AFTER_ALL_POPULATION = 30
    EXTINGUISHING_PERIOD = 300
    GRAPH_DELAY = 150
    TRUE = 1
    FALSE = 0
    FIRST_LANE = 0
    LAST_LANE = 8

    # double constants
    ACCELERATION = 0.1

    # string constants
    DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
    NEW_LINE = "\n"
    GRAPH_OUTPUT_LOCATION = '\Tools\GraphInput.txt'
    FITNESS_OUTPUT_LOCATION = '\Tools\FitnessInput.txt'
    FRAME_SIZE = "fullscreen"
    FULL_SCREEN = '-fullscreen'
    TITLE = "Self Driving Simulator"
    STRING_EMPTY = ""


class COLOUR:
    # colour constants
    RED = "red"
    GREEN = "green"
    YELLOW = "yellow"
    BLUE = "blue"
    WHITE = "white"
    BLACK = "black"



