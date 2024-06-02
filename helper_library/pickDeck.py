import os
import tkinter as tk
from tkinter import filedialog

def save_directory_path():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()

    # Open a dialog to select a directory
    selected_directory = filedialog.askdirectory()

    if selected_directory:
        # Get the current directory
        current_directory = os.getcwd()
        
        # Get the relative path from the current directory to the selected directory
        relative_path = os.path.relpath(selected_directory, current_directory)
        
        # Path to the vision_library directory
        vision_library_directory = os.path.join(current_directory, 'vision_library')

        # Ensure the vision_library directory exists
        if not os.path.exists(vision_library_directory):
            os.makedirs(vision_library_directory)
        
        # Path to the deck.txt file
        deck_file_path = os.path.join(vision_library_directory, 'deck.txt')
        
        # Write the relative path to the deck.txt file
        with open(deck_file_path, 'w') as file:
            file.write(relative_path)
        
        print(f"The path '{relative_path}' has been saved to '{deck_file_path}'")
    else:
        print("No directory selected.")

if __name__ == "__main__":
    save_directory_path()
