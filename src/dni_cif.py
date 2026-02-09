class Dni:
    def __init__(self):
        self.dni = ""
        self.numeroSano = None
        self.letraSana = None

    def getDni(self): #
        return self.dni
    
    def setDni(self, dni): #
        self.dni = dni

    def getNumeroSano(self): #
        return self.numeroSano
    
    def getLetraSana(self): #
        return self.letraSana
    
    def checkCIF(self): #
        if not self.dni or len(self.dni) < 2:
            return False
        
        letra = self.dni[-1]

        if letra in "IOUÑ": # Letras prohibidas en el CIF
            return False
        return True 

    def checkDni(self): #
        if len(self.dni) != 9:
            return False
        numero = self.dni[:-1]
        letra = self.dni[-1]
        if not numero.isdigit(): #
            return False
        self.numeroSano = int(numero)
        self.letraSana = "TRWAGMYFPDXBNJZSQVHLCKE"[self.numeroSano % 23]
        return True
    
    def checkLetra(self): #
        if not hasattr(self, "letraSana"): #
            return False
        return self.letraSana == self.dni[-1]
    
    def obtenerLetra(self): #
        if not hasattr(self, "letraSana"): #
            return None
        return self.letraSana
    
    def getParteAlfabeticaDni(self):
        return self.dni[-1]
    
    def getParteNumericaDni(self): #
        if not getattr(self, "numeroSano", False): #
            return ""
        return self.dni[:-1]
