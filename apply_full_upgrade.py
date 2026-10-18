# -*- coding: utf-8 -*-
import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

from build_full_database import INSTA_GAMES_TO_ADD, GYM_1KLASSE_GAMES_TO_ADD

file_path = "github_sportplaner/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Clean up corrupted "weiß..." words
replacements = [
    ('font-weißght', 'font-weight'),
    ('bärauchst', 'brauchst'),
    ('Weißch', 'Weich'),
    ('weißch', 'weich'),
    ('Weißt', 'Weit'),
    ('weißtsprung', 'weitsprung'),
    ('weißt', 'weit'),
    ('Weißter', 'Weiter'),
    ('weißter', 'weiter'),
    ('Zweiß', 'Zwei'),
    ('zweiß', 'zwei'),
    ('Ausweißch', 'Ausweich'),
    ('ausweißch', 'ausweich'),
    ('Schweißf', 'Schweif'),
    ('schweißf', 'schweif'),
    ('Hinweißs', 'Hinweis'),
    ('hinweißs', 'hinweis'),
    ('Hinweiß', 'Hinweis'),
    ('hinweiß', 'hinweis'),
    ('jeweißl', 'jeweil'),
    ('Weißblich', 'Weiblich'),
    ('weißblich', 'weiblich'),
    ('Weißnzettl', 'Weinzettl'),
    ('Erweißterung', 'Erweiterung'),
    ('Abweißchung', 'Abweichung'),
    ('Anweißsung', 'Anweisung'),
    ('Paarweißse', 'Paarweise'),
    ('paarweißse', 'paarweise'),
    ('Bahnenweißses', 'Bahnenweises'),
    ('Stationsweißse', 'Stationsweise'),
    ('schrittweißse', 'schrittweise'),
    ('Zählweißse', 'Zählweise'),
    ('Verweißs', 'Verweis'),
    ('verweißgert', 'verweigert'),
    ('verweißlen', 'verweilen'),
    ('beweißsen', 'beweisen'),
    ('schweißgend', 'schweigend'),
    ('Reichweißte', 'Reichweite'),
    ('Weißß', 'Weiß'),
    ('weißss', 'weiss')
]

for old, new in replacements:
    content = content.replace(old, new)

# 2. Add 'neu_1klasse' tag to all existing schwell_ and hiit_ entries in EXERCISE_DATABASE
def add_neu_1klasse_to_block(match):
    block = match.group(0)
    if '"neu_1klasse"' not in block and "'neu_1klasse'" not in block:
        # replace tags: [ ... ] with tags: ["neu_1klasse", ... ]
        block = re.sub(r'tags:\s*\[', 'tags: ["neu_1klasse", ', block)
    return block

# Match blocks with id: 'schwell_...' or id: 'hiit_...'
content = re.sub(r'\{\s*id:\s*[\'"](?:schwell_|hiit_)[^\}]*?tags:\s*\[[^\]]*\][^\}]*\}', add_neu_1klasse_to_block, content)

# 3. Inject new games
all_new_games = INSTA_GAMES_TO_ADD + GYM_1KLASSE_GAMES_TO_ADD
games_to_inject = []
for g in all_new_games:
    if f"id: '{g['id']}'" not in content and f'id: "{g["id"]}"' not in content:
        games_to_inject.append(g)

print(f"Games to inject: {len(games_to_inject)}")

# Format games as JS objects
js_snippets = []
for g in games_to_inject:
    tags_json = json.dumps(g.get("tags", []), ensure_ascii=False)
    js = f"""      {{
        id: '{g["id"]}',
        title: {json.dumps(g["title"], ensure_ascii=False)},
        category: '{g["category"]}',
        subcat: '{g["subcat"]}',
        phase: '{g["phase"]}',
        ageGroup: '{g["ageGroup"]}',
        duration: {g["duration"]},
        goal: {json.dumps(g["goal"], ensure_ascii=False)},
        desc: {json.dumps(g["desc"], ensure_ascii=False)},
        material: {json.dumps(g["material"], ensure_ascii=False)},
        org: {json.dumps(g["org"], ensure_ascii=False)},
        cues: {json.dumps(g["cues"], ensure_ascii=False)},
        ref: {json.dumps(g["ref"], ensure_ascii=False)},
        tags: {tags_json}
      }}"""
    js_snippets.append(js)

insertion_code = ",\n" + ",\n".join(js_snippets)

