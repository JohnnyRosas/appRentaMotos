import sqlite3
class Cliente:
    def __init__(self):
        self.db= sqlite3.connect("db/dbRentas.db") #coneccion a la base de datos
        self.CI=""
    def consultarCliente(self, CI):
        #consulta para obtener un cliente a partir de su CI
        cliente=self.db.execute("""SELECT * FROM TClientes WHERE CI='{}'""".format(CI)).fetchone()
        return cliente

class Moto:
    def __init__(self):
        self.db=sqlite3.connect("db/dbRentas.db")
    #metodo para ejecutar la consulta de las motos disponibles de una categoria
    def consultarMotosDisponibles(self, categoria):
        motos_disponibles= self.db.execute("""
                                            SELECT 
                                                m.NroMotor,
                                                m.chasis,
                                                m.placa,
                                                m.modelo,
                                                m.detalle,
                                                m.estado,
                                                m.tarifaHr,
                                                c.nombre AS categoria,
                                                ma.nombre AS marca
                                            FROM TMotos m
                                            JOIN TCategorias c ON m.categoriaID = c.categoriaID
                                            JOIN TMarcas ma ON m.marcaID = ma.marcaID
                                            WHERE c.nombre='{}' AND m.estado='DISPONIBLE'
                                                    """.format(categoria)).fetchall()
        return motos_disponibles
    #metodo que obtiene la moto para la renta por medio de su Nro. de motor
    def consultarMoto(self, id):
        moto=self.db.execute("""
                                SELECT 
                                    m.NroMotor,
                                    m.chasis,
                                    m.placa,
                                    m.modelo,
                                    m.detalle,
                                    m.estado,
                                    m.tarifaHr
                                    c.nombre AS categoria,
                                    ma.nombre AS marca
                                FROM TMotos m
                                JOIN TCategorias c ON m.categoriaID = c.categoriaID
                                JOIN TMarcas ma ON m.marcaID = ma.marcaID
                                WHERE m.NroMotor='{}'
                             """.format(id)).fetchone()
        return moto
class Renta:
    def __init__(self):
        self.db=sqlite3.connect("db/dbRentas.db")
    #metodo para realizar el calculo del monto a pagar por el cliente
    def calcularMonto(self, tarifa, horas):
        return tarifa*horas
    #metodo para guardar una renta de moto a un cliente
    def guardar(self,fecha, fi, ff, tarifa, cant, monto, CI,NroMotor):
        self.db.execute("""
                            INSERT INTO TRentas (fecha,hora_inicio,hora_fin,cantidad_horas,tarifa,total,estado,CI,NroMotor) 
                            VALUES('{}','{}','{}',{},{},{},'EN PROCESO','{}','{}')
                        """.format(fecha,fi,ff,cant,tarifa,monto,CI, NroMotor))
        self.db.commit()  
Cliente=Cliente()
print(Cliente.consultarCliente("1234567"))