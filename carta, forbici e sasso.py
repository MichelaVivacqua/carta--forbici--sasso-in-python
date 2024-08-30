import random

print("CARTA, FORBICI E SASSO 1.0")
# Dare il benvenuto al giocatore e chiedergli il nome, per messaggi personalizzati
print("Benvenuto al nostro nuovo minigioco! Inserisci il tuo nome")
nome_giocatore = input()

# Modalità invincibile
modalita_invincibile = input("Vuoi la modalità invincibile? Rispondi si o no      ").lower() == "si"
if modalita_invincibile:
    print("Modalità invincibile attivata!")

# Chiedi al giocatore quante partite vuole svolgere
print("Perfetto, " + nome_giocatore + "! Iniziamo! Quante partite vuoi giocare?")
num_partite = int(input())

# Inizializzare i punteggi
punteggio_giocatore = 0
punteggio_computer = 0

# Esegui il numero di partite richiesto
for i in range(num_partite):
    # Richiedere la scelta al giocatore
    print("Scegli tra CARTA, FORBICI e SASSO")
    scelta_giocatore = input().upper()

    # Assicurarsi che la scelta sia valida
    if scelta_giocatore not in ["CARTA", "FORBICI", "SASSO"]:
        print("Scelta non valida. Il gioco è finito. UFFA!")
        exit()
    else:
        SCELTE_POSSIBILI = ["CARTA", "FORBICI", "SASSO"]
        if modalita_invincibile:
            if scelta_giocatore == "CARTA":
                scelta_computer = "SASSO"
            elif scelta_giocatore == "FORBICI":
                scelta_computer = "CARTA"
            elif scelta_giocatore == "SASSO":
                scelta_computer = "FORBICI"
            else:
               scelta_computer = random.choice(SCELTE_POSSIBILI)
               print("Il computer ha scelto:", scelta_computer)

        # Determinare il vincitore
        if scelta_giocatore == scelta_computer:
            risultato = "Pareggio!"
        elif (scelta_giocatore == "CARTA" and scelta_computer == "SASSO") or \
             (scelta_giocatore == "FORBICI" and scelta_computer == "CARTA") or \
             (scelta_giocatore == "SASSO" and scelta_computer == "FORBICI"):
            risultato = "Hai vinto!"
            punteggio_giocatore += 1
        else:
            risultato = "Hai perso!"
            punteggio_computer += 1

        # Stampare il risultato
        print("Risultato della partita", i + 1, ":", risultato)

# Decretare il vincitore finale
print("Punteggio finale:")
print(nome_giocatore + ": " + str(punteggio_giocatore))
print("Computer: " + str(punteggio_computer))

if punteggio_giocatore > punteggio_computer:
    print("Complimenti " + nome_giocatore + ", hai vinto la serie di partite! " + str(punteggio_giocatore) + " a " + str(punteggio_computer))
elif punteggio_giocatore < punteggio_computer:
    print("Il computer ha vinto la serie di partite. " + str(punteggio_computer) + " a " + str(punteggio_giocatore) + ". Ritenta, sarai più fortunato!")
else:
    print("La serie di partite è terminata in pareggio! " + str(punteggio_giocatore) + " a " + str(punteggio_computer))

# Congedo personalizzato
print("Grazie per aver giocato,", nome_giocatore + "! Alla prossima!")
