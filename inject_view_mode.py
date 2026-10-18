import sys
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'github_sportplaner/index.html',
    'github_sportplaner/SportPlaner_SacreCoeur.html',
    'index.html',
    'SportPlaner_SacreCoeur.html'
]

target_old = "let currentSchwellenFilter = 'all';"
target_new = """let currentSchwellenFilter = 'all';
    let currentDbViewMode = 'cards';

    function setDbViewMode(mode) {
      currentDbViewMode = mode;
      const btnCards = document.getElementById('view-mode-cards');
      const btnTable = document.getElementById('view-mode-table');
      if (btnCards && btnTable) {
        if (mode === 'table') {
          btnTable.classList.add('active');
          btnCards.classList.remove('active');
        } else {
          btnCards.classList.add('active');
          btnTable.classList.remove('active');
        }
      }
      renderDatabase();
    }"""

for p in files:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    if "let currentDbViewMode" not in t:
        t = t.replace(target_old, target_new, 1)
        with open(p, 'w', encoding='utf-8') as f:
            f.write(t)
        print(f"Added currentDbViewMode and setDbViewMode to {p}")
    else:
        print(f"Already present in {p}")
