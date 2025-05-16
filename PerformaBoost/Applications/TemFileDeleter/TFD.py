import os
import shutil
import tkinter as tk
from tkinter import scrolledtext
from Prefabs import windowManager
from Prefabs.windowManager import WindowManager

def delete_temp_files():
    temp_paths = []
    try:
        temp_paths.append(os.environ['TEMP'])
    except KeyError:
        pass

    temp_paths.append('C:\\Windows\\Temp')
    

    deleted_items = []

    for temp_path in temp_paths:
        try:
            # Speicherplatz vor dem Löschen abrufen
            space_before = shutil.disk_usage(temp_path).free

            for item in os.listdir(temp_path):
                try:
                    item_path = os.path.join(temp_path, item)
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                        deleted_items.append(item_path)
                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                        deleted_items.append(item_path)
                except PermissionError as e:
                    print(f"Zugriff verweigert bei {item_path}: {e}")
                except OSError as e:
                    print(f"Fehler beim Löschen von {item_path}: {e}")

            # Speicherplatz nach dem Löschen abrufen
            space_after = shutil.disk_usage(temp_path).free
            freed_space = space_after - space_before

            show_deleted_items(deleted_items, freed_space)

        except PermissionError as e:
            print(f"Zugriff verweigert auf den Ordner {temp_path}: {e}")
        except Exception as e:
            print(f"Ein Fehler ist aufgetreten: {e}")


def show_deleted_items(deleted_items, freed_space):
    num_deleted_items = len(deleted_items)
    message = (
        f"{num_deleted_items} {'Element' if num_deleted_items == 1 else 'Elemente'} gelöscht, "
        f"{freed_space / (1024*1024):.2f} MB Speicherplatz freigegeben:\n"
        + "\n".join(deleted_items)
        if num_deleted_items > 0
        else "Keine temporären Elemente gefunden."
    )




    # Tkinter GUI für die Anzeige der gelöschten Elemente
    result_window = WindowManager("Gelöschte Elemente")
    

    # Setze Mindestgröße für das Fenster
    result_window.root.minsize(300, 60)

    # ScrolledText-Widget hinzufügen und der Größe des Fensters anpassen
    result_text = scrolledtext.ScrolledText(result_window.root, width=40, height=10, wrap="word")
    result_text.insert(tk.END, message)
    result_text.pack(expand=True, fill="both", padx=10, pady=10)

    # Schleifenaufruf für Tkinter GUI
    result_window.run()


def createTempFileDeleterWindow():
    # Tkinter GUI
    windowManager = WindowManager("Temp File Deleter", "800x600")
    windowManager.root.minsize(135, 65)

    # Button zum Löschen der Temp Elemente
    delete_button = tk.Button(windowManager.root, text="Delete Temp Items", command=delete_temp_files)
    delete_button.pack(pady=20)

    # Starte die GUI
    windowManager.run()
