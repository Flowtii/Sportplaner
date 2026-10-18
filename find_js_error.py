import subprocess, os

edge_path = r"C:\Program Files (x86)\Microsoft\EdgeCore\155.0.4283.60\msedge.exe"

# We can create a test html where window.onerror catches the error and writes it to a div!
with open("github_sportplaner/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Put window.onerror right at the very beginning of the script tag!
error_catcher = """
<script>
window.__ERRORS__ = [];
window.onerror = function(msg, url, line, col, error) {
  window.__ERRORS__.push({msg: msg, line: line, col: col});
};
</script>
"""

# And at the end before </body>
reporter = """
<div id="ERROR_REPORT"></div>
<script>
window.addEventListener('load', function() {
  var el = document.getElementById('ERROR_REPORT');
  if (window.__ERRORS__ && window.__ERRORS__.length > 0) {
    el.textContent = 'ERRORS: ' + JSON.stringify(window.__ERRORS__);
  } else {
    el.textContent = 'NO_ERRORS_LOADED';
  }
});
</script>
"""

test_content = html.replace("<head>", "<head>" + error_catcher).replace("</body>", reporter + "</body>")
with open("test_debug.html", "w", encoding="utf-8") as f:
    f.write(test_content)

test_page_path = os.path.abspath("test_debug.html")

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
m = re.search(r'<div id="ERROR_REPORT">(.*?)</div>', p.stdout)
if m:
    print("Report:", m.group(1))
else:
    print("Could not find ERROR_REPORT")
