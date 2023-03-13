# referenced from https://www.cognisys-inc.com/downloads/stackshot/StackShotCommands_1_2.pdf

from enum import IntEnum, auto

STACKSHOT_BAUD_RATE = 38400


class RailStatus(IntEnum):
	IDLE            = 0x00 # The rail is idle
	MOVING          = 0x01 # The rail is currently moving
	SHUTTER         = 0x02 # The shutter is currently firing
	USER_ABORTED    = 0x04 # The user has aborted a move


class StackShotStatus(IntEnum):
    FAILED = 0
    SUCCESS = auto()        # The operation was successful
    BUSY = auto()           # The current operation could not begin because it is already in progress
    DATA_MISSING = auto()   # Data was not fully read
    BAD_SYNC = auto()       # The sync-byte was missing in the communiction stream
    BUFFER_OVERRUN = auto() # The controller returned more data than could be processed
    NOT_EMPTY = auto()      # The requested write operation could not be performed because data was already present (write-once register)
    IO_ERROR = auto()       # An input/output error occured (USB unplugged, bad handle, etc)
    BAD_PARAM = auto()      # One of the parameters passed into the function was rejected by the controller
    NOT_FOUND = auto()      # The requested controller could not be found via USB


class RailAxis(IntEnum):
    ANY = 0              # Use any available axis when opening
    X = auto()           # Only open the X axis
    Y = auto()           # Only open the Y axis
    Z = auto()           # Only open the Z axis
    UNDEFINED = auto()   # The axis stored in the controller is undefined


class Cmd(IntEnum):
	RAIL_MOVE = 0x1000                       # Move the rail to the specified position
	RAIL_POSITION_TARGET = auto()            # Desired target position for the rail
	RAIL_POSITION_CURRENT = auto()           # Current position of the rail
	RAIL_POSITION_ZERO = auto()              # Zero out the current position of the rail
	RAIL_SHUTTER_FIRE = auto()               # Fire the shutter control
	RAIL_STATUS = auto()                     # Retrieve the current controller status
	RAIL_STOP = auto()                       # Stop the rail from moving
	RAIL_MOVE_AT_SPEED = auto()              # Move the rail at the specified speed

	RAIL_CONFIG_NAME = 0x1080                # The name for the current configuration
	RAIL_CONFIG_BACKLIGHT = auto()           # Backlighting configuration
	RAIL_CONFIG_MODE = auto()                # Operating mode of the controller
	RAIL_CONFIG_UNITS = auto()               # Units -- mm/mils/steps
	RAIL_CONFIG_TORQUE = auto()              # Torque setting for the motor
	RAIL_CONFIG_NUM_STEPS = auto()           # Number of steps to use for a stack
	RAIL_CONFIG_NUM_PULSES = auto()          # Number of pulses on the shutter per step
	RAIL_CONFIG_TOTAL_DISTANCE = auto()      # Total distance config
	RAIL_CONFIG_DISTANCE_PER_STEP = auto()   # Distance to travel per step
	RAIL_CONFIG_SETTLE_TIME = auto()         # Settling time
	RAIL_CONFIG_OFF_TIME = auto()            # Off time between shutter pulses
	RAIL_CONFIG_SPEED = auto()               # Speed that the rail will move
	RAIL_CONFIG_RAMP_TIME = auto()           # Ramp time for the rail
	RAIL_CONFIG_DISTANCE_PER_REV = auto()    # Linear distance per revolution of the motor
	RAIL_CONFIG_SHUTTER_DISABLE = auto()     # Shutter disable feature enabled/disabled
	RAIL_CONFIG_AUTO_RETURN = auto()         # Auto-return feature enabled/disabled
	RAIL_CONFIG_SAVE = auto()                # Save the current configuration
	RAIL_CONFIG_LOAD = auto()                # Load the specified configuration
	RAIL_CONFIG_AXIS = auto()                # Get/set the controllers configured axis
	RAIL_CONFIG_TIMELAPSE = auto()           # Time-lapse feature enabled/disabled
	RAIL_CONFIG_PULSE_TIME = auto()          # On time of the shutter pulse
	RAIL_CONFIG_BACKLASH = auto()            # Rail backlash configuration
	RAIL_CONFIG_HOLDING_TORQUE = auto()      # Holding torque for when the rail isn't moving
	RAIL_CONFIG_SPEED_MOVE = auto()          # Speed used by FWD/BACK buttons
	RAIL_CONFIG_POLARITY = auto()            # Direction polarity
	RAIL_CONFIG_IO_MODE = auto()             # IO mode -- Normal, master, slave
	RAIL_CONFIG_IO_DIR = auto()              # IO mode = Master, FWD or BACK
	RAIL_CONFIG_ROTARY_BACKLASH = auto()     # Backlash for rotary tables
	RAIL_CONFIG_ROTARY_RATIO = auto()        # Rotary table gear ratio
	RAIL_CONFIG_ROTARY_DEGREES = auto()      # Degrees to move per step

	RESET = 0x1100                           # Reset the controller
	REFLASH = auto()                         # Start reflash
	SOFTWARE_STRING = auto()                 # Software string (human readable)
	SOFTWARE_ID = auto()                     # Sftware identifier
	HARDWARE_ID = auto()                     # Hardware identifer
	BOOTLOADER_ID = auto()                   # Bootloader identifer
	SOFTWARE_CHECKSUM = auto()               # Software checksum
	SERIAL_NUMBER = auto()                   # The serial number of the device
	NVM_ACCESS = auto()                      # NVM register access
	NAND_ACCESS = auto()
	NOR_ACCESS = auto()
	PING = auto()
	LOG = auto()
	WIFI = auto()
	CLOSE = auto()


class Action(IntEnum):
	MIN = 0
	READ = MIN                  # Read the specified command
	WRITE = auto()              # Write the specified command
	RSP_OK = auto()             # Controller responded with OK
	BAD_PARAM = auto()          # A bad parameter was passed to the controller
	UNSUPPORTED_ACTION = auto() # The action specified is invalid
	UNSUPPORTED_CMD = auto()    # The command passed in is invalid
	FAILED = auto()             # The command failed (no further information available)
	NOT_EMPTY = auto()          # The write operation was to a write-once register and it is no longer empty
	BUSY = auto()               # The controller is already performing the specified action
	MAX = auto()


class RailDir(IntEnum):
	MIN = 0
	FWD = MIN       # Move the rail in the forward direction
	BACK = auto()   # Move the rail in the backward direction
	MAX = auto()


class RailUnits(IntEnum):
	MIN = 0
	ENGLISH = MIN       # English/mils
	METRIC = auto()     # Metric/mm
	STEPS = auto()      # Motor steps
	DEGREES = auto()    # Degrees for rotary moves
	MAX = auto()


# CommRailMode

# CommRailIOMode

# CommRailIODir

# CommRailMovePolarity