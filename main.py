import json

def berechne_naechste_generation(jung, erwachsen, alt):
    # Berechnungen angepasst nach Feedback
    neue_jung = (4*erwachsen) + (2 * alt)
    neue_erwachsen = jung // 2
    neue_alt = erwachsen // 3

    return neue_jung, neue_erwachsen, neue_alt

def speichere_population_in_json(generationen, dateiname="population.json"):
    with open(dateiname, "w") as f:
        json.dump(generationen, f, indent=4)
    print(f"Ergebnisse wurden in {dateiname} gespeichert.")

def main():
    jung = int(input("Anzahl der Mäuse in Altersgruppe Jung: "))
    erwachsen = int(input("Anzahl der Mäuse in Altersgruppe Erwachsen: "))
    alt = int(input("Anzahl der Mäuse in Altersgruppe Alt: "))
    
    anzahl_generationen = int(input("Anzahl der zu berechnenden Generationen: "))
    
    generationen = []
    
    for _ in range(anzahl_generationen):
        generationen.append([jung, erwachsen, alt])
        
        jung, erwachsen, alt = berechne_naechste_generation(jung, erwachsen, alt)
    
    speichere_population_in_json(generationen)

if __name__ == "__main__":
    main()