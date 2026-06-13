import os

replacements = {
    "1620916566398-39f1143ab7be": "1620916566398-39f1143ab7be",
    "1522337660859-02fbefca4702": "1522337660859-02fbefca4702",
    "1581091226825-a6a2a5aee158": "1581091226825-a6a2a5aee158",
    "1556228578-0d85b1a4d571": "1556228578-0d85b1a4d571",
    "1526045431048-f857369baa09": "1526045431048-f857369baa09"
}

for root, dirs, files in os.walk('.'):
    if '.venv' in root or '__pycache__' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.py', '.js')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original = content
                for broken, fixed in replacements.items():
                    content = content.replace(broken, fixed)
                
                if content != original:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Fixed broken images in {path}")
            except Exception as e:
                pass
