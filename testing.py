# Print Past! when input from usb microphone is above threshold.
import sounddevice as sd
import numpy as np
import time

# Set the duration for audio recording (in seconds)
duration = 10

# Set the threshold for audio level
threshold = 60

i=0

# Callback function for the stream
def audio_callback(indata, frames, time_info, status):
    global i
    volume_norm = np.linalg.norm(indata) * 10
    if volume_norm > threshold:
        i += 1
        print("Past!"+str(i))
        for t in range(5, 0, -1):
            print("Sleeping "+str(t)+" more seconds")
            time.sleep(1)  # sleep for 1 second
            
# Open the stream
stream = sd.InputStream(callback=audio_callback)

# Start the stream
with stream:
    while True:
        # Sleep for the duration
        time.sleep(duration)