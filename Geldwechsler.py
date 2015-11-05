import math
from prettytable import PrettyTable

def execute(zahl):
      muenz_liste = init()
      muenz_liste = zahl_in_muenzen_zerlegen(zahl, muenz_liste)
      ausgabe_erstellen(muenz_liste)

def init():
      muenz_liste = {2.00:0,1.00:0,0.50:0,0.20:0,0.10:0,0.05:0,0.02:0,0.01:0}
      return muenz_liste

      def numeric_compare(x, y):
        return x - y

def zahl_in_muenzen_zerlegen(zahl, muenz_liste):
      keys = list(muenz_liste)
      sortierte_keys = sorted(keys, reverse=True)

      for key in sortierte_keys:
            if key <= zahl:
                  anzahl = zahl / key
                  anzahl = math.trunc(anzahl)
                  muenz_liste[key] = anzahl
                  zahl = zahl - anzahl * key

      return muenz_liste

def ausgabe_erstellen(muenz_liste):
      tabelle = PrettyTable(['1', '2'])
      for key in muenz_liste:               
            tabelle.add_row([key, muenz_liste[key]])
      print(tabelle)
      
if __name__ == '__main__':
      execute(1.55)

      
