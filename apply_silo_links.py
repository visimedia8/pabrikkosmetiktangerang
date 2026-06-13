import os
import re

print("Running apply_silo_links.py to inject silo links and homepage anchor text variations...")

# Define anchor text mappings for each of the 12 new articles
article_links_config = {
    "perbedaan-serum-niacinamide-vs-vitamin-c": {
        "pillar_link": "/maklon-serum-wajah.html",
        "pillar_anchors": ["maklon serum wajah"],
        "homepage_anchor": "Pabrik Kosmetik Tangerang", # Branded EMD (20%)
        "homepage_keyword": "Pabrik Kosmetik Tangerang"
    },
    "modal-membuat-brand-serum-wajah-sendiri": {
        "pillar_link": "/maklon-serum-wajah.html",
        "pillar_anchors": ["maklon serum wajah"],
        "homepage_anchor": "jasa maklon kosmetik Tangerang", # Exact Match (40%)
        "homepage_keyword": "jasa maklon kosmetik Tangerang"
    },
    "cara-kerja-hybrid-sunscreen-dan-keunggulannya": {
        "pillar_link": "/maklon-sunscreen.html",
        "pillar_anchors": ["maklon sunscreen"],
        "homepage_anchor": "Pabrik Kosmetik Tangerang", # Branded EMD (20%)
        "homepage_keyword": "Pabrik Kosmetik Tangerang"
    },
    "biaya-moq-maklon-sunscreen-spf-50": {
        "pillar_link": "/maklon-sunscreen.html",
        "pillar_anchors": ["maklon sunscreen"],
        "homepage_anchor": "maklon kosmetik Tangerang", # Exact Match (40%)
        "homepage_keyword": "maklon kosmetik Tangerang"
    },
    "sabun-wajah-low-ph-skin-barrier": {
        "pillar_link": "/maklon-facial-wash.html",
        "pillar_anchors": ["maklon facial wash"],
        "homepage_anchor": "bikin brand kosmetik sendiri", # LSI / Partial (30%)
        "homepage_keyword": "bikin brand kosmetik sendiri"
    },
    "peluang-bisnis-sabun-cuci-muka-mild-surfactant": {
        "pillar_link": "/maklon-facial-wash.html",
        "pillar_anchors": ["maklon facial wash"],
        "homepage_anchor": "jasa maklon kosmetik Tangerang", # Exact Match (40%)
        "homepage_keyword": "jasa maklon kosmetik Tangerang"
    },
    "tips-memilih-bahan-aktif-body-lotion-tone-up": {
        "pillar_link": "/maklon-body-lotion.html",
        "pillar_anchors": ["maklon body lotion"],
        "homepage_anchor": "jasa pembuatan kosmetik", # LSI / Partial (30%)
        "homepage_keyword": "jasa pembuatan kosmetik"
    },
    "modal-maklon-body-lotion-wangi-parfum-mewah": {
        "pillar_link": "/maklon-body-lotion.html",
        "pillar_anchors": ["maklon body lotion"],
        "homepage_anchor": "maklon kosmetik Tangerang", # Exact Match (40%)
        "homepage_keyword": "maklon kosmetik Tangerang"
    },
    "manfaat-eksfoliasi-mingguan-lulur-body-scrub": {
        "pillar_link": "/maklon-body-scrub.html",
        "pillar_anchors": ["maklon body scrub"],
        "homepage_anchor": "maklon kecantikan", # LSI / Partial (30%)
        "homepage_keyword": "maklon kecantikan"
    },
    "panduan-bisnis-lulur-body-scrub-merek-sendiri": {
        "pillar_link": "/maklon-body-scrub.html",
        "pillar_anchors": ["maklon body scrub"],
        "homepage_anchor": "jasa maklon kosmetik Tangerang", # Exact Match (40%)
        "homepage_keyword": "jasa maklon kosmetik Tangerang"
    },
    "mengenal-redensyl-capixyl-penumbuh-rambut": {
        "pillar_link": "/maklon-shampoo-anti-rontok.html",
        "pillar_anchors": ["maklon shampo anti-rontok"],
        "homepage_anchor": "kunjungi beranda kami", # Generic (10%)
        "homepage_keyword": "kunjungi beranda kami"
    },
    "biaya-moq-maklon-shampo-anti-rontok-bpom": {
        "pillar_link": "/maklon-shampoo-anti-rontok.html",
        "pillar_anchors": ["maklon shampo anti-rontok"],
        "homepage_anchor": "bikin brand kosmetik sendiri", # LSI / Partial (30%)
        "homepage_keyword": "bikin brand kosmetik sendiri"
    }
}

