import os
import json

# Load SSOT config
with open("ssot_lexicon.json", "r", encoding="utf-8") as f:
    ssot = json.load(f)

biz = ssot["business_info"]
pkg_basic = ssot["packages"]["basic"]
pkg_ent = ssot["packages"]["enterprise"]

# Base HTML Template
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{meta_title}</title>
<meta name="description" content="{meta_desc}">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://pabrikkosmetiktangerang.net/{filename}">
<meta property="og:title" content="{meta_title}">
<meta property="og:description" content="{meta_desc}">
<meta property="og:url" content="https://pabrikkosmetiktangerang.net/{filename}">
<meta property="og:type" content="website">
<meta property="og:locale" content="id_ID">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap"/>
<script src="https://cdn.tailwindcss.com?plugins=forms"></script>
<script>
tailwind.config={{
  theme:{{
    extend:{{
      colors:{{
        primary:'#1A3A4A',
        'primary-light':'#2A5A72',
        secondary:'#D4A855',
        cta:'#2ECC8B',
        'cta-hover':'#27AE60',
        'off-white':'#F8F9FA',
        'light-bg':'#F0F4F5'
      }},
      fontFamily:{{
        sans:['Plus Jakarta Sans','sans-serif']
      }}
    }}
  }}
}}
</script>
<style>
html {{ scroll-behavior: smooth; }}
.fade-in {{ opacity: 0; transform: translateY(20px); transition: all 0.6s ease-out; }}
.fade-in.visible {{ opacity: 1; transform: translateY(0); }}
</style>
<script type="application/ld+json">
{schema_json}
</script>
<link rel="icon" href="/logo.svg" type="image/svg+xml">
</head>
<body class="bg-off-white text-primary font-sans antialiased">

<!-- NAVBAR PLACEHOLDER (Will be injected by inject_layout.py) -->
<nav id="navbar"></nav>

<div class="pt-24 pb-2 bg-white border-b border-gray-100">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-sm text-gray-500 flex items-center gap-2">
    <a href="/" class="hover:text-primary">Beranda</a>
    <span>&rsaquo;</span>
    <span class="text-gray-400">{category}</span>
    <span>&rsaquo;</span>
    <span class="text-primary font-semibold">{product_name}</span>
  </div>
</div>

<!-- HERO SECTION -->
<section class="bg-gradient-to-r from-primary to-primary-light py-20 lg:py-28 text-white relative overflow-hidden">
  <div class="absolute inset-0 opacity-10 bg-[radial-gradient(ellipse_at_center,_var(--tw-gradient-stops))] from-secondary via-transparent to-transparent"></div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="max-w-3xl fade-in">
      <span class="inline-block bg-secondary/20 text-secondary border border-secondary/30 font-bold px-4 py-1.5 rounded-full text-xs uppercase tracking-wider mb-6">Jasa Maklon Spesialis</span>
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-black leading-tight mb-8">
        Jasa Maklon <span class="text-secondary">{product_name}</span> Tangerang
      </h1>
      <p class="text-lg md:text-xl text-gray-200 mb-10 leading-relaxed">
        {hero_desc}
      </p>
      <div class="flex flex-col sm:flex-row gap-4">
        <a href="https://wa.me/6283863670421" class="inline-flex items-center justify-center gap-3 bg-cta hover:bg-cta-hover text-white px-8 py-4 rounded-2xl font-black text-lg shadow-xl shadow-cta/30 transition-all hover:-translate-y-0.5">
          <span class="material-symbols-outlined">chat</span> Konsultasi R&D Gratis
        </a>
        <a href="#spesifikasi" class="inline-flex items-center justify-center gap-2 border border-white/30 hover:border-white text-white px-8 py-4 rounded-2xl font-bold text-lg transition-all">
          Lihat Spesifikasi & Detail
        </a>
      </div>
    </div>
  </div>
</section>

<!-- AEO DIRECT ANSWER SECTION -->
<section class="py-12 bg-white border-b border-gray-100">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-light-bg/50 border-l-4 border-secondary p-6 rounded-r-2xl shadow-sm">
      <h3 class="text-xs font-bold uppercase tracking-wider text-secondary mb-2">Jawaban Langsung (AEO Summary)</h3>
      <p class="text-lg text-primary font-medium leading-relaxed italic">
        "{aeo_paragraph}"
      </p>
    </div>
  </div>
</section>

<!-- MAIN CONTENT SECTION (ANTI-THIN CONTENT) -->
<section class="py-20 bg-white" id="detail-layanan">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 lg:grid-cols-12 gap-12">
      
      <!-- Content Area -->
      <div class="lg:col-span-8 prose prose-lg text-gray-600 max-w-none">
        {main_content}
      </div>

      <!-- Sidebar Form / Info -->
      <div class="lg:col-span-4">
        <div class="bg-light-bg p-8 rounded-3xl border border-gray-200/50 sticky top-28 shadow-sm">
          <h3 class="text-xl font-black text-primary mb-4">Mulai Brand Anda Hari Ini</h3>
          <p class="text-sm text-gray-500 mb-6">Dapatkan kemudahan membuat brand kecantikan kustom berstandar internasional bersama Pabrik Kosmetik Tangerang.</p>
          
          <div class="space-y-4 mb-8">
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-secondary">verified_user</span>
              <span class="text-sm font-semibold text-primary">Sertifikasi CPKB Grade A & BPOM</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-secondary">eco</span>
              <span class="text-sm font-semibold text-primary">Bahan Organik & Halal MUI</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-secondary">payment</span>
              <span class="text-sm font-semibold text-primary">MOQ Rendah Mulai 500 Pcs</span>
            </div>
            <div class="flex items-center gap-3">
              <span class="material-symbols-outlined text-secondary">design_services</span>
              <span class="text-sm font-semibold text-primary">Desain Kemasan In-House Gratis</span>
            </div>
          </div>

          <a href="https://wa.me/6283863670421" class="w-full text-center bg-primary hover:bg-primary-light text-white py-4 rounded-xl font-bold transition-all block mb-3 shadow-md">
            Hubungi WhatsApp Kami
          </a>
          <a href="/harga-maklon-kosmetik.html" class="w-full text-center border border-gray-300 hover:border-primary text-gray-600 hover:text-primary py-4 rounded-xl font-bold transition-all block text-sm">
            Lihat Rincian Estimasi Biaya
          </a>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- TECHNICAL SPECIFICATIONS -->
<section class="py-20 bg-light-bg" id="spesifikasi">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <span class="text-secondary font-bold tracking-wider uppercase text-sm block mb-2">Formulasi & Kandungan</span>
      <h2 class="text-3xl md:text-4xl font-black text-primary">Spesifikasi Teknis & Bahan Aktif Unggulan</h2>
      <p class="text-gray-500 text-lg max-w-2xl mx-auto mt-4">Kami memadukan sains modern dan bahan aktif teruji untuk menciptakan efikasi produk yang optimal.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      {spec_cards}
    </div>
  </div>
</section>

<!-- COMPARISON TABLE -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <span class="text-secondary font-bold tracking-wider uppercase text-sm block mb-2">Paket Maklon</span>
      <h2 class="text-3xl md:text-4xl font-black text-primary">Perbandingan Skema Maklon Kustom</h2>
      <p class="text-gray-500 text-lg max-w-2xl mx-auto mt-4">Pilih paket investasi yang paling sesuai dengan modal dan target pemasaran brand kosmetik Anda.</p>
    </div>

    <div class="overflow-x-auto rounded-3xl border border-gray-200 shadow-sm fade-in">
      <table class="w-full text-left border-collapse bg-white">
        <thead>
          <tr class="bg-primary text-white">
            <th class="p-6 font-bold text-lg">Fitur & Layanan</th>
            <th class="p-6 font-bold text-lg">Paket Basic (MOQ Rendah)</th>
            <th class="p-6 font-bold text-lg">Paket Enterprise (Custom Formula)</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-200 text-gray-700">
          <tr>
            <td class="p-6 font-semibold bg-gray-50 text-primary">Minimum Order Quantity (MOQ)</td>
            <td class="p-6">{moq_basic}</td>
            <td class="p-6">{moq_enterprise}</td>
          </tr>
          <tr>
            <td class="p-6 font-semibold bg-gray-50 text-primary">Riset & Kustomisasi Formula</td>
            <td class="p-6">Formula standar teruji dari database R&D kami (Aman & Stabil)</td>
            <td class="p-6">Formula kustom eksklusif 100% dari nol, uji klaim klinis khusus</td>
          </tr>
          <tr>
            <td class="p-6 font-semibold bg-gray-50 text-primary">Bahan Aktif (Active Ingredients)</td>
            <td class="p-6">Hingga 3 jenis bahan aktif populer (Niacinamide, AHA/BHA, Centella)</td>
            <td class="p-6">Tak terbatas, termasuk bahan aktif premium impor berpaten</td>
          </tr>
          <tr>
            <td class="p-6 font-semibold bg-gray-50 text-primary">Sertifikasi Legalitas Lengkap</td>
            <td class="p-6">Termasuk Notifikasi BPOM, Halal MUI, HAKI Merek (1 Kelas)</td>
            <td class="p-6">Termasuk Notifikasi BPOM, Halal MUI, HAKI Merek, uji lab pihak ketiga</td>
          </tr>
          <tr>
            <td class="p-6 font-semibold bg-gray-50 text-primary">Layanan Desain Kemasan</td>
            <td class="p-6">Desain label & dus standar (Template Premium)</td>
            <td class="p-6">Desain kustom 3D, pemilihan bentuk botol unik, cetak eksklusif</td>
          </tr>
          <tr>
            <td class="p-6 font-semibold bg-gray-50 text-primary">Estimasi Investasi</td>
            <td class="p-6 font-bold text-secondary">{price_basic}</td>
            <td class="p-6 font-bold text-primary">{price_enterprise}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- STEP BY STEP PROCESS -->
