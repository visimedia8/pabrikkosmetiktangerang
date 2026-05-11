const fs = require('fs');
const path = require('path');

const targetFile = 'D:\\pabrikkosmetiktangerang.net\\index.html';

const htmlContent = `<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>Pabrik Kosmetik Tangerang — Maklon & Private Label</title>
<script src="https://cdn.tailwindcss.com?plugins=forms,container-queries"></script>
<link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap" rel="stylesheet"/>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Lora:ital@1&display=swap" rel="stylesheet"/>
<script id="tailwind-config">
tailwind.config = {
  darkMode: "class",
  theme: {
    extend: {
      colors: {
        "primary": "#1A3A4A",
        "primary-light": "#2A5A72",
        "primary-dark": "#0D1F28",
        "secondary": "#D4A855",
        "accent": "#E8F4F0",
        "cta": "#2ECC8B",
        "cta-hover": "#27B57A",
        "off-white": "#F8F9FA",
        "light-bg": "#F0F4F5",
        "text": "#1C2B33",
        "text-muted": "#5A7080",
        "border": "#DDE5E9"
      },
      fontFamily: {
        sans: ["Plus Jakarta Sans", "sans-serif"],
        serif: ["Lora", "serif"]
      }
    }
  }
};
</script>
<style>
  .hex-bg { background-image: url("data:image/svg+xml,%3Csvg width='40' height='40' viewBox='0 0 40 40' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M20 0l20 10v20L20 40 0 30V10z' fill-opacity='0.03' fill='%23ffffff' fill-rule='evenodd'/%3E%3C/svg%3E"); }
  html { scroll-behavior: smooth; }
  .fade-in { opacity: 0; transform: translateY(20px); transition: opacity 0.6s ease-out, transform 0.6s ease-out; }
  .fade-in.visible { opacity: 1; transform: translateY(0); }
</style>
</head>
<body class="bg-off-white font-sans text-text antialiased">

<!-- NAVBAR -->
<nav class="fixed w-full z-50 bg-white/90 backdrop-blur-md border-b border-border shadow-sm transition-all" id="navbar">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="flex justify-between items-center h-20">
      <a href="#" class="font-bold text-xl md:text-2xl text-primary flex items-center gap-2">
        <span class="material-symbols-outlined text-secondary">science</span>
        Pabrik Kosmetik Tangerang
      </a>
      <div class="hidden md:flex items-center space-x-8">
        <a href="#layanan" class="text-text-muted hover:text-primary font-medium">Layanan</a>
        <a href="#produk" class="text-text-muted hover:text-primary font-medium">Produk</a>
        <a href="#harga" class="text-text-muted hover:text-primary font-medium">Harga</a>
        <a href="#sertifikasi" class="text-text-muted hover:text-primary font-medium">Sertifikasi</a>
        <a href="#kontak" class="bg-cta hover:bg-cta-hover text-white px-6 py-2 rounded-lg font-medium transition-colors shadow-lg shadow-cta/30 flex items-center gap-2">
          <span class="material-symbols-outlined text-[20px]">chat</span> WhatsApp
        </a>
      </div>
    </div>
  </div>
</nav>

<!-- HERO -->
<section class="relative pt-32 pb-20 lg:pt-48 lg:pb-32 bg-primary overflow-hidden">
  <div class="absolute inset-0 hex-bg"></div>
  <div class="absolute right-0 top-0 w-1/2 h-full bg-gradient-to-l from-primary-light/50 to-transparent"></div>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10 grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
    <div class="fade-in">
      <div class="flex flex-wrap gap-2 mb-6">
        <span class="inline-flex items-center gap-1 px-3 py-1 bg-white/10 border border-white/20 rounded-full text-xs font-medium text-white">
          <span class="material-symbols-outlined text-[14px] text-secondary">verified</span> BPOM
        </span>
        <span class="inline-flex items-center gap-1 px-3 py-1 bg-white/10 border border-white/20 rounded-full text-xs font-medium text-white">
          <span class="material-symbols-outlined text-[14px] text-secondary">verified</span> Halal MUI
        </span>
        <span class="inline-flex items-center gap-1 px-3 py-1 bg-white/10 border border-white/20 rounded-full text-xs font-medium text-white">
          <span class="material-symbols-outlined text-[14px] text-secondary">workspace_premium</span> CPKB Grade A
        </span>
      </div>
      <h1 class="text-4xl md:text-5xl lg:text-6xl font-extrabold text-white leading-tight mb-6">
        Maklon & Private Label Skincare Terpercaya
      </h1>
      <p class="text-lg text-white/80 mb-8 max-w-xl">
        Wujudkan brand kosmetik impian Anda bersama pabrik terpercaya di Tangerang. Dari formulasi R&D hingga pengurusan legalitas BPOM & Halal — semua dalam satu atap.
      </p>
      <div class="flex flex-col sm:flex-row gap-4">
        <a href="https://wa.me/6283863670421" class="inline-flex justify-center items-center gap-2 bg-cta hover:bg-cta-hover text-white px-8 py-4 rounded-xl font-bold transition-all shadow-lg shadow-cta/40">
          <span class="material-symbols-outlined">chat</span> Konsultasi Gratis
        </a>
        <a href="#layanan" class="inline-flex justify-center items-center gap-2 border-2 border-white/30 hover:border-white text-white px-8 py-4 rounded-xl font-bold transition-all">
          Lihat Layanan
        </a>
      </div>
    </div>
    <div class="relative fade-in">
      <div class="aspect-[4/3] rounded-2xl overflow-hidden shadow-2xl border border-white/10">
        <img src="https://images.unsplash.com/photo-1579165466949-3180a3d056d5?auto=format&fit=crop&w=800&q=80" alt="Laboratorium Pabrik Kosmetik Tangerang" class="w-full h-full object-cover" />
      </div>
      <div class="absolute -bottom-6 -left-6 bg-white p-6 rounded-xl shadow-xl flex items-center gap-4">
        <div class="w-12 h-12 bg-secondary/20 rounded-full flex items-center justify-center">
          <span class="material-symbols-outlined text-secondary">science</span>
        </div>
        <div>
          <p class="text-sm font-bold text-primary">R&D Laboratory</p>
          <p class="text-xs text-text-muted">Formulasi Skincare Custom</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TRUST BAR -->
<section class="bg-secondary py-6 border-b border-black/10 relative z-20 shadow-md">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-wrap justify-center lg:justify-between items-center gap-6">
    <div class="flex items-center gap-2 text-primary-dark font-bold"><span class="material-symbols-outlined">verified_user</span> BPOM RI Terdaftar</div>
    <div class="flex items-center gap-2 text-primary-dark font-bold"><span class="material-symbols-outlined">task_alt</span> HALAL MUI</div>
    <div class="flex items-center gap-2 text-primary-dark font-bold"><span class="material-symbols-outlined">factory</span> CPKB GRADE A</div>
    <div class="flex items-center gap-2 text-primary-dark font-bold hidden md:flex"><span class="material-symbols-outlined">inventory_2</span> 500+ PRODUK DIPRODUKSI</div>
  </div>
</section>

<!-- KEUNGGULAN -->
<section class="py-24 bg-off-white" id="keunggulan">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">Mengapa Memilih Kami?</h2>
      <p class="text-text-muted text-lg">Keunggulan pabrik kosmetik kami untuk bisnis Anda.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
      <!-- Card 1 -->
      <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-l-4 border-secondary fade-in">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">factory</span>
        <h3 class="text-xl font-bold text-primary mb-2">Fasilitas CPKB Grade A</h3>
        <p class="text-text-muted">Pabrik berstandar tertinggi BPOM untuk produksi kosmetik higienis & aman.</p>
      </div>
      <!-- Card 2 -->
      <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-l-4 border-secondary fade-in">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">all_inclusive</span>
        <h3 class="text-xl font-bold text-primary mb-2">One-Stop Solution</h3>
        <p class="text-text-muted">Dari konsep formulasi, desain kemasan, izin BPOM, hingga produksi massal.</p>
      </div>
      <!-- Card 3 -->
      <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-l-4 border-secondary fade-in">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">low_priority</span>
        <h3 class="text-xl font-bold text-primary mb-2">MOQ Fleksibel</h3>
        <p class="text-text-muted">Cocok untuk pemula maupun brand besar dengan minimum order produksi yang rendah.</p>
      </div>
      <!-- Card 4 -->
      <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-l-4 border-secondary fade-in">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">science</span>
        <h3 class="text-xl font-bold text-primary mb-2">Tim R&D Berpengalaman</h3>
        <p class="text-text-muted">Formulasi inovatif dengan bahan aktif terkini sesuai tren skincare global.</p>
      </div>
      <!-- Card 5 -->
      <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-l-4 border-secondary fade-in">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">gpp_good</span>
        <h3 class="text-xl font-bold text-primary mb-2">Jaminan Legalitas</h3>
        <p class="text-text-muted">Bantuan penuh kepengurusan Notifikasi BPOM, Halal MUI, dan HAKI Merek.</p>
      </div>
      <!-- Card 6 -->
      <div class="bg-white p-8 rounded-2xl shadow-sm hover:shadow-md transition-shadow border-l-4 border-secondary fade-in">
        <span class="material-symbols-outlined text-4xl text-secondary mb-4">local_shipping</span>
        <h3 class="text-xl font-bold text-primary mb-2">Pengiriman Nasional</h3>
        <p class="text-text-muted">Distribusi produk jadi yang aman dan tepat waktu ke seluruh Indonesia.</p>
      </div>
    </div>
  </div>
</section>

<!-- LAYANAN -->
<section class="py-24 bg-light-bg" id="layanan">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">Layanan Maklon Kosmetik</h2>
      <p class="text-text-muted text-lg">Solusi produksi dari hulu ke hilir untuk brand kosmetik Anda.</p>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
      <!-- Service 1 -->
      <div class="bg-primary p-10 rounded-2xl text-white relative overflow-hidden group fade-in">
        <div class="absolute top-0 right-0 w-32 h-32 bg-secondary/10 rounded-full -translate-y-16 translate-x-16 group-hover:scale-150 transition-transform duration-500"></div>
        <span class="material-symbols-outlined text-secondary text-5xl mb-6 relative z-10">face_retouching_natural</span>
        <h3 class="text-2xl font-bold mb-4 relative z-10">Maklon Skincare</h3>
        <p class="text-white/80 mb-6 relative z-10">Jasa pembuatan produk perawatan kulit (serum, cream, toner, dll) dengan formula khusus.</p>
      </div>
      <!-- Service 2 -->
      <div class="bg-primary p-10 rounded-2xl text-white relative overflow-hidden group fade-in">
        <div class="absolute top-0 right-0 w-32 h-32 bg-secondary/10 rounded-full -translate-y-16 translate-x-16 group-hover:scale-150 transition-transform duration-500"></div>
        <span class="material-symbols-outlined text-secondary text-5xl mb-6 relative z-10">inventory_2</span>
        <h3 class="text-2xl font-bold mb-4 relative z-10">Private Label OEM/ODM</h3>
        <p class="text-white/80 mb-6 relative z-10">Pilih dari formula siap pakai kami (OEM) atau kembangkan produk inovatif dari nol (ODM).</p>
      </div>
      <!-- Service 3 -->
      <div class="bg-primary p-10 rounded-2xl text-white relative overflow-hidden group fade-in">
        <div class="absolute top-0 right-0 w-32 h-32 bg-secondary/10 rounded-full -translate-y-16 translate-x-16 group-hover:scale-150 transition-transform duration-500"></div>
        <span class="material-symbols-outlined text-secondary text-5xl mb-6 relative z-10">verified</span>
        <h3 class="text-2xl font-bold mb-4 relative z-10">Pengurusan Legalitas</h3>
        <p class="text-white/80 mb-6 relative z-10">Pendampingan pengurusan Notifikasi BPOM, Sertifikat Halal MUI, dan Pendaftaran Merek.</p>
      </div>
      <!-- Service 4 -->
      <div class="bg-primary p-10 rounded-2xl text-white relative overflow-hidden group fade-in">
        <div class="absolute top-0 right-0 w-32 h-32 bg-secondary/10 rounded-full -translate-y-16 translate-x-16 group-hover:scale-150 transition-transform duration-500"></div>
        <span class="material-symbols-outlined text-secondary text-5xl mb-6 relative z-10">brush</span>
        <h3 class="text-2xl font-bold mb-4 relative z-10">Desain Kemasan</h3>
        <p class="text-white/80 mb-6 relative z-10">Layanan pemilihan botol/pot eksklusif dan desain label kemasan yang premium.</p>
      </div>
    </div>
  </div>
</section>

<!-- PRODUK -->
<section class="py-24 bg-white" id="produk">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">Produk yang Bisa Kami Buat</h2>
      <p class="text-text-muted text-lg">Pilihan kategori produk kosmetik terlengkap.</p>
    </div>
    
    <div class="grid grid-cols-2 md:grid-cols-4 gap-6 fade-in">
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">water_drop</span>
        <h4 class="font-bold text-primary">Serum Wajah</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">light_mode</span>
        <h4 class="font-bold text-primary">Sunscreen</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">clean_hands</span>
        <h4 class="font-bold text-primary">Facial Wash</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">opacity</span>
        <h4 class="font-bold text-primary">Body Lotion</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">face_4</span>
        <h4 class="font-bold text-primary">Moisturizer</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">self_care</span>
        <h4 class="font-bold text-primary">Body Scrub</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">brush</span>
        <h4 class="font-bold text-primary">Color Cosmetics</h4>
      </div>
      <div class="border border-border p-6 rounded-xl text-center hover:border-secondary transition-colors">
        <span class="material-symbols-outlined text-4xl text-primary mb-2">air</span>
        <h4 class="font-bold text-primary">Hair Care</h4>
      </div>
    </div>
  </div>
</section>

<!-- HARGA -->
<section class="py-24 bg-light-bg" id="harga">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">Estimasi Biaya Maklon</h2>
      <p class="text-text-muted text-lg max-w-2xl mx-auto">Biaya produksi berkisar Rp10.000–Rp100.000/unit tergantung jenis produk, formula, kemasan, dan jumlah pesanan (MOQ).</p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
      <div class="bg-white rounded-2xl p-8 border border-border fade-in">
        <h3 class="text-xl font-bold text-primary mb-2">Paket Starter</h3>
        <p class="text-text-muted mb-6">Cocok untuk UMKM & Pemula</p>
        <div class="text-3xl font-extrabold text-primary mb-6">Mulai Rp 15 Juta</div>
        <ul class="space-y-3 mb-8 text-text">
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> MOQ Fleksibel (500 pcs)</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Formula Standard</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Kemasan Ready Stock</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Gratis Notifikasi BPOM</li>
        </ul>
        <a href="https://wa.me/6283863670421" class="block text-center w-full bg-primary hover:bg-primary-light text-white py-3 rounded-lg font-bold transition-colors">Pilih Paket</a>
      </div>
      
      <div class="bg-primary rounded-2xl p-8 text-white relative transform md:-translate-y-4 shadow-xl fade-in">
        <div class="absolute top-0 right-0 bg-secondary text-primary font-bold text-xs px-3 py-1 rounded-bl-lg rounded-tr-lg">PALING POPULER</div>
        <h3 class="text-xl font-bold mb-2">Paket Growth</h3>
        <p class="text-white/70 mb-6">Untuk brand yang siap berkembang</p>
        <div class="text-3xl font-extrabold mb-6">Mulai Rp 35 Juta</div>
        <ul class="space-y-3 mb-8">
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> MOQ Menengah (1000 pcs)</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Custom Formula R&D</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Pilihan Kemasan Variatif</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Gratis BPOM & Sertifikasi Halal</li>
        </ul>
        <a href="https://wa.me/6283863670421" class="block text-center w-full bg-cta hover:bg-cta-hover text-white py-3 rounded-lg font-bold transition-colors shadow-lg shadow-cta/30">Pilih Paket</a>
      </div>
      
      <div class="bg-white rounded-2xl p-8 border border-border fade-in">
        <h3 class="text-xl font-bold text-primary mb-2">Paket Enterprise</h3>
        <p class="text-text-muted mb-6">Produksi skala besar & eksklusif</p>
        <div class="text-3xl font-extrabold text-primary mb-6">Custom</div>
        <ul class="space-y-3 mb-8 text-text">
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> MOQ Skala Besar</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Formula Eksklusif</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Kemasan Full Custom</li>
          <li class="flex gap-2"><span class="material-symbols-outlined text-secondary">check</span> Legalitas Full & Dedicated KAM</li>
        </ul>
        <a href="https://wa.me/6283863670421" class="block text-center w-full bg-primary hover:bg-primary-light text-white py-3 rounded-lg font-bold transition-colors">Hubungi Kami</a>
      </div>
    </div>
  </div>
</section>

<!-- PROSES KERJA -->
<section class="py-24 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 fade-in">
      <h2 class="text-3xl md:text-4xl font-bold text-primary mb-4">Proses Kerja Kami</h2>
      <p class="text-text-muted text-lg">Alur kerja transparan untuk wujudkan produk Anda.</p>
    </div>
    
    <div class="flex flex-col md:flex-row justify-between relative fade-in">
      <div class="hidden md:block absolute top-8 left-0 w-full h-1 bg-border -z-10"></div>
      
      <div class="flex flex-col items-center text-center relative bg-white md:px-4 mb-8 md:mb-0 w-full md:w-1/5">
        <div class="w-16 h-16 bg-primary text-secondary rounded-full flex items-center justify-center font-bold text-xl mb-4 border-4 border-white">1</div>
        <h4 class="font-bold text-primary">Konsultasi</h4>
      </div>
      <div class="flex flex-col items-center text-center relative bg-white md:px-4 mb-8 md:mb-0 w-full md:w-1/5">
        <div class="w-16 h-16 bg-primary text-secondary rounded-full flex items-center justify-center font-bold text-xl mb-4 border-4 border-white">2</div>
        <h4 class="font-bold text-primary">Formulasi & Sampling</h4>
      </div>
      <div class="flex flex-col items-center text-center relative bg-white md:px-4 mb-8 md:mb-0 w-full md:w-1/5">
        <div class="w-16 h-16 bg-primary text-secondary rounded-full flex items-center justify-center font-bold text-xl mb-4 border-4 border-white">3</div>
        <h4 class="font-bold text-primary">Urus Legalitas</h4>
      </div>
      <div class="flex flex-col items-center text-center relative bg-white md:px-4 mb-8 md:mb-0 w-full md:w-1/5">
        <div class="w-16 h-16 bg-primary text-secondary rounded-full flex items-center justify-center font-bold text-xl mb-4 border-4 border-white">4</div>
        <h4 class="font-bold text-primary">Produksi Massal</h4>
      </div>
      <div class="flex flex-col items-center text-center relative bg-white md:px-4 mb-8 md:mb-0 w-full md:w-1/5">
        <div class="w-16 h-16 bg-primary text-secondary rounded-full flex items-center justify-center font-bold text-xl mb-4 border-4 border-white">5</div>
        <h4 class="font-bold text-primary">Pengiriman</h4>
      </div>
    </div>
  </div>
</section>

<!-- CTA SECTION -->
<section class="py-20 bg-primary text-center">
  <div class="max-w-4xl mx-auto px-4 fade-in">
    <h2 class="text-3xl md:text-5xl font-extrabold text-white mb-6">Siap Wujudkan Brand Kosmetik Impian Anda?</h2>
    <p class="text-xl text-white/80 mb-10">Konsultasi gratis dengan tim ahli kami. Tidak ada kewajiban, hanya solusi terbaik untuk bisnis Anda.</p>
    <a href="https://wa.me/6283863670421" class="inline-flex justify-center items-center gap-2 bg-cta hover:bg-cta-hover text-white px-10 py-5 rounded-full font-bold text-lg transition-all shadow-xl shadow-cta/40 hover:scale-105">
      <span class="material-symbols-outlined">chat</span> Chat WhatsApp Sekarang
    </a>
  </div>
</section>

<!-- FOOTER -->
<footer class="bg-primary-dark pt-16 pb-8 border-t border-white/10" id="kontak">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
      <div class="md:col-span-2">
        <a href="#" class="font-bold text-2xl text-white flex items-center gap-2 mb-4">
          <span class="material-symbols-outlined text-secondary">science</span>
          Pabrik Kosmetik Tangerang
        </a>
        <p class="text-text-muted mb-6 max-w-sm">Jasa maklon kosmetik bersertifikat CPKB Grade A, BPOM, dan Halal MUI terpercaya di Indonesia.</p>
        <div class="flex gap-4">
          <!-- Social Icons Placeholder -->
          <div class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center text-white"><span class="material-symbols-outlined">camera_alt</span></div>
          <div class="w-10 h-10 bg-white/10 rounded-full flex items-center justify-center text-white"><span class="material-symbols-outlined">play_arrow</span></div>
        </div>
      </div>
      <div>
        <h4 class="text-white font-bold mb-4">Layanan</h4>
        <ul class="space-y-2 text-text-muted">
          <li><a href="#" class="hover:text-white transition-colors">Maklon Skincare</a></li>
          <li><a href="#" class="hover:text-white transition-colors">Private Label</a></li>
          <li><a href="#" class="hover:text-white transition-colors">OEM / ODM</a></li>
          <li><a href="#" class="hover:text-white transition-colors">Urus BPOM</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-white font-bold mb-4">Kontak Kami</h4>
        <ul class="space-y-4 text-text-muted">
          <li class="flex items-start gap-3">
            <span class="material-symbols-outlined text-secondary">location_on</span>
            Kawasan Industri Tangerang, Banten, Indonesia
          </li>
          <li class="flex items-center gap-3">
            <span class="material-symbols-outlined text-secondary">call</span>
            +62 838 6367 0421
          </li>
          <li class="flex items-center gap-3">
            <span class="material-symbols-outlined text-secondary">mail</span>
            halo@pabrikkosmetiktangerang.net
          </li>
        </ul>
      </div>
    </div>
    <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row justify-between items-center text-text-muted text-sm gap-4">
      <p>&copy; 2026 Pabrik Kosmetik Tangerang. All rights reserved.</p>
      <div class="flex gap-4">
        <a href="#" class="hover:text-white">Kebijakan Privasi</a>
        <a href="#" class="hover:text-white">Syarat & Ketentuan</a>
        <a href="#" class="hover:text-white">Sitemap</a>
      </div>
    </div>
  </div>
</footer>

<!-- FLOATING WA BUTTON -->
<a href="https://wa.me/6283863670421" target="_blank" class="fixed bottom-6 right-6 z-50 w-16 h-16 bg-cta rounded-full flex items-center justify-center shadow-lg shadow-cta/50 hover:scale-110 transition-transform hover:bg-cta-hover">
  <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" fill="white" class="w-8 h-8">
    <path d="M16 0C7.163 0 0 7.163 0 16c0 2.822.736 5.469 2.027 7.769L0 32l8.469-2.015A15.93 15.93 0 0016 32c8.837 0 16-7.163 16-16S24.837 0 16 0zm0 29.333a13.27 13.27 0 01-6.771-1.853l-.485-.289-5.025 1.196 1.217-4.892-.317-.502A13.267 13.267 0 012.667 16C2.667 8.636 8.636 2.667 16 2.667S29.333 8.636 29.333 16 23.364 29.333 16 29.333zm7.27-9.87c-.398-.199-2.355-1.162-2.72-1.294-.365-.133-.631-.199-.897.199-.265.398-1.029 1.294-1.261 1.56-.232.265-.465.298-.863.1-.398-.199-1.682-.62-3.204-1.977-1.184-1.056-1.983-2.36-2.215-2.758-.232-.398-.025-.613.175-.811.179-.178.398-.465.597-.697.199-.232.265-.398.398-.664.133-.265.066-.497-.033-.697-.1-.199-.897-2.162-1.229-2.96-.324-.776-.652-.671-.897-.683l-.764-.013c-.265 0-.697.1-1.062.497-.365.398-1.394 1.362-1.394 3.32 0 1.959 1.427 3.851 1.626 4.117.199.265 2.809 4.29 6.808 6.016.951.41 1.693.655 2.272.839.954.304 1.822.261 2.509.158.765-.114 2.355-.963 2.688-1.893.332-.93.332-1.727.232-1.893-.1-.166-.365-.265-.763-.464z"/>
  </svg>
</a>

<!-- LOCAL BUSINESS SCHEMA -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness","Organization"],
  "name": "Pabrik Kosmetik Tangerang",
  "url": "https://pabrikkosmetiktangerang.net",
  "telephone": "+6283863670421",
  "email": "halo@pabrikkosmetiktangerang.net",
  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Tangerang",
    "addressRegion": "Banten",
    "addressCountry": "ID"
  },
  "areaServed": ["Tangerang","Tangerang Selatan","Jakarta","Bogor","Depok","Bekasi","Indonesia"],
  "knowsAbout": ["Maklon Kosmetik","Contract Manufacturing","Private Label","CPKB","BPOM","Halal Kosmetik"],
  "serviceType": ["Maklon Kosmetik","Contract Manufacturing","Private Label","OEM","ODM","Pengurusan BPOM"]
}
</script>

<!-- SCRIPTS -->
<script>
  // Navbar scroll effect
  window.addEventListener('scroll', () => {
    const nav = document.getElementById('navbar');
    if (window.scrollY > 20) {
      nav.classList.add('shadow-md');
    } else {
      nav.classList.remove('shadow-md');
    }
  });

  // Fade in animation
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));
</script>
</body>
</html>\`;

fs.writeFileSync(targetFile, htmlContent, 'utf8');
console.log('Successfully wrote index.html');
