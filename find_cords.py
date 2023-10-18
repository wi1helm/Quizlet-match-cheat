import pyautogui
import time

try:
    while True:
        # Get the current mouse cursor position
        x, y = pyautogui.position()

        # Print the coordinates
        print(f"Mouse cursor position: x={x}, y={y}")

        # Pause for a short duration to avoid printing too rapidly
        time.sleep(1)
except KeyboardInterrupt:
    # Exit the program if the user presses Ctrl+C
    pass
