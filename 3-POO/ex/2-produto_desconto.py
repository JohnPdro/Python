class Produto :
    def __init__(self, price, name) :
        self.price = price
        self.name = name
    
    def __str__(self) :
        return f"Produto: {self.name} - R${self.price}"
    
    def discount(self, perc_discount) :
        valorDiscount = (self.price / 100) * perc_discount
        finalPrice = self.price - valorDiscount
        
        print(f"O novo valor é R${finalPrice}")
        
sabao = Produto(300.00, "Omo")
sabao.calc_desconto(15)
