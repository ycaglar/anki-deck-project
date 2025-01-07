import csv
import os

import genanki

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
with open(os.path.join(TEMPLATES_DIR, "styles.css"), "r") as file:
    css_styles = file.read()

# Load external JavaScript and inject it into the templates
with open(os.path.join(TEMPLATES_DIR, "scripts.js"), "r") as f:
    js_script = f.read()

# Inject external JavaScrip into the templates
front_template += f"\n<script>{js_script}</script>"
back_template += f"\n<script>{js_script}</script>"

# Define the model
model_id = 1607392319
my_model = genanki.Model(
    model_id,
    "Custom Model",
    fields=[
        {"name": "Question"},
        {"name": "Answer"},
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

# Add notes from CSV
with open(DATA_DIR, "r") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        note = genanki.Note(
            model=my_model,
            fields=[row["Question"], row["Answer"]],
        )
        my_deck.add_note(note)

# Save the deck
os.makedirs(os.path.dirname(OUTPUT_DIR), exist_ok=True)
genanki.Package(my_deck).write_to_file(OUTPUT_DIR)
print(f"Deck created: {OUTPUT_DIR}")