<section class="py-20 bg-light-bg">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <span class="text-secondary font-bold tracking-wider uppercase text-sm block mb-2">Alur Kerjasama</span>
      <h2 class="text-3xl md:text-4xl font-black text-primary">Cara Memulai Maklon {product_name}</h2>
      <p class="text-gray-500 text-lg max-w-2xl mx-auto mt-4">Kami menyederhanakan seluruh alur produksi menjadi 4 langkah transparan agar Anda bisa fokus berbisnis.</p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm relative overflow-hidden fade-in">
        <div class="absolute -top-4 -right-4 text-9xl font-black text-gray-100 select-none">1</div>
        <div class="relative z-10">
          <div class="w-12 h-12 bg-secondary/10 text-secondary rounded-2xl flex items-center justify-center mb-6">
            <span class="material-symbols-outlined text-2xl">forum</span>
          </div>
          <h3 class="text-xl font-bold text-primary mb-3">1. Konsultasi Konsep</h3>
          <p class="text-gray-500 text-sm leading-relaxed">Diskusi mengenai jenis {product_name} yang ingin diproduksi, target sasaran harga (HPP), pemilihan bahan aktif unggulan, serta penentuan tren pasar terkini bersama Product Development kami.</p>
        </div>
      </div>

      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm relative overflow-hidden fade-in">
        <div class="absolute -top-4 -right-4 text-9xl font-black text-gray-100 select-none">2</div>
        <div class="relative z-10">
          <div class="w-12 h-12 bg-secondary/10 text-secondary rounded-2xl flex items-center justify-center mb-6">
            <span class="material-symbols-outlined text-2xl">science</span>
          </div>
          <h3 class="text-xl font-bold text-primary mb-3">2. Riset Formula & Sampel</h3>
          <p class="text-gray-500 text-sm leading-relaxed">Apoteker dan tim formulator ahli kami meracik contoh produk (sampel) khusus untuk Anda. Anda mendapatkan hak revisi sampel secara gratis hingga tekstur, warna, dan khasiatnya sesuai keinginan.</p>
        </div>
      </div>

      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm relative overflow-hidden fade-in">
        <div class="absolute -top-4 -right-4 text-9xl font-black text-gray-100 select-none">3</div>
        <div class="relative z-10">
          <div class="w-12 h-12 bg-secondary/10 text-secondary rounded-2xl flex items-center justify-center mb-6">
            <span class="material-symbols-outlined text-2xl">gavel</span>
          </div>
          <h3 class="text-xl font-bold text-primary mb-3">3. Legalitas & Desain</h3>
          <p class="text-gray-500 text-sm leading-relaxed">Kami mengurus semua administrasi perizinan secara resmi: Sertifikat BPOM (NA), Sertifikasi Halal dari BPJPH, serta pendaftaran hak merek dagang (HAKI). Tim desain kami membuat desain kemasan yang estetik.</p>
        </div>
      </div>

      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm relative overflow-hidden fade-in">
        <div class="absolute -top-4 -right-4 text-9xl font-black text-gray-100 select-none">4</div>
        <div class="relative z-10">
          <div class="w-12 h-12 bg-secondary/10 text-secondary rounded-2xl flex items-center justify-center mb-6">
            <span class="material-symbols-outlined text-2xl">precision_manufacturing</span>
          </div>
          <h3 class="text-xl font-bold text-primary mb-3">4. Produksi & Pengiriman</h3>
          <p class="text-gray-500 text-sm leading-relaxed">Produksi massal dilakukan di pabrik kami yang bersertifikasi CPKB Grade A. Melalui uji stabilitas dan QC ketat, produk jadi kemudian dikirim langsung ke alamat gudang Anda di seluruh Indonesia.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- EEAT SECTION: EXPERT FORMULATOR & SAFETY -->
<section class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
      <div class="fade-in">
        <span class="text-secondary font-bold tracking-wider uppercase text-sm block mb-2">Komitmen E-E-A-T (2026)</span>
        <h2 class="text-3xl md:text-4xl font-black text-primary mb-6">Standar Keamanan, Kredibilitas Formulator & Kebijakan Transparan</h2>
        <p class="text-gray-600 leading-relaxed mb-6">
          Setiap formula {product_name} yang diproduksi di Pabrik Kosmetik Tangerang dirancang oleh formulator ahli berpengalaman dan diawasi oleh apoteker senior terdaftar. Kami memastikan efikasi bahan aktif didasarkan pada publikasi jurnal dermatologi klinis terpercaya (seperti <em>Journal of Clinical and Aesthetic Dermatology</em>).
        </p>
        <div class="space-y-4 mb-6">
          <div class="flex gap-4">
            <span class="material-symbols-outlined text-secondary shrink-0">clinical_notes</span>
            <p class="text-sm text-gray-500"><strong class="text-primary">Studi Klinis Teruji:</strong> Formulasi menggunakan persentase aktif yang stabil untuk meminimalisasi iritasi kulit (misal: uji stabilitas suhu dipercepat 40°C selama 3 bulan).</p>
          </div>
          <div class="flex gap-4">
            <span class="material-symbols-outlined text-secondary shrink-0">verified</span>
            <p class="text-sm text-gray-500"><strong class="text-primary">Formula 100% Milik Anda:</strong> Begitu maklon selesai, hak kepemilikan formula sepenuhnya diberikan kepada Anda, dilindungi perjanjian kerahasiaan tertulis (NDA).</p>
          </div>
          <div class="flex gap-4">
            <span class="material-symbols-outlined text-secondary shrink-0">shield_with_heart</span>
            <p class="text-sm text-gray-500"><strong class="text-primary">Garansi Kualitas & Retur:</strong> Jika terjadi ketidaksesuaian produksi massal dengan sampel yang disepakati, kami menjamin pengerjaan ulang (re-proses) tanpa biaya tambahan.</p>
          </div>
        </div>
      </div>

      <div class="bg-light-bg p-8 rounded-3xl border border-gray-200/50 fade-in">
        <h3 class="text-xl font-bold text-primary mb-6">Tim Ahli R&D & Formulasi Kami</h3>
        <div class="space-y-6">
          <div class="flex items-center gap-4 p-4 bg-white rounded-2xl border border-gray-100">
            <div class="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center shrink-0">
              <span class="material-symbols-outlined text-3xl text-primary">dermatology</span>
            </div>
            <div>
              <h4 class="font-bold text-primary text-base">Dr. dr. Sarah Wijaya, Sp.KK</h4>
              <p class="text-xs text-secondary font-semibold uppercase mb-1">Dermatologist & R&D Advisor</p>
              <p class="text-xs text-gray-500">Konsultan senior spesialis kulit dan kelamin, memastikan formulasi aman untuk kulit sensitif dan efikasi terbukti klinis.</p>
            </div>
          </div>

          <div class="flex items-center gap-4 p-4 bg-white rounded-2xl border border-gray-100">
            <div class="w-16 h-16 rounded-full bg-primary/10 flex items-center justify-center shrink-0">
              <span class="material-symbols-outlined text-3xl text-primary">medical_services</span>
            </div>
            <div>
              <h4 class="font-bold text-primary text-base">Apt. Dinda Lestari, S.Farm</h4>
              <p class="text-xs text-secondary font-semibold uppercase mb-1">Lead Pharmacist & Formulator</p>
              <p class="text-xs text-gray-500">Apoteker Penanggung Jawab Teknis dengan STR-A aktif, mengawasi standar CPKB Grade A dan kepatuhan regulasi BPOM.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- KNOWLEDGE GRAPH & ENTITIES (TOPICAL CONTEXT) -->
<section class="py-16 bg-light-bg border-t border-gray-100">
  <div class="max-w-5xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
      <h3 class="text-xl font-black text-primary mb-4">Informasi Kepatuhan & Entitas Resmi (Knowledge Graph)</h3>
      <p class="text-sm text-gray-600 leading-relaxed mb-6">
        Proses produksi di Pabrik Kosmetik Tangerang sepenuhnya mengikuti ketentuan regulasi nasional dan internasional. Kami menautkan entitas resmi berikut untuk memastikan jaminan kepatuhan hukum:
      </p>
      <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 text-xs text-gray-500">
        <div class="p-4 bg-light-bg rounded-xl border border-gray-200/20">
          <strong class="text-primary block mb-1">Badan Pengawas Obat dan Makanan (BPOM)</strong>
          Lembaga resmi pengawas peredaran kosmetik di Indonesia. Setiap produk maklon wajib memiliki izin Notifikasi Kosmetika (Nomor NA) sebelum dipasarkan.
        </div>
        <div class="p-4 bg-light-bg rounded-xl border border-gray-200/20">
          <strong class="text-primary block mb-1">Majelis Ulama Indonesia & BPJPH</strong>
          Sertifikasi Halal MUI untuk kosmetik menjamin bahwa bahan baku dan alur produksi bebas dari unsur najis dan zat haram.
        </div>
        <div class="p-4 bg-light-bg rounded-xl border border-gray-200/20">
          <strong class="text-primary block mb-1">Cara Pembuatan Kosmetika yang Baik (CPKB)</strong>
          Fasilitas produksi kami bersertifikat CPKB Grade A dari Badan POM, yang merupakan standar tertinggi industri kosmetik nasional (setara ASEAN Cosmetic Directive).
        </div>
        <div class="p-4 bg-light-bg rounded-xl border border-gray-200/20">
          <strong class="text-primary block mb-1">HAKI & Merek Dagang</strong>
          Perlindungan hukum nama brand kosmetik Anda di bawah Direktorat Jenderal Kekayaan Intelektual (DJKI) Kemenkumham RI.
        </div>
      </div>
    </div>
  </div>
</section>

<!-- FAQ SECTION -->
<section class="py-20 bg-white">
  <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <span class="text-secondary font-bold tracking-wider uppercase text-sm block mb-2">FAQ</span>
      <h2 class="text-3xl font-black text-primary">Pertanyaan Umum Seputar Maklon {product_name}</h2>
    </div>

    <div class="space-y-4 fade-in">
      {faq_items}
    </div>
  </div>
</section>

<!-- CALL TO ACTION (CTA) -->
<section class="py-20 bg-secondary text-center">
  <div class="max-w-4xl mx-auto px-4 fade-in">
    <h2 class="text-3xl md:text-5xl font-black text-primary leading-tight mb-6">Konsultasikan Ide Produk {product_name} Anda Sekarang!</h2>
    <p class="text-primary/80 text-lg md:text-xl mb-10 max-w-2xl mx-auto">
      Dapatkan sampel formula kustom gratis dan hitung estimasi HPP produk Anda bersama R&D Pabrik Kosmetik Tangerang.
    </p>
    <a href="https://wa.me/6283863670421" class="inline-flex items-center gap-3 bg-primary text-white hover:bg-primary-light px-10 py-5 rounded-full font-black text-xl hover:scale-105 transition-all shadow-xl shadow-primary/30">
      <span class="material-symbols-outlined text-2xl">chat</span> Hubungi Formulator Kami via WhatsApp
    </a>
  </div>
</section>

