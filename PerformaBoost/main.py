#starte die Anwendung mit: python main.py
import tkinter as tk
from Applications.Settings import settingsWindow
from Prefabs.windowManager import WindowManager

def main():
    windowManager = WindowManager("PerformaBoost", "1000x600")
    
    settings_button = tk.Button(
        windowManager.root, 
        text="Settings", 
        command=settingsWindow.create_settings_window,
        width=20,
        height=2
    )
    settings_button.pack(pady=20)
    
    
    windowManager.run()


if __name__ == "__main__":
    main()
