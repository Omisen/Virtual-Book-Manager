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
        # next((utente for utente in self.utenti if utente.id_utente == id_utente), None).prendi_in_prestito(next((libro for libro in self.libri if libro.titolo == titolo), None))
        if (utente := next((utente for utente in self.utenti if utente.id_utente == id_utente), None)) and (libro := next((libro for libro in self.libri if libro.titolo == titolo), None)):
            utente.prendi_in_prestito(libro)
        else:
            print(f"{"Libro" if not libro else "Utente" if not utente else "Ne Libro e ne Utente"} non trovato")
    
    def restituisci_libro(self, titolo: str, id_utente: int) -> None:
        if (utente := next((utente for utente in self.utenti if utente.id_utente == id_utente), None)) and (libro := next((libro for libro in self.libri if libro.titolo == titolo), None)):
            utente.restituisci(libro)
        else:
            print(f"{"Libro" if not libro else "Utente" if not utente else "Ne Libro e ne Utente"} non trovato")
        
    def mostra_libri_disponibili(self) -> list[Libro]:
        return [libro for libro in self.libri if libro.disponibile]
    
    def mostra_utenti(self) -> list[Utente]:
        return self.utenti