add10 = False
purchase = input("How much did you payfor your shipping? ")
purchase = float(purchase)
if float(purchase) < 50.0:
    add10 = True
if add10:
    purchase = float(purchase)+10.0
print("Your total purchase is GHc {0:.2f}".format(purchase))