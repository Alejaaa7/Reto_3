# Primero se define la clase MenuItem, que representa un elemento del 
# menú. Esta clase tiene atributos como nombre y precio, y un método 
# para calcular el precio total.

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def calculate_total_price(self, quantity: int) -> float:
        return self.price * quantity
    
# Ahora se crean subclases para diferentes tipos de elementos del menú:
    
class Beverage(MenuItem):
    def __init__(self, name: str, price: float):
        super().__init__(name, price)
    
    def calculate_total_price(self, quantity: int) -> float:
        # Se añade un impuesto del 10% para las bebidas:
        return super().calculate_total_price(quantity) * 1.1 
    
class Appetizer(MenuItem):
    def __init__(self, name:str, price: float, flavor: str):
        super().__init__(name, price)
        self.flavor = flavor

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float,type_of_cooking: str):
        super().__init__(name, price)
        self.type_of_cooking = type_of_cooking

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, type_of_dessert: str):
        super().__init__(name, price)
        self.type_of_dessert = type_of_dessert

# Luego, se define la clase Order, que representa un pedido. Esta clase
# tiene métodos para agregar elementos al pedido, calcular el total de la
# cuenta y aplicar descuentos.También tiene un método para imprimir los 
# detalles del pedido.
class Order:
    def __init__(self):
        self.items = []
    
    def add_item(self, item: MenuItem, quantity: int):
        self.items.append((item, quantity))
    
    def calculate_total_bill(self): # -> float:
        total = 0
        for item, quantity in self.items:
            total += item.calculate_total_price(quantity)
        return total
    
    def apply_discount(self, discount_percentaje: float=0):
        total = self.calculate_total_bill()
        if total > 100000:
        # Aplica un descuento adicional del 5% si el total es mayor a 100
            discount_percentaje += 10 
        elif total > 50000:
            discount_percentaje += 5
        
        discount = total * (discount_percentaje / 100)

        return total - discount
    
# Se define un método para imprimir los detalles del pedido, incluyendo
# los elementos, cantidades y precios totales. También se imprime el total
# de la cuenta y el total con descuento:
    def print_order(self):
        print("Los detalles del pedido son:")
        for item, quantity in self.items:
            print(f"{item.name} (x{quantity}): "
        f"${item.calculate_total_price(quantity):.2f}")
        print(f"Total sin descuento: ${self.calculate_total_bill():.2f}")
        print(f"Total con descuento: ${self.apply_discount():.2f}")

# Ahora, se le presenta el menú al cliente y se le permite hacer un pedido:

print("Bienvenido al restaurante. Aquí está nuestro menú:")
print("1. BEBIDAS:" \
    "- Coca Cola - $5000" \
    "- Limonada - $3000" \
    "- Sprite - $2500" \
    "- Jugo - $4500"\
    "- Agua - $1000")

print("2. APERITIVOS:" \
    "- Nachos - $5000" \
    "- Frutitas - $7000" \
    "- Chips - $2000" \
    "- Empanaditas - $1500"\
    "- Sopa - $6000")

print("3. PLATOS FUERTES:" \
    "- Spaguetti - $25000" \
    "- Ajiaco - $20000" \
    "- Sushi - $30000" \
    "- Curry verde de pollo - $35000"
    "- Tacos - $23000")

print("4. POSTRES:" \
    "- Helado de Vainilla - $4000" \
    "- Pastel de Chocolate- $8000" \
    "- Cheesecake - $9000" \
    "- Brownie - $5000" \
    "- Helado de Chocolate - $4500")

order = Order()

# Se le pregunta al cliente si desea agregar un elemento al pedido.
# Si la respuesta es "Sí", se le pide que seleccione una categoría del menú:

while True:
    print("¿Desea agregar un elemento al pedido? (Sí o No): ")
    choice = input().strip().lower()

# Se verifica si la respuesta es "no" o "sí":
# Si la respuesta es "no", se imprime el total de la cuenta y se
# finaliza el programa:
    if choice == "no":
        print("Gracias por su visita. Hasta luego, que tenga un buen día.")
        break
