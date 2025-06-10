from flask import Flask , request, jsonify , render_template

app=Flask(__name__)

@app.route("/")
def startseite():
    return render_template("index.html")

@app.route("/rechnen",methods=["GET"])
def Kinderrechner():
    try:
        zahl1=int(request.args.get("zahl1"))
        zahl2=int(request.args.get("zahl2"))
        aufgabe=request.args.get("aufgabe")
        ergebniseingabe=int(request.args.get("ergebniseingabe"))

        if zahl1 not in range(1, 11) or zahl2 not in range(1, 11):
            return jsonify({
                "error":"❌ Du Schlingel, nur zahlen von 1 bis 10, also 1,2,3,4,5,6,7,8,9,10 💡😄"
                })
        
        if aufgabe not in ["+","-"]:
            return jsonify({
                "error":"❌ Bitte nur ➕ oder ➖"
                })
        
        if aufgabe == "+":
            ergebnis = zahl1 + zahl2
        else:
            ergebnis = zahl1 - zahl2

        if ergebnis>20:
            return jsonify({
                "error":"❌ Wie hast du das geschafft? Wir wollten doch nur bis 20 rechnen!💡"
                })
        
        if ergebnis <0:
            return jsonify({
                "error":"❌ Wenn wir so rechnen, kommen wir in den Minusbereich, das wollen wir noch nicht.❗Das machen wir ein andereres mal, heute sagen wir, weniger als 0 geht nicht. 💡"
                })
        
        if ergebnis == ergebniseingabe:
            return jsonify({
                "antwort": "🎉 Super!Richtig! 🎉",
                "rechnung": f"{zahl1}{aufgabe}{zahl2}={ergebnis}"
                })
        else:
            return jsonify({
                "antwort":"❌ Dein Ergebnis ist leider falsch, versuche es nochmal!",
                "deinErgebnis": ergebniseingabe,
                "richtig": ergebnis
            })

    except(ValueError, TypeError):

        return jsonify({
             "error": "⚠️ Ungültige Eingabe! Bitte gib nur Zahlen von 1 bis 10 ein."
            })

app.run(host="0.0.0.0")

