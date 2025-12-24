import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calorie Tracker", layout="wide", page_icon="🎀")

# Inisialisasi session state agar data tidak hilang saat pindah halaman
if "diary" not in st.session_state: st.session_state.diary = []
if "exercise" not in st.session_state: st.session_state.exercise = []
if "menu_pilihan" not in st.session_state: st.session_state.menu_pilihan = "🏠 Dashboard"

st.markdown("""
<style>
.stApp {
    background-image: url("https://www.transparenttextures.com/patterns/food.png"), 
                      linear-gradient(180deg, #ffe6ef 0%, #fff5f8 100%);
    background-attachment: fixed;
}

/* 1. PERBAIKAN SEMUA KOTAK INPUT (BIAR PUTIH & TEKS HITAM JELAS) */
div[data-baseweb="select"] > div, 
div[data-testid="stNumberInput"] div[data-baseweb="input"],
div[data-baseweb="base-input"] {
    background-color: #ffffff !important;
    border: 2px solid #ffb6c1 !important;
    border-radius: 10px;
}

div[data-baseweb="select"] div, 
div[data-testid="stNumberInput"] input {
    color: #000000 !important;
    -webkit-text-fill-color: #000000 !important;
    font-weight: 500;
}

/* Mengatur warna tombol +/- pada input angka */
div[data-testid="stNumberInput"] button {
    background-color: #ffffff !important;
    color: #ff4d94 !important;
}

/* 2. PERBAIKAN PANAH SIDEBAR (BIAR PINK CERAH) */
button[aria-label="Open sidebar"] svg, 
button[aria-label="Close sidebar"] svg,
button[data-testid="sidebar-button"] svg {
    fill: #ff4d94 !important;
    width: 35px;
    height: 35px;
}

/* 3. SIDEBAR STYLING */
section[data-testid="stSidebar"] { 
    background: linear-gradient(180deg, #ffb6c1, #ffd6e6) !important; 
}
section[data-testid="stSidebar"] label, section[data-testid="stSidebar"] p {
    color: #000000 !important;
    font-weight: bold !important;
}

/* 4. TAMPILAN UTAMA */
.ribbon {
    background: #ff85b3; color: white !important; padding: 20px; border-radius: 25px;
    text-align: center; font-size: 32px; font-weight: bold;
    box-shadow: 0 6px 15px rgba(255,105,180,0.4); margin-bottom: 30px;
    border: 3px dashed rgba(255,255,255,0.5);
}
.main .block-container {
    background-color: rgba(255, 255, 255, 0.8); 
    border-radius: 30px; padding: 40px; margin-top: 20px;
}
[data-testid="stMetricValue"] { color: #ff4d94 !important; font-weight: bold !important; }

.card {
    background-color: #ffffff !important; padding: 15px; border-radius: 20px;
    box-shadow: 0 4px 15px rgba(255,182,193,0.3); margin-bottom: 15px;
    border-left: 5px solid #ff85b3; color: #000000 !important;
}
.card b { color: #ff4d94 !important; }
</style>
""", unsafe_allow_html=True)

