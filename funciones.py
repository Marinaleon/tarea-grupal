

def menu(titulo,opciones = ('Ingresar','Consultar','Modificar', 'Eliminar', 'Retornar al menu principal')):
    print('^'*20)
    print('{}'.format(titulo))
    print('^'*20)
    for op in range(0, len(opciones)):
        print("{}) {}".format(op, opciones[op]))
    opc = input('Elija Opcion [0...{}]: '.format(len(opciones)-1))
    return opc

def valOpciones(args):        
    bol='Usted a seleccionado la opcion '+args+'. ¿Desea continuar? [y/N]   '
    var = input(bol).upper()
    while not (var == 'N' or var == 'Y'):
        os.system('cls||clear')
        var = input(bol).upper()
    if var == 'N':
        print('Operacion cancelada.', 'a')
        bol= False
    else:
        bol=True
    return bol