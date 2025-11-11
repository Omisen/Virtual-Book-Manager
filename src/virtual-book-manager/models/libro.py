class Libro:
    def __init__(self, titolo: str, autore: str, anno: int):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.disponibile: bool = True
    
    def presta(self) -> None:
        self.disponibile = False
    
    def restituisci(self) -> None:
        self.disponibile = True
    
    def to_dict(self) -> dict:
        return {
            "titolo" : self.titolo,
            "autore" : self.autore,
            "anno" : self.anno,
            "disponibile" : self.disponibile
        }
        
    def __str__(self):
        return f"\"{self.titolo}\": ({self.autore})\nPubblicato: {self.anno}\nDisponibile: {"✅" if self.disponibile else "❌"}"