<!-- FOOTER PLACEHOLDER (Will be injected by inject_layout.py) -->
<footer class="bg-gray-900 pt-16 pb-8 border-t border-white/10 mt-12"></footer>

<a href="https://wa.me/6283863670421" target="_blank" class="fixed bottom-6 right-6 z-50 w-14 h-14 bg-cta rounded-full flex items-center justify-center shadow-lg hover:scale-110 transition-transform">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="white" class="w-7 h-7"><path d="M16 0C7.163 0 0 7.163 0 16c0 2.822.736 5.469 2.027 7.769L0 32l8.469-2.015A15.93 15.93 0 0016 32c8.837 0 16-7.163 16-16S24.837 0 16 0zm0 29.333a13.27 13.27 0 01-6.771-1.853l-.485-.289-5.025 1.196 1.217-4.892-.317-.502A13.267 13.267 0 012.667 16C2.667 8.636 8.636 2.667 16 2.667S29.333 8.636 29.333 16 23.364 29.333 16 29.333zm7.27-9.87c-.398-.199-2.355-1.162-2.72-1.294-.365-.133-.631-.199-.897.199-.265.398-1.029 1.294-1.261 1.56-.232.265-.465.298-.863.1-.398-.199-1.682-.62-3.204-1.977-1.184-1.056-1.983-2.36-2.215-2.758-.232-.398-.025-.613.175-.811.179-.178.398-.465.597-.697.199-.232.265-.398.398-.664.133-.265.066-.497-.033-.697-.1-.199-.897-2.162-1.229-2.96-.324-.776-.652-.671-.897-.683l-.764-.013c-.265 0-.697.1-1.062.497-.365.398-1.394 1.362-1.394 3.32 0 1.959 1.427 3.851 1.626 4.117.199.265 2.809 4.29 6.808 6.016.951.41 1.693.655 2.272.839.954.304 1.822.261 2.509.158.765-.114 2.355-.963 2.688-1.893.332-.93.332-1.727.232-1.893-.1-.166-.365-.265-.763-.464z"/></svg>
</a>

<script>
const obs = new IntersectionObserver(entries => {{
  entries.forEach(entry => {{
    if (entry.isIntersecting) {{
      entry.target.classList.add('visible');
    }}
  }});
}}, {{ threshold: 0.1 }});
document.querySelectorAll('.fade-in').forEach(el => obs.observe(el));
</script>
</body>
</html>
"""

# Pages Configuration Data
pages_data = [
    {
        "filename": "maklon-serum-wajah.html",
        "category": "Skincare",
        "product_name": "Serum Wajah",
        "meta_title": "Jasa Maklon Serum Wajah Tangerang | Formula Custom Teruji BPOM",
        "meta_desc": "Ingin punya brand serum wajah sendiri? Jasa maklon serum wajah Tangerang bersertifikat CPKB Grade A. Formula custom anti-aging, acne, brightening. MOQ 500 pcs.",
        "hero_desc": "Ciptakan lini serum wajah eksklusif Anda sendiri. Mulai dari serum pencerah, anti-aging, hingga formulasi jerawat teruji klinis dengan MOQ rendah mulai dari 500 pcs dan pengurusan legalitas BPOM & Halal lengkap.",
        "aeo_paragraph": "Jasa Maklon Serum Wajah di Pabrik Kosmetik Tangerang adalah layanan pembuatan produk serum wajah kustom dengan MOQ rendah mulai dari 500 pcs. Fasilitas kami bersertifikasi CPKB Grade A, mencakup riset formula gratis oleh apoteker ahli, pengurusan izin edar BPOM, sertifikasi Halal, serta desain kemasan produk gratis.",
        "main_content": """
<h2>Mengapa Memilih Jasa Maklon Serum Wajah di Pabrik Kosmetik Tangerang?</h2>
<p>Serum wajah telah menjadi salah satu produk kecantikan dengan tingkat permintaan tertinggi di pasar kosmetik Indonesia. Karena konsentrasi bahan aktifnya yang tinggi dan kemampuannya meresap cepat ke lapisan epidermis, serum dinilai sangat efektif untuk mengatasi berbagai masalah kulit seperti penuaan dini, jerawat, kulit kusam, dan kerusakan skin barrier. Keberhasilan memasarkan produk serum sangat ditentukan oleh kualitas formulasi dan stabilitas bahan aktif yang digunakan.</p>
<p>Bersama kami, Anda bisa menciptakan formula serum premium dengan keunikan tersendiri. Kami menggunakan bahan-bahan aktif bersertifikat yang diimpor dari produsen terkemuka di berbagai belahan dunia (Jepang, Korea, Prancis). Tim formulator kami menguji stabilitas formula pada kondisi suhu ekstrem guna memastikan efektivitas serum tetap terjaga hingga ke tangan konsumen akhir.</p>
<p>Sebagai pabrik maklon bersertifikasi CPKB Grade A di Tangerang, kami menjamin seluruh alur produksi memenuhi standar kebersihan tertinggi. Kami menyadari bahwa produk kosmetik, khususnya yang diaplikasikan langsung pada kulit wajah sensitif, membutuhkan ketelitian tanpa celah dalam hal mikrobiologi dan uji kontaminasi logam berat.</p>

<h2>Jenis-Jenis Formulasi Serum Wajah yang Kami Sediakan</h2>
<p>Kami melayani pembuatan berbagai macam kategori serum wajah yang disesuaikan dengan target pasar brand Anda:</p>
<ul>
  <li><strong>Brightening & Glowing Serum:</strong> Serum pencerah kulit dengan kandungan aktif seperti Niacinamide, Alpha Arbutin, Vitamin C (Ethyl Ascorbic Acid), Tranexamic Acid, dan Licorice Extract yang efektif memudarkan noda hitam.</li>
  <li><strong>Anti-Aging & Firming Serum:</strong> Diformulasikan dengan Retinol (Encapsulated Retinol untuk mengurangi risiko iritasi), Bakuchiol, Collagen, dan berbagai jenis Peptide guna menyamarkan garis halus serta meningkatkan kekenyalan kulit.</li>
  <li><strong>Acne & Pores Clarifying Serum:</strong> Serum khusus kulit berjerawat dan pori-pori besar yang menggunakan bahan seperti Salicylic Acid (BHA), Tea Tree Oil, Centella Asiatica Extract, Mugwort, dan Zinc PCA untuk meredakan kemerahan serta mengontrol sebum berlebih.</li>
  <li><strong>Skin Barrier Hydrating Serum:</strong> Serum pelembap mendalam dengan kombinasi Multi-Ceramide (Ceramide NP, AP, EOP), Hyaluronic Acid (berbagai ukuran molekul), Panthenol (Provitamin B5), dan Aloe Vera untuk memperkuat perlindungan alami kulit.</li>
  <li><strong>Exfoliating Serum (AHA BHA PHA):</strong> Serum eksfoliasi lembut mingguan dengan Glycolic Acid, Lactic Acid, Salicylic Acid, dan Gluconolactone untuk mengangkat sel kulit mati secara optimal tanpa memicu kekeringan atau iritasi parah.</li>
</ul>

<h2>Keunggulan Kompetitif & Bahan Baku Premium</h2>
<p>Kami memastikan bahwa formula serum Anda tidak sekadar mengikuti tren, melainkan memiliki performa efikasi nyata yang didukung oleh literasi dermatologi. Melalui maklon kustom (ODM), Anda dapat menggabungkan bahan aktif lokal asli Indonesia (seperti ekstrak tanaman herbal berkhasiat) dengan bioteknologi modern.</p>
<p>Kami juga menawarkan inovasi tekstur yang beragam mulai dari serum cair ringan water-based, serum gel kental yang menghidrasi, serum minyak wajah (face oil) yang menutrisi, hingga teknologi serum bersuspensi mikro (micro-droplet serum) yang memberikan visual mewah pada kemasan transparan.</p>

<h2>Uji Keamanan & Pengurusan Legalitas Terintegrasi</h2>
<p>Salah satu hambatan terbesar bagi brand owner pemula adalah proses birokrasi legalitas yang rumit. Di Pabrik Kosmetik Tangerang, kami menyediakan layanan terintegrasi <em>One-Stop Solution</em>. Semua berkas persyaratan administratif hingga pendaftaran sampel ke sistem e-BPOM akan diurus secara penuh oleh tim regulasi kami.</p>
<p>Setiap produk kosmetik yang kami produksi dijamin mendapatkan nomor notifikasi BPOM resmi yang dicetak pada kemasan produk, sertifikat Halal dari BPJPH Indonesia, serta pendaftaran merek dagang HAKI guna mengamankan kekayaan intelektual bisnis Anda secara hukum.</p>
        """,
        "spec_cards": """
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">science</span>
        <h3 class="text-xl font-bold text-primary mb-3">Niacinamide (Vitamin B3)</h3>
        <p class="text-gray-500 text-sm">Konsentrasi stabil 2%–10% untuk meminimalkan iritasi kulit. Berfungsi mencerahkan, menyamarkan noda hitam, dan memperkuat skin barrier.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">hourglass_empty</span>
        <h3 class="text-xl font-bold text-primary mb-3">Encapsulated Retinol</h3>
        <p class="text-gray-500 text-sm">Teknologi enkapsulasi untuk pelepasan retinol secara perlahan ke kulit. Mengurangi tanda penuaan dini dengan risiko iritasi minimal.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">spa</span>
        <h3 class="text-xl font-bold text-primary mb-3">Centella Asiatica (Cica)</h3>
        <p class="text-gray-500 text-sm">Bahan alami penenang kulit sensitif. Membantu meredakan kemerahan, menyembuhkan jerawat, serta merangsang kolagen.</p>
      </div>
        """,
        "faq_items": """
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa biaya pembuatan sampel formula serum?</h4>
        <p class="text-gray-600">Riset formula dan pembuatan sampel serum wajah di Pabrik Kosmetik Tangerang adalah gratis untuk calon mitra maklon. Kami memberikan kesempatan revisi hingga formula disepakati.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa MOQ (Minimum Order Quantity) untuk maklon serum?</h4>
        <p class="text-gray-600">MOQ untuk produk serum wajah adalah 500 pcs per varian untuk Paket Basic, dan 1.000+ pcs untuk formula kustom eksklusif (Paket Enterprise).</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa lama izin BPOM serum diterbitkan?</h4>
        <p class="text-gray-600">Proses pendaftaran hingga terbitnya nomor Notifikasi BPOM (NA) kosmetik biasanya berkisar antara 1 hingga 2 bulan, bergantung pada antrean di BPOM RI.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah formula serum dari pabrik dijamin eksklusif?</h4>
        <p class="text-gray-600">Ya, untuk pendaftaran maklon sistem ODM (Enterprise), kami menjamin 100% eksklusivitas formula Anda. Formula tersebut tidak akan digunakan untuk brand lain dan terikat kontrak NDA.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah saya bisa menggunakan kemasan serum sendiri?</h4>
        <p class="text-gray-600">Tentu saja. Anda bisa melakukan sourcing kemasan botol serum sendiri, atau menyerahkan sourcing kemasan sepenuhnya kepada tim kami demi efisiensi dan jaminan sterilitas.</p>
      </div>
        """,
        "schema_json": ""
    },
    {
        "filename": "maklon-sunscreen.html",
        "category": "Skincare",
        "product_name": "Sunscreen",
        "meta_title": "Jasa Maklon Sunscreen SPF 30-50+ | Formula Ringan Tanpa Whitecast",
        "meta_desc": "Mulai brand sunscreen Anda! Jasa maklon sunscreen Tangerang bersertifikat CPKB Grade A. Formula mineral, chemical, hybrid SPF 30-50+ PA++++. MOQ 500 pcs.",
        "hero_desc": "Kembangkan produk pelindung surya premium yang disukai pasar tropis. Kami memformulasikan sunscreen SPF tinggi, tekstur ringan cepat meresap, non-comedogenic, dan tanpa efek whitecast.",
        "aeo_paragraph": "Jasa Maklon Sunscreen di Pabrik Kosmetik Tangerang melayani pembuatan tabir surya kustom (mineral, chemical, hybrid) SPF 30 hingga 50+ PA++++. Layanan kami mencakup riset formula gratis, pengujian nilai SPF in-vitro/in-vivo, pengurusan notifikasi BPOM & Halal, dengan MOQ rendah mulai dari 500 pcs.",
        "main_content": """
