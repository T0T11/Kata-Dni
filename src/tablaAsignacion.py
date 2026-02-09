class TablaAsignacion:

    def __init__(self): #
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]
    
    def getTabla(self): #
        return self.tabla
    
    def getLetra(self, posicion): #
        tabla = self.getTabla()
        if 0 <= posicion < len(tabla):
            return tabla[posicion]
        else:
            return "Posicion letra fuera de rango"
        
    def getModulo(self): #
        return 23
    
    def isLetraPermitida(self, letra): #
        return letra in self.getTabla()
    
    def calcularLetra(self, numero_dni): #
        modulo = self.getModulo()
        posicion = int(numero_dni) % modulo
        return self.getLetra(posicion)
    
    def __repr__(self) -> str:
        return ' '.join(self.getTabla())
