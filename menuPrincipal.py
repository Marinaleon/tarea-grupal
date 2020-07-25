from int_PlanCuentas import ejecutar_plancuenta
from int_Grupo import ejecutar_grupo
from funciones import menuprincipal, valOpciones


def ejec():
    while True:
        opc= menuprincipal(('GRUPOS', 'Plan cuentas', 'Salir'),'MENU PRINCIPAL')
        if opc == '0':
            ejecutar_grupo()
        elif opc == '1':
            ejecutar_plancuenta()
        elif opc == '2':
            if valOpciones ('Salir'):
                print('<<<Gracias por usar el Sistema>>>')
                input('Presione enter para continuar')
            break    
ejec()
