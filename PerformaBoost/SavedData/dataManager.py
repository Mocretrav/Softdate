import json
import os
from Applications.FileManager import fileFinder 

currentFolder = currentFolder = os.path.dirname(os.path.abspath(__file__))
sysDataPath = os.path.join(currentFolder, "SysData")


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
                print(f"Found in {filename}: {value}")
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
                print("Datei gefunden")
                print(data)
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
