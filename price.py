price = float(input("Enter the price you bought the product: "))
transport = float(input("Enter the transport price: "))
seling = float(input("Enter the seling price:"))

remainingseling = seling - transport - price
vat = remainingseling - 0.18

print(f"The remaining seling price is {vat} ")

