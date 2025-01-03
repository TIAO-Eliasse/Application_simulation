import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



#st.write("Mecanisme de transmission des fluctuations des prix de pétrole dans l'économmie de la Guinée Equatoriale")

# Insérer un style CSS dans Streamlit
st.markdown(
    """
    <style>
    .element-container {
        margin-bottom: 0rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)




secteur=["Secteur réel", "commerce extérieur","secteur financier", "Bloc budgétaire et fiscalité"]
# Sélection du pays via un menu déroulant
Secteur_activite = st.sidebar.selectbox(
    "Sélectionnez un secteur d'activité :", 
    options=secteur, 
    key="select_secteur"
)


## Analyse exploratoire par secteur

data=pd.read_excel("base_final.xlsx", sheet_name="Feuil2")

#st.write(data[:5])


# Fonction pour tracer la courbe
def plot_evolution(df, year_col='Années', col1="PRP", col2="Prix du baril de pétrole"):
    """
    Tracer l'évolution du taux d'emploi en fonction des années et des catégories d'âge avec Plotly.

    Args:
        df (pd.DataFrame): DataFrame contenant les données.
        year_col (str): Nom de la colonne représentant les années.
        unemployment_col (str): Nom de la colonne représentant le taux de chômage.
        age_col (str): Nom de la colonne représentant les catégories d'âge.
        selected_age (str, optional): Tranche d'âge à afficher. Si None, toutes les catégories seront affichées.

    Returns:
        plotly.graph_objects.Figure: Graphique interactif.
    """
    
    fig = px.line (
        df,
        x=year_col,
        y=col1,
        labels={"Années", col2}
    )
    fig.update_traces(mode="lines")  # Ajouter des points sur la courbe
    fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        xaxis_title="Années",
        yaxis_title=col2,
        height=250,
        
    )
    return fig





def plot_evolution2(df, year_col='Années', col1="PRP", col2="TPIB"):
    """
    Tracer l'évolution de deux variables en fonction des années avec Plotly.

    Args:
        df (pd.DataFrame): DataFrame contenant les données.
        year_col (str): Nom de la colonne représentant les années.
        col1 (str): Nom de la première variable à tracer (ex: PRP).
        col2 (str): Nom de la deuxième variable à tracer (ex: TPIB).

    Returns:
        plotly.graph_objects.Figure: Graphique interactif.
    """
    # Transformation pour tracer deux variables sur une seule figure
    df_melted = df.melt(id_vars=[year_col], value_vars=[col1, col2], 
                        var_name="Variable", value_name="Valeur")
    
    # Tracer les courbes
    fig = px.line(
        df_melted,
        x=year_col,
        y="Valeur",
        color="Variable",
        labels={year_col: "Années", "Valeur": "Valeur", "Variable": "Variable"}
    )
    
    fig.update_traces(mode="lines+markers")  # Ajouter des points sur les courbes
    fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        #xaxis_title="Années",
        #yaxis_title="Valeur",
        height=400,
        legend_title="Variables"
    )
    return fig


with st.container():

    if Secteur_activite=="Secteur réel":
        col1=st.columns(2)
        with col1[0]:
            fig=plot_evolution(data,year_col='Années', col1="PRP", col2="¨Prix du baril de pétrole($US)")
            st.plotly_chart(fig,use_container_width=True)
        with col1[1]:
            fig=plot_evolution(data,year_col='Années', col1="TPIB",col2="Taux de croissance annuelle du PIB")
            st.plotly_chart(fig,use_container_width=True)
        col2=st.columns(2)
        with col1[0]:
            fig=plot_evolution(data, year_col="Années", col1="CHO", col2="Taux de chômage")
            st.plotly_chart(fig,use_container_width=True)

        with col1[1]:
            fig=plot_evolution(data, year_col="Années", col1="TPOA", col2="Taux de croissance de pop active")
            st.plotly_chart(fig,use_container_width=True)
        col3=st.columns(2)
        
        with col1[0]:
            fig=plot_evolution2(data, year_col='Années', col1="PRP", col2="TPIB")
            st.plotly_chart(fig,use_container_width=True)
        with col1[1]:
            fig=plot_evolution2(data, year_col='Années', col1="PRP", col2="TINV(%)")
            st.plotly_chart(fig,use_container_width=True)
        with col1[0]:
            fig=plot_evolution2(data, year_col='Années', col1="TPOA(%)", col2="TPIB")
            st.plotly_chart(fig,use_container_width=True)

    if Secteur_activite=="commerce extérieur":
        col1=st.columns(2)
        with col1[0]:
            fig=plot_evolution(data,year_col='Années', col1="EXP", col2="Exportations($US)")
            st.plotly_chart(fig,use_container_width=True)
        with col1[1]:
            fig=plot_evolution(data,year_col='Années', col1="IMP", col2="Importations($US)")
            st.plotly_chart(fig,use_container_width=True)
        col2=st.columns(2)
        with col1[0]:
            fig=plot_evolution(data, year_col="Années", col1="BLE",col2="BLE(%)")
            st.plotly_chart(fig,use_container_width=True)

        with col1[1]:
            fig=plot_evolution(data, year_col="Années", col1="PRP", col2="Prix pétrole($US)")
            st.plotly_chart(fig,use_container_width=True)
        with col1[0]:
            fig=plot_evolution2(data, year_col='Années', col1="PRP", col2="BLE")
            st.plotly_chart(fig,use_container_width=True)
        with col1[1]:
            fig=plot_evolution2(data, year_col='Années', col1="PRP", col2="TEXP(%)")
            st.plotly_chart(fig,use_container_width=True)
        with col1[0]:
            fig=plot_evolution2(data, year_col='Années', col1="PRP", col2="TIM(%)")
            st.plotly_chart(fig,use_container_width=True)


    if Secteur_activite=="secteur financier":
        col1=st.columns(2)
        with col1[0]:
            fig=plot_evolution(data,year_col='Années', col1="MM(%)", col2="Varation de la masse monétaire")
            st.plotly_chart(fig)
        with col1[1]:
            fig=plot_evolution(data,year_col='Années', col1="INF", col2="Taux d'inflation")
            st.plotly_chart(fig)
        col2=st.columns(2)
        with col2[0]:
            fig=plot_evolution(data, year_col="Années", col1="TCDI(%)",col2="variation du credit offert au secteur privé")
            st.plotly_chart(fig)

        with col2[1]:
            fig=plot_evolution(data, year_col="Années", col1="PRP", col2="Prix pétrole($US)")
            st.plotly_chart(fig)

    if Secteur_activite=="Bloc budgétaire et fiscalité":
        col1=st.columns(2)
        with col1[0]:
            fig=plot_evolution(data,year_col='Années', col1="Ttaxe(%)", col2="Variation des taxes nettes sur les produits")
            st.plotly_chart(fig,use_container_width=True)
        with col1[1]:
            fig=plot_evolution(data,year_col='Années', col1="RECT", col2="Variation annuelle des recettes")
            st.plotly_chart(fig,use_container_width=True)
        col2=st.columns(2)
        with col2[0]:
            fig=plot_evolution(data, year_col="Années", col1=" DEPT",col2="Depense publique en variation annuelle")
            st.plotly_chart(fig,use_container_width=True)
        with col2[1]:
            fig=plot_evolution(data, year_col="Années", col1="Subv", col2="Subvention")
            st.plotly_chart(fig,use_container_width=True)
