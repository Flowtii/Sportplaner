import sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'github_sportplaner/index.html',
    'github_sportplaner/SportPlaner_SacreCoeur.html',
    'index.html',
    'SportPlaner_SacreCoeur.html'
]

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    old = "id: 'tu_m1_pyramide_gruppe',\n        title: 'Geräteparcours zum Thema \"Bergsteigen\" & Hindernisbahn'"
    new = "id: 'tu_m1_parcours_bergsteigen',\n        title: 'Geräteparcours zum Thema \"Bergsteigen\" & Hindernisbahn'"
    if old in t:
        t = t.replace(old, new)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Fixed duplicate ID in {p}")
    else:
        print(f"Could not find exact pattern in {p}")
