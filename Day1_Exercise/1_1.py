def convert_to_usd(krw):
    usd=round(krw/1300,2)
    return usd

def convert_to_krw(usd):
    krw=round(usd*1300,2)
    return krw

krw1=15000
usd1=convert_to_usd(krw1)
usd2=2.08
krw2=convert_to_krw(usd2)
print(f"{krw1} won is equivalent to {usd1}")
print(f"{krw2} won is equivalent to {usd2}")


