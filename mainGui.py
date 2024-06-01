import tkinter as tk
from tkinter import ttk, messagebox, Menu
import threading
import time
import random

class PokerGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("AntEater - Poker Engine")
        self.geometry("800x600")
        
        self.icon = tk.PhotoImage(file="icon.png")  # Load the image
        self.iconphoto(False, self.icon)  # Set the window icon

        self.create_menu()
        self.create_widgets()
        self.create_background_process()
    
    def create_menu(self):
        menu_bar = Menu(self)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open WSOP", command=self.openWSOP)
        file_menu.add_command(label="Resize WSOP Window", command=self.resizeWSOP)
        file_menu.add_command(label="Move WSOP Window", command=self.moveWSOP)
        file_menu.add_command(label="Open Login Details", command=self.openLogin)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="Setup", menu=file_menu)
        vision_menu = Menu(menu_bar, tearoff=0)
        vision_menu.add_command(label="Create Points", command=self.createPoints)
        menu_bar.add_cascade(label="Vision", menu=vision_menu)
        assistant_menu = Menu(menu_bar, tearoff=0)
        assistant_menu.add_command(label="Odds", command=self.oddsToWin)
        menu_bar.add_cascade(label="Assistant", menu=assistant_menu)
        anteater_menu = Menu(menu_bar, tearoff=0)
        anteater_menu.add_command(label="Cash", command=self.oddsToWin)
        anteater_menu.add_command(label="Tournament", command=self.oddsToWin)
        anteater_menu.add_command(label="Daily Blitz", command=self.oddsToWin)
        menu_bar.add_cascade(label="AntEater", menu=anteater_menu)
        self.config(menu=menu_bar)
    
    def create_widgets(self):
        # Header Frame
        header_frame = ttk.Frame(self)
        header_frame.pack(fill=tk.X)
        
        self.error_log = tk.StringVar()
        error_label = ttk.Label(header_frame, textvariable=self.error_log, foreground="red")
        error_label.pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Poker Board Frame
        board_frame = ttk.Frame(self)
        board_frame.pack(expand=True, fill=tk.BOTH)
        
        self.board_canvas = tk.Canvas(board_frame, background="green")
        self.board_canvas.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)
        
        # Players Frame
        players_frame = ttk.Frame(self)
        players_frame.pack(fill=tk.X)
        
        self.players = []
        for i in range(9):
            player_frame = ttk.Frame(players_frame, relief=tk.SUNKEN, borderwidth=1)
            player_frame.grid(row=0, column=i, padx=5, pady=5, sticky="nsew")
            player_label = ttk.Label(player_frame, text=f"Player {i+1}")
            player_label.pack(padx=5, pady=5)
            self.players.append(player_frame)
        
        # Buttons Frame
        buttons_frame = ttk.Frame(self)
        buttons_frame.pack(fill=tk.X, pady=10)
        
        button_names = ["Start", "Fold", "Call", "Raise", "Check"]
        for name in button_names:
            button = ttk.Button(buttons_frame, text=name, command=lambda n=name: self.button_action(n))
            button.pack(side=tk.LEFT, padx=5)
        
        # Background Process Number
        bg_number_frame = ttk.Frame(self)
        bg_number_frame.pack(fill=tk.X, pady=10)
        
        self.bg_number = tk.StringVar(value="0")
        bg_number_label = ttk.Label(bg_number_frame, text="Background Number:")
        bg_number_label.pack(side=tk.LEFT, padx=5)
        bg_number_value = ttk.Label(bg_number_frame, textvariable=self.bg_number)
        bg_number_value.pack(side=tk.LEFT, padx=5)
    
    def create_background_process(self):
        def update_number():
            while True:
                time.sleep(1)
                new_number = random.randint(1, 100)
                self.bg_number.set(str(new_number))
        
        threading.Thread(target=update_number, daemon=True).start()
    
    def openWSOP(self):
        import webbrowser
        url = "https://www.playwsop.com/play"
        try:
            webbrowser.open(url)
            print(f"Opening website: {url}")
        except Exception as e:
            print(f"Error opening website: {e}")
    
    def resizeWSOP(self):
        import os
        try:
            os.system('python resize.py')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run script: {e}")
            print(f"Error: {e}")
    
    def moveWSOP(self):
        import os
        try:
            os.system('python place.py')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to run script: {e}")
            print(f"Error: {e}")

    def openLogin(self):
        pass # to do, notepad with login details to accounts

    def createPoints(self):
        pass # to do, move the function which allows user to click points here

    def oddsToWin(self):
        pass # for actually assisting with live games
if __name__ == "__main__":
    app = PokerGUI()
    app.mainloop()
