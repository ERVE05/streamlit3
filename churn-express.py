import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st
import sklearn.tree
# Chargez le modèle depuis le fichier

st.title("prediction du depart des clients")
st.write("Cette application permet de savoir si le client va quitter l'opérateur.\n")

# Chargez le modèle depuis le fichier
#with open('clf_churn.pkl', 'rb') as fichier:
     #model = pickle.load(fichier)

#pour la prediction
def predict(feature):
    prediction = model.predict(feature)
    return prediction[0]
def main():


    MONTANT = st.number_input ("Entrez le montant de recharge ", min_value= 1.0, max_value=470000.0, value=45000.0)
    FREQUENCE_RECH = st.number_input ("nombre de rechargement ", min_value= 1.0, max_value=133.0, value=50.0)
    DATA_VOLUME = st.number_input ("Entrez le nombre de connexions ", min_value= 0.0, max_value=2000000.0, value=45000.0)
    ON_NET  = st.number_input ("Le nombre d'appel inter expresso ", min_value= 0.0, max_value=60000.0, value=4000.0)
    ORANGE = st.number_input ("Le nombre d'appel vers Orange ", min_value=0.0, max_value=25000.0, value=4000.0)
    TIGO = st.number_input ("Le nombre d'appel vers TIGO", min_value=0.0, max_value=5000.0, value=450.0)
    ZONE1 = st.number_input ("Le nombre d'appel vers Zone1 ", min_value=0.0, max_value=5000.0, value=450.0)
    ZONE2 = st.number_input ("Le nombre d'appel vers Zone2", min_value=0.0, max_value=4000.0, value=45.0)
    REGULARITY = st.number_input ("Le nombre de fois que le client est actif ", min_value=1.0, max_value=70.0, value=45.0)
    FREQ_TOP_PACK = st.number_input ("nombre de fois que le client a activé les pack", min_value=1.0, max_value=715.0, value=250.0)

    features = {
        'MONTANT': [MONTANT],
        'FREQUENCE_RECH': [FREQUENCE_RECH],
        'DATA_VOLUME': [DATA_VOLUME],
        'ON_NET': [ON_NET],
        'ORANGE': [ORANGE],
        'TIGO': [TIGO],
        'ZONE1': [ZONE1],
        'ZONE2': [ZONE2],
        'REGULARITY': [REGULARITY],
        'FREQ_TOP_PACK': [FREQ_TOP_PACK]
    }
    df_input = pd.DataFrame(features)


    if st.button('Predire'):
        pred = predict(df_input)
        st.write(f'predict: {"Yes" if pred == 1 else "No"}')

if __name__ == '__main__':
     main()
