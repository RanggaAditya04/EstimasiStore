import pickle
import streamlit as st

model = pickle.load(open('Estimasi_Store.sav', 'rb'))

st.title('Estimasi Penjualan Supermarket')

Store_Sales = st.number_input('Input Penjualan Toko')
Daily_Customer_Count = st.number_input('Input Pembeli Harian')
Items_Available = st.number_input('Input Barang Yang Tersedia')

predict = ''

if st.button('Estimasi Penjualan Supermarket'):
    predict = model.predict(
        [[Store_Sales, Daily_Customer_Count, Items_Available]]
    )
    st.write ('Estimasi Jumlah Store Area di Setiap Supermarket : ', predict)