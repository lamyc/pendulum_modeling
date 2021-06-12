import warnings
import serial
import serial.tools.list_ports

def get_nano_port():
    arduino_ports = [
            p.device
            for p in serial.tools.list_ports.comports()
            if 'Nano' in p.description
    ]

    if not arduino_ports:
        raise IOError("No Arduino found")
    if len(arduino_ports) > 1:
        warnings.warn("Multiple Arduinos found - using the first")

    return arduino_ports[0]

if __name__ == "__main__":
    print(get_nano_port())
    pass
