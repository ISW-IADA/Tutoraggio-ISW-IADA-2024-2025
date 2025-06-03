"""
Esempio di utilizzo del debugger pdb per trovare e risolvere un bug.

Questo script mostra come usare breakpoint() per esaminare il problema
nella funzione mediana che abbiamo introdotto appositamente.
"""

from mathutils.stats import mediana

def main():
    # Creiamo un array di test che dovrebbe avere mediana = 2.5
    dati = [1, 2, 3, 4]
    
    print(f"Dati di input: {dati}")
    print("Calcolo della mediana...")
    
    # Inseriamo un breakpoint per esaminare l'esecuzione
    breakpoint()
    
    risultato = mediana(dati)
    
    print(f"La mediana calcolata è: {risultato}")
    print("Il valore corretto dovrebbe essere: 2.5")

if __name__ == "__main__":
    main()
