from ctr_PlanCuentas import CtrPlanCuenta
from mod_PlanCuentas import ModPlanCuenta
from funciones import menu, valOpciones

ctr = CtrPlanCuenta()
def insertar(rango):
    for i in range(int(rango)):
        codigo = input('Ingrese codigo: ')
        grupo = input('Ingrese grupo: ')
        descripcion = input('Ingrese descripcion: ')
        naturaleza = input('Ingrese naturaleza: ')
        estado = input('Ingrese estado: ')
        gru = ModPlanCuenta(cod=codigo,gru=grupo, des=descripcion, nat=naturaleza, est=estado)
        if ctr.ingresar(gru):
            print('Registro grabado correctamente')
        else:
            print('Error al grabar el Registro')

def modificar():
    idpc =  input('Ingrese id: ')
    codigo = input('Ingrese codigo: ')
    grupo = input('Ingrese grupo: ')
    descripcion = input('Ingrese descripcion: ')
    naturaleza = input('Ingrese naturaleza: ')
    estado = input('Ingrese estado: ')
    pc = ModPlanCuenta(id= idpc,cod=codigo,gru=grupo, des=descripcion, nat=naturaleza, est=estado)
    if ctr.modificar(pc):
        print('Registro modificado correctamente')
    else:
        print('Error al modificar el Registro')

def eliminar():
    codigo = input('--Ingrese id: ')
    gru = ModPlanCuenta(cod=codigo)
    if ctr.eliminar(gru):
        print('Registro eliminado correctamente')
    else:
        print('Error al eliminar el Registro')

def consultar():
    buscar = input('Ingrese nombre a buscar: ')
    gru = ctr.consulta(buscar)
    print('Id   Codigo       Grupo      Descripcion     Naturaleza    Estado')
    for registro in gru:
        print('{:2} \t{:8} \t{:1}\t {:1} \t\t{:15}\t {:1}'.format(registro[0], registro[1], registro[2], registro[3], registro[4],registro[5],))

def ejecutar_plancuenta():
    opc = ''
    while opc != '4':
        opc = str(menu('Menu Plan de Cuentas',
            ('Ingresar', 'Modificar', 'Eliminar', 'Consultar', 'Salir'),
            ))
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
            if valOpciones ('Salir'):
                print('<<<Gracias por usar el Sistema>>>')
            break
        elif opc != '4':
            print('Seleccione una opción correcta')


