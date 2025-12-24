import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calorie Tracker", layout="wide", page_icon="🎀")

st.markdown("""
<style>
.stApp {
    background-image: url("https://www.transparenttextures.com/patterns/food.png"), 
                      linear-gradient(180deg, #ffe6ef 0%, #fff5f8 100%);
    background-attachment: fixed;
}
.main .block-container {
    background-color: rgba(255, 255, 255, 0.8); 
    border-radius: 30px;
    padding: 40px;
    margin-top: 20px;
    box-shadow: 0 10px 30px rgba(255, 182, 193, 0.3);
}
.ribbon {
    background: #ff85b3; color: white; padding: 20px; border-radius: 25px;
    text-align: center; font-size: 32px; font-weight: bold;
    box-shadow: 0 6px 15px rgba(255,105,180,0.4); 
    margin-bottom: 30px;
    border: 3px dashed rgba(255,255,255,0.5);
}
section[data-testid="stSidebar"] { 
    background: linear-gradient(180deg, #ffb6c1, #ffd6e6); 
}
.card {
    background-color: #ffffff !important; 
    padding: 15px; 
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(255,182,193,0.3); 
    margin-bottom: 15px;
    border-left: 5px solid #ff85b3;
    color: #000000 !important; /* INI SUPAYA TEKS JADI HITAM PEKAT */
}
.card b {
    color: #ff4d94 !important; /* INI SUPAYA JUDUL MAKANAN PINK TUA */
}
</style>
""", unsafe_allow_html=True)

