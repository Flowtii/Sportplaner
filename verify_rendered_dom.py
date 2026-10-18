import subprocess, json, os

edge_path = r"C:\Program Files (x86)\Microsoft\EdgeCore\155.0.4283.60\msedge.exe"

with open("github_sportplaner/index.html", "r", encoding="utf-8") as f:
    html = f.read()

test_script = """
<script>
window.addEventListener('DOMContentLoaded', () => {
  try {
    const res = {};
    res.totalDb = EXERCISE_DATABASE.length;
    
    // 1. Test neu_1klasse
    setSchwellenFilter('neu_1klasse');
    res.neu1k_cards = document.querySelectorAll('.exercise-card').length;
    res.neu1k_badge = document.getElementById('db-count-badge').textContent;
    
    // 2. Test table mode
    setDbViewMode('table');
    res.neu1k_table_rows = document.querySelectorAll('.db-compact-table tbody tr').length;
    
    // 3. Test insta_hit
    setSchwellenFilter('insta_hit');
    res.insta_table_rows = document.querySelectorAll('.db-compact-table tbody tr').length;
    res.insta_badge = document.getElementById('db-count-badge').textContent;
    
    // 4. Test back to cards
    setDbViewMode('cards');
    res.insta_cards = document.querySelectorAll('.exercise-card').length;
    
    const div = document.createElement('div');
    div.id = 'FINAL_TEST_RESULT';
    div.textContent = JSON.stringify(res);
    document.body.appendChild(div);
  } catch(e) {
    const div = document.createElement('div');
    div.id = 'FINAL_TEST_RESULT';
    div.textContent = 'ERROR: ' + e.message;
    document.body.appendChild(div);
  }
});
</script>
"""

with open("test_page.html", "w", encoding="utf-8") as f:
    f.write(html + test_script)

test_page_path = os.path.abspath("test_page.html")

cmd = [
    edge_path,
    "--headless",
    "--disable-gpu",
    "--virtual-time-budget=2000",
    "--dump-dom",
    f"file:///{test_page_path.replace(os.sep, '/')}"
]

p = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")
import re
m = re.search(r'<div id="FINAL_TEST_RESULT">(.*?)</div>', p.stdout)
if m:
    print("Edge test result:", m.group(1))
else:
    print("Could not find FINAL_TEST_RESULT in stdout")
