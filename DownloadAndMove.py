import time
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/july_/Downloads"

#Classe Gerenciadora de eventos
class FileMovementHandler(FileSystemEventHandler):
    #Código para gerenciar o evento
    def on_created(self, event):
        #return super().on_created(event)
        
        print(event)
    
#inicialize a calsse Gerenciadora
event_handler = FileMovementHandler()

#inicialize o Observer
observer = Observer()

#Agende o Observer
observer.schedule(event_handler, from_dir, recursive=True)

#inicie o Observer
observer.start()

while True:
    time.sleep(2)
    print("executando...")
 
num_list = [5,0,2]

for elem in num_list:
    try:
        result = 5/elem
        print("O resultado de 5/", elem, "é", result)
    except ZeroDivisionError:
        print("opa! Houve um erro!")
    