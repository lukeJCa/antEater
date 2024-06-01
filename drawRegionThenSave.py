import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageGrab, ImageTk
import json

class ScreenshotEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Screenshot Editor")
        
        self.screenshot = self.take_screenshot()
        self.image = ImageTk.PhotoImage(self.screenshot)
        self.canvas = Canvas(self.root, width=self.screenshot.width, height=self.screenshot.height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)

        self.points = [(100, 100), (200, 100), (200, 200), (100, 200)]
        self.drag_data = {"x": 0, "y": 0, "item": None}

        self.draw_points_and_lines()

        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.root.bind("<space>", self.save_coordinates)

        self.root.mainloop()

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        return screenshot

    def draw_points_and_lines(self):
        self.canvas.delete("point")
        self.canvas.delete("line")
        for point in self.points:
            self.canvas.create_oval(point[0] - 5, point[1] - 5, point[0] + 5, point[1] + 5, fill="red", tags="point")
        
        for i in range(len(self.points)):
            self.canvas.create_line(self.points[i][0], self.points[i][1], self.points[(i+1) % len(self.points)][0], self.points[(i+1) % len(self.points)][1], fill="blue", tags="line")

    def on_press(self, event):
        closest_point = None
        min_distance = float("inf")
        for i, point in enumerate(self.points):
            distance = (event.x - point[0]) ** 2 + (event.y - point[1]) ** 2
            if distance < min_distance:
                closest_point = i
                min_distance = distance
        
        if min_distance < 100:
            self.drag_data["item"] = closest_point
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y

    def on_drag(self, event):
        if self.drag_data["item"] is not None:
            dx = event.x - self.drag_data["x"]
            dy = event.y - self.drag_data["y"]
            point_index = self.drag_data["item"]
            self.points[point_index] = (self.points[point_index][0] + dx, self.points[point_index][1] + dy)
            self.drag_data["x"] = event.x
            self.drag_data["y"] = event.y
            self.draw_points_and_lines()

    def save_coordinates(self, event):
        with open("rectangle_coordinates.txt", "w") as f:
            json.dump(self.points, f)
        print("Coordinates saved to rectangle_coordinates.txt")

if __name__ == "__main__":
    ScreenshotEditor()
