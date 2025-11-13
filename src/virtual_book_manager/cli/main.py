#region Imports
from virtual_book_manager.manager import *
from virtual_book_manager.models import *
from types import SimpleNamespace
#endregion

def mostra_menu():
    return """
[MENU] Seleziona un'opzione:
[1] Mostra libri disponibili
[2] Aggiungi libro
[3] Registra utente
[4] Presta libro
[5] Restituisci libro
[6] Mostra utenti
[7] Mostra libri prestati di un utente
[8] Esci
"""

def gestione_input(libreria: Libreria) -> bool:
    scelta = input("Scelta: ").strip()
    match scelta:
        case "1":
            try:
                disponibili = libreria.mostra_libri_disponibili()
            except Exception:
                disponibili = [l for l in getattr(libreria, "libri", []) if getattr(l, "disponibile", True)]
            if not disponibili:
                print("Nessun libro disponibile.")
            else:
                for b in disponibili:
                    print(str(b))
            return True

        case "2":
            titolo = input("Titolo: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno: ").strip())
            except Exception:
                anno = 0
            # creazione di new dict se in libro assente
            try:
                libro = Libro(titolo, autore, anno)
            except Exception:
                # create a simple shim object if Libro is unavailable
                def _presta():
                    shim.disponibile = False

                def _restituisci():
                    shim.disponibile = True

                shim = SimpleNamespace(
                    titolo=titolo,
                    autore=autore,
                    anno=anno,
                    disponibile=True,
                    presta=_presta,
                    restituisci=_restituisci,
                    __str__=lambda: f'"{titolo}": ({autore})\nPubblicato: {anno}\nDisponibile: {"✅" if True else "❌"}',
                )
                libro = shim

            if hasattr(libreria, "aggiungi_libro"):
                libreria.aggiungi_libro(libro)
            else:
                getattr(libreria, "libri", []).append(libro)
            print("Libro aggiunto.")
            return True

        case "3":
            nome = input("Nome utente: ").strip()
            try:
                utente = Utente(nome)
            except Exception:
                shim = SimpleNamespace(
                    nome = nome,
                    id_utente = None,
                    libri_prestati = [],
                    prendi_in_prestito = lambda l: shim.libri_prestati.append(l),
                    restituisci = lambda l: shim.libri_prestati.remove(l) if l in shim.libri_prestati else None,
                    mostra_libri_prestati = lambda: [getattr(x, "titolo", str(x)) for x in shim.libri_prestati],
                    __str__ = lambda: f"[{getattr(shim, 'id_utente', 'n/a')}]: {nome}"
                )
                utente = shim

            if hasattr(libreria, "registra_utente"):
                libreria.registra_utente(utente)
            else:
                getattr(libreria, "utenti", []).append(utente)
            print(f"Utente registrato: {utente}")
            return True

        case "4":
            titolo = input("Titolo da prestare: ").strip()
            try:
                id_u = int(input("ID utente: ").strip())
            except Exception:
                print("ID utente non valido")
                return True
            if hasattr(libreria, "presta_libro"):
                libreria.presta_libro(titolo, id_u)
            else:
                utente = next((u for u in getattr(libreria, "utenti", []) if getattr(u, "id_utente", None) == id_u), None)
                libro = next((l for l in getattr(libreria, "libri", []) if getattr(l, "titolo", None) == titolo), None)
                if utente and libro:
                    if hasattr(utente, "prendi_in_prestito"):
                        utente.prendi_in_prestito(libro)
                    else:
                        getattr(utente, "libri_prestati", []).append(libro)
                    print("Prestito effettuato.")
                else:
                    print("Utente o libro non trovato.")
            return True

        case "5":
            titolo = input("Titolo da restituire: ").strip()
            try:
                id_u = int(input("ID utente: ").strip())
            except Exception:
                print("ID utente non valido")
                return True
            if hasattr(libreria, "restituisci_libro"):
                libreria.restituisci_libro(titolo, id_u)
            else:
                utente = next((u for u in getattr(libreria, "utenti", []) if getattr(u, "id_utente", None) == id_u), None)
                libro = next((l for l in getattr(libreria, "libri", []) if getattr(l, "titolo", None) == titolo), None)
                if utente and libro:
                    if hasattr(utente, "restituisci"):
                        utente.restituisci(libro)
                    else:
                        try:
                            getattr(utente, "libri_prestati", []).remove(libro)
                        except ValueError:
                            pass
                    print("Restituzione effettuata.")
                else:
                    print("Utente o libro non trovato.")
            return True

        case "6":
            try:
                utenti = libreria.mostra_utenti()
            except Exception:
                utenti = getattr(libreria, "utenti", [])
            if not utenti:
                print("Nessun utente registrato.")
            else:
                for u in utenti:
                    print(str(u))
            return True

        case "7":
            try:
                id_u = int(input("ID utente: ").strip())
            except Exception:
                print("ID utente non valido")
                return True
            utente = next((u for u in getattr(libreria, "utenti", []) if getattr(u, "id_utente", None) == id_u), None)
            if not utente:
                print("Utente non trovato")
            else:
                try:
                    libri = utente.mostra_libri_prestati()
                except Exception:
                    libri = [getattr(l, "titolo", str(l)) for l in getattr(utente, "libri_prestati", [])]
                print("Libri prestati:", ", ".join(libri) if libri else "nessuno")
            return True

        case "8":
            return False

    print("Opzione non valida")
    return True

def run():
    libreria = Libreria()
    if not hasattr(libreria, "libri") or libreria.libri is None:
        libreria.libri = []
    if not hasattr(libreria, "utenti") or libreria.utenti is None:
        libreria.utenti = []

    running = True
    while running:
        print(mostra_menu())
        running = gestione_input(libreria)

if __name__ == "__main__":
    run()