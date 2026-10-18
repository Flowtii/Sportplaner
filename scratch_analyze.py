import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open("github_sportplaner/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Find all blocks in EXERCISE_DATABASE
# Look for id: '...' and tags: [...]
pattern = re.compile(r"\{\s*id:\s*['\"]([^'\"]+)['\"],\s*title:\s*['\"]([^'\"]+)['\"].*?tags:\s*(\[[^\]]*\])", re.DOTALL)
matches = pattern.findall(text)

print(f"Total parsed objects with tags: {len(matches)}")
insta = [m for m in matches if m[0].startswith("insta_")]
print(f"insta_ games: {len(insta)}")
for item in insta:
    print(f"  {item[0]}: {item[1]}")

schwell = [m for m in matches if m[0].startswith("schwell_") or m[0].startswith("hiit_")]
print(f"schwell_/hiit_ games: {len(schwell)}")
for item in schwell:
    print(f"  {item[0]}: {item[1]}")

# Also check how many have 'neu_1klasse' tag currently
neu_1k = [m for m in matches if "neu_1klasse" in m[2]]
print(f"Total with neu_1klasse tag: {len(neu_1k)}")
