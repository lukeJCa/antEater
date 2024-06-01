import pygame
import pyautogui
import sys

def main():
    # Initialize Pygame
    pygame.init()

    # Define the screen dimensions
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Drag and Capture")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)

    # Initial rectangle parameters
    rect_width = 200
    rect_height = 150
    rect_x = 50
    rect_y = 50
    rect_dragging = False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if (rect_x < event.pos[0] < rect_x + rect_width and
                        rect_y < event.pos[1] < rect_y + rect_height):
                        rect_dragging = True
                        mouse_x, mouse_y = event.pos
                        offset_x = rect_x - mouse_x
                        offset_y = rect_y - mouse_y
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    rect_dragging = False
            elif event.type == pygame.MOUSEMOTION:
                if rect_dragging:
                    mouse_x, mouse_y = event.pos
                    rect_x = mouse_x + offset_x
                    rect_y = mouse_y + offset_y
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    capture_screenshot(rect_x, rect_y, rect_width, rect_height)

        screen.fill(WHITE)
        pygame.draw.rect(screen, RED, (rect_x, rect_y, rect_width, rect_height))
        pygame.display.flip()
        clock.tick(30)

def capture_screenshot(x, y, width, height):
    # Take a screenshot of the specified region
    screenshot = pyautogui.screenshot(region=(x, y, width, height))
    screenshot.save('screenshot.png')
    print("Screenshot saved as 'screenshot.png'")

if __name__ == "__main__":
    main()