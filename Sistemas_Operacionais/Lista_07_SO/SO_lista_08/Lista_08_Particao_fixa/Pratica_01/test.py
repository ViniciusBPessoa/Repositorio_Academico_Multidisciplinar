import math

from memoria import Memoria
from processo import Processo

y = Processo(1, "Valorant", 3, 7)
z = Processo(2, "Photoshop", 3, 1)
x = Memoria(10,2)
x.inicializador_particao()
x.aloca_processo(y, "First-fit")
x.aloca_processo(z, "First-fit")
x.remove_processo(y.espacos_memoria)
x.to_string()