import serial
import time
import sys, os
import traceback
from tqdm import tqdm

def read_serial(elapsed_time, num_measurements, port_path, dir_path, baud=9600,
        timeout=1, index_start=0):
    '''
    Read serial data for an given time from Arduino and export to a tsv.

    Parameters
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
    if not os.path.exists(port_path):
        raise IOError("Could not find the specified Arduino port")
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    for i in tqdm(range(num_measurements)):
        file_path = os.path.join(dir_path, 'trial%d.tsv'%(i + index_start))
        try:
            mytsv = open(file_path, 'w')
        except IOError:
            print("failed to open file")
            traceback.print_exc()
        except:
            print(repr(Exception))
            traceback.print_exc()

        if timeout is None:
            raise Exception('timeout must be specified.')

        print('starting trial %d...'%(i + index_start))
        start = time.perf_counter()
        with serial.Serial(port_path, baud, timeout=timeout) as ser:
            while (time.perf_counter() - start < elapsed_time):
                line = ser.readline()
                mytsv.write(line.decode('UTF-8'))

        mytsv.close()
    print("data logged successfully.")

def monitor(port_path, baud=9600, timeout=1):
    '''
    Read serial data indefinitely from Arduino device.

    Parameters
    ------------
    port_path: string
                path to the Arduino port.
    baud: int, optional
                baud rate of the serial communication.
    timeout: int, optional
                timeout for reading the serial print, in seconds.

    '''
    with serial.Serial(port_path, baud, timeout=timeout) as ser:
        while True:
            line = ser.readline()
            print(line.decode('UTF-8'), end='')

if __name__=="__main__":
    read_serial(1200, 30, "/dev/ttyACM0", "measurements")
    # monitor("/dev/ttyS4")
    pass
