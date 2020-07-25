from ctr_Grupo import CtrGrupo
from mod_Grupo import ModGrupoCuenta
from funciones import menu

ctr = CtrGrupo()
def insertar(rango):
    for i in range(int(rango)):
        descripcion = input('Ingrese descripcion: ')
        
        gru = ModGrupoCuenta(des=descripcion)
        if ctr.ingresar(gru):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar el Registro')

def modificar():
    codigo = input('Ingrese id: ')
    descripcion = input('Ingrese descripcion: ')
    gru = ModGrupoCuenta(cod=codigo,des=descripcion)
    if ctr.modificar(gru):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar el Registro')

def eliminar():
    codigo = input('--Ingrese id: ')
    gru = ModGrupoCuenta(cod=codigo)
    if ctr.eliminar(gru):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar el Registro')

def consultar():
    buscar = input('Ingrese nombre a buscar: ')
    gru = ctr.consulta(buscar)
    print('  Codigo   Descripcion')
    for registro in gru:
        print('{:7} {:3}'.format(registro[0], registro[1]))

def ejecutar_grupo():
    opc = ''
    while opc != '4':
        opc = str(menu(
            ['Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Salir'],
            'Menu Grupo'))
        if opc == '0':
            print('\n<<<Insertar datos>>> ')
            valor = input('-Ingrese cantidad de datos a Ingresar')
            insertar(valor)
        elif opc == '1':
            print('\n<<<Modificar datos>>>')
            modificar()
        elif opc == '2':
            print('\n<<<Eliminar datos>>>')
            eliminar()
        elif opc == '3':
            print('\n<<<Consultar datos>>>')
            consultar()
        elif opc == '4':
            print('<<<Gracias por usar el Sistema>>>')
        elif opc != '4':
            print('Seleccione una opción correcta')
ejecutar_grupo()