import os
import glob
import random
import re

anchor_variations = [
    "pabrik kosmetik Tangerang",
    "jasa maklon kosmetik Tangerang",
    "maklon kosmetik Tangerang",
    "pabrik maklon kosmetik di Tangerang",
    "pabrik maklon skincare Tangerang",
    "pabrik kosmetik terbaik di Tangerang"
]

def inject_links():
    # Target all html files in artikel/
    files = glob.glob("d:/pabrikkosmetiktangerang.net/artikel/*.html")
    
    # Pillar pages
    pillar_pages = [
        "d:/pabrikkosmetiktangerang.net/maklon-body-care.html",
        "d:/pabrikkosmetiktangerang.net/maklon-kosmetik-dekoratif.html",
        "d:/pabrikkosmetiktangerang.net/maklon-hair-care.html",
        "d:/pabrikkosmetiktangerang.net/maklon-parfum.html",
        "d:/pabrikkosmetiktangerang.net/maklon-skincare.html"
    ]
    
    all_files = files + pillar_pages
    
    for filepath in all_files:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Check if we already injected a specific internal link block
        if "<!-- SEO INTERNAL LINK -->" in content:
            continue
            
        # Pick a random anchor text
        anchor = random.choice(anchor_variations)
        
        # Sentences wrapping the anchor text naturally
        sentences = [
            f"<p><!-- SEO INTERNAL LINK -->Sebagai <a href=\"/\" class=\"text-secondary font-bold hover:underline\">{anchor}</a> yang terpercaya, kami siap mewujudkan produk impian Anda dengan standar CPKB Grade A.</p>",
            f"<p><!-- SEO INTERNAL LINK -->Bekerjasama dengan <a href=\"/\" class=\"text-secondary font-bold hover:underline\">{anchor}</a> memberikan Anda keunggulan kompetitif dalam hal efisiensi biaya dan legalitas terjamin.</p>",
            f"<p><!-- SEO INTERNAL LINK -->Jika Anda mencari mitra produksi yang handal, <a href=\"/\" class=\"text-secondary font-bold hover:underline\">{anchor}</a> kami menawarkan layanan one-stop solution dari formulasi hingga desain kemasan.</p>",
            f"<p><!-- SEO INTERNAL LINK -->Keberhasilan brand Anda adalah prioritas kami selaku <a href=\"/\" class=\"text-secondary font-bold hover:underline\">{anchor}</a> berpengalaman yang telah melahirkan berbagai brand sukses di Indonesia.</p>"
        ]
        
        injection = random.choice(sentences)
        
        # Inject before the CTA box in articles, or before closing </section> in pillar pages
        if "bg-primary/5 p-8 rounded-2xl mt-12" in content:
            # Article CTA box
            new_content = content.replace('<div class="bg-primary/5 p-8 rounded-2xl mt-12', injection + '\n\n      <div class="bg-primary/5 p-8 rounded-2xl mt-12')
        elif "</section>" in content:
            # In pillar pages, try to find the last section before the footer or CTA
            # Let's just find the CTA section and inject before it
            if "bg-secondary text-center" in content:
                new_content = content.replace('<section class="py-20 bg-secondary text-center">', f'<section class="py-12 bg-white"><div class="max-w-3xl mx-auto px-4 text-center text-lg text-gray-600">{injection}</div></section>\n<section class="py-20 bg-secondary text-center">')
            else:
                continue
        else:
            continue
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
            
    print(f"Processed {len(all_files)} files for internal link injection.")

if __name__ == "__main__":
    inject_links()
