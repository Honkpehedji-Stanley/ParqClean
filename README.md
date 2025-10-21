# ParqClean

Pipeline simple pour nettoyer des CSV et produire des fichiers Parquet optimisés.

## 🚀 But
Ingest → Validate → Transform → Export (Parquet). Notebook publicisé via GitHub Pages.

## 🧱 Stack
Python, Pandas, PyArrow, Click, PyTest, Jupyter, GitHub Actions

## ⚙️ Usage rapide
### 1. Créer venv & installer :
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
### 2. Lancer le pipeline :
parqclean --input data/raw/*.csv --output data/clean/ --partition year country
### 3. Voir le notebook rendu sur GitHub Pages :
`https://<ton-user>.github.io/ParqClean/ParqClean_demo.html`

## 🧪 Tests
pytest -q