<h2>Peluang Pasar Maklon Sunscreen SPF Tinggi di Indonesia</h2>
<p>Sebagai negara tropis yang disinari matahari sepanjang tahun, kesadaran masyarakat Indonesia akan pentingnya menggunakan tabir surya atau sunscreen meningkat sangat pesat. Sunscreen bukan lagi sekadar produk pelengkap, melainkan kebutuhan dasar harian yang wajib digunakan untuk mencegah penuaan dini (photoaging), bintik hitam, dan risiko kanker kulit. Permintaan produk tabir surya di e-commerce selalu menduduki jajaran produk terlaris.</p>
<p>Namun, merancang formulasi sunscreen bukanlah hal mudah. Banyak keluhan konsumen mengenai sunscreen yang lengket, menimbulkan komedo (acne-prone), memicu whitecast (efek abu-abu pada wajah), atau perih di mata. Di Pabrik Kosmetik Tangerang, tim R&D kami secara khusus memecahkan masalah ini dengan merancang formula sunscreen bersensorik tinggi yang nyaman digunakan di bawah terik matahari tropis.</p>
<p>Kami memfasilitasi pembuatan formula tabir surya dengan berbagai tingkat proteksi, mulai dari SPF 30 untuk penggunaan dalam ruangan, hingga SPF 50+ PA++++ untuk perlindungan maksimal aktivitas luar ruangan. Seluruh formulasi diuji nilainya secara akurat guna menjamin klaim SPF yang dicantumkan pada kemasan benar-benar terbukti secara ilmiah.</p>

<h2>Pilihan Formulasi Sunscreen yang Dapat Anda Maklon</h2>
<p>Kami menyediakan tiga jenis teknologi proteksi sinar UV yang dapat disesuaikan dengan konsep brand kosmetik Anda:</p>
<ul>
  <li><strong>Physical / Mineral Sunscreen:</strong> Menggunakan bahan aktif pemantul sinar UV seperti Titanium Dioxide dan Zinc Oxide. Sangat aman untuk kulit sensitif, anak-anak, serta ibu hamil karena tidak menyerap ke dalam pembuluh darah. Kami memformulasikannya dengan teknologi mikronisasi untuk menekan efek whitecast seminimal mungkin.</li>
  <li><strong>Chemical Sunscreen:</strong> Memanfaatkan filter UV organik yang menyerap sinar matahari dan mengubahnya menjadi energi panas. Sunscreen jenis ini memiliki kelebihan tekstur yang sangat transparan (zero whitecast), ringan seperti air, dan sangat mudah dibaurkan ke kulit.</li>
  <li><strong>Hybrid Sunscreen:</strong> Menggabungkan kelebihan physical dan chemical filter dalam satu formula. Memberikan perlindungan ganda yang sangat kuat namun tetap mempertahankan kenyamanan tekstur yang ringan dan minim risiko iritasi. Ini adalah tipe sunscreen paling populer di pasar lokal saat ini.</li>
</ul>

<h2>Inovasi Tekstur Sunscreen untuk Target Pasar Anda</h2>
<p>Agar brand Anda tampil menonjol di pasar yang kompetitif, kami menawarkan berbagai variasi bentuk sediaan tabir surya modern:</p>
<p>1. <strong>Sunscreen Gel & Watery Essence:</strong> Tekstur berbasis air yang langsung mencair saat menyentuh kulit, memberikan sensasi dingin yang menyegarkan, cocok untuk tipe kulit berminyak dan berjerawat.</p>
<p>2. <strong>Sunscreen Cream & Lotion:</strong> Memberikan hidrasi ekstra bagi pemilik kulit kering. Sering kali dikombinasikan dengan bahan pelembap seperti Hyaluronic Acid atau Ceramide.</p>
<p>3. <strong>Sunscreen Spray & Mist:</strong> Format praktis untuk re-apply sunscreen di luar ruangan tanpa merusak riasan wajah. Memiliki formula yang cepat mengering dan tidak lengket.</p>
<p>4. <strong>Tinted Sunscreen:</strong> Tabir surya yang dilengkapi dengan sedikit pigmen warna kulit (foundation ringan) untuk meratakan warna wajah sekaligus melindungi kulit secara optimal.</p>

<h2>Standar Kualitas & Uji SPF Terpercaya</h2>
<p>Setiap produk sunscreen yang diproduksi di pabrik kami wajib melewati pengujian nilai proteksi UV. Kami bekerja sama dengan laboratorium pengujian independen terakreditasi untuk melakukan uji SPF In-Vitro (menggunakan spektrofotometer) maupun In-Vivo (uji langsung pada sukarelawan) untuk menjamin kebenaran klaim proteksi sebelum produk didaftarkan ke BPOM RI.</p>
<p>Fasilitas manufaktur kami yang steril menjamin tidak ada kontaminasi mikroba pada produk tabir surya Anda. Dengan bermitra bersama kami, Anda memegang hak formula eksklusif sepenuhnya untuk memajukan bisnis kecantikan Anda ke tingkat global.</p>
        """,
        "spec_cards": """
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">wb_sunny</span>
        <h3 class="text-xl font-bold text-primary mb-3">Titanium Dioxide & Zinc Oxide</h3>
        <p class="text-gray-500 text-sm">Mineral filter pelindung fisik bersertifikat. Menghalangi radiasi UVA & UVB seketika setelah diaplikasikan tanpa menyerap ke kulit.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">water</span>
        <h3 class="text-xl font-bold text-primary mb-3">Hyaluronic Acid & Ceramide</h3>
        <p class="text-gray-500 text-sm">Bahan tambahan penunjang hidrasi kulit. Mencegah kekeringan akibat paparan sinar matahari dan menjaga keutuhan skin barrier.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">verified_user</span>
        <h3 class="text-xl font-bold text-primary mb-3">Non-Comedogenic Filters</h3>
        <p class="text-gray-500 text-sm">Filter UV kimiawi generasi terbaru yang stabil terhadap cahaya (photostable) dan tidak menyumbat pori-pori wajah.</p>
      </div>
        """,
        "faq_items": """
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa biaya uji SPF untuk maklon sunscreen?</h4>
        <p class="text-gray-600">Uji SPF standar In-Vitro termasuk dalam biaya riset awal formula kami. Namun, untuk uji klinis SPF In-Vivo resmi (pihak ketiga), biayanya akan disesuaikan dengan tarif laboratorium independen mitra kami.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa MOQ maklon sunscreen wajah?</h4>
        <p class="text-gray-600">MOQ sunscreen wajah adalah 500 pcs untuk kemasan standar dari stok katalog kami, dan minimal 1.000 pcs jika Anda menginginkan kemasan botol/tube khusus kustom.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah sunscreen yang dibuat di pabrik aman untuk terumbu karang (reef-safe)?</h4>
        <p class="text-gray-600">Ya, kami dapat merancang formulasi tabir surya ramah lingkungan (reef-safe sunscreen) dengan menghindari penggunaan bahan kimia berbahaya seperti Oxybenzone dan Octinoxate.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah saya bisa membuat sunscreen berbentuk stik (sunscreen stick)?</h4>
        <p class="text-gray-600">Tentu saja. Kami memiliki jalur produksi khusus untuk sediaan kosmetik padat/semi-padat seperti sunscreen stick, balm, dan cushion sunscreen.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Bagaimana klaim perlindungan air (waterproof/water-resistant) didaftarkan?</h4>
        <p class="text-gray-600">Klaim ketahanan air memerlukan uji klinis ketahanan tambahan. Formula sunscreen akan dirancang menggunakan agen pembentuk lapisan tipis (film former) khusus agar tidak luntur saat berkeringat.</p>
      </div>
        """,
        "schema_json": ""
    },
    {
        "filename": "maklon-facial-wash.html",
        "category": "Skincare",
        "product_name": "Facial Wash",
        "meta_title": "Jasa Maklon Facial Wash Tangerang | Sabun Wajah Kustom pH Balanced",
        "meta_desc": "Bikin brand sabun cuci muka sendiri. Jasa maklon facial wash & cleanser di Tangerang. Formula pH balanced lembut, non-SLS, BPOM, Halal MUI. MOQ 500 pcs.",
        "hero_desc": "Produksi sabun pembersih wajah berkualitas premium dengan formulasi pH seimbang (pH-balanced) yang membersihkan kotoran secara mendalam tanpa merusak kelembapan alami kulit wajah.",
        "aeo_paragraph": "Jasa Maklon Facial Wash di Pabrik Kosmetik Tangerang menawarkan produksi sabun wajah kustom (foam, gel, scrub, non-SLS) dengan formula pH balanced yang lembut. Sudah mencakup riset formula gratis, sertifikasi BPOM, Halal MUI, dan kemasan estetik dengan MOQ mulai 500 pcs.",
        "main_content": """
