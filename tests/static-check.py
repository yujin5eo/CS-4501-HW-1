from pathlib import Path
import re
root=Path('.')
required=['index.html','baseline.html','review.html','data.js','shared.js','anti.js','baseline.js','review.js','styles.css','README.md','docs/violations.md','docs/walkthrough.md','docs/testing.md']
assert all((root/x).is_file() for x in required)
for page in ['index.html','baseline.html','review.html']:
 s=(root/page).read_text()
 for ref in re.findall(r'(?:src|href)="([^"#]+)',s):
  if ':' not in ref and not ref.startswith('mailto:'): assert (root/ref.split('?',1)[0]).exists(),f'{page}: missing {ref}'
 assert not re.search(r'(?:src|href)="/',s),f'{page}: root absolute path'
anti=(root/'anti.js').read_text(); html=(root/'index.html').read_text()
views=set(re.findall(r'data-view="([^"]+)',html))|set(re.findall(r"view==='([^']+)",anti))
for v in set(re.findall(r'data-view="([^"]+)',html)): assert v in views
css=(root/'styles.css').read_text();assert '@media(max-width:700px)' in css and 'prefers-reduced-motion' in css
print('static checks passed: required files, local relative assets, navigation view coverage, responsive/reduced-motion CSS')
