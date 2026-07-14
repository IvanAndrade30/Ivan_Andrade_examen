import os
os.system('cls')

productos = {
    'M001': ['Alimento Premium', 'comida', 'DogPlus', 10, True, False],
    'M002': ['Arena Aglomerante', 'higiene', 'CatClean', 8, False, False],
    'M003': ['Snack Dental', 'snack', 'BiteJoy', 1, True, True],
    'M004': ['Shampoo Suave', 'higiene', 'PetCare', 0.5, False, True],
    'M005': ['Correa Nylon', 'accesorio', 'WalkPro', 0.3, True, False],
    'M006': ['Cama Mediana', 'accesorio', 'CozyPet', 2, False, False],
    
} 

stock = {
    'M001': [32990, 12],
    'M002': [9990, 0],
    'M003': [5490, 25],
    'M004': [7990, 5],
    'M005': [11990, 7],
    'M006': [24990, 3],
    
}

def menu():
    os.system('cls')
    print('========== MENU PRINCIPAL ==========')
    print('1. Unidades por categoria')
    print('2. Busqueda de productos por rango de precio')
    print('3. Actualizar precio de producto')
    print('4. Agregar producto')
    print('5. Eliminar producto')
    print('6. Salir')
    print('=====================================')

def seleccionar_opcion():
    while True:
        try:
            opcion=int(input('Ingresa una opcion: '))
        
            if opcion <= 1 or opcion >= 6:
                return opcion
            print('la opcion debe ser numerica')
        except:
            error_numerico()
            return opcion

    

def error_numerico():
    print('la opcion debe ser numerica')
    input('enter para continuar')


def unidades_categorias(categoria):
    total = 0
    for codigo in productos:
        if productos[codigo][1].loser() == categoria.loser():
            total= stock[codigo][1]


def buscar_precio(precio_min,precio_max):
    resultados =[]
    for codigo in stock:
        precio=stock[codigo][0]
        unidades=stock[codigo][1]
    if precio_min <= precio <= precio_max and unidades 1 = 0:


def agregar_producto():
    pass

def eliminar_producto():
    pass

def buscar_nombre():
    pass

def precio_min():
    pass

def precio_max():
    pass

def buscar_producto():
    pass

def actualizar_precio():
    pass

def unidades_categoria():
    pass




def main():
    while True:
        menu()
        opcion = seleccionar_opcion()
        match opcion:
            case 1:
                unidades_categoria()
            case 2:
                buscar_producto()
            case 3:
                actualizar_precio()
            case 4:
                agregar_producto()
            case 5:
                eliminar_producto()
            case 6:
                print('salir.')
                break

main()
            

