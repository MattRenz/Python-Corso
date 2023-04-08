""""Trova la parola più lunga all'interno di una lista"""


frase = input("Scrivi una frase")

parole = frase.split() #inserisce le parole all'interno di una lista
print(parole) #stampa le parole in una lista

print("")

lunghezza = 0 #variabile 0 che aumenterà al numero del carattere pi gande
risposte = [] #lista vuota

for x in parole:  #leggi le parole
    l = len(x) #restituisci la lunghezza di ogni singola parola
        
    if l > lunghezza: #se la variabile "l" è più grande della variabile lunghezza allora:
        risposte = [x] #risposte, la lista vuota, diventerà la parola più lunga

        lunghezza = l #e la lunghezza della parola più grande prenderà il posto della varaibile l
        
    elif l == lunghezza: #se la vairabile "l" è uguale alla variabile lunghezza:
        risposte.append(x) #aggiungi alla lista risposte la parola

print(f'Le parole più lunghe sono {risposte}, lunghe {lunghezza}') #stampa la parola più lunga e la lunghezza della parola



