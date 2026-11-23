from banco_dados import *

def liberar_slots_servidor(banco_dados, id_evento, qtd_liberada):
    if id_evento in banco_dados["eventos_live"]:
        if qtd_liberada <= 0:
            return -1
        else:
            banco_dados["eventos_live"][id_evento]["slots_servidor"] += qtd_liberada
            return banco_dados["eventos_live"][id_evento]["slots_servidor"]
    return -1

print(liberar_slots_servidor(banco_dados, 101, 5))