<h2>Mengapa Formulasi Facial Wash yang Tepat Sangat Penting bagi Konsumen?</h2>
<p>Langkah terpenting dalam rutinitas perawatan wajah adalah pembersihan (cleansing). Sabun cuci muka atau facial wash adalah produk kosmetik yang paling sering dibeli karena habis digunakan setiap hari. Konsumen saat ini semakin cerdas dalam memilih pembersih wajah; mereka cenderung menghindari sabun wajah tradisional yang menghasilkan busa melimpah namun membuat kulit terasa kering, ketarik, dan merusak lapisan pelindung alami kulit (skin barrier).</p>
<p>Di Pabrik Kosmetik Tangerang, kami memformulasikan facial wash modern dengan standar keasaman kulit alami manusia (pH Balanced berkisar antara 5.0 hingga 5.5). Pembersih wajah yang terlalu basa (seperti sabun berbahan dasar sabun kalium/natrium konvensional) dapat mengganggu pH alami kulit, memicu perkembangbiakan bakteri penyebab jerawat, dan memperparah kulit sensitif.</p>
<p>Kami menggunakan surfaktan alternatif yang sangat lembut (mild surfactants) seperti Sodium Cocoyl Glutamate, Cocamidopropyl Betaine, atau Lauryl Glucoside yang berasal dari minyak kelapa alami. Surfaktan bebas SLS (Sodium Lauryl Sulfate) ini membersihkan kulit secara efektif tanpa melarutkan lipid esensial kulit wajah.</p>

<h2>Pilihan Jenis Pembersih Wajah (Cleanser) untuk Lini Produk Anda</h2>
<p>Kami memfasilitasi pembuatan berbagai jenis sediaan pembersih wajah kustom sesuai preferensi target pasar Anda:</p>
<ul>
  <li><strong>Gentle Facial Wash Gel:</strong> Sediaan berbentuk gel bening bebas sabun keras (soap-free), minim busa, dan diperkaya dengan bahan penenang kulit seperti Panthenol, Chamomile Extract, atau Calendula.</li>
  <li><strong>Acne Cleansing Foam (Salicylic Acid):</strong> Sabun muka khusus berjerawat dengan tambahan BHA mikro-eksfoliasi yang mampu meresap ke dalam pori-pori untuk melarutkan minyak berlebih dan sel kulit mati penyebab komedo.</li>
  <li><strong>Brightening Facial Foam:</strong> Menghasilkan busa krim lembut melimpah untuk membersihkan kotoran mikro secara mendalam, dipadukan dengan Niacinamide atau Vitamin C untuk mencerahkan wajah kusam.</li>
  <li><strong>Exfoliating Facial Wash (with Scrub / Beads):</strong> Dilengkapi dengan butiran eksfoliasi halus alami (seperti jojoba esters atau bubuk aprikot) untuk mengangkat kotoran menyumbat tanpa melukai kulit wajah.</li>
  <li><strong>Cleansing Balm & Oil Cleanser:</strong> Sediaan pembersih berbasis minyak untuk metode _double cleansing_ yang efektif meluruhkan riasan tahan air (waterproof makeup) dan tabir surya sisa seharian.</li>
</ul>

<h2>Teknologi CPKB Grade A & Higienitas Produksi</h2>
<p>Pembersih wajah mengandung kadar air yang cukup tinggi, sehingga sangat rentan terhadap kontaminasi bakteri Pseudomonas aeruginosa apabila diproduksi di lingkungan yang kurang bersih. Pabrik Kosmetik Tangerang memiliki ruang produksi steril yang didukung oleh sistem tata udara HEPA filter untuk mengendalikan partikel debu dan mikroba secara presisi.</p>
<p>Apoteker pengendali mutu (Quality Control) kami melakukan pengujian organoleptis, stabilitas pH, viskositas, dan uji mikrobiologi cermat pada setiap bets produksi sebelum produk dikemas ke dalam kemasan botol atau tube siap edar.</p>

<h2>One-Stop Solution: Dari Sampel Hingga Izin Edar BPOM</h2>
<p>Mendirikan brand kosmetik sendiri bersama kami sangatlah mudah. Kami mendampingi Anda melewati seluruh tahap perancangan produk: mulai dari penentuan nama merek, pembuatan sampel formula gratis, pemilihan botol pump atau tube estetik, hingga pendaftaran izin edar BPOM dan logo Halal MUI. Layanan kami berfokus pada kecepatan layanan tanpa mengorbankan kualitas dan legalitas hukum.</p>
        """,
        "spec_cards": """
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">soap</span>
        <h3 class="text-xl font-bold text-primary mb-3">SLS/SLES Free Surfactants</h3>
        <p class="text-gray-500 text-sm">Menggunakan surfaktan turunan asam amino alami yang sangat lembut. Membersihkan kotoran secara maksimal tanpa memicu iritasi mata atau kulit kering.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">percent</span>
        <h3 class="text-xl font-bold text-primary mb-3">pH Balanced (5.0 - 5.5)</h3>
        <p class="text-gray-500 text-sm">Formula khusus yang disesuaikan dengan tingkat keasaman kulit alami. Menjaga kelembapan epidermis dan melindungi barrier asam kulit.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">local_pharmacy</span>
        <h3 class="text-xl font-bold text-primary mb-3">Salicylic Acid & Zinc PCA</h3>
        <p class="text-gray-500 text-sm">Bahan aktif untuk mengatasi jerawat dan minyak. Membantu membersihkan pori-pori tersumbat serta mengontrol kelenjar sebum.</p>
      </div>
        """,
        "faq_items": """
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa MOQ untuk maklon sabun cuci muka?</h4>
        <p class="text-gray-600">MOQ untuk pembuatan produk facial wash di pabrik kami dimulai dari 500 pcs per varian untuk Paket Basic. Cocok bagi pemula yang ingin meminimalkan risiko modal.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah saya bisa meminta formula dengan klaim busa sedikit?</h4>
        <p class="text-gray-600">Tentu saja. Tren sabun wajah lembut minim busa (gentle low-pH cleanser) sangat diminati saat ini. Tim formulator kami dapat merancang formula sabun gel non-soap yang sangat lembut.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa biaya pengurusan BPOM dan Halal untuk facial wash?</h4>
        <p class="text-gray-600">Biaya pengurusan Notifikasi BPOM, sertifikasi Halal, dan HAKI sudah termasuk dalam paket maklon terintegrasi yang kami tawarkan. Silakan hubungi tim sales kami untuk rincian biayanya.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah pabrik menyediakan opsi kemasan botol pump dan tube foaming?</h4>
        <p class="text-gray-600">Ya, kami menyediakan beragam pilihan kemasan botol pump, kemasan tube plastik laminasi (matte/glossy), botol foaming pump (yang otomatis menghasilkan busa), dan tube dengan aplikator silikon brush.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah formula sabun wajah bisa menggunakan wewangian alami?</h4>
        <p class="text-gray-600">Ya, kami dapat menambahkan minyak atsiri alami (essential oil) seperti Lavender atau Rose Water sebagai pemberi aroma alami untuk menghindari penggunaan parfum sintetik sensitif.</p>
      </div>
        """,
        "schema_json": ""
    },
    {
        "filename": "maklon-body-lotion.html",
        "category": "Body Care",
        "product_name": "Body Lotion",
        "meta_title": "Jasa Maklon Body Lotion Tangerang | Formula Wangi Mewah Tahan Lama",
        "meta_desc": "Jasa maklon body lotion Tangerang bersertifikat CPKB Grade A. Formula tone-up pencerah, wangi parfum mewah tahan lama, BPOM, Halal MUI. MOQ 500 pcs.",
        "hero_desc": "Miliki brand body lotion kustom Anda sendiri. Dapatkan formula lotion pelembap eksklusif yang cepat meresap tanpa rasa lengket, dilengkapi aroma parfum mewah yang tahan seharian.",
        "aeo_paragraph": "Jasa Maklon Body Lotion di Pabrik Kosmetik Tangerang memproduksi losion tubuh kustom (tone-up pencerah, wewangian parfum mewah, pelembap mendalam) dengan MOQ mulai 500 pcs. Fasilitas CPKB Grade A kami menjamin keamanan formula, pengurusan BPOM, sertifikasi Halal, dan HAKI merek lengkap.",
        "main_content": """
<h2>Peluang Bisnis Maklon Body Lotion Wangi Parfum Mewah</h2>
<p>Kategori produk perawatan tubuh (body care) terus mengalami lonjakan permintaan yang pesat di Indonesia. Salah satu produk wajib harian yang dikonsumsi masyarakat luas adalah body lotion. Selain fungsi utamanya untuk menjaga kelembapan kulit dari AC dan cuaca panas, tren body lotion saat ini telah bergeser ke arah fungsionalitas ganda: mencerahkan kulit secara instan (tone-up effect) dan memiliki aroma mewah seperti parfum kelas dunia (perfumed body lotion).</p>
<p>Di Pabrik Kosmetik Tangerang, kami memahami perilaku pasar yang menyukai losion tubuh dengan daya serap cepat tanpa menyisakan rasa lengket atau licin saat terkena air. Tim R&D kami memformulasikan losion dengan struktur emulsi minyak dalam air (oil-in-water) yang sangat stabil, menyebarkan kelembapan secara merata dan meninggalkan lapisan perlindungan halus di permukaan kulit.</p>
<p>Kami memiliki akses ke ratusan varian fragrance premium bersertifikat IFRA (International Fragrance Association) yang terbukti aman bagi kulit sensitif namun memiliki ketahanan aroma (long-lastingness) yang setara dengan Eau de Parfum.</p>

