from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

etudiants = []

@app.route('/')
def index():
    return render_template("index.html", etudiants=etudiants)

@app.route('/etudiants', methods=['GET'])
def get_etudiants():
    return jsonify(etudiants)

@app.route('/etudiants', methods=['POST'])
def add_etudiant():
    # Vérifie si c'est un formulaire HTML ou une requête API
    if request.form:
        nom = request.form.get("nom")
        age = request.form.get("age")
        etudiants.append({"nom": nom, "age": age})
        return redirect(url_for("index"))
    else:
        data = request.get_json()
        etudiants.append(data)
        return jsonify({"message": "Étudiant ajouté avec succès"}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5008)
