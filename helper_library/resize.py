import pygetwindow as gw
import pyautogui

class WindowResizer:
    def __init__(self, window_title):
        self.window_title = window_title
        self.window = self._get_window_by_title(window_title)

    def _get_window_by_title(self, title):
        windows = gw.getWindowsWithTitle(title)
        if not windows:
            raise ValueError(f"No window with title '{title}' found")
        return windows[0]

    def resize_window(self, width, height):
        if self.window:
            self.window.resizeTo(width, height)

    def move_window(self, x, y):
        if self.window:
            self.window.moveTo(x, y)

    def resize_and_center(self, width, height):
        screen_width, screen_height = pyautogui.size()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.move_window(x, y)
        self.resize_window(width, height)

# Example usage:
if __name__ == "__main__":
    window_title = "World Series Of Poker"  # Replace with the title of your window
    resizer = WindowResizer(window_title)
    resizer.resize_and_center(1280, 960)