<h2>Varian Formulasi Body Lotion yang Kami Tawarkan</h2>
<p>Anda dapat memilih dan memodifikasi formulasi losion tubuh sesuai konsep brand unik Anda:</p>
<ul>
  <li><strong>Brightening & Tone-Up Lotion:</strong> Losion pencerah instan yang merata tanpa menyumbat pori-pori. Menggabungkan Titanium Dioxide (UV filter fisik), Niacinamide, dan Glutathione untuk mencerahkan warna kulit secara bertahap dan instan tanpa efek dempul abu-abu.</li>
  <li><strong>Deep Moisture Body Butter / Cream:</strong> Sediaan losion pekat bertekstur mentega yang kaya akan minyak nabati alami seperti Shea Butter, Cocoa Butter, Jojoba Oil, dan Olive Oil untuk merehabilitasi kulit yang sangat kering, bersisik, atau pecah-pecah.</li>
  <li><strong>AHA BHA Exfoliating Body Lotion:</strong> Losion tubuh penangkal kulit kasar ("kulit ayam" atau keratosis pilaris) dengan kandungan asam eksfoliasi lembut yang meluruhkan sel kulit mati di area lipatan tubuh.</li>
  <li><strong>Soothing & Cooling Gel Lotion:</strong> Formula losion berbasis gel ringan dengan sensasi dingin (cooling sensation) dari ekstrak Aloe Vera atau mentol, sangat nyaman digunakan setelah berjemur atau beraktivitas luar ruangan.</li>
</ul>

<h2>Fasilitas Produksi CPKB Grade A & Jaminan Mutu</h2>
<p>Sebagai produsen maklon kosmetik berpengalaman di Tangerang, kami memproduksi losion tubuh menggunakan mesin pengemulsi vakum berkecepatan tinggi (vacuum homogenizer emulsifier). Proses ini memastikan fase minyak dan air menyatu secara homogen sempurna pada tingkat mikro, sehingga losion tidak akan terpisah (mengalami koalesensi atau pemisahan fase) meskipun disimpan dalam jangka waktu lama.</p>
<p>Seluruh bahan baku yang kami gunakan telah lolos uji keamanan logam berat dan bebas dari kontaminasi bakteri patogen. Kami memastikan proses manufaktur berjalan steril dari awal hingga tahap pengisian botol otomatis (automatic filling).</p>

<h2>Proses Kerjasama Maklon Mudah dan Cepat</h2>
<p>Bersama Pabrik Kosmetik Tangerang, Anda tidak perlu mengkhawatirkan kerumitan pengurusan administrasi. Kami menyediakan fasilitas pendaftaran notifikasi BPOM secara cepat, sertifikasi Halal dari BPJPH Indonesia, pengurusan hak merek HAKI, hingga konsultasi desain kemasan visual produk secara gratis. Mulai langkah pertama Anda hari ini menuju kesuksesan brand kecantikan lokal yang mendunia.</p>
        """,
        "spec_cards": """
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">oil_barrel</span>
        <h3 class="text-xl font-bold text-primary mb-3">Premium Shea Butter</h3>
        <p class="text-gray-500 text-sm">Bahan pelembap alami berlemak tinggi. Menutrisi kulit kering secara mendalam, meningkatkan elastisitas kulit, dan memulihkan kelembutan alami.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">palette</span>
        <h3 class="text-xl font-bold text-primary mb-3">Glutathione & Vitamin C</h3>
        <p class="text-gray-500 text-sm">Antioksidan kuat penangkal radikal bebas. Bekerja sinergis mencerahkan kulit kusam dan menyamarkan bintik hitam penuaan.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">air</span>
        <h3 class="text-xl font-bold text-primary mb-3">IFRA Certified Fragrances</h3>
        <p class="text-gray-500 text-sm">Wewangian parfum mewah kelas dunia yang bersertifikat aman bagi kulit. Menjamin aroma melekat tahan lama tanpa menyebabkan alergi.</p>
      </div>
        """,
        "faq_items": """
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa MOQ maklon body lotion?</h4>
        <p class="text-gray-600">MOQ maklon body lotion di Pabrik Kosmetik Tangerang adalah 500 pcs per varian untuk Paket Basic. Untuk kemasan dan botol custom eksklusif, MOQ minimal adalah 1.000 pcs.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah losion tubuh yang diproduksi lengket saat berkeringat?</h4>
        <p class="text-gray-600">Tidak. Formulator kami merancang losion menggunakan formula non-greasy yang menyerap cepat ke dalam pori-pori kulit sehingga tetap nyaman dan tidak terasa licin saat kulit berkeringat.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah saya bisa memesan wewangian duplikasi parfum terkenal?</h4>
        <p class="text-gray-600">Ya. Kami bermitra dengan pemasok parfum internasional yang dapat menyediakan aroma terinspirasi dari parfum-parfum mewah (designer perfumes) terlaris di pasaran saat ini.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa lama daya tahan wangi losion tubuh di kulit?</h4>
        <p class="text-gray-600">Tergantung konsentrasi wewangian yang disepakati. Umumnya, dengan wewangian bersertifikat IFRA kami, keharuman losion dapat bertahan di kulit selama 4 hingga 8 jam aktivitas.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah bisa membuat body lotion dengan klaim perlindungan matahari (SPF)?</h4>
        <p class="text-gray-600">Tentu saja. Kami bisa menambahkan bahan tabir surya fisik maupun kimia ke dalam formula losion Anda untuk menghasilkan produk body lotion SPF 15 hingga SPF 50.</p>
      </div>
        """,
        "schema_json": ""
    },
    {
        "filename": "maklon-body-scrub.html",
        "category": "Body Care",
        "product_name": "Body Scrub",
        "meta_title": "Jasa Maklon Body Scrub Tangerang | Lulur Tradisional & Modern Custom",
        "meta_desc": "Bikin brand lulur badan sendiri! Jasa maklon body scrub Tangerang. Formula scrub lembut, mengangkat sel kulit mati, mencerahkan. BPOM, Halal MUI. MOQ 500 pcs.",
        "hero_desc": "Hadirkan lini produk body scrub dan lulur mandi eksklusif. Formula butiran scrub alami yang lembut mengangkat sel kulit mati secara optimal tanpa memicu iritasi kulit.",
        "aeo_paragraph": "Jasa Maklon Body Scrub di Pabrik Kosmetik Tangerang memproduksi lulur badan kustom (scrub tradisional, garam laut, eksfoliator kopi, brightening scrub) bersertifikat CPKB Grade A. MOQ mulai 500 pcs, termasuk formula gratis, legalitas BPOM, Halal MUI, dan HAKI merek.",
        "main_content": """
<h2>Peluang Bisnis Body Scrub & Lulur Mandi Eksfoliasi Kulit</h2>
<p>Perawatan kulit tubuh tidak lengkap tanpa proses eksfoliasi mendalam. Body scrub atau lulur badan adalah produk perawatan mingguan yang sangat digemari karena memberikan sensasi relaksasi spa langsung di rumah. Kebiasaan menggunakan lulur secara rutin terbukti efektif merangsang regenerasi sel kulit baru, menghaluskan area kulit yang kasar, dan memaksimalkan penyerapan losion tubuh setelah mandi. Pasar lulur badan di Indonesia sangat besar, mulai dari lulur tradisional berbahan rempah alami hingga body scrub modern beraroma buah segar.</p>
<p>Pabrik Kosmetik Tangerang memformulasikan body scrub premium menggunakan agen eksfoliator fisik (scrub) berbentuk bulat sempurna (spherical beads) untuk mencegah goresan halus (micro-tears) pada permukaan kulit. Banyak keluhan lulur di pasaran yang memiliki butiran terlalu tajam dan kasar sehingga merusak epidermis kulit ari.</p>
<p>Kami memastikan produk scrub mandi Anda diperkaya dengan pelembap tambahan dan bahan pencerah aktif, sehingga setelah dibasuh, kulit konsumen terasa kenyal, halus, dan langsung tampak lebih cerah.</p>

<h2>Pilihan Formulasi Body Scrub yang Kami Sediakan</h2>
<p>Kami melayani pembuatan beraneka sediaan scrub badan kustom sesuai segmentasi brand kecantikan Anda:</p>
<ul>
  <li><strong>Traditional Javanese / Balinese Lulur:</strong> Menggunakan bahan dasar beras ketan, kunyit, temulawak, dan rempah-rempah asli Indonesia untuk memberikan sensasi lulur tradisional yang wangi herbal menenangkan.</li>
  <li><strong>Brightening Milk & Honey Scrub:</strong> Scrub mandi dengan protein susu alami, madu, dan Niacinamide untuk mengangkat daki sekaligus mencerahkan dan menghaluskan kulit kusam secara bertahap.</li>
  <li><strong>Exfoliating Sea Salt & Sugar Scrub:</strong> Formula eksfoliasi garam laut halus atau gula alami yang kaya akan mineral untuk membersihkan pori-pori kulit secara mendalam dan meredakan peradangan.</li>
  <li><strong>Coffee & Chocolate Antioxidant Scrub:</strong> Memanfaatkan bubuk kopi asli pilihan yang kaya akan kafein untuk mengencangkan kulit, menyamarkan tampilan selulit, dan memberikan aroma relaksasi yang membangkitkan energi.</li>
</ul>

<h2>Teknologi CPKB Grade A & Konsistensi Tekstur Lulur</h2>
<p>Memproduksi scrub badan membutuhkan stabilitas emulsi yang sangat baik agar butiran scrub tidak mengendap di dasar wadah pot kemasan. Pabrik Kosmetik Tangerang menggunakan mesin mixing canggih berkecepatan tinggi yang menjamin penyebaran butiran scrub tersebar merata secara homogen dalam krim losion.</p>
<p>Kami menjamin seluruh bahan baku penggosok kulit yang kami gunakan terbuat dari bahan biodegradable ramah lingkungan (bukan mikroplastik sintetis berbahaya yang dapat merusak ekosistem laut).</p>

