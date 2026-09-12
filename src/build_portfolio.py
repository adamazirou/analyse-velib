"""Construit une page d'accueil statique pour parcourir les analyses Vélib'."""

from pathlib import Path
import json


ROOT = Path(__file__).resolve().parent.parent


def station_count() -> int | None:
    data_file = ROOT / "station_informations.json"
    if not data_file.exists():
        return None
    with data_file.open(encoding="utf-8") as handle:
        return len(json.load(handle).get("data", {}).get("stations", []))


def build() -> Path:
    count = station_count()
    count_label = f"{count:,}".replace(",", " ") if count else "—"
    cards = [
        ("01", "Stations", "Explorez les stations, leur position et leur capacité.", "stations_map.html", "Carte interactive"),
        ("02", "Triangulation", "Visualisez les proximités spatiales du réseau de stations.", "velib_stations_map.html", "Delaunay"),
        ("03", "Couverture", "Observez les zones d'influence avec le diagramme de Voronoï.", "velib_voronoi_map.html", "Voronoï"),
        ("04", "Connectivité", "Parcourez l'arbre couvrant minimal des connexions du réseau.", "velib_acm_map.html", "ACM"),
    ]
    card_html = "".join(
        f'''<a class="card" href="{target}"><span class="card__number">{number}</span><span class="card__tag">{tag}</span><h2>{title}</h2><p>{description}</p><span class="card__cta">Ouvrir l'analyse <b>→</b></span></a>'''
        for number, title, description, target, tag in cards
    )
    html = f'''<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Vélib' | Analyse spatiale</title><meta name="description" content="Exploration visuelle du réseau Vélib' Métropole.">
<style>
  :root {{ --ink:#10243e; --muted:#60718a; --accent:#00a878; --blue:#1c6dd0; --paper:#f5f7fb; }}
  * {{ box-sizing:border-box; }} body {{ margin:0; color:var(--ink); background:var(--paper); font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
  .hero {{ overflow:hidden; position:relative; padding:88px max(7vw,28px) 72px; color:white; background:linear-gradient(125deg,#0c2340,#145d89 57%,#00a878); }}
  .hero:after {{ content:""; position:absolute; width:620px; height:620px; right:-220px; top:-330px; border:1px solid rgba(255,255,255,.28); border-radius:50%; box-shadow:0 0 0 72px rgba(255,255,255,.05),0 0 0 144px rgba(255,255,255,.04); }}
  .hero__inner,.content {{ position:relative; z-index:1; max-width:1120px; margin:auto; }} .eyebrow {{ margin:0 0 16px; font-size:.78rem; font-weight:800; letter-spacing:.13em; text-transform:uppercase; color:#a6f5d9; }}
  h1 {{ max-width:760px; margin:0; font-size:clamp(2.5rem,6vw,5rem); line-height:.98; letter-spacing:-.06em; }} .intro {{ max-width:620px; margin:24px 0 0; font-size:1.08rem; line-height:1.65; color:#e4f4fa; }}
  .stats {{ display:flex; gap:28px; margin-top:44px; }} .stat {{ border-left:2px solid #7ae3c2; padding-left:15px; }} .stat strong {{ display:block; font-size:1.6rem; }} .stat span {{ font-size:.85rem; color:#d6edf5; }}
  .content {{ padding:56px 0 72px; }} .section-title {{ display:flex; justify-content:space-between; align-items:end; gap:20px; margin-bottom:25px; }} .section-title h2 {{ margin:0; font-size:1.45rem; letter-spacing:-.03em; }} .section-title p {{ margin:0; color:var(--muted); }}
  .grid {{ display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:18px; }} .card {{ position:relative; min-height:238px; padding:26px; overflow:hidden; text-decoration:none; color:inherit; background:white; border:1px solid #e0e7f0; border-radius:18px; box-shadow:0 7px 20px rgba(20,48,82,.06); transition:transform .18s ease,box-shadow .18s ease; }} .card:hover {{ transform:translateY(-4px); box-shadow:0 15px 32px rgba(20,48,82,.14); }}
  .card__number {{ position:absolute; top:18px; right:22px; color:#c8d4e1; font-weight:800; }} .card__tag {{ color:#147598; font-size:.75rem; font-weight:800; letter-spacing:.1em; text-transform:uppercase; }} .card h2 {{ margin:22px 0 8px; font-size:1.5rem; letter-spacing:-.035em; }} .card p {{ max-width:330px; margin:0; color:var(--muted); line-height:1.55; }} .card__cta {{ position:absolute; bottom:24px; color:#146c94; font-weight:750; }} .card__cta b {{ padding-left:6px; font-size:1.15rem; }}
  footer {{ padding:26px max(7vw,28px); color:#60718a; background:#e9eef5; font-size:.86rem; }} footer div {{ max-width:1120px; margin:auto; }} @media(max-width:680px) {{ .hero {{ padding-top:60px; }} .grid {{ grid-template-columns:1fr; }} .stats {{ gap:17px; }} .section-title {{ display:block; }} .section-title p {{ margin-top:8px; }} }}
</style></head><body>
<header class="hero"><div class="hero__inner"><p class="eyebrow">Data visualisation · Paris & Métropole</p><h1>Le réseau Vélib', lu par les données.</h1><p class="intro">Une série d'analyses spatiales interactives pour comprendre la distribution, la couverture et la connectivité des stations.</p><div class="stats"><div class="stat"><strong>{count_label}</strong><span>stations analysées</span></div><div class="stat"><strong>4</strong><span>visualisations interactives</span></div></div></div></header>
<main class="content"><div class="section-title"><h2>Explorer les analyses</h2><p>Choisissez une visualisation pour ouvrir la carte.</p></div><section class="grid">{card_html}</section></main>
<footer><div>Données : Vélib' Métropole · Réalisation : projet d'analyse spatiale en Python</div></footer>
</body></html>'''
    output = ROOT / "index.html"
    output.write_text(html, encoding="utf-8")
    return output


if __name__ == "__main__":
    print(f"Portfolio généré : {build()}")
