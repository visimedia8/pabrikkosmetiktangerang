import re

BASE = "d:/pabrikkosmetiktangerang.net"

# ─────────────────────────────────────────────
# 1. FIX index.html — tambah syarat-cara-maklon ke nav
#    dan tambah section "Semua Layanan" yg link ke pillar pages
# ─────────────────────────────────────────────
with open(f"{BASE}/index.html", "r", encoding="utf-8") as f:
    idx = f.read()

# Tambah syarat-cara-maklon di desktop nav (sebelum Blog)
if "syarat-cara-maklon" not in idx:
    idx = idx.replace(
        '<a href="/artikel.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Blog</a>',
        '<a href="/syarat-cara-maklon.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Cara Maklon</a>\n                    <a href="/artikel.html" class="text-gray-600 hover:text-primary font-semibold transition-colors">Blog</a>'
    )
    # Mobile menu juga
    idx = idx.replace(
        '<a href="/artikel.html" class="block text-lg font-bold text-gray-700">Blog</a>',
        '<a href="/syarat-cara-maklon.html" class="block text-lg font-bold text-gray-700">Cara Maklon</a>\n            <a href="/artikel.html" class="block text-lg font-bold text-gray-700">Blog</a>'
    )
    print("  - Added syarat-cara-maklon to index.html nav")
else:
    print("  - syarat-cara-maklon already in index.html nav")

# Inject "Semua Layanan Maklon" section sebelum section harga
LAYANAN_SECTION = """
    <!-- SEMUA LAYANAN SECTION -->
    <section id="layanan-lengkap" class="py-20 bg-light-bg">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-14 fade-in">
                <h2 class="text-3xl md:text-4xl font-black text-primary mb-4">Semua Layanan Maklon Kami</h2>
                <p class="text-gray-500 text-lg max-w-2xl mx-auto">Kami memproduksi semua kategori kosmetik dengan standar CPKB Grade A, BPOM, dan Halal MUI.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
                <a href="/maklon-skincare.html" class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all fade-in group">
                    <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">face</span>
                    <h3 class="text-xl font-black text-primary mb-2 group-hover:text-secondary transition-colors">Maklon Skincare</h3>
                    <p class="text-gray-500 text-sm">Serum, sunscreen, moisturizer, facial wash, toner, dan produk perawatan wajah lainnya.</p>
                    <span class="text-secondary font-bold text-sm mt-4 block">Lihat Detail &rarr;</span>
                </a>
                <a href="/maklon-body-care.html" class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all fade-in group">
                    <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">self_care</span>
                    <h3 class="text-xl font-black text-primary mb-2 group-hover:text-secondary transition-colors">Maklon Body Care</h3>
                    <p class="text-gray-500 text-sm">Body lotion, body scrub, body wash, lulur, hand cream, dan produk perawatan tubuh.</p>
                    <span class="text-secondary font-bold text-sm mt-4 block">Lihat Detail &rarr;</span>
                </a>
                <a href="/maklon-hair-care.html" class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all fade-in group">
                    <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">dry_cleaning</span>
                    <h3 class="text-xl font-black text-primary mb-2 group-hover:text-secondary transition-colors">Maklon Hair Care</h3>
                    <p class="text-gray-500 text-sm">Shampo, kondisioner, hair mask, hair serum, hair tonic, dan produk perawatan rambut.</p>
                    <span class="text-secondary font-bold text-sm mt-4 block">Lihat Detail &rarr;</span>
                </a>
                <a href="/maklon-kosmetik-dekoratif.html" class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all fade-in group">
                    <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">brush</span>
                    <h3 class="text-xl font-black text-primary mb-2 group-hover:text-secondary transition-colors">Maklon Kosmetik Dekoratif</h3>
                    <p class="text-gray-500 text-sm">Lipstik, lip cream, foundation, bedak, blush on, eyeshadow, dan makeup lainnya.</p>
                    <span class="text-secondary font-bold text-sm mt-4 block">Lihat Detail &rarr;</span>
                </a>
                <a href="/maklon-parfum.html" class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-lg hover:-translate-y-1 transition-all fade-in group">
                    <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">water</span>
                    <h3 class="text-xl font-black text-primary mb-2 group-hover:text-secondary transition-colors">Maklon Parfum</h3>
                    <p class="text-gray-500 text-sm">Eau de Parfum, Eau de Toilette, body mist, cologne, dan produk wewangian premium.</p>
                    <span class="text-secondary font-bold text-sm mt-4 block">Lihat Detail &rarr;</span>
                </a>
                <a href="/syarat-cara-maklon.html" class="bg-primary p-8 rounded-2xl hover:shadow-lg hover:-translate-y-1 transition-all fade-in group">
                    <span class="material-symbols-outlined text-4xl text-secondary mb-4 block">checklist</span>
                    <h3 class="text-xl font-black text-white mb-2">Syarat & Cara Maklon</h3>
                    <p class="text-white/70 text-sm">Pelajari alur kerja, persyaratan dokumen, dan SOP produksi kami yang transparan.</p>
                    <span class="text-secondary font-bold text-sm mt-4 block">Pelajari Selengkapnya &rarr;</span>
                </a>
            </div>
        </div>
    </section>
"""

