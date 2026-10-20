import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('github_sportplaner/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(r'\{\s*id:\s*[\'"]([^\'"]+)[\'"].*?title:\s*[\'"]([^\'"]+)[\'"].*?tags:\s*(\[[^\]]*\])', re.DOTALL)
matches = pattern.findall(text)

insta_games = [m for m in matches if 'insta_hit' in m[2]]
print(f"Total exercises with 'insta_hit' tag: {len(insta_games)}")
for idx, (gid, title, tags) in enumerate(insta_games):
    print(f"{idx+1}. {gid}: {title}")
