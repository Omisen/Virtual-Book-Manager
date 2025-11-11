#region Imports
from models.libro import Libro
#endregion

class Utente:
    def __init__(self, nome: str):
        self.nome = nome
        self.id_utente: int #! rivedere
        self.libri_prestati: list[Libro]
    
    def prendi_in_prestito(self, libro: Libro) -> None:
        libro.presta()
        self.libri_prestati.append(libro)
    
    def restituisci(self, libro: Libro) -> None:
        libro.restituisci()
        self.libri_prestati.remove(libro)
    
    def mostra_libri_prestati(self) -> list[str]:
        return [libro.titolo for libro in self.libri_prestati]
    