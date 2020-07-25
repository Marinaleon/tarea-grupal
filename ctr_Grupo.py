from dao_Grupo import DaoGrupo
from mod_Grupo import ModGrupoCuenta
class CtrGrupo:
    def __init__(self, emp=None):
        self.empleado = emp

    def consulta(self, buscar):
        objDao = DaoGrupo()
        return objDao.consultar(buscar)

    def ingresar(self, emp):
        objDao = DaoGrupo()
        return objDao.ingresar(emp)

    def modificar(self, emp):
        objDao = DaoGrupo()
        return objDao.modificar(emp)

    def eliminar(self, emp):
        objDao = DaoGrupo()
        return objDao.eliminar(emp)