# Si la respuesta es "sí", se le pide al cliente que seleccione una 
#ccategoría del menú:
    elif choice == "sí" or choice == "si":
        category = input("Seleccione la categoría del menú (Bebida, " \
        "Aperitivo, Plato Fuerte, Postre): ").strip().lower()
# Se verifica la categoría seleccionada:
# Si la categoría es "bebida", se le pide al cliente que seleccione
# una bebida del menú y se agrega al pedido usando el método
# add_item de la clase Order:
        if category == "bebida":
            beberage = input("Seleccione la bebida: ")
            if beberage == "coca cola":
                order.add_item(Beverage("Coca Cola", 5000), 1)
            elif beberage == "lemonade":
                order.add_item(Beverage("Lemonade", 3000), 1)
            elif beberage == "sprite":
                order.add_item(Beverage("Sprite", 2500), 1)
            elif beberage == "jugo":
                order.add_item(Beverage("Jugo", 4500), 1)
            elif beberage == "agua":
                order.add_item(Beverage("Agua", 1000), 1)
# Si la categoría es "aperitivo", se le pide al cliente que seleccione
# un aperitivo del menú y se agrega al pedido usando el método:
        elif category == "aperitivo":
            appetizer = input("Seleccione el aperitivo: ")
            if appetizer == "nachos":
                order.add_item(Appetizer("Nachos", 5000, "Salty"), 1)
            elif appetizer == "frutitas":
                order.add_item(Appetizer("Frutitas", 7000, "Sweet"), 1)
            elif appetizer == "chips":
                order.add_item(Appetizer("Chips", 2000, "Salty"), 1)
            elif appetizer == "empanaditas":
                order.add_item(Appetizer("Empanaditas", 1500, \
                                         "Salty"), 1)
            elif appetizer == "sopa":
                order.add_item(Appetizer("Sopa", 6000, "Salty"), 1)

# Si la categoría es "plato fuerte", se le pide al cliente que seleccione
# un plato fuerte del menú y se agrega al pedido usando el método:
        elif category == "plato fuerte":
            main_course = input("Seleccione el plato fuerte: ")
            if main_course == "spaguetti":
                order.add_item(MainCourse("Spaguetti", 25000, \
                                          "Italian food"), 1)
            elif main_course == "ajiaco":
                order.add_item(MainCourse("Ajiaco", 20000,\
                                           "Colombian food"), 1)
            elif main_course == "sushi":
                order.add_item(MainCourse("Sushi", 30000,\
                                           "Japanese food"), 1)
            elif main_course == "curry verde de pollo":
                order.add_item(MainCourse("Curry verde de pollo",\
                                           35000, "Indian food"), 1)
            elif main_course == "tacos":
                order.add_item(MainCourse("Tacos", 23000, \
                                          "Mexican food"), 1)
                
# Si la categoría es "postre", se le pide al cliente que seleccione
# un postre del menú y se agrega al pedido usando el método:
        elif category == "postre":
            dessert = input("Seleccione el postre: ")
            if dessert == "helado de vainilla":
                order.add_item(Dessert("Helado de Vainilla", 4000, \
                                       "Ice Cream"), 1)
            elif dessert == "pastel de chocolate":
                order.add_item(Dessert("Pastel de Chocolate", 8000, \
                                       "Cake"), 1)
            elif dessert == "cheesecake":
                order.add_item(Dessert("Cheesecake", 9000, "Cake"), 1)
            elif dessert == "brownie":
                order.add_item(Dessert("Brownie", 5000, "Cake"), 1)
            elif dessert == "helado de chocolate":
                order.add_item(Dessert("Helado de Chocolate", 4500, \
                                       "Ice Cream"), 1)
        else:
            print("Categoría no válida. Por favor, intente de nuevo.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")

# Finalmente, se imprime el total de la cuenta y se finaliza el programa:

order.print_order() 
