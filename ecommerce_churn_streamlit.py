# Deploy Churn Predictor

# ======================================================
import pandas as pd
import numpy as np

from xgboost.sklearn import XGBClassifier
import streamlit as st
import pickle


# ======================================================

# Judul Utama
st.write('''
# CHURN CUSTOMER PREDICTOR
''')

# sidebar
st.sidebar.header("Please input customer's features")


# ======================================================

# buat function untuk user input feature
def user_input_feature():

    # st.sidebar.slider('label', min, mav, value)
    # st.sidebar.selectbox('label', (cat1,cat2,cat3))

    # numerical: slider atau number input
    Tenure = st.sidebar.number_input('Tenure', min_value=1, max_value=61, value=5, step=1)
    WarehouseToHome = st.sidebar.number_input('WarehouseToHome', 1, 33, 15, 1)
    NumberOfDeviceRegistered = st.sidebar.number_input('NumberOfDeviceRegistered', 1, 6, 3, 1)
    DaySinceLastOrder = st.sidebar.number_input('DaySinceLastOrder', 1,30,3,1)
    CashbackAmount = st.sidebar.number_input('CashbackAmount', 0,500,100,1)
    NumberOfAddress = st.sidebar.number_input('NumberOfAddress', 1,22,5,1)


    # categorical: selectbox
    MaritalStatus = st.sidebar.selectbox('MaritalStatus', ('Single','Married','Divorced'))
    Complain = st.sidebar.selectbox('Complain', (0,1))
    PreferedOrderCat = st.sidebar.selectbox('PreferedOrderCat',('Laptop & Accessory','Mobile Phone','Fashion','Grocery','Others'))
    SatisfactionScore = st.sidebar.selectbox('SatisfactionScore', (1,2,3,4,5))

    df = pd.DataFrame()
    df['Tenure'] = [Tenure]
    df['WarehouseToHome'] = [WarehouseToHome]
    df['NumberOfDeviceRegistered'] = [NumberOfDeviceRegistered]
    df['MaritalStatus'] = [MaritalStatus]
    df['PreferedOrderCat'] = [PreferedOrderCat]
    df['SatisfactionScore'] = [SatisfactionScore]
    df['NumberOfAddress'] = [NumberOfAddress]
    df['CashbackAmount'] = [CashbackAmount]
    df['Complain'] = [Complain]
    df['DaySinceLastOrder'] = [DaySinceLastOrder]

    return df

df_customer = user_input_feature()
df_customer.index = ['value']

# predict a customer
model_loaded = pickle.load(open('ecommerce_churn_model.sav','rb'))

kelas = model_loaded.predict(df_customer)



# ======================================================

# buat 2 container di kiri dan kanan
col1, col2 = st.columns(2)

# bagian kiri (col1)
with col1:
    # Tampilkan dataframe hasil user input (customer feature)
    st.subheader("Customer Features:")
    st.write(df_customer.transpose())


# bagian kanan (col2)
with col2:
    st.write("0 means No")
    st.write("1 means Yes")

    # Tampilkan hasil prediksi
    st.subheader("Prediction")

    if kelas == 1:
        st.write('Class 1: this customer will CHURN')
    else:
        st.write('Class 0: this customer will STAY')