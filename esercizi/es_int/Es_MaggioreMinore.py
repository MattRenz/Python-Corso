""" Confronta due numeri e distingue se è maggiore minore o uguale"""

def maggiore_minore():
    """Riconosce se due numeri sono fra loro maggiori minori o uguali
    """
    par1 = input("Numero1")
    par2 = input("Numero2")

    if int(par1) > int(par2):
        print("Numero 1 è magiore di Numero 2")
    elif int(par1) == int (par2):
        print("Numero 1 è uguale numero 2")
    else:
        print("Numero 1 è minore di Numero 2")

maggiore_minore()
