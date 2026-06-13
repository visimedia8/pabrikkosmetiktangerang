import os
import re

print("Scanning artikel/ directory dynamically...")

articles = []
for file in os.listdir('artikel'):
    if file.endswith('.html'):
        slug = file[:-5]
        path = os.path.join('artikel', file)
        with open(path, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Parse title
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
        title = title_match.group(1).strip() if title_match else ""
        title = re.sub(r'<[^>]+>', '', title) # clean HTML tags if any
        
        # Parse description
        desc_match = re.search(r'<meta name="description" content="(.*?)"', html)
        desc = desc_match.group(1).strip() if desc_match else ""
        
        # Parse category
        cat_match = re.search(r'<span class="text-secondary font-bold tracking-wider uppercase mb-4 block text-sm">(.*?)</span>', html)
        cat = cat_match.group(1).strip() if cat_match else "Formulasi"
        
        # Parse image
        img_match = re.search(r'<img src="(.*?)"', html)
        img = img_match.group(1).strip() if img_match else "https://images.unsplash.com/photo-1556228578-0d85b1a4d571?auto=format&fit=crop&w=600&q=80"
        
        # We don't want to list pages that aren't actually articles (just in case)
        if title and desc:
            articles.append({
                "title": title,
                "slug": slug,
                "category": cat,
                "description": desc,
                "image": img
            })

print(f"Found {len(articles)} articles.")

# Sort articles by name or date if needed (for consistency, let's sort them alphabetically by title or keep file order)
articles.sort(key=lambda x: x["title"])

html_cards = ""
for a in articles:
    html_cards += f"""
      <a href="/artikel/{a['slug']}.html" class="block group fade-in">
        <div class="bg-light-bg rounded-3xl overflow-hidden mb-4 h-56 relative border border-gray-100">
          <img src="{a['image']}" alt="{a['title']}" class="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" loading="lazy">
        </div>
        <div class="px-2">
          <span class="text-secondary text-sm font-bold tracking-wider uppercase mb-2 block">{a['category']}</span>
          <h2 class="text-xl font-black text-primary group-hover:text-secondary transition-colors mb-3 leading-snug">{a['title']}</h2>
          <p class="text-gray-500 text-sm line-clamp-2">{a['description']}</p>
        </div>
      </a>
"""

with open("artikel.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace the grid content
grid_pattern = re.compile(r'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">.*?</div>\s*</div>\s*</section>', re.DOTALL)
new_grid = f'<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">\n{html_cards}\n    </div>\n  </div>\n</section>'

new_content = grid_pattern.sub(new_grid, content)

with open("artikel.html", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully updated artikel.html with all articles!")
