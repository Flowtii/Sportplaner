import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')

with open("github_sportplaner/index.html", "r", encoding="utf-8") as f:
    text = f.read()

# Extract all exercise objects
# Match blocks { id: '...' ... }
pattern = re.compile(r"\{\s*id:\s*['\"]([^'\"]+)['\"].*?tags:\s*(\[[^\]]*\])", re.DOTALL)
matches = pattern.findall(text)

print(f"Total parsed exercises: {len(matches)}")

neu_1k = [m for m in matches if "neu_1klasse" in m[1]]
insta = [m for m in matches if "insta_hit" in m[1]]
null_mat = [m for m in matches if "null_material" in m[1]]
huetchen = [m for m in matches if "huetchen_reifen" in m[1]]
baelle = [m for m in matches if "baelle" in m[1]]
hiit = [m for m in matches if "high_intensity" in m[1]]
koop = [m for m in matches if "kooperation" in m[1]]

print(f"⭐ neu_1klasse: {len(neu_1k)}")
print(f"📱 insta_hit: {len(insta)}")
print(f"🟢 null_material: {len(null_mat)}")
print(f"🟡 huetchen_reifen: {len(huetchen)}")
print(f"🏐 baelle: {len(baelle)}")
print(f"🔥 high_intensity: {len(hiit)}")
print(f"🤝 kooperation: {len(koop)}")

# Check for any remaining corrupted words
bad_words = ['font-weißght', 'bärauchst', 'Weißch', 'weißch', 'Weißt', 'weißtsprung', 'paarweiß']
for w in bad_words:
    cnt = text.count(w)
    if cnt > 0:
        print(f"WARNING: still found {w}: {cnt}")
print("Word check complete.")
