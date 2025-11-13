#region Imports
from virtual_book_manager.models import *
#endregion

class Libreria:
    def __init__(self):
        # inizializza le collezioni
        self.libri: list[Libro] = []
        self.utenti: list[Utente] = []
    
    def aggiungi_libro(self, libro: Libro) -> None:
        self.libri.append(libro)
        
    def registra_utente(self, utente: Utente) -> None:
        self.utenti.append(utente)
        
    def presta_libro(self, titolo: str, id_utente: int) -> None:
        # next((utente for utente in self.utenti if utente.id_utente == id_utente), None).prendi_in_prestito(next((libro for libro in self.libri if libro.titolo == titolo), None))
        utente = next((u for u in self.utenti if getattr(u, "id_utente", None) == id_utente), None)
        libro = next((l for l in self.libri if getattr(l, "titolo", None) == titolo), None)
        if libro is None:
            print("Libro non trovato")
            return
        if utente is None:
            print("Utente non trovato")
            return
        utente.prendi_in_prestito(libro)
    
    def restituisci_libro(self, titolo: str, id_utente: int) -> None:
        utente = next((u for u in self.utenti if getattr(u, "id_utente", None) == id_utente), None)
        libro = next((l for l in self.libri if getattr(l, "titolo", None) == titolo), None)
        if libro is None:
            print("Libro non trovato")
            return
        if utente is None:
            print("Utente non trovato")
            return
        utente.restituisci(libro)
        
    def mostra_libri_disponibili(self) -> list[Libro]:
        return [libro for libro in self.libri if libro.disponibile]
    
    def mostra_utenti(self) -> list[Utente]:
        return self.utenti
    
    def salva_dati(self, path: str) -> None:
        pass
    
    def carica_dati(self, path: str) -> None:
        pass