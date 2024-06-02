import pygame
import pyautogui
import sys
import pyperclip


def save_to_clipboard(text):
    """
    Saves the given text to the clipboard.

    Args:
        text (str): The text to be saved to the clipboard.
    """
    pyperclip.copy(text)
    print(f"Text saved to clipboard: {text}")

def track_mouse_and_save_coordinates():
    # Initialize Pygame
    pygame.init()

    # Set up the display
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Mouse Tracker")

    # Font for displaying the coordinates
    font = pygame.font.Font(None, 36)

    saved_coordinates = None

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    saved_coordinates = pyautogui.position()
                    save_to_clipboard(str(saved_coordinates))
                    print(f"Coordinates saved: {saved_coordinates}")

        # Get the current mouse position
        mouse_x, mouse_y = pyautogui.position()

        # Clear the screen
        screen.fill((255, 255, 255))

        # Render the current coordinates
        text = font.render(f"Mouse Position: ({mouse_x}, {mouse_y})", True, (0, 0, 0))
        screen.blit(text, (20, 80))

        # Update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Example usage:
if __name__ == "__main__":
    track_mouse_and_save_coordinates()