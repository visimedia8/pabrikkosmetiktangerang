import os

PROCESS_SECTION = """
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <h2 class="text-3xl md:text-4xl font-black text-primary mb-4">Proses Maklon Kosmetik</h2>
      <p class="text-gray-500 text-lg">Langkah mudah mewujudkan brand impian Anda dari ide hingga siap jual.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
      <div class="text-center fade-in">
        <div class="w-16 h-16 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-2xl font-black mb-4">1</div>
        <h4 class="font-bold text-primary text-xl mb-2">Konsultasi</h4>
        <p class="text-gray-600 text-sm">Diskusi konsep produk, target pasar, bahan aktif, kemasan, hingga estimasi HPP bersama tim R&D.</p>
      </div>
      <div class="text-center fade-in">
        <div class="w-16 h-16 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-2xl font-black mb-4">2</div>
        <h4 class="font-bold text-primary text-xl mb-2">Pembuatan Sampel</h4>
        <p class="text-gray-600 text-sm">Tim kami meracik sampel. Anda dapat merevisi formula hingga mendapatkan tekstur dan hasil yang sesuai.</p>
      </div>
      <div class="text-center fade-in">
        <div class="w-16 h-16 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-2xl font-black mb-4">3</div>
        <h4 class="font-bold text-primary text-xl mb-2">Legalitas & Desain</h4>
        <p class="text-gray-600 text-sm">Pengurusan Notifikasi BPOM, Sertifikasi Halal, HAKI, serta finalisasi desain kemasan primer dan sekunder.</p>
      </div>
      <div class="text-center fade-in">
        <div class="w-16 h-16 mx-auto bg-primary text-white rounded-full flex items-center justify-center text-2xl font-black mb-4">4</div>
        <h4 class="font-bold text-primary text-xl mb-2">Produksi Massal</h4>
        <p class="text-gray-600 text-sm">Produksi skala besar di pabrik standar CPKB Grade A. Produk dikemas dan siap dikirim ke gudang Anda.</p>
      </div>
    </div>
  </div>
</section>

<section class="py-20 bg-light-bg">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <h2 class="text-3xl font-black text-primary mb-10 text-center fade-in">Pertanyaan Seputar Maklon (FAQ)</h2>
    <div class="space-y-4 fade-in">
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa Minimum Order Quantity (MOQ)?</h4>
        <p class="text-gray-600">MOQ kami sangat fleksibel untuk UMKM, mulai dari 500 pcs - 1.000 pcs per varian tergantung jenis kemasan dan formula.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa lama proses dari awal hingga produk jadi?</h4>
        <p class="text-gray-600">Estimasi waktu keseluruhan sekitar 2-3 bulan, sebagian besar waktu digunakan untuk menunggu keluarnya izin Notifikasi BPOM.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah pabrik bisa bantu desain kemasan?</h4>
        <p class="text-gray-600">Tentu! Tim desain in-house kami siap membantu mendesain logo, kemasan primer (botol/tube), dan sekunder (box) yang estetik.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah kerahasiaan formula terjamin?</h4>
        <p class="text-gray-600">Kami menjamin 100% kerahasiaan formula eksklusif brand Anda dengan Surat Perjanjian Kerahasiaan (Non-Disclosure Agreement).</p>
      </div>
    </div>
  </div>
</section>
"""

money_pages = [
    'maklon-skincare.html',
    'maklon-body-care.html',
    'maklon-hair-care.html',
    'maklon-kosmetik-dekoratif.html',
    'maklon-parfum.html',
    'harga-maklon-kosmetik.html'
]

for page in money_pages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Insert before the SEO Internal Link section or the CTA section
        target = '<section class="py-12 bg-white">'
        if target in content and PROCESS_SECTION not in content:
            content = content.replace(target, PROCESS_SECTION + '\n' + target)
            with open(page, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Expanded content in {page}")
