import os
import re

NAVBAR_HTML = """<nav id="navbar" class="fixed w-full z-50 bg-white/90 backdrop-blur-md border-b border-gray-200 transition-all duration-300">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <a href="/" class="flex items-center gap-2">
                    <span class="material-symbols-outlined text-secondary text-3xl">science</span>
                    <span class="font-extrabold text-xl md:text-2xl tracking-tight text-primary uppercase">Pabrik <span class="text-secondary">Kosmetik</span></span>
                </a>
                
                <!-- Desktop Nav -->
                <div class="hidden md:flex items-center space-x-6">
                    <a href="/" class="text-gray-600 hover:text-primary font-semibold transition-colors">Beranda</a>
                    <a href="/maklon-skincare.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Layanan</a>
                    <a href="/harga-maklon-kosmetik.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Harga</a>
                    <a href="/sertifikasi-bpom-halal.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Sertifikasi</a>
                    <a href="/tentang-kami.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Tentang Kami</a>
                    <a href="/artikel.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Blog</a>
                    <a href="https://wa.me/6283863670421" class="bg-cta hover:bg-cta-hover text-white px-6 py-2.5 rounded-full font-bold transition-all flex items-center gap-2 shadow-lg shadow-cta/30 hover:shadow-cta/50 hover:-translate-y-0.5">
                        <span class="material-symbols-outlined text-[20px]">chat</span> WhatsApp
                    </a>
                </div>
            </div>
        </div>
    </nav>"""

FOOTER_HTML = """<footer class="bg-gray-900 pt-16 pb-8 border-t border-white/10 mt-12">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">
      <div>
        <a href="/" class="flex items-center gap-2 mb-6"><span class="material-symbols-outlined text-secondary text-4xl">science</span><span class="font-extrabold text-2xl text-white uppercase">Pabrik <span class="text-secondary">Kosmetik</span></span></a>
        <p class="text-gray-400 text-sm leading-relaxed">Jasa maklon skincare & kosmetik bersertifikat CPKB Grade A, BPOM, dan Halal MUI di Tangerang. Kami siap membantu Anda membangun brand impian.</p>
      </div>
      <div>
        <h4 class="text-white font-bold mb-6 text-lg">Layanan Maklon</h4>
        <ul class="space-y-4 text-gray-400 text-sm">
          <li><a href="/maklon-skincare.html" class="hover:text-secondary transition-colors">Maklon Skincare</a></li>
          <li><a href="/maklon-body-care.html" class="hover:text-secondary transition-colors">Maklon Body Care</a></li>
          <li><a href="/maklon-hair-care.html" class="hover:text-secondary transition-colors">Maklon Hair Care</a></li>
          <li><a href="/maklon-kosmetik-dekoratif.html" class="hover:text-secondary transition-colors">Maklon Dekoratif</a></li>
          <li><a href="/maklon-parfum.html" class="hover:text-secondary transition-colors">Maklon Parfum</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-bold mb-6 text-lg">Perusahaan</h4>
        <ul class="space-y-4 text-gray-400 text-sm">
          <li><a href="/tentang-kami.html" class="hover:text-secondary transition-colors">Tentang Kami</a></li>
          <li><a href="/harga-maklon-kosmetik.html" class="hover:text-secondary transition-colors">Harga Maklon</a></li>
          <li><a href="/sertifikasi-bpom-halal.html" class="hover:text-secondary transition-colors">Sertifikasi & Legalitas</a></li>
          <li><a href="/artikel.html" class="hover:text-secondary transition-colors">Blog & Edukasi</a></li>
          <li><a href="/hubungi-kami.html" class="hover:text-secondary transition-colors">Hubungi Kami</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-bold mb-6 text-lg">Legal & Kontak</h4>
        <ul class="space-y-4 text-gray-400 text-sm">
          <li><a href="/privacy-policy.html" class="hover:text-secondary transition-colors">Kebijakan Privasi</a></li>
          <li><a href="/terms-of-service.html" class="hover:text-secondary transition-colors">Syarat dan Ketentuan</a></li>
          <li class="flex items-start gap-2 mt-4"><span class="material-symbols-outlined text-secondary text-sm">location_on</span><span>Kawasan Industri Tangerang, Banten 15143, Indonesia</span></li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-sm">mail</span><a href="mailto:halo@pabrikkosmetiktangerang.net" class="hover:text-secondary transition-colors">halo@pabrikkosmetiktangerang.net</a></li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-sm">call</span><a href="https://wa.me/6283863670421" class="hover:text-secondary transition-colors">+62 838-6367-0421</a></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-gray-800 pt-8 flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-500">
      <p>&copy; 2026 Pabrik Kosmetik Tangerang. All rights reserved.</p>
    </div>
  </div>
</footer>"""

FAVICON_TAG = '<link rel="icon" href="/logo.svg" type="image/svg+xml">'

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Nav
    if '<nav' in content:
        content = re.sub(r'<nav.*?</nav>', NAVBAR_HTML, content, flags=re.DOTALL)
    else:
        # If no nav, insert after <body>
        content = re.sub(r'<body[^>]*>', lambda m: m.group(0) + '\\n' + NAVBAR_HTML, content)
    
    # Update Footer
    if '<footer' in content:
        content = re.sub(r'<footer.*?</footer>', FOOTER_HTML, content, flags=re.DOTALL)
    else:
        # If no footer, insert before </body>
        content = content.replace('</body>', FOOTER_HTML + '\\n</body>')
    
    # Remove old logo.png
    content = content.replace('<link rel="icon" href="/logo.png" type="image/png">', '')
    
    # Update Favicon (add to head if not present)
    if '<head>' in content and FAVICON_TAG not in content:
        content = content.replace('</head>', f'    {FAVICON_TAG}\\n</head>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for root, dirs, files in os.walk('.'):
    if '.venv' in root or '__pycache__' in root or '.git' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            path = os.path.join(root, file)
            update_file(path)
            print(f"Updated layout for {path}")
