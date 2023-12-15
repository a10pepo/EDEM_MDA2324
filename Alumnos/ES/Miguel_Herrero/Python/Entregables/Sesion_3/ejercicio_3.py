def es_bisiesto(ano):
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def identificar_bisiesto(lista_anos):
    for ano in lista_anos:
        if es_bisiesto(ano):
            print(f"{ano} es un año bisiesto.")
        else:
            print(f"{ano} no es un año bisiesto.")

if __name__ == "__main__":
    anos_a_verificar = [1965, 1944, 1992, 2010, 2001, 1444, 2104]
    identificar_bisiesto(anos_a_verificar)