# Add fallback keywords for homepage links inside old articles to ensure wide linking
old_article_homepage_links = [
    ("maklon kosmetik Tangerang", "Exact"),
    ("jasa maklon kosmetik Tangerang", "Exact"),
    ("Pabrik Kosmetik Tangerang", "Branded"),
    ("bikin brand kosmetik sendiri", "LSI"),
    ("jasa pembuatan kosmetik", "LSI"),
    ("kunjungi beranda kami", "Generic")
]

# Apply updates to each HTML file in articles/
for filename in os.listdir("artikel"):
    if not filename.endswith(".html"):
        continue
    
    slug = filename[:-5]
    filepath = os.path.join("artikel", filename)
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    updated = False
    
    # If it is one of the 12 new spoke articles, apply specific silo configurations
    if slug in article_links_config:
        config = article_links_config[slug]
        
        # 1. Silo Link (Spoke to Pillar)
        # Find the first occurrences of pillar anchor keywords and wrap in link
        for anchor in config["pillar_anchors"]:
            # Match the text but avoid replacing it if it's already inside an <a> tag
            pattern = re.compile(rf'(?<!href=")(?<!">){re.escape(anchor)}', re.IGNORECASE)
            if pattern.search(content):
                # Replace only the first occurrence
                content = pattern.sub(f'<a href="{config["pillar_link"]}" class="text-secondary font-bold hover:underline">{anchor}</a>', content, count=1)
                updated = True
                
        # 2. Homepage link injection
        # Look for the homepage keyword. In case it doesn't exist, we'll append a contextual sentence.
        keyword = config["homepage_keyword"]
        # Match keyword but avoid replacing it if it's already in an <a> tag
        pattern = re.compile(rf'(?<!href=")(?<!">){re.escape(keyword)}', re.IGNORECASE)
        if pattern.search(content):
            content = pattern.sub(f'<a href="/" class="text-secondary font-bold hover:underline">{config["homepage_anchor"]}</a>', content, count=1)
            updated = True
        else:
            # Append a clean linking sentence before the closing tags of the content area
            linking_sentence = f'\n    <p>Sebagai bagian dari komitmen kami, <a href="/" class="text-secondary font-bold hover:underline">{config["homepage_anchor"]}</a> selalu mengutamakan standardisasi kualitas produk terbaik.</p>'
            content = content.replace("</article>", linking_sentence + "\n</article>")
            updated = True
            
    # For older articles, let's inject a homepage link using one of the keywords if not already present
    else:
        # Check if they already have homepage links
        if 'href="/"' not in content and 'href="https://pabrikkosmetiktangerang.net"' not in content:
            # Let's see if we can find one of our homepage keywords to link
            for keyword, _ in old_article_homepage_links:
                pattern = re.compile(rf'(?<!href=")(?<!">){re.escape(keyword)}', re.IGNORECASE)
                if pattern.search(content):
                    content = pattern.sub(f'<a href="/" class="text-secondary font-bold hover:underline">{keyword}</a>', content, count=1)
                    updated = True
                    break
            
            # If no keyword found, append a generic sentence at the bottom of the article
            if not updated:
                linking_sentence = '\n    <p>Untuk informasi lengkap profil perusahaan kami, silakan <a href="/" class="text-secondary font-bold hover:underline">kunjungi beranda kami</a>.</p>'
                content = content.replace("      <div class=\"bg-primary/5", linking_sentence + "\n      <div class=\"bg-primary/5")
                updated = True

    if updated:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Injected silo/homepage links in {filepath}")

print("Silo internal links applied successfully!")