# Inject sebelum section harga (cari id="harga")
if 'id="layanan-lengkap"' not in idx:
    idx = idx.replace('<section id="harga"', LAYANAN_SECTION + '\n    <section id="harga"')
    print("  - Added Semua Layanan section to index.html")
else:
    print("  - Semua Layanan section already exists in index.html")

with open(f"{BASE}/index.html", "w", encoding="utf-8") as f:
    f.write(idx)
print("  index.html saved.")

# ─────────────────────────────────────────────
# 2. FIX maklon-skincare.html — tambah Blog & syarat ke nav
#    dan tambah "Layanan Terkait" cross-links section
# ─────────────────────────────────────────────
PILLAR_FILES = [
    "maklon-skincare.html",
    "maklon-body-care.html",
    "maklon-hair-care.html",
    "maklon-kosmetik-dekoratif.html",
    "maklon-parfum.html",
]

# Cross-link definitions: for each pillar, which other pillars to link to
CROSS_LINKS = {
    "maklon-skincare.html": [
        ("/maklon-body-care.html", "Maklon Body Care", "self_care"),
        ("/maklon-hair-care.html", "Maklon Hair Care", "dry_cleaning"),
        ("/maklon-kosmetik-dekoratif.html", "Maklon Dekoratif", "brush"),
        ("/maklon-parfum.html", "Maklon Parfum", "water"),
    ],
    "maklon-body-care.html": [
        ("/maklon-skincare.html", "Maklon Skincare", "face"),
        ("/maklon-hair-care.html", "Maklon Hair Care", "dry_cleaning"),
        ("/maklon-kosmetik-dekoratif.html", "Maklon Dekoratif", "brush"),
        ("/maklon-parfum.html", "Maklon Parfum", "water"),
    ],
    "maklon-hair-care.html": [
        ("/maklon-skincare.html", "Maklon Skincare", "face"),
        ("/maklon-body-care.html", "Maklon Body Care", "self_care"),
        ("/maklon-kosmetik-dekoratif.html", "Maklon Dekoratif", "brush"),
        ("/maklon-parfum.html", "Maklon Parfum", "water"),
    ],
    "maklon-kosmetik-dekoratif.html": [
        ("/maklon-skincare.html", "Maklon Skincare", "face"),
        ("/maklon-body-care.html", "Maklon Body Care", "self_care"),
        ("/maklon-hair-care.html", "Maklon Hair Care", "dry_cleaning"),
        ("/maklon-parfum.html", "Maklon Parfum", "water"),
    ],
    "maklon-parfum.html": [
        ("/maklon-skincare.html", "Maklon Skincare", "face"),
        ("/maklon-body-care.html", "Maklon Body Care", "self_care"),
        ("/maklon-hair-care.html", "Maklon Hair Care", "dry_cleaning"),
        ("/maklon-kosmetik-dekoratif.html", "Maklon Dekoratif", "brush"),
    ],
}

