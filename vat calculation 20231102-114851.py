pcs=int(input("how much item:"))
item_price=float(input("how much price :"))

without_vat=(pcs*item_price)
vat_range=int(input("how much vat: "))
vat=(without_vat*vat_range)/100
total_ammount=(without_vat+vat)
print('total_without vat: ',without_vat)
print('total amount with vat: ',total_ammount)
    