class TablaAsignacion:
    def getTabla(self): #
        return [
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
