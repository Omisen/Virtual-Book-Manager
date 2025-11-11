#region Imports
from models.libro import Libro
from models.utente import Utente
#endregion

class Libreria:
    def __init__(self):
        self.libri: list[Libro] 
        self.utenti: list[Utente]
    
    def aggiungi_libro(self, libro: Libro) -> None:
        self.libri.append(libro)
        
    def registra_utente(self, utente: Utente) -> None:
        self.utenti.append(utente)
        
    def presta_libro(self, titolo: str, id_utente: int) -> None:
        pass