"""Habillage autonome des cartes HTML générées avec Folium."""

from pathlib import Path


def decorate_map_page(path: str | Path, title: str, description: str, tag: str) -> None:
    """Ajoute une en-tête lisible sans introduire de dépendance web externe."""
    output = Path(path)
    html = output.read_text(encoding="utf-8")

    style = """
    <style>
      :root { color-scheme: light; }
      body { margin: 0; background: #f5f7fb; font-family: Inter, ui-sans-serif, system-ui, sans-serif; }
      .portfolio-header {
        position: fixed; z-index: 1000; top: 18px; left: 18px; max-width: 390px;
        padding: 16px 18px; border: 1px solid rgba(255,255,255,.72); border-radius: 16px;
        color: #11213a; background: rgba(255,255,255,.91); box-shadow: 0 16px 38px rgba(17,33,58,.16);
        backdrop-filter: blur(12px);
      }
      .portfolio-header__eyebrow { margin: 0 0 6px; color: #146c94; font-size: .73rem; font-weight: 800; letter-spacing: .11em; text-transform: uppercase; }
      .portfolio-header h1 { margin: 0; font-size: 1.05rem; line-height: 1.25; }
      .portfolio-header p:last-child { margin: 7px 0 0; color: #52627a; font-size: .82rem; line-height: 1.45; }
      @media (max-width: 600px) { .portfolio-header { top: 10px; left: 10px; right: 10px; max-width: none; } }
    </style>
    """
    header = f'''<aside class="portfolio-header" aria-label="Contexte de l'analyse">
      <p class="portfolio-header__eyebrow">{tag}</p><h1>{title}</h1><p>{description}</p>
    </aside>'''
    html = html.replace("</head>", f"{style}</head>", 1)
    html = html.replace("<body>", f"<body>{header}", 1)
    output.write_text(html, encoding="utf-8")
