# StackShot3X API for Python
[**日本語**](./README.ja.md)

API to controll StackShot3X on Python


# Environment
+ Python 3.8
+ PyFtdi 0.54.0


# Setup
+ You need to install libusb-win32 or libusbK to controll StackShot3X. The following is the procedure for installing the driver using [Zadig](https://zadig.akeo.ie/).
	1. Start Zadig, and select *Options > List All Devices*<br>
	![](/images/step1.png)

	1. Select StackShot3x from devices list.<br>
	![](/images/step2.png)

	1. Select driver libusb-win32 or libusbK, and click *Replace Driver*.<br>
	![](/images/step3.png)


+ Install pip package for this API
	```
	pip install pyftdi
	```


+ By installing PySide6, you can operate StackShot3X using the GUI for testing.
	```
	pip install PySide6
	python test.py
	```

# APIs
The following is an implementation based on [this](https://www.cognisys-inc.com/downloads/stackshot/StackShotCommands_1_2.pdf).


## class StackShotController

### open(device=None)

> Start communication with StackShot3X specified for the `device` connected via USB.
> If no device is specified (`device=None`), communication start with one of the StackShot3X devices connected via USB.
> 
> Parameters:
> - `device(Device)`: FTDI USB device(PyUSB instance)
> 
> Return type: `None`



### close()

> Close connection with StackShot3X.
>
> Return type: `None`


### get_status(axis)

> Get the state of the StackShot specified in `axis`.
>
> Parameters:
> - `axis(RailAxis)`: Axis of the rail.
>
> Return Type: `RailStatus`
>
> Returns: Status of the rail.

### move(axis, dir, dist, units)

> Move the StackShot specified in `axis`
>
> Parameters:
> - `axis(RailAxis)`: Axis of movement.
> - `dir(RailDir)`: Direction of movement.
> - `dist(float)`: Distance of movement.
> - `units(RailUnits)`: Units of distance specified in `dist`.
>
> Return Type: `None`


### stop(axis)

> Stop the movement of the StackShot specified in `axis`.
>
> Parameters:
> - `axis(RailAxis)`: StackShot to stop.
>
> Return Type: `None`

### shutter(num_pulses, pulse_duration, pulse_off_time)

> Shutter Fire.
>
> Parameters:
> - `num_pulses(int)`: The number of pulses to generate on the shutter output.
> - `pulse_duration(float)`: The "on" time of each pulse, in seconds.
> - `pulse_off_time(float)`: The "off" time of each pulse, in seconds.
>
> Return Type: `None`


## class RailStatus

Enum class representing the status of the rail on a particular axis


## class StackShotStatus

Enum class representing the status of StackShot3X


## class RailAxis

Enum class representing the axis of a StackShot3X rail


## class Cmd

Enum class representing each command in StackShot3X


## class Action

Enum class representing actions for StackShot3X


## class RailDir

Enum class representing directions of travel on the rail


## class RailUnits

Enum class representing units of distance to move the rail


# Acknowledgements
This software was supported by JSPS Grant-in-Aid for Scientific Research (B)22H03710.