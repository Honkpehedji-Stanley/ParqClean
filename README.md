# ParqClean

Pipeline simple pour nettoyer des CSV et produire des fichiers Parquet optimisés.

## 🚀 But
Ingest → Validate → Transform → Export (Parquet). Notebook publicisé via GitHub Pages.

## 🧱 Stack
Python, Pandas, PyArrow, Click, PyTest, Jupyter, GitHub Actions

## 📦 Installation

### 1. Cloner le projet
```bash
git clone https://github.com/Honkpehedji-Stanley/ParqClean.git
cd ParqClean
```

### 2. Créer un environnement virtuel et installer les dépendances
```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Installer le package en mode développement
```bash
pip install -e .
```

## 🔨 Build

### Option 1 : Utiliser le package Python directement (Recommandé)
Après l'installation avec `pip install -e .`, la commande `parqclean` est directement disponible dans votre environnement virtuel.

### Option 2 : Construire un exécutable standalone avec PyInstaller
Pour créer un binaire exécutable (Linux/Mac/Windows) :

```bash
# Installer PyInstaller si nécessaire
pip install pyinstaller

# Construire l'exécutable
pyinstaller parqclean.spec

# L'exécutable sera disponible dans dist/parqclean
```

**Note :** Les binaires générés ne sont pas versionnés (dossier `bin/` ignoré dans `.gitignore`) car ils sont spécifiques à chaque plateforme.

## ⚙️ Usage

### Commande de base
```bash
parqclean --input data/raw/*.csv --output data/clean/
```

### Avec partitionnement
```bash
parqclean --input data/raw/*.csv --output data/clean/ --partition year country
```

### Options disponibles
- `--input`, `-i` : Fichiers CSV à traiter (peut être spécifié plusieurs fois ou avec wildcard)
- `--output`, `-o` : Répertoire de sortie pour les fichiers Parquet
- `--partition`, `-p` : Colonnes pour partitionner les données (optionnel)

### Exemple complet
```bash
# Activer l'environnement virtuel
source .venv/bin/activate

# Lancer le pipeline
parqclean -i data/raw/sales_2023.csv -i data/raw/sales_2024.csv -o data/clean/ -p year -p country

# Ou avec wildcard
parqclean -i data/raw/*.csv -o data/clean/ -p year country
```

## 🧪 Tests
```bash
pytest -q
```

## 📊 Notebooks
Voir le notebook de démonstration rendu sur GitHub Pages :
`https://Honkpehedji-Stanley.github.io/ParqClean/ParqClean_demo.html`

## 🛠️ Développement

### Structure du projet
```
ParqClean/
├── parqclean/          # Code source principal
│   ├── cli.py          # Interface ligne de commande
│   ├── ingest.py       # Lecture des CSV
│   ├── validate.py     # Validation des données
│   ├── transform.py    # Transformations
│   └── io.py           # Export Parquet
├── tests/              # Tests unitaires
├── notebooks/          # Notebooks Jupyter
├── data/               # Données (ignorées par git)
│   ├── raw/            # CSV bruts
│   └── clean/          # Parquet générés
├── setup.py            # Configuration du package
├── parqclean.spec      # Configuration PyInstaller
└── requirements.txt    # Dépendances Python
```