import sys, re
sys.stdout.reconfigure(encoding='utf-8')

with open("github_sportplaner/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

insta_lines = []
schwell_lines = []
for idx, line in enumerate(lines):
    if "id: 'insta_" in line or 'id: "insta_' in line:
        insta_lines.append((idx+1, line.strip()))
    elif "id: 'schwell_" in line or 'id: "schwell_' in line or "id: 'hiit_" in line or 'id: "hiit_' in line:
        schwell_lines.append((idx+1, line.strip()))

print(f"Total insta_ items found: {len(insta_lines)}")
for item in insta_lines[:5]:
    print("  ", item)
print(f"Total schwell/hiit items found: {len(schwell_lines)}")
for item in schwell_lines[:5]:
    print("  ", item)

# Find the end of EXERCISE_DATABASE
for idx, line in enumerate(lines):
    if "EXERCISE_DATABASE" in line and "=" in line:
        print(f"EXERCISE_DATABASE starts at line {idx+1}")
    if line.strip() == "];" and idx > 2760 and idx < 12000:
        print(f"Candidate array end at line {idx+1}: {line.strip()}")
