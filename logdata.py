from src.communication.read import export_measurements
from src.communication.upload_script import upload
import os

# script_path = os.path.join("nano", "script", "ReadAccelerometer", "ReadAccelerometer.ino")
# upload(script_path)
path = os.path.join("nano", "measurements")
export_measurements(60*60, path, "952_2g.csv")
