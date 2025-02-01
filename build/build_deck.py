import html
import os

import genanki
import yaml

# Define paths
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(PROJECT_ROOT_DIR, "templates")
CSS_DIR = os.path.join(PROJECT_ROOT_DIR, "css")
JS_DIR = os.path.join(PROJECT_ROOT_DIR, "js")
DATA_DIR = os.path.join(PROJECT_ROOT_DIR, "data")
OUTPUT_DIR = os.path.join(PROJECT_ROOT_DIR, "output")

# Load project components
with open(os.path.join(TEMPLATES_DIR, "front.html"), "r") as file:
    front_template = file.read()
with open(os.path.join(TEMPLATES_DIR, "back.html"), "r") as file:
    back_template = file.read()
with open(os.path.join(CSS_DIR, "styles.css"), "r") as file:
    css_styles = file.read()
with open(os.path.join(JS_DIR, "scripts.js"), "r") as file:
    js_scripts = file.read()

# Inject external JavaScript into the templates
front_template += f"\n<script>{js_scripts}</script>"
back_template += f"\n<script>{js_scripts}</script>"

# Define the model
model_id = 1607392319
my_model = genanki.Model(
    model_id,
    "Custom Model",
    fields=[
        {"name": "Front"},
        {"name": "Back"},
    ],
    templates=[
        {
            "name": "Card 1",
            "qfmt": front_template,
            "afmt": back_template,
        },
    ],
    css=css_styles,
)

# Create the deck
deck_id = 2059400110
my_deck = genanki.Deck(deck_id, "Sample Deck")

# Load notes from YAML instead of CSV
yaml_file_path = os.path.join(DATA_DIR, "cards.yaml")

with open(yaml_file_path, "r", encoding="utf-8") as file:
    cards = yaml.safe_load(file)

# for card in cards:
#     note = genanki.Note(
#         model=my_model,
#         fields=[card["front"], card["back"]],
#     )
#     my_deck.add_note(note)

for card in cards:
    front_text = html.escape(card["front"])  # Escape HTML special characters
    back_text = html.escape(card["back"])

    note = genanki.Note(
        model=my_model,
        fields=[front_text, back_text],
    )
    my_deck.add_note(note)

# Save the deck
output_path = os.path.join(OUTPUT_DIR, "anki_deck.apkg")
os.makedirs(OUTPUT_DIR, exist_ok=True)  # Ensure the directory exists
genanki.Package(my_deck).write_to_file(output_path)

print(f"Deck created: {output_path}")