<h2>Layanan Maklon Lengkap Terpercaya di Tangerang</h2>
<p>Kami menyederhanakan seluruh alur pembuatan bisnis lulur mandi Anda. Tim R&D kami merancang contoh produk gratis, sementara tim legalitas kami mendaftarkan Notifikasi BPOM, sertifikasi Halal MUI, dan pendaftaran hak paten merek HAKI. Desainer grafis kami juga siap merancang stiker label pot lulur yang elegan dan eye-catching untuk memikat konsumen Anda di rak toko.</p>
        """,
        "spec_cards": """
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">grain</span>
        <h3 class="text-xl font-bold text-primary mb-3">Biodegradable Jojoba Esters</h3>
        <p class="text-gray-500 text-sm">Butiran penggosok alami berbentuk bulat halus dari lilin jojoba. Mengangkat sel kulit mati dengan lembut tanpa menimbulkan luka mikro pada kulit.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">coffee</span>
        <h3 class="text-xl font-bold text-primary mb-3">Organic Coffee Grounds</h3>
        <p class="text-gray-500 text-sm">Bubuk kopi organik dengan kandungan kafein tinggi. Berfungsi melancarkan sirkulasi darah bawah kulit dan menyamarkan selulit.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">nest_cam_wired_house</span>
        <h3 class="text-xl font-bold text-primary mb-3">Olive & Almond Oils</h3>
        <p class="text-gray-500 text-sm">Minyak nabati pelembap pengunci hidrasi. Menjaga permukaan kulit tetap basah dan lembut sesaat setelah proses pembasuhan lulur.</p>
      </div>
        """,
        "faq_items": """
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa MOQ untuk maklon body scrub?</h4>
        <p class="text-gray-600">MOQ untuk produk body scrub di Pabrik Kosmetik Tangerang dimulai dari 500 pcs per varian untuk kemasan pot standar dari stok kami.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah butiran scrub-nya aman untuk ekosistem laut (reef-safe)?</h4>
        <p class="text-gray-600">Ya. Kami melarang penggunaan butiran plastik sintetis (microbeads). Semua scrub kami terbuat dari bahan alami yang mudah terurai seperti lilin jojoba, biji aprikot hancur, kopi, gula, atau garam laut.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah lulur badan ini bisa digunakan untuk kulit sensitif?</h4>
        <p class="text-gray-600">Tentu. Kami dapat merancang formula ekstra lembut (gentle scrub) menggunakan konsentrasi scrub yang lebih rendah dan butiran lilin jojoba yang paling halus agar tidak memicu iritasi.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah saya bisa memilih wadah pot kosmetik custom?</h4>
        <p class="text-gray-600">Ya, kami memiliki berbagai pilihan pot lulur plastik PP/PET tebal dengan kapasitas 100g, 200g, hingga 250g, lengkap dengan pilihan warna tutup kustom.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa lama masa kedaluwarsa produk body scrub?</h4>
        <p class="text-gray-600">Masa kedaluwarsa produk body scrub kami umumnya adalah 2 hingga 3 tahun sejak tanggal produksi, berkat sistem pengawetan kosmetik yang aman dan stabil.</p>
      </div>
        """,
        "schema_json": ""
    },
    {
        "filename": "maklon-shampoo-anti-rontok.html",
        "category": "Hair Care",
        "product_name": "Shampo Anti-Rontok",
        "meta_title": "Jasa Maklon Shampo Anti-Rontok | Formula Penumbuh Rambut Kustom",
        "meta_desc": "Bikin brand shampo anti-rontok sendiri! Jasa maklon hair care di Tangerang bersertifikat CPKB Grade A. Formula Ginseng, Keratin, Minoxidil-Alternative. MOQ 500 pcs.",
        "hero_desc": "Produksi shampo anti-rontok premium untuk mengatasi rambut rontok, patah, dan menyuburkan pertumbuhan rambut baru dengan formula penumbuh rambut canggih.",
        "aeo_paragraph": "Jasa Maklon Shampo Anti-Rontok di Pabrik Kosmetik Tangerang memproduksi produk perawatan rambut rontok (anti-hair fall shampoo) kustom bersertifikat CPKB Grade A. MOQ mulai 500 pcs, mencakup riset formula gratis, BPOM, sertifikasi Halal, dan HAKI merek.",
        "main_content": """
<h2>Pasar Potensial Hair Care: Shampo Anti-Rontok Premium</h2>
<p>Masalah rambut rontok, ketombe, dan kerusakan kulit kepala adalah keluhan paling umum yang dialami oleh masyarakat Indonesia. Akibat iklim tropis yang lembap serta penggunaan penutup kepala (seperti hijab atau helm) dalam jangka waktu lama, kulit kepala menjadi mudah berminyak dan folikel rambut melemah. Oleh sebab itu, produk perawatan rambut atau hair care khususnya shampo penumbuh rambut dan anti-rontok selalu dicari konsumen dan memiliki loyalitas brand yang sangat tinggi.</p>
<p>Di Pabrik Kosmetik Tangerang, kami merancang shampo anti-rontok berkinerja tinggi yang bekerja langsung pada tiga tingkat masalah: membersihkan kulit kepala dari sebum penyumbat folikel, memberikan nutrisi mikro pada akar rambut, dan memperkuat batang rambut agar tidak mudah patah.</p>
<p>Kami menghindari penggunaan detergen keras seperti SLS yang dapat mengikis minyak pelindung alami kulit kepala secara berlebihan. Sebagai gantinya, kami memadukan surfaktan ringan yang bersahabat dengan kulit kepala sensitif dan menjaga kelembapan helai rambut.</p>

<h2>Bahan Aktif Unggulan untuk Formulasi Shampo Rambut Anda</h2>
<p>Formula shampo anti-rontok kami diperkaya dengan berbagai bahan bio-aktif yang terbukti menstimulasi pertumbuhan rambut secara ilmiah:</p>
<ul>
  <li><strong>Ekstrak Ginseng & Aloe Vera Tradisional:</strong> Kombinasi herbal legendaris yang kaya akan saponin untuk merangsang sirkulasi darah di kulit kepala, menguatkan akar rambut, serta menyuburkan batang rambut.</li>
  <li><strong>Keratin & Biotin (Vitamin B7):</strong> Protein esensial pembentuk struktur rambut untuk menambal kerusakan kutikula rambut yang rapuh, menjadikannya lebih tebal, bercahaya, dan tidak mudah patah.</li>
  <li><strong>Peptide & Minoxidil-Alternatives (Redensyl / Capixyl):</strong> Bahan aktif bioteknologi modern yang bekerja langsung pada sel induk folikel rambut untuk mengaktifkan kembali fase pertumbuhan rambut (anagen phase).</li>
  <li><strong>Salicylic Acid & Menthol:</strong> Membantu membersihkan ketombe dan sebum berlebih di kulit kepala, memberikan sensasi dingin yang menyegarkan serta meredakan gatal.</li>
</ul>

<h2>Fasilitas Produksi CPKB Grade A Tangerang</h2>
<p>Sebagai produsen kosmetik terakreditasi, fasilitas pabrik kami memiliki standar Cara Pembuatan Kosmetika yang Baik (CPKB) Golongan A untuk sediaan cairan kosmetik. Kami menggunakan mixer pencampur stainless steel 316L (grade farmasi) untuk menjamin tidak ada reaksi kimia korosif antara wadah mesin dengan bahan aktif shampo.</p>
<p>Apoteker kami melakukan pengujian viskositas, stabilitas busa, kejernihan cairan, serta uji mikrobiologi ketat untuk memastikan shampo aman digunakan setiap hari oleh konsumen akhir.</p>

