from flask import Flask, request, jsonify
import os

app = Flask(__name__)

COULEURS = {
    "blanc": "#FFFFFF",
    "noir":  "#231f20",
    "rose":  "#F4A1A7",
    "lilas": "#CB90BF",
}

TEMPLATES = {
    "maman":       "maman-bouquet-TEMPLATE.svg",
    "mamie":       "mamie-bouquet-TEMPLATE.svg",
    "grand-maman": "grand-maman-bouquet-TEMPLATE.svg",
    "mamou":       "mamou-bouquet-TEMPLATE.svg",
}

BASE_DIR = os.path.dirname(__file__)

def charger_template(variante):
    nom_fichier = TEMPLATES.get(variante.lower().strip())
    if not nom_fichier:
        return None, f"Variante inconnue: {variante}"
    chemin = os.path.join(BASE_DIR, nom_fichier)
    if not os.path.exists(chemin):
        return None, f"Fichier introuvable: {nom_fichier}"
    with open(chemin, encoding="utf-8") as f:
        return f.read(), None

@app.route("/generer", methods=["POST"])
def generer():
    data = request.json
    if not data:
        return jsonify({"error": "Aucune donnée reçue"}), 400
    texte = data.get("custom_text", "").strip()
    text_color = COULEURS.get(data.get("text_color", "").lower().strip(), "#231f20")
    design_color = COULEURS.get(data.get("design_color", "").lower().strip(), "#231f20")
    variante = data.get("variante", "maman").strip()
    svg, erreur = charger_template(variante)
    if erreur:
        return jsonify({"error": erreur}), 400
    svg = svg.replace("{{custom_text}}", texte)
    svg = svg.replace("{{text_color}}", text_color)
    svg = svg.replace("{{design_color}}", design_color)
    return jsonify({"svg": svg, "status": "ok", "variante": variante})

@app.route("/", methods=["GET"])
def accueil():
    return jsonify({"status": "en ligne", "variantes": list(TEMPLATES.keys()), "couleurs": list(COULEURS.keys())})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
