import pygetwindow as gw

def move_window_to_top_left(window_title):
    windows = gw.getWindowsWithTitle(window_title)
    if not windows:
        raise ValueError(f"No window with title '{window_title}' found")
    
    window = windows[0]
    window.moveTo(0, 0)
    print(f"Window '{window_title}' moved to the top-left corner of the screen.")

# Example usage:
if __name__ == "__main__":
    window_title = "World Series Of Poker"  # Replace with the title of your window
    move_window_to_top_left(window_title)