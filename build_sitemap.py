import os
from datetime import datetime

print("Generating dynamic sitemap.xml...")

# Base URL
BASE_URL = "https://pabrikkosmetiktangerang.net"

# Get current date formatted for lastmod tag
today = datetime.now().strftime("%Y-%m-%d")

# Lists to hold URLs
urls = []

# Scan root directory for HTML files
for file in os.listdir('.'):
    if file.endswith('.html'):
        # Filter out temporary files if any
        if file.startswith('temp_') or file == 'google_verify.html':
            continue
            
        priority = "0.8"
        changefreq = "monthly"
        
        # Set priorities for main pages
        if file == 'index.html':
            priority = "1.0"
            changefreq = "weekly"
            url_path = ""
        else:
            url_path = file
            
        # Services pages prioritised higher
        if file.startswith('maklon-') or file.startswith('harga-'):
            priority = "0.9"
            changefreq = "weekly" if file.startswith('maklon-') else "monthly"
        elif file in ['privacy-policy.html', 'terms-of-service.html']:
            priority = "0.3"
            changefreq = "yearly"
            
        urls.append({
            "loc": f"{BASE_URL}/{url_path}",
            "lastmod": today,
            "changefreq": changefreq,
            "priority": priority
        })

# Scan artikel/ directory for blog posts
if os.path.exists('artikel'):
    for file in os.listdir('artikel'):
        if file.endswith('.html'):
            urls.append({
                "loc": f"{BASE_URL}/artikel/{file}",
                "lastmod": today,
                "changefreq": "monthly",
                "priority": "0.7"
            })

# Construct XML content
xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

for url in urls:
    xml_content += f"""  <url>
    <loc>{url['loc']}</loc>
    <lastmod>{url['lastmod']}</lastmod>
    <changefreq>{url['changefreq']}</changefreq>
    <priority>{url['priority']}</priority>
  </url>\n"""

xml_content += '</urlset>\n'

# Write to sitemap.xml
with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(xml_content)

print(f"Sitemap updated successfully with {len(urls)} URLs!")
