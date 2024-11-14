import abc
from datetime import datetime

# Absztrakt autó osztály
class Auto(abc.ABC):
    def __init__(self, rendszam, tipus, berleti_dij):
        self.rendszam = rendszam
        self.tipus = tipus
        self.berleti_dij = berleti_dij
        self.elerheto = True  # Az autó elérhető-e bérlésre

    @abc.abstractmethod
    def __str__(self):
        pass

# Személyautó osztály
class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)


    def __str__(self):
        return f"Személyautó {self.rendszam}, {self.tipus},  {self.berleti_dij} Ft/nap"

# Teherautó osztály
class Teherauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij):
        super().__init__(rendszam, tipus, berleti_dij)


    def __str__(self):
        return f"Teherautó {self.rendszam}, {self.tipus}, {self.berleti_dij} Ft/nap"

# Bérlés osztály
class Berles:
    def __init__(self, auto, berles_nap):
        self.auto = auto
        self.berles_nap = berles_nap
        self.osszeg = auto.berleti_dij * berles_nap

    def __str__(self):
        return f"{self.auto} - Bérlés ideje: {self.berles_nap} nap, Összeg: {self.osszeg} Ft"

# Autókölcsönző osztály
class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []  # Autók listája
        self.berlesek = []  # Aktuális bérlések listája

    def autok_adatfeltoltese(self):
        # Autók előre feltöltése
        self.autok.append(Szemelyauto("BNH-444", "Wolswagen Golf", 5000 ))
        self.autok.append(Szemelyauto("DEF-456", "Honda Civic", 6000))
        self.autok.append(Teherauto("GHI-789", "Ford Focus", 9500))


    def autok_berlese(self, rendszam, berles_nap):
        # Autó bérlésének kezelése
        for auto in self.autok:
            if auto.rendszam == rendszam and auto.elerheto:
                auto.elerheto = False
                berles = Berles(auto, berles_nap)
                self.berlesek.append(berles)
                return f"Sikeres bérlés: {berles}"
        return "Ez az autó már nem elérhető!"

    def berlesek_listazasa(self):
        # Aktuális bérlések listázása
        if self.berlesek:
            for berles in self.berlesek:
                print(berles)
        else:
            print("Nincs aktív bérlés.")

    def berles_lemondasa(self, rendszam):
        # Bérlés lemondása
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                berles.auto.elerheto = True
                self.berlesek.remove(berles)
                return f"Bérlés lemondva: {berles}"
        return "Nem található ilyen bérlés."

# Fájlkezelés és adatok kiírása
def kiir_adatok():
    with open("adatok.txt", "w") as file:
        file.write("Név: Tran Quoc Le Anh\n")
        file.write("Szak: Üzemmérnök-informatikus\n")
        file.write("Neptun kód: G5IFEU\n")

def main():
    # Autókölcsönző létrehozása és adatfeltöltés
    kolcsonzo = Autokolcsonzo("XY Autókölcsönző")
    kolcsonzo.autok_adatfeltoltese()

    while True:
        print("\n--- Autókölcsönző Rendszer ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Válasszon egy opciót (1-4): ")

        if valasztas == '1':
            rendszam = input("Adja meg a bérlendő autó rendszámát: ")
            berles_nap = int(input("Hány napra szeretné bérelni? "))
            print(kolcsonzo.autok_berlese(rendszam, berles_nap))
        elif valasztas == '2':
            rendszam = input("Adja meg a lemondandó bérlés rendszámát: ")
            print(kolcsonzo.berles_lemondasa(rendszam))
        elif valasztas == '3':
            kolcsonzo.berlesek_listazasa()
        elif valasztas == '4':
            print("Köszönjük, hogy igénybe vette a szolgáltatásunkat!")
            break
        else:
            print("Érvénytelen választás! Kérem válasszon újra.")

if __name__ == "__main__":

    main()
