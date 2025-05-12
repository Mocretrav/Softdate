import os

def findFilePath(fileName):
    path = ""
    
    #als erstes in PerformanceBoost suchen.
    try:
        path = os.path.abspath("PerformaBoost")
    except (FileNotFoundError):
        print("Application PerformaBoost not found")
        #TODO fuege suche hinzu wenn Applikation nicht gefunden.
        #TODO speichere pfad und aktualisiere wenn gespeicherter nicht klappt
        return ""
 
    for wurzel, ordner, dateien in os.walk(path):
        if fileName in dateien:
            return os.path.join(wurzel,fileName)

    return path




def existsFile(fileName):
    if findFilePath == "":
        return false
    return true

