import os
import json

import sys
sys.path.append(os.getcwd())
import build_articles

articles = build_articles.articles

for a in articles:
    title = a['title']
    desc = a['description']
    
    expanded_content = f"""
    <p class="lead text-xl text-gray-700 font-medium mb-8"><em>{desc}</em></p>
    
    <h2 class="text-2xl font-bold text-primary mt-8 mb-4">1. Pendahuluan</h2>
    <p>Dalam dunia bisnis kosmetik dan skincare yang kompetitif saat ini, memahami topik mengenai <strong>{title}</strong> adalah kunci kesuksesan. Banyak brand owner pemula yang terjebak karena kurangnya literasi dan persiapan di tahap awal. Oleh karena itu, bersama Pabrik Kosmetik Tangerang, kami akan membedah secara tuntas mengapa hal ini sangat krusial.</p>
    <p>Industri kecantikan di Indonesia diproyeksikan akan terus bertumbuh pesat hingga tahun 2026 dan seterusnya. Pertumbuhan ini didorong oleh kesadaran masyarakat akan pentingnya perawatan diri, serta kemudahan akses untuk membangun brand melalui sistem maklon (contract manufacturing). Namun, peluang besar ini tentu dibarengi dengan tantangan yang tidak sedikit.</p>

    <h2 class="text-2xl font-bold text-primary mt-8 mb-4">2. Memahami Esensi dari {title}</h2>
    <p>Ketika Anda memutuskan untuk berinvestasi di industri ini, Anda tidak hanya menjual produk, tetapi juga kepercayaan. Konsumen saat ini sangat kritis; mereka memeriksa nomor BPOM, sertifikasi Halal, hingga rincian bahan aktif yang digunakan. Mengabaikan aspek-aspek ini sama dengan merencanakan kegagalan bisnis Anda.</p>
    <ul class="list-disc pl-6 space-y-2 mb-6">
        <li><strong>Kualitas dan Standar:</strong> Produk yang diproduksi di pabrik bersertifikat CPKB Grade A memiliki jaminan mutu yang konsisten.</li>
        <li><strong>Inovasi Berkelanjutan:</strong> Tren kosmetik sangat dinamis. Tim R&D yang handal diperlukan untuk menciptakan formula yang relevan dengan kebutuhan pasar.</li>
        <li><strong>Legalitas Terjamin:</strong> Produk tanpa izin edar BPOM berisiko ditarik dari pasaran dan merusak reputasi brand Anda secara permanen.</li>
    </ul>

    <h2 class="text-2xl font-bold text-primary mt-8 mb-4">3. Strategi Implementasi untuk Brand Anda</h2>
    <p>Langkah pertama yang harus Anda ambil adalah bermitra dengan pabrik maklon yang tepat. Pabrik Kosmetik Tangerang menawarkan layanan One-Stop Solution, mulai dari riset formula, desain kemasan, hingga pengurusan legalitas HAKI, BPOM, dan Halal MUI. Dengan demikian, Anda bisa fokus 100% pada strategi pemasaran dan distribusi.</p>
    <p>Sebagai contoh, jika Anda berencana merilis produk baru, pastikan Anda telah memperhitungkan Harga Pokok Penjualan (HPP) dengan akurat. HPP tidak hanya mencakup biaya isi produk, tetapi juga kemasan primer, kemasan sekunder, biaya legalitas, hingga biaya logistik. Margin yang sehat sangat penting untuk mendukung kampanye marketing Anda kelak.</p>

    <h2 class="text-2xl font-bold text-primary mt-8 mb-4">4. Kesalahan Umum yang Harus Dihindari</h2>
    <p>Banyak pengusaha kosmetik yang gagal karena tergiur dengan biaya maklon yang tidak wajar murahnya. Perlu diingat bahwa ada harga, ada kualitas. Bahan baku premium (grade kosmetik), proses sterilisasi, dan uji stabilitas produk membutuhkan investasi yang wajar. Jangan korbankan keamanan konsumen demi margin sesaat.</p>
    
    <h2 class="text-2xl font-bold text-primary mt-8 mb-4">5. Kesimpulan</h2>
    <p>Menguasai pemahaman tentang <strong>{title}</strong> akan menempatkan Anda selangkah lebih maju dibandingkan kompetitor. Jangan ragu untuk terus belajar dan berkonsultasi dengan para ahli di bidangnya. Pabrik Kosmetik Tangerang selalu terbuka untuk menjadi mitra strategis Anda dalam perjalanan membangun brand impian yang sukses, aman, dan legal.</p>
    """
    
    a['content'] = expanded_content

with open('build_articles.py', 'r', encoding='utf-8') as f:
    content = f.read()

template_start = content.find('template = """')
template_end = content.find('"""', template_start + 14) + 3
template_str = content[template_start:template_end]

new_build_script = f"""import os
import json

{template_str}

articles = {json.dumps(articles, indent=4, ensure_ascii=False)}

# Build process
os.makedirs('artikel', exist_ok=True)
for a in articles:
    html = template.format(
        title=a['title'],
        slug=a['slug'],
        category=a['category'],
        description=a['description'],
        content=a['content']
    )
    with open(f"artikel/{{a['slug']}}.html", 'w', encoding='utf-8') as f:
        f.write(html)
print("Berhasil membuat semua artikel!")
"""

with open('build_articles.py', 'w', encoding='utf-8') as f:
    f.write(new_build_script)
print("build_articles.py updated with expanded content.")
