import os

for root, dirs, files in os.walk('.'):
    if '.venv' in root or '__pycache__' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # The literal string we want to replace is a backslash followed by 'n'
            literal_n = '\\n'
            
            if literal_n in content:
                # We specifically look for the ones we accidentally injected
                # It was injected as: `f'    {FAVICON_TAG}\\n</head>'`
                # And `<body[^>]*>` -> `group(0) + '\\n' + NAVBAR_HTML`
                # And `</body>` -> `FOOTER_HTML + '\\n</body>'`
                
                content = content.replace('<body class="bg-off-white text-primary font-sans antialiased">\\n', '<body class="bg-off-white text-primary font-sans antialiased">\n')
                content = content.replace(literal_n + '</body>', '\n</body>')
                content = content.replace(literal_n + '</head>', '\n</head>')
                content = content.replace(literal_n + '    <link rel="icon"', '\n    <link rel="icon"')
                
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Fixed newlines in {path}")
