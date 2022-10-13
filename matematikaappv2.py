import streamlit as st 

st.write("""
# MATEMATIKA ITU MUDAH !!!
DISINI KALIAN DAPAT MENGHITUNG LUAS DARI SEMUA BANGUN DATAR"""
)
st.write("""
# ________________________""")

option = st.sidebar.radio(
    'BANGUN DATAR : ',
    ('Persegi Panjang', 'Persegi', 'Segitiga', 'Jajargenjang', 'Trapesium', 'Belah Ketupat', 'Layang-layang', 'Lingkaran 1', 'Lingkaran 2')
)

if option == 'Persegi Panjang' or option == '':
    st.write("""# Persegi Panjang""")

    panjang = st.number_input("Masukkan Panjang", 0)
    lebar = st.number_input("Masukkan Lebar", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = panjang * lebar
        st.success(f"Luas persegi panjangnya adalah = {luas}")

elif option == 'Persegi' or option == '':
    st.write("""# Persegi""")

    sisi = st.number_input("Masukkan Sisi", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = sisi * sisi
        st.success(f"Luas perseginya adalah = {luas}")

elif option == 'Segitiga' or option == '':
    st.write("""# Segitiga""")

    alas = st.number_input("Masukkan Alas", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 1/2 * alas * tinggi
        st.success(f"Luas segitinganya adalah = {luas}")

        
elif option == 'Jajargenjang' or option == '':
    st.write("""# Jajargenjang""")

    alas = st.number_input("Masukkan Alas", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = alas * tinggi
        st.success(f"Luas jajargenjangnya adalah = {luas}")

elif option == 'Trapesium' or option == '':
    st.write("""# Trapesium""")

    sisiA = st.number_input("Masukkan Sisi A", 0)
    sisiB = st.number_input("Masukkan Sisi B", 0)
    tinggi = st.number_input("Masukkan Tinggi", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 1/2 * (sisiA + sisiB) * tinggi
        st.success(f"Luas trapesiumnya adalah = {luas}")

elif option == 'Belah Ketupat' or option == '':
    st.write("""# Belah Ketupat""")

    d1 = st.number_input("Masukkan Diagonal 1", 0)
    d2 = st.number_input("Masukkan Diagonal 2", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 1/2 * d1 * d2
        st.success(f"Luas belah ketupatnya adalah = {luas}")

elif option == 'Layang-layang' or option == '':
    st.write("""# Layang-layang""")

    d1 = st.number_input("Masukkan Diagonal 1", 0)
    d2 = st.number_input("Masukkan Diagonal 2", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 1/2 * d1 * d2
        st.success(f"Luas layang-layangnya adalah = {luas}")

elif option == 'Lingkaran 1' or option == '':
    st.write("""# Lingkaran 1
    GUNAKAN RUMUS LINGKARAN 1 INI UNTUK PHI 22/7""")

    r = st.number_input("Masukkan Jari-jari", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 22/7 * r * r
        st.success(f"Luas lingkarannya adalah = {luas}")

elif option == 'Lingkaran 2' or option == '':
    st.write("""# Lingkaran 2
    GUNAKAN RUMUS LINGKARAN 2 INI UNTUK PHI 3,14""")

    r = st.number_input("Masukkan Jari-jari", 0)
    hitung = st.button("Hitung Luas")

    if hitung:
        luas = 3.14 * (r * r)
        st.success(f"Luas lingkarannya adalah = {luas}")