import cv2
import numpy as np

# Get the IP address of your iPhone
ip_address = "192.168.71.133"

# Create a VideoCapture object to capture frames from your iPhone
cap = cv2.VideoCapture(ip_address + "/video")

while True:
    # Read the next frame from your iPhone
    ret, frame = cap.read()

    # If the frame is not empty, display it
    if ret:
        cv2.imshow("Frame", frame)

        # Press Q to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Release the VideoCapture object
cap.release()

# Close all windows
cv2.destroyAllWindows()