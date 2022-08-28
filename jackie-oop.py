class Jackie_stewart:
    def __init__(self,sor):
        ev,verseny,nyert,dobogos,elso,gyors = sor.strip().split("\t")
        self.ev = int(ev)
        self.verseny = int(verseny)
        self.nyert = int(nyert)
        self.dobogos = int(dobogos)
        self.elso = int(elso)
        self.gyors = int(gyors)
    
with open("jackie.txt","r",encoding="utf-8") as f:
    fejlec = f.readline()
    lista = [Jackie_stewart(sor) for sor in f]
    
print(f"3.feladat: {len(lista)}")

legtobb_verseny= [(sor.verseny, sor) for sor in lista]
leggtob, adatok = max(legtobb_verseny)

print(f"4.feladat: {adatok.ev}")

evek_70_es = sum([sor.nyert for sor in lista if 1970 <= sor.ev <= 1979])
evek_60_as = sum([sor.nyert for sor in lista if 1960 <= sor.ev <= 1969])

print(f"""5.feladat:
       70-es évek: {evek_70_es} megnyert verseny
       60-es évek: {evek_60_as} megnyert verseny""")

#6.feladat passz nem tom