# Find the end of EXERCISE_DATABASE
# Pattern: \n\s*\];\s*\n\s*/\*\s*={10,}\s*\n\s*2\.\s*THEMEN-KATALOG
catalog_pattern = re.compile(r'(\n\s*\];\s*\n\s*/\*\s*={10,}\s*\n\s*2\.\s*THEMEN-KATALOG)')
if catalog_pattern.search(content):
    content = catalog_pattern.sub(insertion_code + r'\1', content, count=1)
    print("Successfully injected new games before THEMEN-KATALOG!")
else:
    print("WARNING: Could not find exact THEMEN-KATALOG boundary. Trying fallback...")
    # fallback search for first "];\n\n    /* =======" after line 2760
    pos = content.find("];\n\n    /* =====================================================================")
    if pos != -1:
        content = content[:pos] + insertion_code + "\n" + content[pos:]
        print("Successfully injected using fallback!")
    else:
        print("ERROR: Could not locate insertion point!")

# 4. Update the Schwellen-Pills in HTML
new_pills_html = """        <div class="schwellen-pills-wrap">
          <button class="schwellen-pill active" data-schwellen="all" onclick="setSchwellenFilter('all', this)">⚡ Alle 500+ Einheiten</button>
          <button class="schwellen-pill" data-schwellen="neu_1klasse" onclick="setSchwellenFilter('neu_1klasse', this)" style="border: 2px solid #fbbf24; background: rgba(251,191,36,0.18); font-weight: 800; color: #fff;">⭐ 50+ Neue Spiele (1. Klasse Gym)</button>
          <button class="schwellen-pill" data-schwellen="insta_hit" onclick="setSchwellenFilter('insta_hit', this)" style="border: 2px solid #f472b6; background: rgba(244,114,182,0.18); font-weight: 800; color: #fff;">📱 50+ Instagram &amp; TikTok Hits</button>
          <button class="schwellen-pill" data-schwellen="null_material" onclick="setSchwellenFilter('null_material', this)">🟢 0 Min. Aufbau (Null Material)</button>
          <button class="schwellen-pill" data-schwellen="huetchen_reifen" onclick="setSchwellenFilter('huetchen_reifen', this)">🟡 Nur Hütchen &amp; Reifen</button>
          <button class="schwellen-pill" data-schwellen="baelle" onclick="setSchwellenFilter('baelle', this)">🏐 Bälle &amp; Wurfspiele</button>
          <button class="schwellen-pill" data-schwellen="high_intensity" onclick="setSchwellenFilter('high_intensity', this)">🔥 Puls hoch (Auspowern &amp; HIIT)</button>
          <button class="schwellen-pill" data-schwellen="kooperation" onclick="setSchwellenFilter('kooperation', this)">🤝 Teambuilding &amp; Kooperation</button>
        </div>"""

old_pills_pattern = re.compile(r'<div class="schwellen-pills-wrap">.*?</div>\s*</div>\s*<div class="db-layout">', re.DOTALL)
if old_pills_pattern.search(content):
    content = old_pills_pattern.sub(new_pills_html + '\n      </div>\n\n      <div class="db-layout">', content, count=1)
    print("Updated Schwellen-Pills HTML!")
else:
    print("WARNING: Could not find old pills wrap!")

# 5. Add View Toggle above db-results-container
old_results_header = re.compile(
    r'<div style="display:\s*flex;\s*justify-content:\s*space-between;\s*align-items:\s*center;\s*margin-bottom:\s*1rem;">\s*'
    r'<div style="font-weight:\s*700;\s*color:\s*var\(--dark\);">\s*'
    r'Gefundene &Uuml;bungen &amp; Spiele:\s*<span id="db-count-badge"[^>]*>0</span>\s*</div>\s*'
    r'<div style="font-size:\s*0\.85rem;\s*color:\s*var\(--text-muted\);">\s*'
    r'W&auml;hle <strong>"In Stunde einf&uuml;gen"</strong>[^<]*</div>\s*</div>',
    re.DOTALL
)

new_results_header = """          <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem; flex-wrap: wrap; gap: 8px;">
            <div style="font-weight: 700; color: var(--dark); display: flex; align-items: center; gap: 8px;">
              <span>Gefundene &Uuml;bungen &amp; Spiele:</span>
              <span id="db-count-badge" class="badge-warmup phase-badge" style="font-size: 0.95rem;">0</span>
            </div>
            
            <div style="display: flex; align-items: center; gap: 8px;">
              <div class="view-toggle-wrap" style="display: flex; background: #e2e8f0; border-radius: 8px; padding: 3px; gap: 3px;">
                <button id="view-mode-cards" class="view-mode-btn active" onclick="setDbViewMode('cards')">🗂️ Detail-Karten</button>
                <button id="view-mode-table" class="view-mode-btn" onclick="setDbViewMode('table')">📋 Kompakt-Tabelle (Auf einen Blick)</button>
              </div>
            </div>
          </div>"""

