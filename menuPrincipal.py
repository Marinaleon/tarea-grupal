from int_PlanCuentas import ejecutar_plancuenta
from int_Grupo import ejecutar_grupo
from funciones import *


def ejec():
    while True:
        paso=menu('MENU PRINCIPAL', ('GRUPOS', 'Plan cuentas', 'Salir'))
        if menu == '0':
            ejecutar_grupo()
        elif menu == '1':
            ejecutar_plancuenta()
        elif menu == '2':
            if valOpciones ('Salir'):
                print('<<<Gracias por usar el Sistema>>>')
                input('Presione enter para continuar')
                break

ejec()