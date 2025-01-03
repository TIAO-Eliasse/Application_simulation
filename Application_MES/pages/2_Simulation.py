import streamlit as st
import pandas as pd
import numpy as np
import statsmodels.api as sm
import pandas as pd
from linearmodels.system import SUR
from statsmodels.tools import add_constant

st.write("Bienvenue dans la partie simulation")
from Accueil import data_dir
data_path=data_dir("base_final.xlsx")
base=pd.read_excel(data_path)

#base=pd.read_excel("base_final.xlsx")



# Définir les séries temporelles
Depense = pd.Series(base[' DEPT'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Investissement = pd.Series(base['TINV(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Taux_de_change = pd.Series(base['Tchange'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Recettes_totales = pd.Series(base['RECT'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Taux_de_chomage = pd.Series(base['CHO'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Inflation = pd.Series(base['INF'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Indice_prix = pd.Series(base['IPC'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Epargne = pd.Series(base['EPG'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Balance_exterieure = pd.Series(base['BLE'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Prix_petrole = pd.Series(base['PRP'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Produit_Interieur = pd.Series(base['TPIB'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Exportation = pd.Series(base['TEXP(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Importation = pd.Series(base['TIMP(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Masse_monetaire = pd.Series(base['MM(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Taux_population_active = pd.Series(base['TPOA(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
CDI = pd.Series(base['TCDI(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))
Taxe = pd.Series(base['Ttaxe(%)'].values, index=pd.date_range(start='2005', periods=len(base), freq='A'))

# Renommer les variables
TDEPT = Depense
TINV = Investissement
TCHE = Taux_de_change
TRECT = Recettes_totales
TCHO = Taux_de_chomage
INF = Inflation
IPC = Indice_prix
EPG = Epargne
BLE = Balance_exterieure
PRP = Prix_petrole
TPIB = Produit_Interieur
TEXP = Exportation
TIMP = Importation
MM = Masse_monetaire
TPOA = Taux_population_active
TCDI = CDI
TTaxe = Taxe

# Créer un DataFrame avec toutes les variables
data1 = pd.DataFrame({' DEPT': TDEPT, 'TINV': TINV, 'TCHE': TCHE, 'RECT': TRECT, 'TCHO': TCHO, 
    'INF': INF, 'PRP': PRP, 'TPIB': TPIB, 'TEXP': TEXP, 'TIMP': TIMP, 
    'MM': MM, 'TPOA': TPOA, 'TCDI': TCDI, 'TTaxe': TTaxe
})


import pandas as pd
import numpy as np



# Fonction pour créer un décalage (lag) d'une variable
def retarder(v, k=1):
    return np.concatenate([np.full(k, np.nan), v[:-k]])

# Décalages pour TCHO
TCHO_lag1 = retarder(TCHO, k=1)
TCHO_lag2 = retarder(TCHO, k=2)
TCHO_lag3 = retarder(TCHO, k=3)
TCHO_lag4 = retarder(TCHO, k=4)
TCHO_lag5 = retarder(TCHO, k=5)

# Décalages pour TPIB
TPIB_lag1 = retarder(TPIB, k=1)
TPIB_lag2 = retarder(TPIB, k=2)
TPIB_lag3 = retarder(TPIB, k=3)
TPIB_lag4 = retarder(TPIB, k=4)
TPIB_lag5 = retarder(TPIB, k=5)

# Décalages pour PRP
PRP_lag1 = retarder(PRP, k=1)
PRP_lag2 = retarder(PRP, k=2)
PRP_lag3 = retarder(PRP, k=3)
PRP_lag4 = retarder(PRP, k=4)
PRP_lag5 = retarder(PRP, k=5)

# Décalages pour TPOA
TPOA_lag1 = retarder(TPOA, k=1)
TPOA_lag2 = retarder(TPOA, k=2)
TPOA_lag3 = retarder(TPOA, k=3)
TPOA_lag4 = retarder(TPOA, k=4)
TPOA_lag5 = retarder(TPOA, k=5)

# Décalages pour MM
MM_lag1 = retarder(MM, k=1)
MM_lag2 = retarder(MM, k=2)
MM_lag3 = retarder(MM, k=3)
MM_lag4 = retarder(MM, k=4)
MM_lag5 = retarder(MM, k=5)

# Décalages pour TRECT
TRECT_lag1 = retarder(TRECT, k=1)
TRECT_lag2 = retarder(TRECT, k=2)
TRECT_lag3 = retarder(TRECT, k=3)

# Décalages pour TCDI
TCDI_lag1 = retarder(TCDI, k=1)
TCDI_lag2 = retarder(TCDI, k=2)
TCDI_lag3 = retarder(TCDI, k=3)
TCDI_lag4 = retarder(TCDI, k=4)
TCDI_lag5 = retarder(TCDI, k=5)

# Décalages pour INF
INF_lag1 = retarder(INF, k=1)
INF_lag2 = retarder(INF, k=2)

# Décalages pour TDEPT
TDEPT_lag1 = retarder(TDEPT, k=1)
TDEPT_lag2 = retarder(TDEPT, k=2)
TDEPT_lag3 = retarder(TDEPT, k=3)
TDEPT_lag4 = retarder(TDEPT, k=4)

# Décalages pour TINV
TINV_lag1 = retarder(TINV, k=1)
TINV_lag2 = retarder(TINV, k=2)
TINV_lag3 = retarder(TINV, k=3)
TINV_lag4 = retarder(TINV, k=4)
TINV_lag5 = retarder(TINV, k=5)

# Décalages pour TEXP
TEXP_lag1 = retarder(TEXP, k=1)
TEXP_lag2 = retarder(TEXP, k=2)
TEXP_lag3 = retarder(TEXP, k=3)
TEXP_lag4 = retarder(TEXP, k=4)

# Décalages pour TIMP
TIMP_lag1 = retarder(TIMP, k=1)
TIMP_lag2 = retarder(TIMP, k=2)
TIMP_lag3 = retarder(TIMP, k=3)
TIMP_lag4 = retarder(TIMP, k=4)
TIMP_lag5 = retarder(TIMP, k=5)

# Décalages pour TTaxe
TTaxe_lag1 = retarder(TTaxe, k=1)
TTaxe_lag2 = retarder(TTaxe, k=2)
TTaxe_lag3 = retarder(TTaxe, k=3)
TTaxe_lag4 = retarder(TTaxe, k=4)
TTaxe_lag5 = retarder(TTaxe, k=5)

# Créer le DataFrame avec les différentes variables décalées
base_modelisation = pd.DataFrame({
    'TCHO_lag1': TCHO_lag1, 'TCHO': TCHO, 'TCHO_lag2': TCHO_lag2, 'TCHO_lag3': TCHO_lag3,
    'TCHO_lag4': TCHO_lag4, 'TCHO_lag5': TCHO_lag5, 'TPIB': TPIB, 'TPIB_lag1': TPIB_lag1,
    'TPIB_lag2': TPIB_lag2, 'TPIB_lag3': TPIB_lag3, 'TPIB_lag4': TPIB_lag4, 'TPIB_lag5': TPIB_lag5,
    'PRP': PRP, 'PRP_lag1': PRP_lag1, 'PRP_lag2': PRP_lag2, 'PRP_lag3': PRP_lag3, 'PRP_lag4': PRP_lag4,
    'PRP_lag5': PRP_lag5, 'TPOA': TPOA, 'TPOA_lag1': TPOA_lag1, 'TPOA_lag2': TPOA_lag2,
    'TPOA_lag3': TPOA_lag3, 'TPOA_lag4': TPOA_lag4, 'TPOA_lag5': TPOA_lag5, 'MM': MM, 'MM_lag1': MM_lag1,
    'MM_lag2': MM_lag2, 'MM_lag3': MM_lag3, 'MM_lag4': MM_lag4, 'MM_lag5': MM_lag5, 'TRECT': TRECT,
    'TRECT_lag1': TRECT_lag1, 'TRECT_lag2': TRECT_lag2, 'TRECT_lag3': TRECT_lag3, 'TCDI': TCDI,
    'TCDI_lag1': TCDI_lag1, 'TCDI_lag2': TCDI_lag2, 'TCDI_lag3': TCDI_lag3, 'TCDI_lag4': TCDI_lag4,
    'TCDI_lag5': TCDI_lag5, 'INF': INF, 'INF_lag1': INF_lag1, 'INF_lag2': INF_lag2, 'TDEPT': TDEPT,
    'TDEPT_lag1': TDEPT_lag1, 'TDEPT_lag2': TDEPT_lag2, 'TDEPT_lag3': TDEPT_lag3, 'TDEPT_lag4': TDEPT_lag4,
    'TINV': TINV, 'TINV_lag1': TINV_lag1, 'TINV_lag2': TINV_lag2, 'TINV_lag3': TINV_lag3, 'TINV_lag4': TINV_lag4,
    'TINV_lag5': TINV_lag5, 'TEXP': TEXP, 'TEXP_lag1': TEXP_lag1, 'TEXP_lag2': TEXP_lag2,
    'TEXP_lag3': TEXP_lag3, 'TEXP_lag4': TEXP_lag4, 'TIMP': TIMP, 'TIMP_lag1': TIMP_lag1,
    'TIMP_lag2': TIMP_lag2, 'TIMP_lag3': TIMP_lag3, 'TIMP_lag4': TIMP_lag4, 'TIMP_lag5': TIMP_lag5,
    'TTaxe': TTaxe, 'TTaxe_lag1': TTaxe_lag1, 'TTaxe_lag2': TTaxe_lag2, 'TTaxe_lag3': TTaxe_lag3,
    'TTaxe_lag4': TTaxe_lag4, 'TTaxe_lag5': TTaxe_lag5
})



# Supprimer les valeurs manquantes
basetcd1 = base_modelisation.dropna()

# Calculer la matrice de corrélation
cor = basetcd1.corr()

# Exporter la matrice de corrélation dans un fichier Excel
cor.to_excel("cor.xlsx", index=True)

# Afficher la matrice de corrélation
st.write(cor)

import pandas as pd
from linearmodels.system import SUR
from statsmodels.tools import add_constant

# Créer un DataFrame avec les variables nécessaires
data = pd.DataFrame({
    'TCHO': TCHO, 'TCHO_lag1': TCHO_lag1, 'TCHO_lag2': TCHO_lag2, 'TPIB': TPIB,
    'TPIB_lag1': TPIB_lag1, 'TPIB_lag2': TPIB_lag2, 'TPIB_lag3': TPIB_lag3, 'TPOA': TPOA,
    'TPOA_lag1': TPOA_lag1, 'TINV': TINV, 'TINV_lag1': TINV_lag1, 'TINV_lag2': TINV_lag2,
    'TCDI': TCDI, 'TCDI_lag1': TCDI_lag1, 'TCDI_lag2': TCDI_lag2, 'TTaxe': TTaxe,
    'TTaxe_lag1': TTaxe_lag1, 'TTaxe_lag2': TTaxe_lag2, 'PRP': PRP, 'PRP_lag1': PRP_lag1,
    'PRP_lag2': PRP_lag2, 'PRP_lag3': PRP_lag3, 'INF': INF, 'INF_lag1': INF_lag1,
    'INF_lag2': INF_lag2, 'MM': MM, 'MM_lag1': MM_lag1, 'MM_lag2': MM_lag2,
    'TRECT': TRECT, 'TRECT_lag1': TRECT_lag1, 'TRECT_lag2': TRECT_lag2, 'TDEPT': TDEPT,
    'TDEPT_lag1': TDEPT_lag1, 'TDEPT_lag2': TDEPT_lag2
})

# Définir les équations simultanées comme chaînes de caractères
equations = {
    'TCHO': 'TCHO ~ TCHO_lag1 + TCHO_lag2 + TPIB + TPIB_lag1 + TPIB_lag2 + TPIB_lag3 + TPOA + TPOA_lag1',
    'TPIB': 'TPIB ~ TPIB_lag1 + TPIB_lag2 + PRP + PRP_lag1 + TPOA + TPOA_lag1 + PRP_lag2',
    'TINV': 'TINV ~ TINV_lag1 + TINV_lag2 + TCDI + TCDI_lag1 + TCDI_lag2 + TTaxe + TTaxe_lag1 + TTaxe_lag2 + PRP + PRP_lag1',
    'TEXP': 'TEXP ~ TEXP_lag1 + TEXP_lag2 + TINV + TINV_lag1 + TINV_lag2 + PRP + PRP_lag1 + PRP_lag2 + PRP_lag3',
    'TIMP': 'TIMP ~ TIMP_lag1 + TIMP_lag2 + PRP + PRP_lag1 + PRP_lag2 + TPIB + TPIB_lag1',
    'INF': 'INF ~ INF_lag1 + INF_lag2 + MM + MM_lag1 + MM_lag2 + TTaxe + TTaxe_lag1 + PRP',
    'TRECT': 'TRECT ~ TRECT_lag1 + TRECT_lag2 + PRP + PRP_lag1 + PRP_lag2 + TPOA + TPOA_lag1 + TTaxe',
    'TDEPT': 'TDEPT ~ TDEPT_lag1 + TDEPT_lag2 + PRP + PRP_lag1 + PRP_lag2 + TPOA + TPOA_lag1',
    'TPOA': 'TPOA ~ TPOA_lag1 + TPOA_lag2',
    'MM': 'MM ~ MM_lag1 + PRP + PRP_lag1 + TPIB + TPIB_lag1',
    'TCDI': 'TCDI ~ TCDI_lag1 + TCDI_lag2 + PRP + PRP_lag1 + PRP_lag2 + TPIB + TPIB_lag1 + TPIB_lag2',
    'TTaxe': 'TTaxe ~ TTaxe_lag1 + TTaxe_lag2 + PRP + PRP_lag1 + PRP_lag2 + TPIB + TPIB_lag1 + TPIB_lag2'
}
var=["TPIB","TINV","TEXP","TIMP","INF","TRECT","TDEPT","TPOA","MM","TCDI","TTaxe"]

# Créer un modèle 3SLS (Three-Stage Least Squares)
model = SUR.from_formula(equations, data)
x=data["PRP"]
# Ajuster le modèle
results = model.fit()

# Afficher les résultats
st.write(results.summary)

# Prédire les valeurs des autres variables en utilisant les résultats ajustés
predictions = results.predict()
# Convertir predictions en DataFrame si c'est un dictionnaire
# Variable de prediction
var=["TPIB","TINV","TEXP","TIMP","INF","TRECT","TDEPT","TPOA","MM","TCDI","TTaxe"]


