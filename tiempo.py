def segundos_a_minutos(segundos):
    return segundos/60

if __name__=="__main__":
    segundos = 150
    minutos = segundos_a_minutos(segundos)
    print(f"{segundos} segundos equivalen a {minutos} minutos")