from enum import IntEnum, auto

STACKSHOT_BAUD_RATE = 38400

RAIL_STATUS_IDLE            = 0x00 # The rail is idle
RAIL_STATUS_MOVING          = 0x01 # The rail is currently moving
RAIL_STATUS_SHUTTER         = 0x02 # The shutter is currently firing
RAIL_STATUS_USER_ABORTED    = 0x04 # The user has aborted a move


class Status(IntEnum):
    COMM_STATUS_FAILED = 0
    COMM_STATUS_SUCCESS = auto()        # The operation was successful
    COMM_STATUS_BUSY = auto()           # The current operation could not begin because it is already in progress
    COMM_STATUS_DATA_MISSING = auto()   # Data was not fully read
    COMM_STATUS_BAD_SYNC = auto()       # The sync-byte was missing in the communiction stream
    COMM_STATUS_BUFFER_OVERRUN = auto() # The controller returned more data than could be processed
    COMM_STATUS_NOT_EMPTY = auto()      # The requested write operation could not be performed because data was already present (write-once register)
    COMM_STATUS_IO_ERROR = auto()       # An input/output error occured (USB unplugged, bad handle, etc)
    COMM_STATUS_BAD_PARAM = auto()      # One of the parameters passed into the function was rejected by the controller
    COMM_STATUS_NOT_FOUND = auto()      # The requested controller could not be found via USB


class RailAxis(IntEnum):
    COMM_RAIL_AXIS_ANY = 0              # Use any available axis when opening
    COMM_RAIL_AXIS_X = auto()           # Only open the X axis
    COMM_RAIL_AXIS_Y = auto()           # Only open the Y axis
    COMM_RAIL_AXIS_Z = auto()           # Only open the Z axis
    COMM_RAIL_AXIS_UNDEFINED = auto()   # The axis stored in the controller is undefined