for fname in PILLAR_FILES:
    fpath = f"{BASE}/{fname}"
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    # Fix nav: add Blog link if missing
    if '/artikel.html" class="text-gray-600 hover:text-primary font-semibold">Blog' not in content:
        content = content.replace(
            '<a href="https://wa.me/6283863670421" class="bg-cta text-white px-6 py-2.5 rounded-full font-bold flex items-center gap-2"><span class="material-symbols-outlined text-lg">chat</span>WhatsApp</a>',
            '<a href="/syarat-cara-maklon.html" class="text-gray-600 hover:text-primary font-semibold">Cara Maklon</a>\n      <a href="/artikel.html" class="text-gray-600 hover:text-primary font-semibold">Blog</a>\n      <a href="https://wa.me/6283863670421" class="bg-cta text-white px-6 py-2.5 rounded-full font-bold flex items-center gap-2"><span class="material-symbols-outlined text-lg">chat</span>WhatsApp</a>'
        )
        changed = True
        print(f"  - Fixed nav in {fname}")

    # Fix footer: replace simple footer with full footer
    SIMPLE_FOOTER = '<footer class="bg-gray-900 pt-16 pb-8 border-t border-white/10">'
    FULL_FOOTER = """<footer class="bg-gray-900 pt-16 pb-8 border-t border-white/10">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-10 mb-12">
      <div>
        <a href="/" class="flex items-center gap-2 mb-6"><span class="material-symbols-outlined text-secondary text-4xl">science</span><span class="font-extrabold text-2xl text-white uppercase">Pabrik <span class="text-secondary">Kosmetik</span></span></a>
        <p class="text-gray-400 text-sm leading-relaxed">Jasa maklon skincare & kosmetik bersertifikat CPKB Grade A, BPOM, dan Halal MUI di Tangerang.</p>
      </div>
      <div>
        <h4 class="text-white font-black text-lg mb-5">Layanan</h4>
        <ul class="space-y-3 text-gray-400 text-sm">
          <li><a href="/maklon-skincare.html" class="hover:text-secondary">Maklon Skincare</a></li>
          <li><a href="/maklon-body-care.html" class="hover:text-secondary">Maklon Body Care</a></li>
          <li><a href="/maklon-hair-care.html" class="hover:text-secondary">Maklon Hair Care</a></li>
          <li><a href="/maklon-kosmetik-dekoratif.html" class="hover:text-secondary">Maklon Dekoratif</a></li>
          <li><a href="/maklon-parfum.html" class="hover:text-secondary">Maklon Parfum</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-black text-lg mb-5">Informasi</h4>
        <ul class="space-y-3 text-gray-400 text-sm">
          <li><a href="/harga-maklon-kosmetik.html" class="hover:text-secondary">Harga Maklon</a></li>
          <li><a href="/syarat-cara-maklon.html" class="hover:text-secondary">Syarat & Cara Maklon</a></li>
          <li><a href="/sertifikasi-bpom-halal.html" class="hover:text-secondary">Sertifikasi BPOM & Halal</a></li>
          <li><a href="/tentang-kami.html" class="hover:text-secondary">Tentang Kami</a></li>
          <li><a href="/artikel.html" class="hover:text-secondary">Blog & Edukasi</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-black text-lg mb-5">Hubungi Kami</h4>
        <ul class="space-y-3 text-gray-400 text-sm">
          <li class="flex items-start gap-2"><span class="material-symbols-outlined text-secondary text-base mt-0.5">location_on</span><span>Kaw. Industri Jatake, Tangerang 15143</span></li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-base">phone</span><a href="https://wa.me/6283863670421" class="hover:text-secondary">+62 838-6367-0421</a></li>
          <li class="flex items-center gap-2"><span class="material-symbols-outlined text-secondary text-base">email</span><span>halo@pabrikkosmetiktangerang.net</span></li>
        </ul>
      </div>
    </div>
    <div class="border-t border-gray-800 pt-6 flex flex-col md:flex-row justify-between items-center gap-4 text-sm text-gray-500">
      <p>&copy; 2026 Pabrik Kosmetik Tangerang. All rights reserved.</p>
      <div class="flex gap-4"><a href="/sitemap.xml" class="hover:text-secondary">Sitemap</a></div>
    </div>
  </div>"""

    if SIMPLE_FOOTER in content and 'grid-cols-4' not in content:
        content = content.replace(SIMPLE_FOOTER, FULL_FOOTER)
        changed = True
        print(f"  - Upgraded footer in {fname}")

    # Add cross-links "Layanan Lainnya" section before footer CTA / before footer
    cross = CROSS_LINKS.get(fname, [])
    if cross and 'Layanan Kami Lainnya' not in content:
        cards = ""
        for url, label, icon in cross:
            cards += f"""
                <a href="{url}" class="bg-white p-5 rounded-xl shadow-sm hover:shadow-md hover:-translate-y-0.5 transition-all flex items-center gap-4">
                    <span class="material-symbols-outlined text-3xl text-secondary shrink-0">{icon}</span>
                    <div><h4 class="font-black text-primary text-base">{label}</h4><span class="text-secondary text-sm font-semibold">Lihat Detail &rarr;</span></div>
                </a>"""

        CROSS_SECTION = f"""
<section class="py-16 bg-light-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-2xl font-black text-primary mb-8 text-center">Layanan Kami Lainnya</h2>
    <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">{cards}
    </div>
  </div>
</section>

"""
        # Inject before footer
        content = content.replace('<footer class="bg-gray-900', CROSS_SECTION + '<footer class="bg-gray-900')
        changed = True
        print(f"  - Added cross-links section to {fname}")

    if changed:
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  - Saved {fname}")
    else:
        print(f"  - No changes needed for {fname}")

print("\nAll nav/orphan/footer fixes done.")
