from .cli import run
from .manager import Libreria
from .models import *


#per l'esportazione clobale fuori da "/src"
__all__ = ["run","Libreria","Libro","Utente"]