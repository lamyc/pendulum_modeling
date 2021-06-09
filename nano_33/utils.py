import serial
import time
import sys, os

def read_serial(elapsed_time, port_path, baud=9600, timeout=1):
    '''
    Parameters:
    ------------
    elapsed_time: float or int
                elapsed time for reading the serial print, in seconds.
    port_path: string
                path to the Arduino port.
    baud: int, optional
                baud rate of the serial communication.
    timeout: int, optional
                timeout for reading the serial print, in seconds.

    '''
    if timeout is None:
        raise Exception('timeout must be specified.')
    start = time.perf_counter()
    with serial.Serial(port_path, baud, timeout=timeout) as ser:
        while (time.perf_counter() - start < elapsed_time):
            line = ser.readline()
            print(line.decode('UTF-8'), end='')

if __name__=="__main__":
    read_serial(1, "/dev/ttyS4")