if old_results_header.search(content):
    content = old_results_header.sub(new_results_header, content, count=1)
    print("Replaced results header with View Toggle!")
else:
    print("WARNING: Could not find old results header pattern directly, attempting fallback...")
    content = content.replace(
        '<div style="font-weight: 700; color: var(--dark);">\n              Gefundene &Uuml;bungen &amp; Spiele: <span id="db-count-badge" class="badge-warmup phase-badge" style="font-size: 0.95rem;">0</span>\n            </div>',
        """<div style="font-weight: 700; color: var(--dark); display: flex; align-items: center; gap: 8px;">
              <span>Gefundene &Uuml;bungen &amp; Spiele:</span>
              <span id="db-count-badge" class="badge-warmup phase-badge" style="font-size: 0.95rem;">0</span>
            </div>
            <div class="view-toggle-wrap" style="display: flex; background: #e2e8f0; border-radius: 8px; padding: 3px; gap: 3px;">
              <button id="view-mode-cards" class="view-mode-btn active" onclick="setDbViewMode('cards')">🗂️ Detail-Karten</button>
              <button id="view-mode-table" class="view-mode-btn" onclick="setDbViewMode('table')">📋 Kompakt-Tabelle (Auf einen Blick)</button>
            </div>"""
    )

# 6. Add CSS for View Toggle and Table
css_to_add = """
    /* View Toggle & Compact Table */
    .view-mode-btn {
      background: transparent;
      border: none;
      padding: 6px 12px;
      font-size: 0.82rem;
      font-weight: 700;
      color: #64748b;
      border-radius: 6px;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }
    .view-mode-btn.active {
      background: white;
      color: #0f172a;
      box-shadow: 0 1px 4px rgba(0,0,0,0.12);
    }
    .view-mode-btn:hover:not(.active) {
      color: #1e293b;
      background: rgba(255,255,255,0.5);
    }
    .db-compact-table {
      width: 100%;
      border-collapse: collapse;
      font-size: 0.88rem;
      text-align: left;
    }
    .db-compact-table th {
      padding: 10px 12px;
      background: #f1f5f9;
      color: #334155;
      font-weight: 700;
      border-bottom: 2px solid #cbd5e1;
    }
    .db-compact-table td {
      padding: 10px 12px;
      border-bottom: 1px solid #e2e8f0;
      vertical-align: top;
    }
    .db-compact-table tr:hover {
      background: #f0f9ff !important;
    }
"""

if ".view-mode-btn" not in content:
    content = content.replace("/* Database Layout */", css_to_add + "\n    /* Database Layout */")
    print("Injected View Toggle & Table CSS!")

# 7. Add setDbViewMode JS and enhance matchesSchwellenCondition + renderDatabase
js_view_logic = """
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
    }
"""

if "function setDbViewMode" not in content:
    content = content.replace("function setSchwellenFilter(tag, btnEl) {", js_view_logic + "\n    function setSchwellenFilter(tag, btnEl) {")
    print("Injected setDbViewMode JavaScript!")

# 8. Ensure matchesSchwellenCondition supports 'neu_1klasse'
if "if (filter === 'neu_1klasse')" not in content:
    content = content.replace(
        "if (filter === 'null_material') {",
        "if (filter === 'neu_1klasse') {\n        return tags.includes('neu_1klasse');\n      }\n      if (filter === 'null_material') {"
    )
    print("Added filter === 'neu_1klasse' in matchesSchwellenCondition!")

