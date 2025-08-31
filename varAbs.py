#Se crea el dato abstracto "Persona"

class Persona:

    #Esta clase representa a una persona

    def __init__(self):
        self.nombre = ""
        self.apPaterno = ""
        self.apMaterno = ""

    def mostrar_nombre_completo(self):
        return print(self.nombre,self.apPaterno,self.apMaterno)
    
p1 = Persona()
p1.nombre = "David"
p1.apPaterno = "López"
p1.apMaterno = "Návarez" 

p2 = Persona()
p3 = Persona()
p4 = Persona()
p5 = Persona()

array = [p1,p2,p3,p4,p5]
array[0].mostrar_nombre_completo()
