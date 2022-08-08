en = set("AaBCcEeHKMOoPpTXxy")
ru = set("АаВСсЕеНКМОоРрТХху")
a = {input() for i in range(3)}
if a.issubset(en):
    print('en')
elif a.issubset(ru):
    print('ru')
else:
    print('mix')