class Cmd(IntEnum):
	CC_RAIL_MOVE = 0x1000               # Move the rail to the specified position
	CC_RAIL_POSITION_TARGET = auto()    # Desired target position for the rail
	CC_RAIL_POSITION_CURRENT = auto()   # Current position of the rail
	CC_RAIL_POSITION_ZERO = auto()      # Zero out the current position of the rail
	CC_RAIL_SHUTTER_FIRE = auto()       # Fire the shutter control
	CC_RAIL_STATUS = auto()             # Retrieve the current controller status
	CC_RAIL_STOP = auto()               # Stop the rail from moving
	CC_RAIL_MOVE_AT_SPEED = auto()      # Move the rail at the specified speed

	CC_RAIL_CONFIG_NAME = 0x1080        # The name for the current configuration
	CC_RAIL_CONFIG_BACKLIGHT = auto()   # Backlighting configuration
	CC_RAIL_CONFIG_MODE = auto()        # Operating mode of the controller
	CC_RAIL_CONFIG_UNITS = auto()       # Units -- mm/mils/steps
	CC_RAIL_CONFIG_TORQUE = auto()      # Torque setting for the motor
	CC_RAIL_CONFIG_NUM_STEPS = auto()   # Number of steps to use for a stack
	CC_RAIL_CONFIG_NUM_PULSES = auto()  # Number of pulses on the shutter per step
	CC_RAIL_CONFIG_TOTAL_DISTANCE = auto()  #Total distance config
	CC_RAIL_CONFIG_DISTANCE_PER_STEP = auto()   # Distance to travel per step
	CC_RAIL_CONFIG_SETTLE_TIME = auto()         # Settling time
	CC_RAIL_CONFIG_OFF_TIME = auto()            # Off time between shutter pulses
	CC_RAIL_CONFIG_SPEED = auto()               # Speed that the rail will move
	CC_RAIL_CONFIG_RAMP_TIME = auto()           # Ramp time for the rail
	CC_RAIL_CONFIG_DISTANCE_PER_REV = auto()    # Linear distance per revolution of the motor
	CC_RAIL_CONFIG_SHUTTER_DISABLE = auto()     # Shutter disable feature enabled/disabled
	CC_RAIL_CONFIG_AUTO_RETURN = auto()         # Auto-return feature enabled/disabled
	CC_RAIL_CONFIG_SAVE = auto()                # Save the current configuration
	CC_RAIL_CONFIG_LOAD = auto()                # Load the specified configuration
	CC_RAIL_CONFIG_AXIS = auto()                # Get/set the controllers configured axis
	CC_RAIL_CONFIG_TIMELAPSE = auto()           # Time-lapse feature enabled/disabled
	CC_RAIL_CONFIG_PULSE_TIME = auto()          # On time of the shutter pulse
	CC_RAIL_CONFIG_BACKLASH = auto()            # Rail backlash configuration
	CC_RAIL_CONFIG_HOLDING_TORQUE = auto()      # Holding torque for when the rail isn't moving
	CC_RAIL_CONFIG_SPEED_MOVE = auto()          # Speed used by FWD/BACK buttons
	CC_RAIL_CONFIG_POLARITY = auto()            # Direction polarity
	CC_RAIL_CONFIG_IO_MODE = auto()             # IO mode -- Normal, master, slave
	CC_RAIL_CONFIG_IO_DIR = auto()              # IO mode = Master, FWD or BACK
	CC_RAIL_CONFIG_ROTARY_BACKLASH = auto()     # Backlash for rotary tables
	CC_RAIL_CONFIG_ROTARY_RATIO = auto()        # Rotary table gear ratio
	CC_RAIL_CONFIG_ROTARY_DEGREES = auto()      # Degrees to move per step

	CC_RESET = 0x1100                           # Reset the controller
	CC_REFLASH = auto()                         # Start reflash
	CC_SOFTWARE_STRING = auto()                 # Software string (human readable)
	CC_SOFTWARE_ID = auto()                     # Sftware identifier
	CC_HARDWARE_ID = auto()                     # Hardware identifer
	CC_BOOTLOADER_ID = auto()                   # Bootloader identifer
	CC_SOFTWARE_CHECKSUM = auto()               # Software checksum
	CC_SERIAL_NUMBER = auto()                   # The serial number of the device
	CC_NVM_ACCESS = auto()                      # NVM register access
	CC_NAND_ACCESS = auto()
	CC_NOR_ACCESS = auto()
	CC_PING = auto()
	CC_LOG = auto()
	CC_WIFI = auto()
	CC_CLOSE = auto()


class Action(IntEnum):
	COMM_ACTION_MIN = 0
	COMM_ACTION_READ = COMM_ACTION_MIN      # Read the specified command
	COMM_ACTION_WRITE = auto()              # Write the specified command
	COMM_ACTION_RSP_OK = auto()             # Controller responded with OK
	COMM_ACTION_BAD_PARAM = auto()          # A bad parameter was passed to the controller
	COMM_ACTION_UNSUPPORTED_ACTION = auto() # The action specified is invalid
	COMM_ACTION_UNSUPPORTED_CMD = auto()    # The command passed in is invalid
	COMM_ACTION_FAILED = auto()             # The command failed (no further information available)
	COMM_ACTION_NOT_EMPTY = auto()          # The write operation was to a write-once register and it is no longer empty
	COMM_ACTION_BUSY = auto()               # The controller is already performing the specified action
	COMM_ACTION_MAX = auto()


class RailDir(IntEnum):
	COMM_RAIL_DIR_MIN = 0
	COMM_RAIL_DIR_FWD = COMM_RAIL_DIR_MIN   # Move the rail in the forward direction
	COMM_RAIL_DIR_BACK = auto()             # Move the rail in the backward direction
	COMM_RAIL_DIR_MAX = auto()


class RailUnits(IntEnum):
	COMM_RAIL_UNITS_MIN = 0
	COMM_RAIL_UNITS_ENGLISH = COMM_RAIL_UNITS_MIN   # English/mils
	COMM_RAIL_UNITS_METRIC = auto()                 # Metric/mm
	COMM_RAIL_UNITS_STEPS = auto()                  # Motor steps
	COMM_RAIL_UNITS_DEGREES = auto()                # Degrees for rotary moves
	COMM_RAIL_UNITS_MAX = auto()
