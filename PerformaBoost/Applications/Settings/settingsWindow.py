import tkinter as tk
from tkinter import ttk
from tkinter import *
from Prefabs.windowManager import WindowManager
from SavedData import dataManager





def saveSettings():
    # Speichere Änderungen dauerhaft in dataManager
    is_dark = checkbox_var.get()
    selected_language = language_combobox.get()
    print(f"[save] Dark mode is: {is_dark}")
    print(f"[save] Selected language: {selected_language}")

    
    
        
    # Save settings
    try:
        theme_value = "dark-mode" if is_dark else "light-mode"
        dataManager.setKeyValue("generellSettings.json", "theme", theme_value)
        dataManager.setKeyValue("generellSettings.json", "language", selected_language)
        WindowManager.reload_design_for_all_windows()

        print("[save] Settings saved successfully.")
    except Exception as e:
        print(f"[save] Error saving settings: {e}")


def create_settings_window():
    windowManager = WindowManager("Einstellungen", "800x600")
    

    # Global variables
    global checkbox_var
    global language_combobox

    # Theme from dataManager
    theme = dataManager.findAndGetKeyValue("theme")
    backgroundColor = dataManager.findAndGetKeyValue(theme, "background-color")

    checkbox_var = tk.BooleanVar(value=(theme == "dark-mode"))

    # Language from dataManager
    languages = ["German", "English"]
    current_language = "German"
    
    
    
    

    mainContainer = Frame(windowManager.root, bg=backgroundColor)
    mainContainer.pack(fill="both", expand=True)

    contentFrame = Frame(mainContainer, bg=backgroundColor)
    contentFrame.pack(side="top", fill="both", expand=True)

    settingsFrame = Frame(contentFrame, width=200, bg=backgroundColor)
    settingsFrame.pack(side="left", fill="both")




    # Checkbutton für Theme
    checkbox = tk.Checkbutton(settingsFrame, text="Dark Mode?", variable=checkbox_var)
    #checkbox.grid(pady=5, anchor="w")
    checkbox.grid(pady=5)
    if theme == "dark-mode":
        checkbox.select()
    


    
   

    language_combobox = ttk.Combobox(settingsFrame, values=languages)
    language_combobox.set(current_language if current_language in languages else languages[0])
    language_combobox.grid(pady=10)

    # Set the current language from settings
    #current_language = dataManager.findAndGetKeyValue("language")
    current_language = "German"
    if current_language in languages:
        language_combobox.set(current_language)
    else:
        language_combobox.set(languages[0])
    
    #language_combobox.pack(pady=10, anchor="w")
    language_combobox.grid(pady=10)

    # Footer mit Buttons
    footerFrame = Frame(windowManager.root, bg=backgroundColor)
    footerFrame.pack(side="bottom", fill="x")

    save_button = tk.Button(footerFrame, text="Save", command=saveSettings)
    save_button.grid(pady=10)




    cancelButton = tk.Button(footerFrame, text="Cancel", command=WindowManager.print_all_open_window_titles)
    cancelButton.grid(column=1, row=0, padx=10, pady=5)
    
    windowManager.run()
