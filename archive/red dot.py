import pygame
import sys

def draw_red_dot(x, y):
    # Initialize Pygame
    pygame.init()

    # Define the screen dimensions (you can adjust these as needed)
    screen_width, screen_height = 1920, 1080
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
    pygame.display.set_caption("Red Dot")

    # Colors
    RED = (255, 0, 0)
    BLACK = (0, 0, 0, 0)

    # Create a transparent surface
    overlay = pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 0))  # Fill with transparent color

    # Draw the red dot on the overlay
    pygame.draw.circle(overlay, RED, (x, y), 5)  # Radius of 5 pixels

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(overlay, (0, 0))  # Draw the overlay on the screen
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Example usage:
if __name__ == "__main__":
    # Define the coordinates for the red dot
    x, y = 100, 100
    draw_red_dot(x, y)