import cv2
import numpy as np
import pyautogui
import time

def livestream_screen():
    while True:
        start_time = time.time()
        
        # Capture the screen
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(screenshot)

        # Convert the color from RGB to BGR (OpenCV uses BGR)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Display the frame
        cv2.imshow('Screen Livestream', frame)

        # Calculate and print the latency
        latency = time.time() - start_time
        print(f"Latency: {latency:.4f} seconds")

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # Release the display window
        cv2.destroyAllWindows()

if __name__ == "__main__":
    livestream_screen()