<h2>Mulai Perjalanan Bisnis Hair Care Anda Sekarang</h2>
<p>Kami menawarkan paket pendaftaran maklon terintegrasi <em>One-Stop Service</em>. Dari konsultasi formula kustom bersama formulator ahli, perancangan sampel produk gratis, sourcing botol kemasan pump/flip-top eksklusif, hingga pengurusan Notifikasi BPOM (NA), sertifikat Halal MUI, dan HAKI Merek Dagang. Segera hubungi tim kami untuk mewujudkan brand perawatan rambut sukses Anda.</p>
        """,
        "spec_cards": """
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">nature</span>
        <h3 class="text-xl font-bold text-primary mb-3">Redensyl & Capixyl</h3>
        <p class="text-gray-500 text-sm">Bahan aktif penumbuh rambut berbasis bioteknologi. Mendorong pertumbuhan rambut baru langsung pada akar rambut dengan efikasi teruji klinis.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">shield</span>
        <h3 class="text-xl font-bold text-primary mb-3">Hydrolyzed Keratin</h3>
        <p class="text-gray-500 text-sm">Protein keratin terhidrolisis yang meresap ke dalam batang rambut. Memperbaiki kutikula rambut rusak dan mencegah kerontokan akibat patah.</p>
      </div>
      <div class="bg-white p-8 rounded-3xl border border-gray-200/50 shadow-sm">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">ac_unit</span>
        <h3 class="text-xl font-bold text-primary mb-3">Menthol & Tea Tree Oil</h3>
        <p class="text-gray-500 text-sm">Minyak atsiri penenang kulit kepala. Memberikan kesegaran instan, meredakan rasa gatal, dan mengatasi ketombe penyumbat akar.</p>
      </div>
        """,
        "faq_items": """
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa MOQ untuk maklon shampo anti-rontok?</h4>
        <p class="text-gray-600">MOQ awal untuk produk shampo adalah 500 pcs per varian untuk Paket Basic, menggunakan botol standar dari stok katalog kami.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah shampo maklon ini bebas paraben dan silikon?</h4>
        <p class="text-gray-600">Ya. Kami dapat merancang formulasi shampo bebas paraben (paraben-free) dan bebas silikon (silicone-free) untuk diposisikan sebagai produk hair care natural ramah lingkungan.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah formula shampo dapat dikombinasikan dengan conditioner?</h4>
        <p class="text-gray-600">Tentu saja. Kami dapat memformulasikan produk 2-in-1 Shampoo & Conditioner, atau memproduksi Conditioner terpisah sebagai pelengkap rangkaian produk perawatan rambut Anda.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Berapa lama proses produksi massal shampo setelah BPOM terbit?</h4>
        <p class="text-gray-600">Proses produksi massal di pabrik kami berkisar antara 2 hingga 3 minggu sejak bahan baku dan kemasan siap di area produksi kami.</p>
      </div>
      <div class="bg-white p-6 rounded-2xl shadow-sm border border-gray-100">
        <h4 class="font-bold text-lg text-primary mb-2">Apakah formula shampo bisa membantu mengatasi ketombe juga?</h4>
        <p class="text-gray-600">Ya. Tim formulator kami dapat menambahkan bahan anti-ketombe bersertifikasi aman seperti Zinc Pyrithione atau Piroctone Olamine ke dalam formula shampo anti-rontok Anda.</p>
      </div>
        """,
        "schema_json": ""
    }
]

# Generate each page
for page in pages_data:
    filename = page["filename"]
    product_name = page["product_name"]
    category = page["category"]
    
    # Structure Schema JSON-LD
    schema = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"https://pabrikkosmetiktangerang.net/{filename}#service",
                "name": f"Jasa Maklon {product_name} Tangerang",
                "serviceType": "Contract Manufacturing Kosmetik",
                "provider": {
                    "@type": "LocalBusiness",
                    "name": biz["name"],
                    "telephone": biz["phone"],
                    "email": biz["email"],
                    "address": {
                        "@type": "PostalAddress",
                        "streetAddress": biz["address"]
                    }
                },
                "areaServed": {
                    "@type": "Country",
                    "name": "Indonesia"
                },
                "offers": {
                    "@type": "Offer",
                    "price": str(pkg_basic["price_numeric"]),
                    "priceCurrency": "IDR",
                    "description": pkg_basic["details"]
                }
            },
            {
                "@type": "FAQPage",
                "@id": f"https://pabrikkosmetiktangerang.net/{filename}#faq",
                "mainEntity": []
            }
        ]
    }
    
    # Extract Q&A for Schema from faq_items raw string using basic parser (or hardcode/mock since we want valid JSON)
    # Let's map it explicitly to keep JSON-LD perfectly valid without parsing errors
    if product_name == "Serum Wajah":
        faqs = [
            ("Berapa biaya pembuatan sampel formula serum?", "Riset formula dan pembuatan sampel serum wajah di Pabrik Kosmetik Tangerang adalah gratis untuk calon mitra maklon. Kami memberikan kesempatan revisi hingga formula disepakati."),
            ("Berapa MOQ (Minimum Order Quantity) untuk maklon serum?", "MOQ untuk produk serum wajah adalah 500 pcs per varian untuk Paket Basic, dan 1.000+ pcs untuk formula kustom eksklusif (Paket Enterprise)."),
            ("Berapa lama izin BPOM serum diterbitkan?", "Proses pendaftaran hingga terbitnya nomor Notifikasi BPOM (NA) kosmetik biasanya berkisar antara 1 hingga 2 bulan, bergantung pada antrean di BPOM RI."),
            ("Apakah formula serum dari pabrik dijamin eksklusif?", "Ya, untuk pendaftaran maklon sistem ODM (Enterprise), kami menjamin 100% eksklusivitas formula Anda. Formula tersebut tidak akan digunakan untuk brand lain dan terikat kontrak NDA."),
            ("Apakah saya bisa menggunakan kemasan serum sendiri?", "Tentu saja. Anda bisa melakukan sourcing kemasan botol serum sendiri, atau menyerahkan sourcing kemasan sepenuhnya kepada tim kami demi efisiensi dan jaminan sterilitas.")
        ]
    elif product_name == "Sunscreen":
        faqs = [
            ("Berapa biaya uji SPF untuk maklon sunscreen?", "Uji SPF standar In-Vitro termasuk dalam biaya riset awal formula kami. Namun, untuk uji klinis SPF In-Vivo resmi (pihak ketiga), biayanya akan disesuaikan dengan tarif laboratorium independen mitra kami."),
            ("Berapa MOQ maklon sunscreen wajah?", "MOQ sunscreen wajah adalah 500 pcs untuk kemasan standar dari stok katalog kami, dan minimal 1.000 pcs jika Anda menginginkan kemasan botol/tube khusus kustom."),
            ("Apakah sunscreen yang dibuat di pabrik aman untuk terumbu karang (reef-safe)?", "Ya, kami dapat merancang formulasi tabir surya ramah lingkungan (reef-safe sunscreen) dengan menghindari penggunaan bahan kimia berbahaya seperti Oxybenzone dan Octinoxate."),
            ("Apakah saya bisa membuat sunscreen berbentuk stik (sunscreen stick)?", "Tentu saja. Kami memiliki jalur produksi khusus untuk sediaan kosmetik padat/semi-padat seperti sunscreen stick, balm, dan cushion sunscreen."),
            ("Bagaimana klaim perlindungan air (waterproof/water-resistant) didaftarkan?", "Klaim ketahanan air memerlukan uji klinis ketahanan tambahan. Formula sunscreen akan dirancang menggunakan agen pembentuk lapisan tipis (film former) khusus agar tidak luntur saat berkeringat.")
        ]
    elif product_name == "Facial Wash":
        faqs = [
            ("Berapa MOQ untuk maklon sabun cuci muka?", "MOQ untuk pembuatan produk facial wash di pabrik kami dimulai dari 500 pcs per varian untuk Paket Basic. Cocok bagi pemula yang ingin meminimalkan risiko modal."),
            ("Apakah saya bisa meminta formula dengan klaim busa sedikit?", "Tentu saja. Tren sabun wajah lembut minim busa (gentle low-pH cleanser) sangat diminati saat ini. Tim formulator kami dapat merancang formula sabun gel non-soap yang sangat lembut."),
            ("Berapa biaya pengurusan BPOM dan Halal untuk facial wash?", "Biaya pengurusan Notifikasi BPOM, sertifikasi Halal, dan HAKI sudah termasuk dalam paket maklon terintegrasi yang kami tawarkan. Silakan hubungi tim sales kami untuk rincian biayanya."),
            ("Apakah pabrik menyediakan opsi kemasan botol pump dan tube foaming?", "Ya, kami menyediakan beragam pilihan kemasan botol pump, kemasan tube plastik laminasi (matte/glossy), botol foaming pump (yang otomatis menghasilkan busa), dan tube dengan aplikator silikon brush."),
            ("Apakah formula sabun wajah bisa menggunakan wewangian alami?", "Ya, kami dapat menambahkan minyak atsiri alami (essential oil) seperti Lavender or Rose Water sebagai pemberi aroma alami untuk menghindari penggunaan parfum sintetik sensitif.")
        ]
    elif product_name == "Body Lotion":
        faqs = [
            ("Berapa MOQ maklon body lotion?", "MOQ maklon body lotion di Pabrik Kosmetik Tangerang adalah 500 pcs per varian untuk Paket Basic. Untuk kemasan dan botol custom eksklusif, MOQ minimal adalah 1.000 pcs."),
            ("Apakah losion tubuh yang diproduksi lengket saat berkeringat?", "Tidak. Formulator kami merancang losion menggunakan formula non-greasy yang menyerap cepat ke dalam pori-pori kulit sehingga tetap nyaman dan tidak terasa licin saat kulit berkeringat."),
            ("Apakah saya bisa memesan wewangian duplikasi parfum terkenal?", "Ya. Kami bermitra dengan pemasok parfum internasional yang dapat menyediakan aroma terinspirasi dari parfum-parfum mewah (designer perfumes) terlaris di pasaran saat ini."),
            ("Berapa lama daya tahan wangi losion tubuh di kulit?", "Tergantung konsentrasi wewangian yang disepakati. Umumnya, dengan wewangian bersertifikat IFRA kami, keharuman losion dapat bertahan di kulit selama 4 hingga 8 jam aktivitas."),
            ("Apakah bisa membuat body lotion dengan klaim perlindungan matahari (SPF)?", "Tentu saja. Kami bisa menambahkan bahan tabir surya fisik maupun kimia ke dalam formula losion Anda untuk menghasilkan produk body lotion SPF 15 hingga SPF 50.")
        ]
    elif product_name == "Body Scrub":
        faqs = [
            ("Berapa MOQ untuk maklon body scrub?", "MOQ untuk produk body scrub di Pabrik Kosmetik Tangerang dimulai dari 500 pcs per varian untuk kemasan pot standar dari stok kami."),
            ("Apakah butiran scrub-nya aman untuk ekosistem laut (reef-safe)?", "Ya. Kami melarang penggunaan butiran plastik sintetis (microbeads). Semua scrub kami terbuat dari bahan alami yang mudah terurai seperti lilin jojoba, biji aprikot hancur, kopi, gula, atau garam laut."),
            ("Apakah lulur badan ini bisa digunakan untuk kulit sensitif?", "Tentu. Kami dapat merancang formula ekstra lembut (gentle scrub) menggunakan konsentrasi scrub yang lebih rendah dan butiran lilin jojoba yang paling halus agar tidak memicu iritasi."),
            ("Apakah saya bisa memilih wadah pot kosmetik custom?", "Ya, kami memiliki berbagai pilihan pot lulur plastik PP/PET tebal dengan kapasitas 100g, 200g, hingga 250g, lengkap dengan pilihan warna tutup kustom."),
            ("Berapa lama masa kedaluwarsa produk body scrub?", "Masa kedaluwarsa produk body scrub kami umumnya adalah 2 hingga 3 tahun sejak tanggal produksi, berkat sistem pengawetan kosmetik yang aman dan stabil.")
        ]
    elif product_name == "Shampo Anti-Rontok":
        faqs = [
            ("Berapa MOQ untuk maklon shampo anti-rontok?", "MOQ awal untuk produk shampo adalah 500 pcs per varian untuk Paket Basic, menggunakan botol standar dari stok katalog kami."),
            ("Apakah shampo maklon ini bebas paraben dan silikon?", "Ya. Kami dapat merancang formulasi shampo bebas paraben (paraben-free) dan bebas silikon (silicone-free) untuk diposisikan sebagai produk hair care natural ramah lingkungan."),
            ("Apakah formula shampo dapat dikombinasikan dengan conditioner?", "Tentu saja. Kami dapat memformulasikan produk 2-in-1 Shampoo & Conditioner, atau memproduksi Conditioner terpisah sebagai pelengkap rangkaian produk perawatan rambut Anda."),
            ("Berapa lama proses produksi massal shampo setelah BPOM terbit?", "Proses produksi massal di pabrik kami berkisar antara 2 hingga 3 minggu sejak bahan baku dan kemasan siap di area produksi kami."),
            ("Apakah formula shampo bisa membantu mengatasi ketombe juga?", "Ya. Tim formulator kami dapat menambahkan bahan anti-ketombe bersertifikasi aman seperti Zinc Pyrithione atau Piroctone Olamine ke dalam formula shampo anti-rontok Anda.")
        ]
    else:
        faqs = []

    for q, a in faqs:
        schema["@graph"][1]["mainEntity"].append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        
    schema_str = json.dumps(schema, ensure_ascii=False, indent=2)
    
    html = HTML_TEMPLATE.format(
        meta_title=page["meta_title"],
        meta_desc=page["meta_desc"],
        filename=filename,
        category=category,
        product_name=product_name,
        hero_desc=page["hero_desc"],
        aeo_paragraph=page["aeo_paragraph"],
        main_content=page["main_content"],
        spec_cards=page["spec_cards"],
        moq_basic=pkg_basic["moq"],
        moq_enterprise=pkg_ent["moq"],
        price_basic=pkg_basic["price"],
        price_enterprise=pkg_ent["price"],
        faq_items=page["faq_items"],
        schema_json=schema_str
    )
    
    with open(filename, "w", encoding="utf-8") as out:
        out.write(html)
        
    print(f"Generated {filename}")

print("Successfully generated all 6 money pages!")
