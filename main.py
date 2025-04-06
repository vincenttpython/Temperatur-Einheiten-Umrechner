# Geg.: Temperatur in Grad Celsius C
# Ges.: Temperatur in Kelvin K
# Ges.: Temperatur in Grad Fahrenheit F
# Ges.: Temperatur in Grad Rankine R
# K = C + 273.15
# F = C * 9/5 +32
# R = C * 9/5 + 491.67

def get_temperature():
    while True:
        C = input("Gib die Temperatur in Grad Celsius ein: ")
        try:
                C = float(C)
                return C
        except ValueError:
            print("Das ist keine gültige Angabe für eine Temperatur.")
def convert_to_kelvin(C):
    K = C + 273.15
    return K
def convert_to_fahrenheit(C):
    F = C * 9/5 + 32
    return F
def convert_to_rankine(C):
    R = C * 9/5 + 491.67
    return R

C = get_temperature()
if C >= -273.15:
    print("Das sind " + str(convert_to_kelvin(C)) + " Kelvin")
    print("Das sind " + str(convert_to_fahrenheit(C)) + " Grad Fahrenheit")
    print("Das sind " + str(convert_to_rankine(C)) + " Grad Rankine")
else:
    print("Der absolute Nullpunkt beträgt -273.15°C. Die gegebene Temperatur ist physikalisch nicht erreichbar. Erfahre mehr auf https://de.wikipedia.org/wiki/Absoluter_Nullpunkt")