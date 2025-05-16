import json
import os
from Applications.FileManager import fileFinder 

currentFolder = currentFolder = os.path.dirname(os.path.abspath(__file__))
sysDataPath = os.path.join(currentFolder, "SysData")

class ThemeStyleManager:
    def __init__(self, theme_name):
        """
        Initialize the ThemeStyleManager with a specific theme.
        Loads the style data from style.json.
        
        Args:
            theme_name (str): Name of the theme to load (e.g., 'dark-mode' or 'light-mode')
        """
        self.theme_name = theme_name
        self.style_data = self._load_theme_data()

    def _load_theme_data(self):
        """Load the theme data from style.json"""
        style_path = os.path.join(sysDataPath, "style.json")
        try:
            with open(style_path, 'r') as file:
                data = json.load(file)
                if self.theme_name in data:
                    return data[self.theme_name]
                else:
                    raise ValueError(f"Theme '{self.theme_name}' not found in style.json")
        except FileNotFoundError:
            raise FileNotFoundError(f"Could not find style.json at {style_path}")

    def get_style_value(self, key):
        """
        Get a style value by its key.
        
        Args:
            key (str): The style key to retrieve
            
        Returns:
            The value associated with the key, or None if not found
        """
        return self.style_data.get(key)


def getKeyValueFromFile(path, key, secondkey=None):
    try:
        with open(path,'r') as file:
            data = json.load(file)
            if secondkey is not None:
                if key in data and secondkey in data[key]:
                    return data[key][secondkey]
            else:
                if key in data:
                    return data[key]
    except FileNotFoundError:
            print("The file was not found.")
    except json.JSONDecodeError:
            print("Error decoding JSON.")
    except KeyError:
        print("Key not found in Function getKeyValueFromFile")
    except Exception as e:
        print(f"Unexpected Error in File {path}: {e}")

    return None

def findAndGetKeyValue(key, secondkey=None):
    keyValue = ""
   
    for filename in os.listdir(sysDataPath):
        if filename.endswith(".json"):
            file_path = os.path.join(sysDataPath, filename)
            value = getKeyValueFromFile(file_path, key, secondkey)
            if value is not None:
                return value
    print("Key not found in Function getKeyValue")
    return ""

def getKeyValueWithFileName(filename, key, secondkey=None):
    file_path = os.path.join(sysDataPath, filename)
    
    return getKeyValueFromFile(file_path, key, secondkey)

def setKeyValue(filename, key, value):
    file_path = os.path.join(sysDataPath, filename)

    try:
        # Falls Datei nicht existiert, leeres Dictionary verwenden
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                data = json.load(file)
        else:
            print("Datei " + file_path + "nicht vorhanden")
            return
        print(value)
        
        # Wert setzen
        data[key] = value
        



        # Datei überschreiben
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        print("Wert erfolgreich gespeichert.")
    except Exception as e:
        print(f"Fehler beim Speichern in Datei {file_path}: {e}")
