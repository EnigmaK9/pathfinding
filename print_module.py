# print_module.py
def print_path(matriz):
    print("===========================================")
    # Visualizamos A1 y A2
    for fila in matriz:
        for valor in fila:
            if valor == 0:
                print(".", end=" ")
            elif valor == 1:
                print("#", end=" ")
            elif valor == 2:
                print("A1", end=" ")
            elif valor == 3:
                print("A2", end=" ")
            elif valor == 5:
                print("G", end=" ")
            elif valor == "x":
                print("x", end=" ")
            elif valor == "y":
                print("y", end=" ")
        print()
    print("===========================================")
