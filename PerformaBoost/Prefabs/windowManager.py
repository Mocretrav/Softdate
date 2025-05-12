import tkinter as tk
from SavedData import dataManager
from SavedData import SysData
from Applications.FileManager import fileFinder 
import json

openWindows = {}


class WindowManager:
    def __init__(self, title, geometry=None):
        global openWindows
        self.title = title
        self.is_main_window = not openWindows
        if self.is_main_window:
            self.root = tk.Tk()
        else:
            self.root = tk.Toplevel()

        self.root.title(title)

        if geometry is None:
            self.root.geometry("100x100")
        else:    
            self.root.geometry(geometry)
        
        theme = "dark-mode"
        backgroundColor = "#000010"
        try:
            theme = dataManager.getKeyValueWithFileName("generellSettings.json", "theme")
            backgroundColor = dataManager.getKeyValueWithFileName("style.json", theme, "background-color")
        except Exception as e:
            print(f"Fehler beim Laden des Designs: {e}")
        
        
        self.root.configure(bg=backgroundColor)

        # Beim Schließen das Fenster aus openWindows entfernen
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        # Fenster registrieren
        openWindows[title] = self


    def on_close(self):
        global openWindows
        # Fenster aus Dictionary entfernen
        if self.title in openWindows:
            del openWindows[self.title]

        # Fenster schließen
        self.root.destroy()

        # Falls das Hauptfenster geschlossen wird, gesamten Tkinter-Loop beenden
        if self.is_main_window:
            try:
                tk._exit()
            except:
                pass

    def apply_theme(self):
        try:
            self.theme = dataManager.getKeyValueWithFileName("generellSettings.json", "theme")
            self.backgroundColor = dataManager.getKeyValueWithFileName("style.json", self.theme, "background-color")
            self.root.configure(bg=self.backgroundColor)
            self._update_widget_colors(self.root, self.backgroundColor)
            print(f"Design neu geladen für Fenster: {self.title}")
        except Exception as e:
            print(f"Fehler beim Anwenden des Designs: {e}")

    def _update_widget_colors(self, widget, backgroundColor):
        try:
            widget_type = widget.winfo_class()

            if widget_type in ["TFrame", "TLabelframe"]:
                widget.configure(style="Custom.TFrame")  # optional via Style
            elif isinstance(widget, (tk.Tk, tk.Toplevel, tk.Frame, tk.LabelFrame)):
                widget.configure(bg=backgroundColor)
            elif isinstance(widget, tk.Label):
                widget.configure(bg=backgroundColor, fg="#FFFFFF")
            elif isinstance(widget, tk.Button):
                widget.configure(bg=backgroundColor, fg="#FFFFFF", activebackground="#222244")
            elif isinstance(widget, tk.Checkbutton):
                widget.configure(bg=backgroundColor, fg="#FFFFFF", selectcolor=backgroundColor)
            elif isinstance(widget, tk.Entry):
                widget.configure(bg="#1e1e2f", fg="#ffffff", insertbackground="#ffffff")
            elif isinstance(widget, tk.Text):
                widget.configure(bg="#1e1e2f", fg="#ffffff", insertbackground="#ffffff")
            elif widget_type == "TCombobox":
                self._style_ttk_combobox(widget, backgroundColor)
            # Weitere ttk Widgets hier einbauen

        except Exception as e:
            print(f"Fehler beim Anpassen von {widget}: {e}")

        # Rekursiv alle Kinder
        for child in widget.winfo_children():
            self._update_widget_colors(child, backgroundColor)

    def _style_ttk_combobox(self, widget, backgroundColor):
        try:
            style = ttk.Style()
            
            # Stelle sicher, dass das gewünschte Theme aktiv ist
            style.theme_use("default")

            # Nutze eine eindeutige Style-ID, um Konflikte zu vermeiden
            style_name = f"{widget.winfo_id()}.TCombobox"

            # Optional: Style vorher zurücksetzen (nicht direkt möglich, aber durch Neuvergabe)
            style.configure(style_name,
                            fieldbackground=backgroundColor,
                            background=backgroundColor,
                            foreground="#000000" if self._is_light_color(backgroundColor) else "#FFFFFF",
                            arrowcolor="#000000" if self._is_light_color(backgroundColor) else "#FFFFFF")

            widget.configure(style=style_name)
        except Exception as e:
            print(f"Fehler beim Stylen von Combobox: {e}")

    @staticmethod
    def reload_design_for_all_windows():
        global openWindows
        for wm in openWindows.values():
            wm.apply_theme()
        
    def print_all_open_window_titles():
        global openWindows
        print("Offene Fenster:")
        for title in openWindows:
            print(f"- {title}")


    def run(self):
        self.root.mainloop()

    