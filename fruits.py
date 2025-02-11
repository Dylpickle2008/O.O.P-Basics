class Fruit:
    def __init__(self, name, color, taste, price):
        self.name = name
        self.color = color
        self.taste = taste
        self.price = float(price)

    #Below: prints fruit details

    def details(self):
        print(f"""
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            Fruit Type: {self.name}
            Fruit Color: {self.color}
            Fruit Taste: {self.taste}
            Fruit Cost: {self.price}
            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~   
            """)

    def calc_sales_tax(self, tax):
        total = (self.price*tax) + self.price
        print(f"""
        #####################
        Total Cost: {self.name}: {total}
        #####################
        """)



apple = Fruit("Apple", "Red", "Sweet", 1.25)
pear = Fruit("Pear", "Green", "Bitter", 1.50)
strawberry = Fruit("Strawberry", "Red", "Tart", 3.75)

apple.details()
pear.details()
strawberry.details()

apple.calc_sales_tax(.04)
pear.calc_sales_tax(.04)
strawberry.calc_sales_tax(.04)

#print(f"Your fruit is {apple.name}, the color is {apple.color}.")
#Your fruit is {self.name}, the color is {self.color}, it has a {self.taste} taste.

