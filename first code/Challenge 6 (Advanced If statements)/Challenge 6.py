charge = input("What is the charge for your order? ")
country = input("What country are you from? ")
country = country.lower()
charge = float(charge)
canada = False
alberta = False
onn = False
gst = ((0.05)/100) * charge
hst = ((0.13)/100) * charge
pst = ((0.06)/100) * charge
if country == "canada":
    province = input("What province do you live in? ")
    province = province.lower()
    if province == "alberta":
        alberta = True
    if province == "ontario" or "new brunswick" or "nova scotia":
        onn = True
    if alberta:
        totalcharge = charge + gst
        print("Your total cost for shipping is GHc {0:.2f}".format(totalcharge))
    elif onn:
        totalcharge = charge + hst
        print("Your total cost for shipping is GHc {0:.2f}".format(totalcharge))
    elif not alberta or not onn:
        totalcharge = charge + pst + hst
        print("Your total cost for shipping is GHc {0:.2f}".format(totalcharge))
else:
     print("Your total cost for shipping is GHc {0:.2f}".format(charge))