import re

with open('app/static/css/style.css', 'r') as f:
    content = f.read()

new_submenu = """.submenu {
  max-height: 0;
  opacity: 0;
  visibility: hidden;
  transition: max-height 0.3s ease, opacity 0.3s ease, visibility 0.3s ease, margin-top 0.3s ease;
  overflow: hidden;
}
.submenu.open {
  max-height: 500px;
  opacity: 1;
  visibility: visible;
  margin-top: 8px;
}"""

content = re.sub(r'\.submenu \{.*?\n\}', '.submenu {\n  max-height: 0;\n  opacity: 0;\n  visibility: hidden;\n  transition: max-height 0.3s ease, opacity 0.3s ease, visibility 0.3s ease, margin-top 0.3s ease;\n  overflow: hidden;\n}', content, flags=re.DOTALL)
content = re.sub(r'\.submenu\.open \{.*?\n\}', '.submenu.open {\n  max-height: 500px;\n  opacity: 1;\n  visibility: visible;\n  margin-top: 8px;\n}', content, flags=re.DOTALL)

with open('app/static/css/style.css', 'w') as f:
    f.write(content)
