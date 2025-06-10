# Projektidee:
# Ein Rechner im kleinen Zahlenbereich (Eingabezahlen 1-10)
# Kinderfreundliche Oberfläche
# Einfaches Rechnen ( + und -)

# Printausgabe für mich und spätere Text Idee

print("👋 Hallo, wollen wir ein wenig rechnen Üben? ")
print(" Das Spiel ist ganz einfach, du musst eine Zahl zwischen 1 und 10 eingeben.")
print(" Wir rechnen nur mit ➕ und ➖. ")
print(" Wenn du etwas falsch gemacht hat kommt ein ❌") 
print(" Wenn du etwas richtig gemacht hast, kommt ein ✅")
print(" Es ist nicht schlimm wenn du etwas falsch gemacht hast, wir wollen ja üben.")
print(" Denke einfach nochmal nach und versuche es erneut 🤔")
print(" Wenn du das schon alle könntest, bräuchtest du ja nicht mehr üben 😄")
print("Wollen wir Anfangen?🔢")
print("Zuerst überlegst du dir, welche zwei Zahlen du rechnen möchtest. Dann rechnest du die im Kopf. ")
print("Wenn du dein Ergebnis überprüfen möctest, schreib die Zahlen in den Rechner.")
try:
    
    zahl1 = int(input("Schreibe deine erste Zahl zwischen 1 und 10: "))
    if zahl1 < 1 or zahl1 >10:
            print("❌ Du Schlingel, nur zahlen von 1 bis 10, also 1,2,3,4,5,6,7,8,9,10 💡😄")
    else:
        aufgabe = input(" Möchtest du ➕ oder ➖ rechnen?🤔 Schreibe ➕ oder ➖ : ")
        if aufgabe not in ["+","-"]:
            print("❌ Bitte nur ➕ oder ➖")
        else:
            zahl2 = int(input(" Jetzt schreibe die zweite Zahl, welche du entweder dazuadieren ➕ oder suptrahieren ➖ rechnen möchtest: ")) 
            if zahl1 < 1 or zahl1 >10 or zahl2 <1 or zahl2 > 10:
                print("❌ Du Schlingel, nur zahlen von 1 bis 10, also 1,2,3,4,5,6,7,8,9,10 💡😄")
            elif aufgabe == "+":
                ergebnis =zahl1+zahl2
                if ergebnis>20:
                    print("❌ Wie hast du das geschafft? Wir wollten doch nur bis 20 rechnen!💡")
                else:
                    ergebniseingabe = int(input("🤔 Rechne im Kopf und schreibe dein Ergebnis hier hin: "))
                    if ergebnis == ergebniseingabe:
                        print(" \n 🎉 Super!Richtig! 🎉")
                        print("━━━━━━━━━━━━━━━━━━━━━━")
                        print(f"{zahl1}+{zahl2}={ergebnis}✅")
                        print("━━━━━━━━━━━━━━━━━━━━━━\n")
                    else:
                        print("❌ Dein Ergebnis ist leider falsch, versuche es nochmal!")
            elif aufgabe == "-":
                ergebnis = zahl1 - zahl2
                if ergebnis <0:
                    print("❌ Wenn wir so rechnen, kommen wir in den Minusbereich, das wollen wir noch nicht.❗")
                    print(" Das machen wir ein andereres mal, heute sagen wir, weniger als 0 geht nicht. 💡")
                else:
                    ergebniseingabe = int(input("🤔 Rechne im Kopf und schreibe dein Ergebnis hier hin: "))
                    if ergebnis == ergebniseingabe:
                        print("\n 🎉Super!Richtig! 🎉")
                        print("━━━━━━━━━━━━━━━━━━━━━━")
                        print(f"{zahl1}-{zahl2}={ergebnis}✅")
                        print("━━━━━━━━━━━━━━━━━━━━━━\n")
                    else:
                        print("❌ Dein Ergebnis ist leider falsch, versuche es nochmal!")
except ValueError:
    print("⚠️  Bitte gib eine Zahl ein! 💡 ")