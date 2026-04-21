from flask import Flask, request, jsonify
import os

app = Flask(__name__)

COULEURS = {
    "noir":        "#231f20",
    "blanc":       "#FFFFFF",
    "rouge":       "#D32F2F",
    "rose":        "#E91E8C",
    "bleu marine": "#1A237E",
    "bleu ciel":   "#29B6F6",
    "vert":        "#2E7D32",
    "mauve":       "#7B1FA2",
    "orange":      "#E65100",
    "turquoise":   "#00838F",
    "or":          "#F9A825",
    "gris":        "#616161",
}

TEMPLATES = {
    "maman":       "maman-bouquet-TEMPLATE.svg",
    "mamie":       "mamie-bouquet-TEMPLATE.svg",
    "grand-maman": "grand-maman-bouquet-TEMPLATE.svg",
    "mamou":       "mamou-bouquet-TEMPLATE.svg",
}

BASE_DIR = os
