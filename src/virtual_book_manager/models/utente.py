#region Imports
from virtual_book_manager.models.libro import Libro
#endregion

class Utente:
    
    id = 4
    
    def __init__(self, nome: str):
        self.nome = nome
        # inizializza la lista dei libri prestati
        self.libri_prestati: list[Libro] = []
        # usa la variabile di classe Utente.id per assegnare l'id
        self.id_utente: int = Utente.id
        Utente.id += 1
    
    def prendi_in_prestito(self, libro: Libro) -> None:
        libro.presta()
        self.libri_prestati.append(libro)
    
    def restituisci(self, libro: Libro) -> None:
        libro.restituisci()
        self.libri_prestati.remove(libro)
    
    def mostra_libri_prestati(self) -> list[str]:
        return [libro.titolo for libro in self.libri_prestati]
    
    def __str__(self) -> str:
        return f"[{self.id_utente}]: {self.nome}"