# 9. Update renderDatabase table view implementation
old_render_start = "container.innerHTML = '';\n\n      if (filtered.length === 0) {"
table_render_code = """container.innerHTML = '';

      if (filtered.length === 0) {
        container.innerHTML = '<div style="grid-column: 1/-1; padding: 2.5rem; text-align: center; color: #64748b; background: white; border-radius: 8px; border: 1px dashed #cbd5e1; font-size: 0.95rem;">Keine Übungen mit diesen Kriterien gefunden.<br><button class="btn btn-primary btn-sm" style="margin-top: 10px;" onclick="resetDbFilter()">⚡ Alle Übungen anzeigen</button></div>';
        return;
      }

      if (currentDbViewMode === 'table') {
        container.style.display = 'block';
        let tableHtml = `
          <div style="overflow-x: auto; background: white; border-radius: 12px; border: 1px solid #cbd5e1; box-shadow: 0 4px 12px rgba(0,0,0,0.05);">
            <table class="db-compact-table">
              <thead>
                <tr>
                  <th style="width: 35px;">#</th>
                  <th style="min-width: 190px;">Spiel / &Uuml;bung</th>
                  <th style="min-width: 140px;">Material &amp; Aufbau</th>
                  <th style="width: 80px; white-space: nowrap;">Dauer</th>
                  <th style="min-width: 280px;">Ablauf &amp; Clou (Auf einen Blick)</th>
                  <th style="text-align: right; min-width: 110px;">Aktion</th>
                </tr>
              </thead>
              <tbody>
        `;
        filtered.forEach((ex, idx) => {
          let catIcon = '🏃';
          if (ex.category === 'leichtathletik') catIcon = '🏃';
          else if (ex.category === 'ball') catIcon = '🏀';
          else if (ex.category === 'spiele') catIcon = '🎲';
          else if (ex.category === 'motorik') catIcon = '🧠';
          else if (ex.category === 'fitness') catIcon = '⚡';
          else if (ex.category === 'turnen') catIcon = '🤸';
          else if (ex.category === 'kampfklettern') catIcon = '🧗';

          let badges = '';
          const tags = ex.tags || [];
          if (tags.includes('null_material')) badges += '<span style="font-size:0.68rem; background:#dcfce7; color:#15803d; padding:2px 6px; border-radius:10px; font-weight:700;">🟢 0 Min</span> ';
          if (tags.includes('huetchen_reifen')) badges += '<span style="font-size:0.68rem; background:#fef3c7; color:#b45309; padding:2px 6px; border-radius:10px; font-weight:700;">🟡 Hütchen</span> ';
          if (tags.includes('baelle')) badges += '<span style="font-size:0.68rem; background:#e0e7ff; color:#3730a3; padding:2px 6px; border-radius:10px; font-weight:700;">🏐 Ball</span> ';
          if (tags.includes('high_intensity')) badges += '<span style="font-size:0.68rem; background:#fee2e2; color:#b91c1c; padding:2px 6px; border-radius:10px; font-weight:700;">🔥 HIIT</span> ';
          if (tags.includes('insta_hit')) badges += '<span style="font-size:0.68rem; background:#f3e8ff; color:#7e22ce; padding:2px 6px; border-radius:10px; font-weight:700;">📱 Insta</span> ';

          const bgRow = (idx % 2 === 0) ? '#ffffff' : '#f8fafc';
          tableHtml += `
            <tr style="background: ${bgRow};">
              <td style="font-weight: 700; color: #94a3b8;">${idx + 1}</td>
              <td>
                <div style="font-weight: 700; color: #0f172a; font-size: 0.95rem;">${catIcon} ${ex.title}</div>
                <div style="font-size: 0.75rem; color: #0284c7; font-weight: 600; margin-top: 2px;">🎯 ${ex.goal}</div>
                <div style="margin-top: 4px;">${badges}</div>
              </td>
              <td>
                <span style="font-size: 0.78rem; background: #f1f5f9; padding: 3px 8px; border-radius: 6px; font-weight: 600; color: #334155; display: inline-block;">🎒 ${ex.material}</span>
                <div style="font-size: 0.72rem; color: #64748b; margin-top: 3px;">👥 ${ex.org}</div>
              </td>
              <td style="white-space: nowrap; font-weight: 700; color: #475569;">⏱️ ${ex.duration} min</td>
              <td style="line-height: 1.45; color: #334155;">
                <div style="font-size: 0.85rem;">${ex.desc}</div>
                <div style="font-size: 0.75rem; color: #64748b; margin-top: 4px;"><strong>Tipp:</strong> ${ex.cues || 'Saubere Ausführung'}</div>
              </td>
              <td style="text-align: right;">
                <button class="btn btn-primary btn-sm" onclick="addExerciseDirectly('${ex.id}')" style="white-space: nowrap; font-size: 0.78rem; padding: 5px 9px;">+ In Stunde</button>
              </td>
            </tr>
          `;
        });
        tableHtml += `</tbody></table></div>`;
        container.innerHTML = tableHtml;
        return;
      } else {
        container.style.display = 'grid';
      }"""

if old_render_start in content:
    content = content.replace(old_render_start, table_render_code)
    print("Updated renderDatabase with Table View rendering!")
else:
    print("WARNING: Could not find exact old_render_start!")

# Save to github_sportplaner/index.html
with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print(f"Updated {file_path}")

# Sync to SportPlaner_SacreCoeur.html
with open("github_sportplaner/SportPlaner_SacreCoeur.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated github_sportplaner/SportPlaner_SacreCoeur.html")

# Sync to root index.html and SportPlaner_SacreCoeur.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated ./index.html")

with open("SportPlaner_SacreCoeur.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Updated ./SportPlaner_SacreCoeur.html")
