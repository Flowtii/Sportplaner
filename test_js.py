import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open("github_sportplaner/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Check script blocks
scripts = re.findall(r'<script>(.*?)</script>', html, re.DOTALL)
print(f"Found {len(scripts)} script blocks.")

# In the main script block, check EXERCISE_DATABASE
main_script = scripts[0]

# Check if EXERCISE_DATABASE has balanced brackets
db_start = main_script.find("const EXERCISE_DATABASE = [")
db_end = main_script.find("];\n\n    /* =====================================================================")

print("db_start:", db_start, "db_end:", db_end)
db_chunk = main_script[db_start:db_end+2]

# Count { and } in db_chunk
open_braces = db_chunk.count('{')
close_braces = db_chunk.count('}')
print(f"Braces in EXERCISE_DATABASE: open={open_braces}, close={close_braces}")
assert open_braces == close_braces, "Brace mismatch in EXERCISE_DATABASE!"

# Count items by looking at "id: '"
ids = re.findall(r"id:\s*['\"]([^'\"]+)['\"]", db_chunk)
print(f"Total exercises declared in EXERCISE_DATABASE: {len(ids)}")

# Check duplicates in IDs
duplicates = [x for x in ids if ids.count(x) > 1]
print(f"Duplicate IDs: {set(duplicates)}")
assert len(duplicates) == 0, f"Found duplicate IDs: {set(duplicates)}"

print("JavaScript EXERCISE_DATABASE is structurally valid!")
