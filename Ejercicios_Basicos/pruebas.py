lista_productos = [
    ("mantequilla", 1200),
    ("azúcar", 1000),
    ("arroz", 1200),
    ("fideos", 890),
    ("bebida 2L", 1800),
    ("galletas", 870),
]

def listar_productos(mis_productos):
    for i, producto in enumerate(mis_productos):
        print(f"{i+1}.- {producto[0]}")



listar_productos(lista_productos)