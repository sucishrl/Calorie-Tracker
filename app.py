import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calorie Tracker", layout="wide", page_icon="🎀")

if "step" not in st.session_state: st.session_state.step = 1
if "diary" not in st.session_state: st.session_state.diary = []
if "exercise" not in st.session_state: st.session_state.exercise = []

bg_patterns = {
    1: "https://www.transparenttextures.com/patterns/healthy-food.png", 
    2: "https://www.transparenttextures.com/patterns/pinstripe.png",     
    3: "https://www.transparenttextures.com/patterns/restaurant.png",    
    4: "https://www.transparenttextures.com/patterns/pyramid.png",       
    5: "https://www.transparenttextures.com/patterns/skulls.png"         
}

bg_gradients = {
    1: "linear-gradient(180deg, #ff9a9e 0%, #fad0c4 100%)", 
    2: "linear-gradient(180deg, #a1c4fd 0%, #c2e9fb 100%)", 
    3: "linear-gradient(180deg, #f6d365 0%, #fda085 100%)", 
    4: "linear-gradient(180deg, #84fab0 0%, #8fd3f4 100%)", 
    5: "linear-gradient(180deg, #cfd9df 0%, #e2ebf0 100%)"  
}

current_pattern = bg_patterns.get(st.session_state.step)
current_grad = bg_gradients.get(st.session_state.step)

st.markdown(f"""
<style>
.stApp {{
    background-image: url("{current_pattern}"), {current_grad};
    background-attachment: fixed;
}}
.main .block-container {{
    background-color: rgba(255, 255, 255, 0.9);
    border-radius: 30px;
    padding: 50px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}}
.big-title {{
    text-align: center; color: white;
    background: linear-gradient(90deg, #ff4d94, #ff85b3);
    padding: 30px; border-radius: 30px;
    font-size: 50px; font-weight: bold;
    border: 5px dashed white; margin-bottom: 20px;
}}
.stButton>button {{
    width: 100%; background: linear-gradient(90deg, #ff4d94, #ff85b3) !important;
    color: white !important; border-radius: 20px !important;
    height: 55px; font-weight: bold !important; border: none !important;
}}
</style>
""", unsafe_allow_html=True)

