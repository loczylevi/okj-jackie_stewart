#year   races/hany verseny    win   podiums/dobogos    poles/elso_helyrol_indul    fastests
with open("jackie.txt","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [sor.strip().split("\t") for sor in f]
    
print(f"3.feladat: {len(lista)}")

legtobb_verseny= [(sor[1], sor) for sor in lista]
leggtob, adatok = max(legtobb_verseny)

print(f"4.feladat: {adatok[0]}")

evek_70_es = sum([int(sor[2]) for sor in lista if 1970 <= int(sor[0]) <= 1979])
evek_60_as = sum([int(sor[2]) for sor in lista if 1960 <= int(sor[0]) <= 1969])

print(f"""5.feladat:
       70-es évek: {evek_70_es} megnyert verseny
       60-es évek: {evek_60_as} megnyert verseny""")

#6.feladat passz nem tom
