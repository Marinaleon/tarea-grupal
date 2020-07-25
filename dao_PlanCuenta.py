import sys
from conexion import Conector

class DaoPlanCuenta(Conector):
    def __init__(self):
        super().__init__()

    def consultar(self, buscar):
        result = False
        try:
            sql = "Select id_PC id, codigo cod, grupo gru, descripcion des, naturaleza nat, estado est From plancuenta where descripcion like '%" + str(buscar) + "%' order by id"
            print(sql)
            self.conectar()
            self.conector.execute(sql)
            result = self.conector.fetchall()
            self.conn.commit()
        except Exception as e:
            print("Error en la consulta del grupo",e)
            self.conn.rollback()
        finally: self.cerrar()
        return result

    def ingresar(self, pc):
        correcto = True
        try:
            sql = "insert into plancuenta (codigo, grupo, descripcion, naturaleza, estado) values (%s, %s,%s,%s,%s)"
            self.conectar()
            self.conector.execute(sql, (pc.codigo, pc.grupo, pc.descripcion, pc.naturaleza, pc.estado ))
            self.conn.commit()
        except Exception as e:
            print("Error al insertar plan de cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def modificar(self, pc):
        correcto = True
        try:
            sql = 'Update plancuenta set codigo = %s, grupo = %s ,descripcion = %s, naturaleza = %s, estado = %s where id_PC = %s'
            self.conectar()
            self.conector.execute(sql, (pc.codigo, pc.grupo, pc.descripcion, pc.naturaleza, pc.estado,pc.id_PC))
            self.conn.commit()
        except Exception as e:
            print("Error al modificar plan de cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto

    def eliminar(self, pc):
        correcto = True
        try:
            sql = 'delete from plancuenta where id_PC = %s'
            self.conectar()
            self.conector.execute(sql, (pc.id_PC))
            self.conn.commit()
        except Exception as e:
            print("Error al eliminar plan de cuenta",e)
            correcto = False
            self.conn.rollback()
        finally: self.cerrar()
        return correcto


""" con = DaoPlanCuenta()
grupo = con.consultar("")
print(grupo) 
for pc in grupo: 
    print(pc[1])  """