foods = [
    {"name": "Nasi Putih", "cal": 175, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Merah", "cal": 165, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Kuning", "cal": 180, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Kentang Rebus", "cal": 130, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Ubi Rebus", "cal": 160, "unit": "Porsi", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Roti Putih", "cal": 80, "unit": "Lembar", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Roti Gandum", "cal": 90, "unit": "Lembar", "cat": "Makanan", "category": "Karbohidrat"},
    {"name": "Nasi Ayam Geprek", "cal": 550, "unit": "Porsi", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ayam Goreng", "cal": 250, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ayam Panggang", "cal": 190, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Daging Sapi", "cal": 270, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ikan Goreng", "cal": 220, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Ikan Tuna", "cal": 180, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Salmon", "cal": 208, "unit": "Potong", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Cumi", "cal": 92, "unit": "Porsi", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Telur Rebus", "cal": 70, "unit": "Butir", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Telur Dadar", "cal": 90, "unit": "Butir", "cat": "Makanan", "category": "Protein Hewani"},
    {"name": "Capcay", "cal": 95, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sayur Asem", "cal": 80, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sayur Lodeh", "cal": 160, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sayur Sop", "cal": 70, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sayur Supa (Jamur)", "cal": 35, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Gulai Jengkol", "cal": 190, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Kangkung Tumis", "cal": 45, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Tumis Toge", "cal": 40, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Bayam Bening", "cal": 25, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Wortel Rebus", "cal": 40, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Brokoli Rebus", "cal": 55, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Brokoli Putih (Kembang Kol)", "cal": 25, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Labu Siam Rebus", "cal": 30, "unit": "Buah", "cat": "Makanan", "category": "Sayur"},
    {"name": "Pare Tumis", "cal": 55, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Sawi Putih", "cal": 15, "unit": "Mangkok", "cat": "Makanan", "category": "Sayur"},
    {"name": "Terong Balado", "cal": 110, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Orak Arik Buncis", "cal": 85, "unit": "Porsi", "cat": "Makanan", "category": "Sayur"},
    {"name": "Tomat", "cal": 22, "unit": "Buah", "cat": "Makanan", "category": "Sayur"},
    {"name": "Timun", "cal": 15, "unit": "Buah", "cat": "Makanan", "category": "Sayur"},
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
    {"name": "Alpukat", "cal": 234, "unit": "Buah", "cat": "Makanan", "category": "Buah"},
    {"name": "Burger", "cal": 295, "unit": "Porsi", "cat": "Makanan", "category": "Junk Food"},
    {"name": "Pizza", "cal": 285, "unit": "Slice", "cat": "Makanan", "category": "Junk Food"},
    {"name": "Fried Chicken", "cal": 320, "unit": "Potong", "cat": "Makanan", "category": "Junk Food"},
    {"name": "French Fries", "cal": 312, "unit": "Porsi", "cat": "Makanan", "category": "Junk Food"},
    {"name": "Hot Dog", "cal": 250, "unit": "Porsi", "cat": "Makanan", "category": "Junk Food"},
    {"name": "Donut", "cal": 250, "unit": "Pcs", "cat": "Makanan", "category": "Junk Food"},
    {"name": "Mie Instan", "cal": 380, "unit": "Bungkus", "cat": "Makanan", "category": "Lainnya"},
    {"name": "Bakso", "cal": 250, "unit": "Mangkok", "cat": "Makanan", "category": "Lainnya"},
    {"name": "Nasi Padang", "cal": 650, "unit": "Porsi", "cat": "Makanan", "category": "Lainnya"},
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
exercises = [
    {"name": "Tidak Olahraga", "burn_rate": 0},
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


if st.session_state.step == 1:
    st.markdown('<div class="big-title">🎀 Calorie Tracker 🎀</div>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>Halo! Selamat Datang ✨</h2>", unsafe_allow_html=True)
    if st.button("Mulai Sekarang 🚀"):
        st.session_state.step = 2
        st.rerun()

elif st.session_state.step == 2:
    st.header("👤 Profil & Data Diri")
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Jenis Kelamin", ["Perempuan", "Laki-laki"])
        weight = st.number_input("Berat Badan (kg)", 30, 200, 55)
    with col2:
        height = st.number_input("Tinggi Badan (cm)", 100, 250, 160)
        age = st.number_input("Usia", 5, 100, 20)
    
    tdee = (10 * weight) + (6.25 * height) - (5 * age) + (5 if gender == "Laki-laki" else -161)
    st.session_state.target = tdee * 1.375
    
    st.info(f"Target Harian Kamu: {int(st.session_state.target)} kcal")
    if st.button("Lanjut ke Catat Makanan 📔"):
        st.session_state.step = 3
        st.rerun()

elif st.session_state.step == 3:
    st.header("📔 Food Diary")
    waktu = st.selectbox("Waktu Makan", ["Sarapan", "Makan Siang", "Makan Malam", "Cemilan"])
    kat = st.radio("Kategori", ["Makanan", "Minuman"], horizontal=True)
    pilihan = st.selectbox(f"Pilih {kat}", sorted([f["name"] for f in foods if f["cat"] == kat]))
    item = next(f for f in foods if f["name"] == pilihan)
    porsi = st.number_input(f"Jumlah ({item['unit']})", 0.5, 10.0, 1.0)
    
    if st.button("➕ Tambah Makanan"):
        st.session_state.diary.append({"time": waktu, "name": pilihan, "cal": item["cal"] * porsi})
        st.success(f"{pilihan} Berhasil dicatat!")

    if st.button("Lanjut ke Aktivitas 🏃"):
        st.session_state.step = 4
        st.rerun()

elif st.session_state.step == 4:
    st.header("🏃 Aktivitas")
    pilihan_ex = st.selectbox("Pilih Olahraga", [ex["name"] for ex in exercises])
    burn = 0
    if pilihan_ex != "Tidak Olahraga":
        durasi = st.number_input("Durasi (Menit)", 1, 300, 30)
        data_ex = next(ex for ex in exercises if ex["name"] == pilihan_ex)
        burn = int((data_ex["burn_rate"] / 30) * durasi)
        st.info(f"Kalori terbakar: {burn} kcal")
    
    if st.button("Lihat Dashboard Akhir! 📊"):
        st.session_state.exercise.append({"act": pilihan_ex, "burn": burn})
        st.session_state.step = 5
        st.rerun()

elif st.session_state.step == 5:
    st.header("📊 Dashboard Hasil")
    total_in = sum(item['cal'] for item in st.session_state.diary)
    total_out = sum(item['burn'] for item in st.session_state.exercise)
    remaining = st.session_state.target - (total_in - total_out)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Masuk", f"{int(total_in)} kcal")
    col2.metric("Keluar", f"{int(total_out)} kcal")
    col3.metric("Sisa Kuota", f"{int(remaining)} kcal")

    if st.session_state.diary:
        st.write("### Grafik Konsumsi Kalori")
        df = pd.DataFrame(st.session_state.diary)
        st.bar_chart(df.groupby('name')['cal'].sum(), color="#ff4d94")

    if st.button("Reset & Mulai Lagi 🔄"):
        st.session_state.step = 1
        st.session_state.diary = []
        st.session_state.exercise = []
        st.rerun()
