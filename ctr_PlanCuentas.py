from dao_PlanCuenta import DaoPlanCuenta
from mod_PlanCuentas import ModPlanCuenta
class CtrPlanCuenta:
    def __init__(self, emp=None):
        self.empleado = emp

    def consulta(self, buscar):
        objDao = DaoPlanCuenta()
        return objDao.consultar(buscar)

    def ingresar(self, emp):
        objDao = DaoPlanCuenta()
        return objDao.ingresar(emp)

    def modificar(self, emp):
        objDao = DaoPlanCuenta()
        return objDao.modificar(emp)

    def eliminar(self, emp):
        objDao = DaoPlanCuenta()
        return objDao.eliminar(emp)

