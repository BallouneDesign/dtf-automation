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

@app.route("/generer", methods=["POST"]
