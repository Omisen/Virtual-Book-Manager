#region Imports
from models.libro import Libro
from models.utente import Utente
#endregion

class Libreria:
    def __init__(self):
        self.libri: list[Libro] 
        self.utenti: list[Utente]
    
    