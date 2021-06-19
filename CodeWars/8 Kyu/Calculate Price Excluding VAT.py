def excluding_vat_price(price):
    if price==None or price==0:
        return -1
    else:
        return round(price/1.15,2)