foods = [
    {"name": "Nasi Putih", "cal": 175, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Merah", "cal": 165, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Kuning", "cal": 180, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Kentang Rebus", "cal": 130, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Ubi Rebus", "cal": 160, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Roti Putih", "cal": 80, "unit": "Lembar", "type": "int", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Roti Gandum", "cal": 90, "unit": "Lembar", "type": "int", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Ayam Goreng", "cal": 250, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ayam Panggang", "cal": 190, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Daging Sapi", "cal": 270, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ikan Goreng", "cal": 220, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ikan Tuna", "cal": 180, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Salmon", "cal": 208, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Cumi", "cal": 92, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Telur Rebus", "cal": 70, "unit": "Butir", "type": "int", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Telur Dadar", "cal": 90, "unit": "Butir", "type": "int", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Apel", "cal": 95, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Pisang", "cal": 110, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Mangga", "cal": 135, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Jeruk", "cal": 60, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Anggur", "cal": 62, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Semangka", "cal": 45, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Stroberi", "cal": 50, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Nanas", "cal": 82, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Pepaya", "cal": 59, "unit": "Potong", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Kiwi", "cal": 61, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Durian", "cal": 357, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Salak", "cal": 82, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Rambutan", "cal": 68, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Manggis", "cal": 73, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Kelapa", "cal": 283, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Sirsak", "cal": 66, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Jambu Air", "cal": 46, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Buah Naga", "cal": 60, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Blueberry", "cal": 84, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Buah"},
    {"name": "Alpukat", "cal": 234, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Buah"},
    {"name": "Bayam", "cal": 25, "unit": "Mangkok", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Kangkung", "cal": 35, "unit": "Mangkok", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Wortel", "cal": 40, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Tomat", "cal": 22, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Sayur"},
    {"name": "Buncis", "cal": 44, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Kol", "cal": 25, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sawi", "cal": 23, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Selada", "cal": 15, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Terong", "cal": 35, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Singkong", "cal": 160, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Timun", "cal": 15, "unit": "Buah", "type": "int", "cat": "Makanan", "category": "Sayur"},
    {"name": "Brokoli", "cal": 55, "unit": "Mangkok", "type": "decimal", "cat": "Makanan", "category": "Sayur"},
    {"name": "Burger", "cal": 295, "unit": "Porsi", "type": "int", "cat": "Makanan", "category": "Cepat Saji"},
    {"name": "Pizza", "cal": 285, "unit": "Slice", "type": "int", "cat": "Makanan", "category": "Cepat Saji"},
    {"name": "Fried Chicken", "cal": 320, "unit": "Potong", "type": "int", "cat": "Makanan", "category": "Cepat Saji"},
    {"name": "Mie Instan", "cal": 380, "unit": "Bungkus", "type": "int", "cat": "Makanan", "category": "Makanan Lainnya"},
    {"name": "Bakso", "cal": 250, "unit": "Mangkok", "type": "decimal", "cat": "Makanan", "category": "Makanan Lainnya"},
    {"name": "Nasi Padang", "cal": 650, "unit": "Porsi", "type": "decimal", "cat": "Makanan", "category": "Makanan Lainnya"},
    {"name": "Kopi Americano", "cal": 5, "unit": "Cangkir", "type": "decimal", "cat": "Minuman", "category": "Kopi"},
    {"name": "Kopi Susu", "cal": 120, "unit": "Cangkir", "type": "decimal", "cat": "Minuman", "category": "Kopi"},
    {"name": "Air Putih", "cal": 0, "unit": "Gelas", "type": "int", "cat": "Minuman", "category": "Dasar"},
    {"name": "Jus Apel", "cal": 120, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus"},
    {"name": "Jus Pisang", "cal": 150, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus"},
    {"name": "Jus Mangga", "cal": 130, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus"},
    {"name": "Jus Wortel", "cal": 80, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus Sayur"},
    {"name": "Jus Tomat Mix Wortel", "cal": 75, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus Mix"},
    {"name": "Jus Timun Mix Pir", "cal": 90, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus Mix"},
    {"name": "Jus Buah Naga Mix Pisang", "cal": 160, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus Mix"},
    {"name": "Jus Buah Naga Mix Stroberi", "cal": 110, "unit": "Gelas", "type": "decimal", "cat": "Minuman", "category": "Jus Mix"},
]

exercises = [
    {"name": "Angkat Beban (30 mnt)", "burn_rate": 150},
    {"name": "Lari (30 mnt)", "burn_rate": 300},
    {"name": "Jalan Santai (30 mnt)", "burn_rate": 150},
    {"name": "Berenang (30 mnt)", "burn_rate": 400},
    {"name": "Badminton (30 mnt)", "burn_rate": 300},
    {"name": "Padel (30 mnt)", "burn_rate": 300},
    {"name": "Basket (30 mnt)", "burn_rate": 650},
    {"name": "Sepak bola (30 mnt)", "burn_rate": 300},
    {"name": "Golf (30 mnt)", "burn_rate": 100}
]

if "diary" not in st.session_state: st.session_state.diary = []
if "exercise" not in st.session_state: st.session_state.exercise = []

with st.sidebar:
    st.title("🎀 Profil & Menu")
    st.subheader("👤 Data Pengguna")
    gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
    weight = st.number_input("Berat Badan (kg)", 30, 200, 55)
    height = st.number_input("Tinggi Badan (cm)", 100, 250, 160)
    age = st.number_input("Usia", 5, 100, 20)
    
    bmi = weight / ((height/100)**2)
    st.write(f"**BMI Kamu:** {bmi:.1f}")
    
    if gender == "Laki-laki":
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    else:
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    
    tdee = bmr * 1.375
    st.info(f"Kebutuhan Kalori Harian: **{int(tdee)} kcal**")
    
    st.divider()
    menu = st.radio("Pindah Halaman:", ["🏠 Dashboard", "🍎 Database Makanan", "📔 Food Diary", "🏃 Aktivitas"])

st.markdown('<div class="ribbon">🎀 Calorie Tracker 🎀</div>', unsafe_allow_html=True)

if menu == "🏠 Dashboard":
    st.subheader("📊 Ringkasan Hari Ini")
    total_in = sum(item['cal'] for item in st.session_state.diary)
    total_out = sum(item['burn'] for item in st.session_state.exercise)
    remaining = tdee - (total_in - total_out)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Kalori Masuk", f"{total_in} kcal")
    col2.metric("Kalori Keluar", f"{total_out} kcal")
    col3.metric("Sisa Kuota", f"{int(remaining)} kcal")

    progress = min(total_in / tdee, 1.0) if tdee > 0 else 0
    st.write(f"**Progress Kuota Kalori Harian ({int(progress*100)}%)**")
    st.progress(progress)

    if st.session_state.diary:
        st.write("### 📈 Grafik Kalori per Waktu Makan")
        df = pd.DataFrame(st.session_state.diary)
        chart_data = df.groupby('time')['cal'].sum()
        st.bar_chart(chart_data)
    else:
        st.info("Belum ada data konsumsi. Silakan catat makanan kamu di menu Food Diary!")

elif menu == "🍎 Database Makanan":
    st.header("🍎 Daftar Nutrisi Lengkap")
    tab1, tab2 = st.tabs(["🍴 Makanan", "🥤 Minuman"])
    with tab1:
        for f in [x for x in foods if x["cat"] == "Makanan"]:
            st.markdown(f"<div class='card'><b>{f['name']}</b> ({f['category']})<br>{f['cal']} kkal per {f['unit']}</div>", unsafe_allow_html=True)
    with tab2:
        for f in [x for x in foods if x["cat"] == "Minuman"]:
            st.markdown(f"<div class='card'><b>{f['name']}</b> ({f['category']})<br>{f['cal']} kkal per {f['unit']}</div>", unsafe_allow_html=True)

elif menu == "📔 Food Diary":
    st.header("📔 Catat Konsumsi")
    waktu_makan = st.selectbox("Pilih Waktu", ["Sarapan", "Makan Siang", "Makan Malam", "Cemilan"])
    kategori_pilihan = st.radio("Kategori", ["Makanan", "Minuman"], horizontal=True)
    
    pilihan_list = sorted([f["name"] for f in foods if f["cat"] == kategori_pilihan])
    pilihan = st.selectbox(f"Pilih {kategori_pilihan}", pilihan_list)
    item_data = next(f for f in foods if f["name"] == pilihan)
    
    porsi = st.number_input(f"Jumlah ({item_data['unit']})", min_value=0.1 if item_data["type"]=="decimal" else 1.0, step=0.1 if item_data["type"]=="decimal" else 1.0, value=1.0)
        
    if st.button("➕ Tambahkan"):
        st.session_state.diary.append({"time": waktu_makan, "name": pilihan, "cal": item_data["cal"] * porsi})
        st.success(f"{pilihan} ({porsi} {item_data['unit']}) berhasil dicatat!")

elif menu == "🏃 Aktivitas":
    st.header("🏃 Log Olahraga")
    pilihan_ex = st.selectbox("Pilih Olahraga", [ex["name"] for ex in exercises])
    durasi = st.number_input("Durasi (Menit)", 1, 300, 30)
    data_ex = next(ex for ex in exercises if ex["name"] == pilihan_ex)
    burn = int((data_ex["burn_rate"] / 30) * durasi)
    
    st.info(f"🔥 Estimasi terbakar: {burn} kcal")
    if st.button("Simpan Aktivitas"):
        st.session_state.exercise.append({"act": pilihan_ex, "burn": burn})

        st.balloons()
