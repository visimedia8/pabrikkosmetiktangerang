import os
import re
from urllib.parse import urlparse

def check_site():
    html_files = []
    for root, dirs, files in os.walk('.'):
        if '.venv' in root or '__pycache__' in root or '.git' in root:
            continue
        for f in files:
            if f.endswith('.html'):
                html_files.append(os.path.join(root, f))
    
    available_files = set()
    for f in html_files:
        # Normalize paths for comparison (e.g., ./artikel.html -> /artikel.html)
        norm_path = '/' + os.path.relpath(f, '.').replace('\\', '/')
        available_files.add(norm_path)
    
    # Also add root
    available_files.add('/')
    available_files.add('/index.html')
    
    broken_links = []
    
    for f in html_files:
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
            
        # Find all href="..." and src="..."
        links = re.findall(r'href="([^"]+)"', content)
        srcs = re.findall(r'src="([^"]+)"', content)
        
        all_refs = links + srcs
        
        for ref in all_refs:
            # Skip external links
            if ref.startswith('http://') or ref.startswith('https://') or ref.startswith('mailto:') or ref.startswith('tel:'):
                continue
            
            # Skip anchor links
            if ref.startswith('#'):
                continue
                
            # Strip query params or hash for local checking
            base_ref = ref.split('?')[0].split('#')[0]
            
            if base_ref == '':
                continue
                
            # Check if internal link exists
            if base_ref not in available_files and not base_ref.startswith('https://fonts.googleapis.com'):
                # Also check if it's an image
                if base_ref.endswith('.svg') or base_ref.endswith('.png') or base_ref.endswith('.jpg'):
                    if not os.path.exists(os.path.join('.', base_ref.lstrip('/'))):
                        broken_links.append((f, ref))
                else:
                    broken_links.append((f, ref))

    if broken_links:
        print("Found broken links:")
        for source, broken in broken_links:
            print(f"File: {source} -> Broken Link: {broken}")
    else:
        print("No broken links found!")

if __name__ == '__main__':
    check_site()