# DAFTAR MAKANAN LENGKAP
foods = [
    {"name": "Nasi Putih", "cal": 175, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Merah", "cal": 165, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Kuning", "cal": 180, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Kentang Rebus", "cal": 130, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Ubi Rebus", "cal": 160, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Roti Putih", "cal": 80, "unit": "Lembar", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Roti Gandum", "cal": 90, "unit": "Lembar", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Ayam Goreng", "cal": 250, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ayam Panggang", "cal": 190, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Daging Sapi", "cal": 270, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ikan Goreng", "cal": 220, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ikan Tuna", "cal": 180, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Salmon", "cal": 208, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Cumi", "cal": 92, "unit": "Porsi", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Telur Rebus", "cal": 70, "unit": "Butir", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Telur Dadar", "cal": 90, "unit": "Butir", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Apel", "cal": 95, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Pisang", "cal": 110, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Mangga", "cal": 135, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Jeruk", "cal": 60, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Anggur", "cal": 62, "unit": "Porsi", "cat": "Makanan", "category": "Buah"},
    {"name": "Semangka", "cal": 45, "unit": "Potong", "cat": "Makanan", "category": "Buah"},
    {"name": "Stroberi", "cal": 50, "unit": "Porsi", "cat": "Makanan", "category": "Buah"},
    {"name": "Nanas", "cal": 82, "unit": "Potong", "cat": "Makanan", "category": "Buah"},
    {"name": "Pepaya", "cal": 59, "unit": "Potong", "cat": "Makanan", "category": "Buah"},
    {"name": "Kiwi", "cal": 61, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Durian", "cal": 357, "unit": "Porsi", "cat": "Makanan", "category": "Buah"},
    {"name": "Salak", "cal": 82, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Rambutan", "cal": 68, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Manggis", "cal": 73, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Kelapa", "cal": 283, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Sirsak", "cal": 66, "unit": "Porsi", "cat": "Makanan", "category": "Buah"},
    {"name": "Jambu Air", "cal": 46, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Buah Naga", "cal": 60, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Blueberry", "cal": 84, "unit": "Porsi", "cat": "Makanan", "category": "Buah"},
    {"name": "Alpukat", "cal": 234, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Bayam", "cal": 25, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Kangkung", "cal": 35, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Wortel", "cal": 40, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Tomat", "cal": 22, "unit": "Buah", "cat": "Makanan", "category": "Sayur"},
    {"name": "Buncis", "cal": 44, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Kol", "cal": 25, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sawi", "cal": 23, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Selada", "cal": 15, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Terong", "cal": 35, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Singkong", "cal": 160, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Timun", "cal": 15, "unit": "Buah", "cat": "Makanan", "category": "Sayur"},
    {"name": "Brokoli", "cal": 55, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Burger", "cal": 295, "unit": "Porsi", "cat": "Makanan", "category": "Cepat Saji"},
    {"name": "Pizza", "cal": 285, "unit": "Slice", "cat": "Makanan", "category": "Cepat Saji"},
    {"name": "Fried Chicken", "cal": 320, "unit": "Potong", "cat": "Makanan", "category": "Cepat Saji"},
    {"name": "Mie Instan", "cal": 380, "unit": "Bungkus", "cat": "Makanan", "category": "Makanan Lainnya"},
    {"name": "Bakso", "cal": 250, "unit": "Mangkok", "cat": "Makanan", "category": "Makanan Lainnya"},
    {"name": "Nasi Padang", "cal": 650, "unit": "Porsi", "cat": "Makanan", "category": "Makanan Lainnya"},
    {"name": "Kopi Americano", "cal": 5, "unit": "Cangkir", "cat": "Minuman", "category": "Kopi"},
    {"name": "Kopi Susu", "cal": 120, "unit": "Cangkir", "cat": "Minuman", "category": "Kopi"},
    {"name": "Air Putih", "cal": 0, "unit": "Gelas", "cat": "Minuman", "category": "Dasar"},
    {"name": "Jus Apel", "cal": 120, "unit": "Gelas", "cat": "Minuman", "category": "Jus"},
    {"name": "Jus Pisang", "cal": 150, "unit": "Gelas", "cat": "Minuman", "category": "Jus"},
    {"name": "Jus Mangga", "cal": 130, "unit": "Gelas", "cat": "Minuman", "category": "Jus"},
    {"name": "Jus Wortel", "cal": 80, "unit": "Gelas", "cat": "Minuman", "category": "Jus Sayur"},
    {"name": "Jus Tomat Mix Wortel", "cal": 75, "unit": "Gelas", "cat": "Minuman", "category": "Jus Mix"},
    {"name": "Jus Timun Mix Pir", "cal": 90, "unit": "Gelas", "cat": "Minuman", "category": "Jus Mix"},
    {"name": "Jus Buah Naga Mix Pisang", "cal": 160, "unit": "Gelas", "cat": "Minuman", "category": "Jus Mix"},
    {"name": "Jus Buah Naga Mix Stroberi", "cal": 110, "unit": "Gelas", "cat": "Minuman", "category": "Jus Mix"},
]

# DAFTAR OLAHRAGA LENGKAP
exercises = [
    {"name": "Angkat Beban (30 mnt)", "burn_rate": 150},
    {"name": "Lari (30 mnt)", "burn_rate": 300},
    {"name": "Jalan Santai (30 mnt)", "burn_rate": 150},
    {"name": "Berenang (30 mnt)", "burn_rate": 400},
    {"name": "Badminton (30 mnt)", "burn_rate": 300},
    {"name": "Padel (30 mnt)", "burn_rate": 300},
    {"name": "Basket (30 mnt)", "burn_rate": 650},
    {"name": "Sepak bola (30 mnt)", "burn_rate": 300},
    {"name": "Golf(30 mnt)", "burn_rate": 100}
]

with st.sidebar:
    st.title("🎀 Profil & Menu")
    gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
    weight = st.number_input("Berat Badan (kg)", 30, 200, 55)
    height = st.number_input("Tinggi Badan (cm)", 100, 250, 160)
    age = st.number_input("Usia", 5, 100, 20)
    
    if gender == "Laki-laki":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    tdee = bmr * 1.375
    
    st.divider()
    list_menu = ["🏠 Dashboard", "🍎 Database Makanan", "📔 Food Diary", "🏃 Aktivitas"]
    idx_sekarang = list_menu.index(st.session_state.menu_pilihan)
    menu = st.radio("Pilih Halaman:", list_menu, index=idx_sekarang)
    st.session_state.menu_pilihan = menu

st.markdown('<div class="ribbon">🎀 Calorie Tracker 🎀</div>', unsafe_allow_html=True)

# HALAMAN DASHBOARD (HANYA MUNCUL JIKA DATA SUDAH LENGKAP)
if st.session_state.menu_pilihan == "🏠 Dashboard":
    st.subheader("📊 Ringkasan Hari Ini")
    
    if st.session_state.diary and st.session_state.exercise:
        total_in = sum(item['cal'] for item in st.session_state.diary)
        total_out = sum(item['burn'] for item in st.session_state.exercise)
        remaining = tdee - (total_in - total_out)
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Masuk", f"{int(total_in)} kcal")
        col2.metric("Keluar", f"{int(total_out)} kcal")
        col3.metric("Sisa", f"{int(remaining)} kcal")

        st.write("### 📈 Grafik Konsumsi")
        df = pd.DataFrame(st.session_state.diary)
        chart_data = df.groupby('time')['cal'].sum().reset_index()
        st.bar_chart(chart_data, x="time", y="cal", color="time", use_container_width=True)
    else:
        st.info("👋 Halo! Grafik Dashboard kamu masih kosong.")
        st.warning("Silakan isi **Food Diary** (makanan) dan **Aktivitas** (olahraga) terlebih dahulu agar ringkasannya muncul di sini!")

# HALAMAN DATABASE
elif st.session_state.menu_pilihan == "🍎 Database Makanan":
    st.header("🍎 Daftar Nutrisi")
    tab1, tab2 = st.tabs(["🍴 Makanan", "🥤 Minuman"])
    with tab1:
        for f in [x for x in foods if x["cat"] == "Makanan"]:
            st.markdown(f"<div class='card'><b>{f['name']}</b> ({f['category']})<br>{f['cal']} kkal / {f['unit']}</div>", unsafe_allow_html=True)
    with tab2:
        for f in [x for x in foods if x["cat"] == "Minuman"]:
            st.markdown(f"<div class='card'><b>{f['name']}</b><br>{f['cal']} kkal / {f['unit']}</div>", unsafe_allow_html=True)

# HALAMAN INPUT MAKANAN
elif st.session_state.menu_pilihan == "📔 Food Diary":
    st.header("📔 Catat Konsumsi")
    waktu = st.selectbox("Waktu", ["Sarapan", "Makan Siang", "Makan Malam", "Cemilan"])
    kat = st.radio("Kategori", ["Makanan", "Minuman"], horizontal=True)
    pilihan = st.selectbox(f"Pilih {kat}", sorted([f["name"] for f in foods if f["cat"] == kat]))
    item = next(f for f in foods if f["name"] == pilihan)
    porsi = st.number_input(f"Jumlah ({item['unit']})", 0.1, 10.0, 1.0)
    
    if st.button("➕ Tambahkan"):
        st.session_state.diary.append({"time": waktu, "name": pilihan, "cal": item["cal"] * porsi})
        st.success(f"Berhasil mencatat {pilihan}!")

# HALAMAN INPUT OLAHRAGA
elif st.session_state.menu_pilihan == "🏃 Aktivitas":
    st.header("🏃 Log Olahraga")
    pilihan_ex = st.selectbox("Pilih Olahraga", [ex["name"] for ex in exercises])
    durasi = st.number_input("Durasi (Menit)", 1, 300, 30)
    data_ex = next(ex for ex in exercises if ex["name"] == pilihan_ex)
    burn = int((data_ex["burn_rate"] / 30) * durasi)
    
    st.info(f"🔥 Estimasi kalori terbakar: {burn} kcal")
    if st.button("Simpan Aktivitas"):
        st.session_state.exercise.append({"act": pilihan_ex, "burn": burn})
        st.success("Aktivitas tersimpan! Silakan cek Dashboard jika sudah selesai input semua.")
