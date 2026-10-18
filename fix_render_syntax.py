import sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'github_sportplaner/index.html',
    'github_sportplaner/SportPlaner_SacreCoeur.html',
    'index.html',
    'SportPlaner_SacreCoeur.html'
]

target_bad = """      } else {
        container.style.display = 'grid';
      }
        container.innerHTML = '<div style="grid-column: 1/-1; padding: 2.5rem; text-align: center; color: #64748b; background: white; border-radius: 8px; border: 1px dashed #cbd5e1; font-size: 0.95rem;">Keine Übungen mit diesen Kriterien gefunden.<br><button class="btn btn-primary btn-sm" style="margin-top: 10px;" onclick="resetDbFilter()">⚡ Alle Übungen anzeigen</button></div>';
        return;
      }

      filtered.forEach(ex => {"""

target_good = """      } else {
        container.style.display = 'grid';
      }

      filtered.forEach(ex => {"""

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    if target_bad in t:
        t = t.replace(target_bad, target_good)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Fixed stray code in {p}")
    else:
        print(f"Could not find exact target_bad in {p}")
