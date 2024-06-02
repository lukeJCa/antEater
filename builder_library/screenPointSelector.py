import pyautogui
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ScreenshotSelector:
    def __init__(self, filename="selected_points.txt"):
        self.points = []
        self.image = None
        self.zoom_level = 1.0
        self.ax = None
        self.fig = None
        self.cid_zoom = None
        self.cid_click = None
        self.cid_key = None
        self.cid_motion = None
        self.drag_start = None
        self.filename = filename

    def take_screenshot(self):
        screenshot = pyautogui.screenshot()
        self.image = np.array(screenshot)

    def select_points(self):
        self.fig, self.ax = plt.subplots()
        self.ax.imshow(self.image)
        self.cid_click = self.fig.canvas.mpl_connect('button_press_event', self.on_click)
        self.cid_zoom = self.fig.canvas.mpl_connect('scroll_event', self.on_zoom)
        self.cid_key = self.fig.canvas.mpl_connect('key_press_event', self.on_key)
        self.cid_motion = self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        plt.show()
        self.save_points()

    def on_click(self, event):
        if event.button == 1:  # Left mouse button
            self.points.append((int(event.xdata), int(event.ydata)))
            self.ax.scatter(event.xdata, event.ydata, c='r', s=40)
            self.fig.canvas.draw()
        elif event.button == 3:  # Right mouse button
            self.drag_start = (event.xdata, event.ydata)

    def on_motion(self, event):
        if self.drag_start is not None:
            dx = event.xdata - self.drag_start[0]
            dy = event.ydata - self.drag_start[1]
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.ax.set_xlim(xlim[0] - dx, xlim[1] - dx)
            self.ax.set_ylim(ylim[0] - dy, ylim[1] - dy)
            self.drag_start = (event.xdata, event.ydata)
            self.fig.canvas.draw()

    def on_zoom(self, event):
        if event.button == 'up':
            self.zoom_level *= 1.1
        elif event.button == 'down':
            self.zoom_level /= 1.1

        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()
        xdata, ydata = event.xdata, event.ydata

        if xdata is not None and ydata is not None:
            new_xlim = [(x - xdata) * self.zoom_level + xdata for x in xlim]
            new_ylim = [(y - ydata) * self.zoom_level + ydata for y in ylim]

            self.ax.set_xlim(new_xlim)
            self.ax.set_ylim(new_ylim)
            self.fig.canvas.draw()

    def on_key(self, event):
        if event.key == 'ctrl+z' and self.points:
            self.points.pop()
            self.ax.images[0].set_data(self.image)
            self.ax.clear()
            self.ax.imshow(self.image)
            for point in self.points:
                self.ax.scatter(point[0], point[1], c='r', s=40)
            self.fig.canvas.draw()

    def save_points(self):
        with open(self.filename, "w") as file:
            for point in self.points:
                file.write(f"{point[0]}, {point[1]}\n")

    def run(self):
        self.take_screenshot()
        self.select_points()

# Example usage
if __name__ == "__main__":
    filename = input("Enter the filename to save the selected points: ")
    selector = ScreenshotSelector('pointStorage/' + filename)
    selector.run()
