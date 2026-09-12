# Analyse spatiale du réseau Vélib'

Une exploration interactive du réseau Vélib' Métropole : localisation des stations, triangulation de Delaunay, zones de couverture de Voronoï et arbre couvrant minimal.

Le projet produit un mini-portfolio statique : une page d'accueil permet de parcourir les quatre analyses et chaque carte possède son propre habillage explicatif.

## Aperçu

| Analyse | Ce qu'elle montre |
| --- | --- |
| Stations | Position et capacité de chaque station |
| Delaunay | Proximité spatiale entre stations voisines |
| Voronoï | Zone géographique la plus proche de chaque station |
| Arbre couvrant minimal | Réseau connecté avec un nombre minimal de liens |

Les fonds de carte utilisent les tuiles Esri, afin de ne pas dépendre du serveur de tuiles OpenStreetMap public.

## Prérequis

- Python 3.10 ou plus récent
- Une connexion Internet (uniquement pour récupérer les données Vélib' et afficher le fond de carte)

## Installation

```bash
git clone https://github.com/zaydc/analyse-velib.git
cd analyse-velib
python -m venv venv
```

Activez ensuite l'environnement virtuel :

```powershell
# Windows PowerShell
.\venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source venv/bin/activate
```

Installez les dépendances :

```bash
pip install -r requirements.txt
```

## Générer le portfolio complet

Exécutez ces commandes depuis la racine du projet :

```bash
python src/data/process_data.py
python src/data/liste_adjacence.py

# Windows PowerShell
$env:PYTHONPATH = "src;src/data"
$env:MPLBACKEND = "Agg"

python src/visualization/view_map_stations.py
python src/data/indice_repartition.py
python src/visualization/voronoi_map.py
python src/visualization/arbre_couvrant.py
python src/build_portfolio.py
```

Ouvrez ensuite `index.html` dans votre navigateur. C'est le point d'entrée du portfolio ; il donne accès à toutes les cartes générées.

> Sous macOS/Linux, remplacez `src;src/data` par `src:src/data` pour la variable `PYTHONPATH`.

## Organisation

```text
src/
├── build_portfolio.py         # construit la page d'accueil
├── data/                      # téléchargement et traitement des données
└── visualization/             # cartes Folium et habillage HTML
    └── page_chrome.py          # en-tête partagé des cartes
```

Les jeux de données et cartes HTML produits localement sont exclus de Git. Ils se régénèrent avec la commande ci-dessus.

## Données et technologies

- Données : [Vélib' Métropole](https://www.velib-metropole.fr/)
- Analyse : Python, NumPy, SciPy, NetworkX
- Cartographie : Folium et Leaflet

## Licence

Distribué sous licence MIT. Consultez [LICENSE](LICENSE).
