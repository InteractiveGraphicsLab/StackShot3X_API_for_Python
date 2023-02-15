import time
import ctypes
import usb.core

from commdefs import *
from pyftdi.ftdi import Ftdi
from pathlib import Path
from autoshooter_error import AutoShooterError

def float2uint(data: float):
    # casted_data = (unsigned int*)&data
    data_ptr = ctypes.pointer(ctypes.c_float(data))
    casted_data_ptr = ctypes.cast(data_ptr, ctypes.POINTER(ctypes.c_uint))
    casted_data = casted_data_ptr.contents.value
    return casted_data


class StackShotAPI:
    def __init__(self):
        self.device = Ftdi()
        self.units = RailUnits.COMM_RAIL_UNITS_METRIC
        self.backlash = False

    def send_command(self, axis: RailAxis, cmd: Cmd, action: Action, data: bytearray | None, lenIn: int):
        cmd = int(cmd)
        if axis == RailAxis.COMM_RAIL_AXIS_ANY:
            action = (int(action) | (int(axis)   << 4))
        else:
            action = (int(action) | (int(axis-1) << 4))

        byte = bytearray()
        byte.extend(b'\x55')
        byte.extend(((cmd >> 8) & 0x0FF).to_bytes(1, 'big'))
        byte.extend(( cmd       & 0x0FF).to_bytes(1, 'big'))
        byte.extend((action & 0x0FF).to_bytes(1, 'big'))
        byte.extend(lenIn.to_bytes(1, 'big')) # CMD length
        if data != None:
            for d in data:
                byte.extend(d.to_bytes(1, 'big'))
        byte.extend(b'\x69') # checksum

        n = self.device.write_data(byte)
        time.sleep(1)

        res = self.device.read_data(100)
        ### wait for response
        time.sleep(1)

        """
        Format of received data:
        buffer[0] = 0xAA (Ack)
        buffer[1] = cmd High
        buffer[2] = cmd Low
        buffer[3] = action
        buffer[4] = Length of data
        buffer[5] = data......
        buffer[n] = checksum;
        """
        # res_cmd = res[1] << 8 | res[2]

        res_response = res[3]
        if res_response != int(Action.COMM_ACTION_RSP_OK):
            if res_response == int(Action.COMM_ACTION_BUSY):
                raise AutoShooterError('device is busy.')
            else:
                raise AutoShooterError('something error was happned.')

        res_buffsize = res[4]

        res_data = None
        if 0 < res_buffsize:
            res_data = bytearray()
            for i in range(5, 5+res_buffsize):
                res_data.extend(res[i].to_bytes(1, 'big'))

        return res_data

    def open(self):
        device_list = self.device.list_devices()
        device = None
        for d in device_list:
            if d[0].description == 'StackShot3x':
                device = usb.core.find(idVendor=d[0].vid, idProduct=d[0].pid)
                break

        if device == None:
            raise AutoShooterError("Device Not Found") # NOTE

        self.device.open_from_device(device)

        self.device.set_bitmode(0xFF, Ftdi.BitMode.CBUS)

        time.sleep(0.5)

        self.device.set_baudrate(STACKSHOT_BAUD_RATE)
        self.device.set_flowctrl('') # no flow controll

    def close(self):
        self.device.set_bitmode(0xF0, Ftdi.BitMode.CBUS)
        self.send_command(RailAxis.COMM_RAIL_AXIS_ANY, Cmd.CC_CLOSE, Action.COMM_ACTION_WRITE, None, 0)
        self.device.close()

    def rail_status(self, axis: RailAxis):
        res = self.send_command(axis, Cmd.CC_RAIL_STATUS, Action.COMM_ACTION_READ, None, 0) # axis不要?
        status = (int(res[0])) | (int(res[1]) << 8) | (int(res[2]) << 16) | (int(res[3]) << 24)

        return status

    def move(self, axis: RailAxis, dir: RailDir, dist: float):
        castedDist = float2uint(dist)

        data = bytearray()
        data.extend(int(dir).to_bytes(1, 'big'))
        data.extend(int(self.units).to_bytes(1, 'big'))
        data.extend(self.backlash.to_bytes(1, 'big'))
        data.extend(( castedDist        & 0x0FF).to_bytes(1, 'big'))
        data.extend(((castedDist >>  8) & 0x0FF).to_bytes(1, 'big'))
        data.extend(((castedDist >> 16) & 0x0FF).to_bytes(1, 'big'))
        data.extend(((castedDist >> 24) & 0x0FF).to_bytes(1, 'big'))

        self.send_command(axis, Cmd.CC_RAIL_MOVE, Action.COMM_ACTION_WRITE, data, 7)

        # wait for rail stop
        while(True):
            if self.rail_status(axis) != RAIL_STATUS_MOVING:
                break
            time.sleep(0.5)

    def stop(self, axis: RailAxis):
        self.send_command(axis, Cmd.CC_RAIL_STOP, Action.COMM_ACTION_WRITE, None, 0)

    def shutter(self,  num_pulses: int, pulse_duration: float, pulse_off_time: float):
        casted_pulse_duration = float2uint(pulse_duration)
        casted_pulse_off_time = float2uint(pulse_off_time)

        data = bytearray()
        data.extend(( num_pulses       & 0x0FF).to_bytes(1, 'big'))
        data.extend(((num_pulses >> 8) & 0x0FF).to_bytes(1, 'big'))
        data.extend(( casted_pulse_duration        & 0x0FF).to_bytes(1, 'big'))
        data.extend(((casted_pulse_duration >>  8) & 0x0FF).to_bytes(1, 'big'))
        data.extend(((casted_pulse_duration >> 16) & 0x0FF).to_bytes(1, 'big'))
        data.extend(((casted_pulse_duration >> 24) & 0x0FF).to_bytes(1, 'big'))
        data.extend(( casted_pulse_off_time        & 0x0FF).to_bytes(1, 'big'))
        data.extend(((casted_pulse_off_time >>  8) & 0x0FF).to_bytes(1, 'big'))
        data.extend(((casted_pulse_off_time >> 16) & 0x0FF).to_bytes(1, 'big'))
        data.extend(((casted_pulse_off_time >> 24) & 0x0FF).to_bytes(1, 'big'))

        self.send_command(RailAxis.COMM_RAIL_AXIS_ANY, Cmd.CC_RAIL_SHUTTER_FIRE, Action.COMM_ACTION_WRITE, data, 10)

        # wait for finish shutter
        while(True):
            if self.rail_status(RailAxis.COMM_RAIL_AXIS_ANY) != RAIL_STATUS_SHUTTER:
                break
            time.sleep(0.5)
