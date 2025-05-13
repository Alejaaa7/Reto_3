import math 

class Point:
    def __init__(self, x:float, y: float):
        self.x = x
        self.y = y

class Line:
    def __init__(self, start: Point, end: Point):
# aquí se calculan y almacenan los valores dentro del constructor,porque
# en el enunciado nos dicen que lenght y slope son atributos, entonces es
# mejor que el usuario no los deba pasar, y los calculemos solo teniendo
# los puntos incial y final:      
        self.start = start
        self.end = end
        self.length = self.compute_length() 
        self.slope = self.compute_slope()
        self.points = [] #esto es para el opcional

    def compute_length(self):
# aquí se buscan los delta x y y, para calcular la hipotenusa entre ellos, 
# o sea, el largo de la línea:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
# aquí llamamos math.hypot para hallar la hipotenusa de dicho "triángulo":
        return math.hypot(dx, dy)

    def compute_slope(self):
# volvemos a definir dx y dy:
        dx = self.end.x - self.start.x
        dy = self.end.y - self.start.y
# usamos math.atan2 que calcula el ángulo de una pendiente usando dy y 
# dx, pero este los devuelve en radianes, entonces usamos math.degrees 
# para convertir los radianes a grados:
        return math.degrees(math.atan2(dy, dx))
    
    def compute_horizontal_cross(self)-> bool:
# primero creamos dos variables y1 y y2, no es completamente indispensable,
# pero es para que las siguientes líneas de código se entiendan más
# fácilmente.
        y1 = self.start.y
        y2 = self.end.y
# ahora se analiza que si alguno de los puntos y inicial o final son 0,
# automáticamente la línea cruzará el eje horizontal, o si el valor del
# inicial y el final son de distinto signo (su producto es negativo), 
# significa que la línea cruza el eje horizontal:
        
        return y1 == 0 or y2 == 0 or (y1 * y2 < 0)
    
    def compute_vertical_cross(self)-> bool:
# se hace un proceso similar al anterior, pero esta vez analizando los 
# puntos x inicial y final.
        x1 = self.start.x
        x2 = self.end.x

        return x1 == 0 or x2 == 0 or (x1 * x2 < 0)
    
#EL OPCIONAL:
    def discretize_line(self, n: int):
# se definen los puntos inicial y final de la línea:
        x1, y1 = self.start.x, self.start.y
        x2, y2 = self.end.x, self.end.y

# se crea un for para repertir el proceso n veces para generar n puntos 
# igualmente espaciados:
        for i in range(n):
# se calcula la coordenada de cada punto, usando interpolación lineal*
            x = x1 + i * (x2 - x1) / (n - 1)
            y = y1 + i * (y2 - y1) / (n - 1)
# se crea una instancia de Point con las coordenadas que calculamos:
            new_point = Point(x, y)
#se agrega a la lista de puntos usando el "add" como vimos en clase:
            self.points.append(new_point) 

class Rectangle:
    def __init__(self, left: Line, right: Line, top: Line, bottom: Line):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom

    def compute_area(self):
        return self.left.length * self.top.length

    def compute_perimeter(self):
        return (self.left.length + self.right.length + self.top.length + 
    self.bottom.length)
    
# interpolación espacial : se calculó  la coordenada de cada punto,  
# tomando el largo de la línea y dividiéndolo en las n veces menos 1, 
# porque estamos dividiendo la línea en n puntos igualmente espaciados, 
# entonces necesitamos dividir el segmento entre sus puntos extremos en 
# n - 1 partes iguales, entonces cada x es el punto inicial más cada i 
# veces cada segmento.


# Probar la clase Line
p1 = Point(-1, -1)
p2 = Point(2, 3)
line = Line(p1, p2)

print(f"Longitud: {line.length:.2f}")
print(f"Pendiente: {line.slope:.2f}°")
print(f"Cruza eje X: {line.compute_horizontal_cross()}")
print(f"Cruza eje Y: {line.compute_vertical_cross()}")

# Probar discretización
line.discretize_line(5)
print("Puntos discretizados:")
for i, pt in enumerate(line.points):
    print(f"  Punto {i+1}: ({pt.x:.2f}, {pt.y:.2f})")

# Probar la clase Rectangle
top = Line(Point(0, 3), Point(4, 3))
bottom = Line(Point(0, 0), Point(4, 0))
left = Line(Point(0, 0), Point(0, 3))
right = Line(Point(4, 0), Point(4, 3))
rect = Rectangle(left, right, top, bottom)

print(f"\nÁrea del rectángulo: {rect.compute_area():.2f}")
print(f"Perímetro del rectángulo: {rect.compute_perimeter():.2f}")
