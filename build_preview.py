"""index.html + style.css + images/ 를 파일 하나로 묶어 확인용 공유 파일로 저장.

python3 build_preview.py            -> ../yujinlee-site-preview.html
python3 build_preview.py princess   -> ../yujinlee-site-princess.html (공주방 테마)
"""
import base64, os, re, sys

theme = sys.argv[1] if len(sys.argv) > 1 else None

s = open('index.html').read()
css = open('style.css').read()
if theme:
    css += '\n' + open(theme + '.css').read()
# @import 는 스타일시트 맨 앞에 있어야 동작하므로 끌어올림
imports = re.findall(r'^@import[^\n]*\n', css, flags=re.M)
css = ''.join(imports) + re.sub(r'^@import[^\n]*\n', '', css, flags=re.M)
s = s.replace('<link rel="stylesheet" href="style.css">', '<style>\n' + css + '</style>')

def inline(m):
    path = m.group(1)
    if not os.path.exists(path):
        return m.group(0)
    ext = path.rsplit('.', 1)[-1].lower()
    mime = {'jpg': 'jpeg', 'jpeg': 'jpeg', 'png': 'png', 'webp': 'webp'}[ext]
    return 'src="data:image/%s;base64,%s"' % (mime, base64.b64encode(open(path, 'rb').read()).decode())

s = re.sub(r'src="(images/[^"]+)"', inline, s)
out = '../yujinlee-site-%s.html' % (theme or 'preview')
open(out, 'w').write(s)
print('ok', len(s) // 1024, 'KB')
