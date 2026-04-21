from flask import Flask, request, jsonify

app = Flask(__name__)

COULEURS = {
    "noir": "#231f20",
    "blanc": "#FFFFFF",
    "rouge": "#D32F2F",
    "rose": "#E91E8C",
    "bleu marine": "#1A237E",
    "bleu ciel": "#29B6F6",
    "vert": "#2E7D32",
    "mauve": "#7B1FA2",
    "orange": "#E65100",
    "turquoise": "#00838F",
    "or": "#F9A825",
    "gris": "#616161",
}

with open("templates/grand-maman-bouquet-TEMPLATE.svg") as f:
    TEMPLATE = f.read()

@app.route("/generer", methods=["POST"])
def generer():
    data = request.json
    texte = data.get("custom_text", "")
    text_color = COULEURS.get(data.get("text_color", "").lower(), "#231f20")
    design_color = COULEURS.get(data.get("design_color", "").lower(), "#231f20")
    svg = TEMPLATE
    svg = svg.replace("{{custom_text}}", texte)
    svg = svg.replace("{{text_color}}", text_color)
    svg = svg.replace("{{design_color}}", design_color)
    return jsonify({"svg": svg, "status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
