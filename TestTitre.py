import streamlit as st

import pandas as pd
import numpy as np
import json
# datetime oprations
from datetime import timedelta
# to get web contents
from urllib.request import urlopen

# basic visualization package
import matplotlib.pyplot as plt
# advanced ploting
import seaborn as sns

# interactive visualization
import plotly.express as px
import plotly.graph_objs as go

# import plotly.figure_factory as ff
from plotly.subplots import make_subplots

# for offline ploting
from plotly.offline import plot, iplot, init_notebook_mode
#init_notebook_mode(connected=True)  

# hide warnings
import warnings
warnings.filterwarnings('ignore')


import plotly.figure_factory as ff
import calmap
import folium

from urllib.request import urlopen

@st.cache_data
def Load_2022():
    df2022=pd.read_csv("valeursfoncieres-2022.txt",sep="|")
    colonne_presque_vide=[colonne for colonne in df2022.columns if df2022[colonne].isnull().sum()>df2022.shape[0]*0.95]
    df2022=df2022.drop(colonne_presque_vide,axis=1)
    df2022=df2022.drop(['No voie'],axis=1)
    df2022=df2022.drop(['Type de voie'],axis=1)
    df2022=df2022.drop(['Code voie'],axis=1)
    df2022=df2022.drop(['Section'],axis=1)
    df2022=df2022.drop(['Voie'],axis=1)
    df2022=df2022.drop(['No plan'],axis=1)
    df2022=df2022.drop(['1er lot'],axis=1)
    df2022=df2022.drop(['2eme lot'],axis=1)
    df2022=df2022.drop(['Nombre de lots'],axis=1)

    df2022['Surface reelle bati']=df2022['Surface reelle bati'].fillna(0)
    df2022['Nombre pieces principales']=df2022['Nombre pieces principales'].fillna(0)
    df2022['Surface terrain']=df2022['Surface terrain'].fillna(0)
    df2022['Valeur fonciere']=df2022['Valeur fonciere'].fillna(0)
    df2022['Valeur fonciere']=df2022['Valeur fonciere'].apply(lambda x : float(str(x).replace(',','.')))
    df2022['Code departement']=df2022['Code departement'].apply(lambda x :str(x))
    df2022["Prix_m"]=df2022["Valeur fonciere"]/df2022['Surface terrain']
    df2022['Surface non batie']=df2022['Surface terrain']-df2022['Surface reelle bati']
    return df2022

@st.cache_data
def Load_2021():

    df2021=pd.read_csv("valeursfoncieres-2021.txt",sep="|")
    colonne_presque_vide=[colonne for colonne in df2021.columns if df2021[colonne].isnull().sum()>df2021.shape[0]*0.95]
    df2021=df2021.drop(colonne_presque_vide,axis=1)
    df2021=df2021.drop(['No voie'],axis=1)
    df2021=df2021.drop(['Type de voie'],axis=1)
    df2021=df2021.drop(['Code voie'],axis=1)
    df2021=df2021.drop(['Section'],axis=1)
    df2021=df2021.drop(['Voie'],axis=1)
    df2021=df2021.drop(['No plan'],axis=1)
    df2021=df2021.drop(['1er lot'],axis=1)
    df2021=df2021.drop(['2eme lot'],axis=1)
    df2021=df2021.drop(['Nombre de lots'],axis=1)
    df2021['Surface reelle bati']=df2021['Surface reelle bati'].fillna(0)
    df2021['Nombre pieces principales']=df2021['Nombre pieces principales'].fillna(0)
    df2021['Surface terrain']=df2021['Surface terrain'].fillna(0)
    df2021['Valeur fonciere']=df2021['Valeur fonciere'].fillna(0)
    df2021['Valeur fonciere']=df2021['Valeur fonciere'].apply(lambda x : float(str(x).replace(',','.')))
    df2021['Code departement']=df2021['Code departement'].apply(lambda x :str(x))
    df2021["Prix_m"]=df2021["Valeur fonciere"]/df2021['Surface terrain']
    df2021['Surface non batie']=df2021['Surface terrain']-df2021['Surface reelle bati']

    return df2021

@st.cache_data
def Load_2020():

    df2020=pd.read_csv("valeursfoncieres-2020.txt",sep="|")
    colonne_presque_vide=[colonne for colonne in df2020.columns if df2020[colonne].isnull().sum()>df2020.shape[0]*0.95]
    df2020=df2020.drop(colonne_presque_vide,axis=1)

    df2020=df2020.drop(['No voie'],axis=1)
    df2020=df2020.drop(['Type de voie'],axis=1)
    df2020=df2020.drop(['Code voie'],axis=1)
    df2020=df2020.drop(['Section'],axis=1)
    df2020=df2020.drop(['Voie'],axis=1)
    df2020=df2020.drop(['No plan'],axis=1)
    df2020=df2020.drop(['1er lot'],axis=1)
    df2020=df2020.drop(['2eme lot'],axis=1)
    df2020=df2020.drop(['Nombre de lots'],axis=1)

    df2020['Surface reelle bati']=df2020['Surface reelle bati'].fillna(0)
    df2020['Nombre pieces principales']=df2020['Nombre pieces principales'].fillna(0)
    df2020['Surface terrain']=df2020['Surface terrain'].fillna(0)
    df2020['Valeur fonciere']=df2020['Valeur fonciere'].fillna(0)

    df2020['Valeur fonciere']=df2020['Valeur fonciere'].apply(lambda x : float(str(x).replace(',','.')))
    df2020['Code departement']=df2020['Code departement'].apply(lambda x :str(x))

    df2020["Prix_m"]=df2020["Valeur fonciere"]/df2020['Surface terrain']
    df2020['Surface non batie']=df2020['Surface terrain']-df2020['Surface reelle bati']

    return df2020

@st.cache_data
def Load_2019():

    df2019=pd.read_csv("valeursfoncieres-2019.txt",sep="|")

    colonne_presque_vide=[colonne for colonne in df2019.columns if df2019[colonne].isnull().sum()>df2019.shape[0]*0.95]
    df2019=df2019.drop(colonne_presque_vide,axis=1)

    df2019=df2019.drop(['No voie'],axis=1)
    df2019=df2019.drop(['Type de voie'],axis=1)
    df2019=df2019.drop(['Code voie'],axis=1)
    df2019=df2019.drop(['Section'],axis=1)
    df2019=df2019.drop(['Voie'],axis=1)
    df2019=df2019.drop(['No plan'],axis=1)
    df2019=df2019.drop(['1er lot'],axis=1)
    df2019=df2019.drop(['2eme lot'],axis=1)
    df2019=df2019.drop(['Nombre de lots'],axis=1)

    df2019['Surface reelle bati']=df2019['Surface reelle bati'].fillna(0)
    df2019['Nombre pieces principales']=df2019['Nombre pieces principales'].fillna(0)
    df2019['Surface terrain']=df2019['Surface terrain'].fillna(0)
    df2019['Valeur fonciere']=df2019['Valeur fonciere'].fillna(0)

    df2019['Valeur fonciere']=df2019['Valeur fonciere'].apply(lambda x : float(str(x).replace(',','.')))
    df2019['Code departement']=df2019['Code departement'].apply(lambda x :str(x))

    df2019["Prix_m"]=df2019["Valeur fonciere"]/df2019['Surface terrain']
    df2019['Surface non batie']=df2019['Surface terrain']-df2019['Surface reelle bati']
    return df2019

@st.cache_data
def Load_2018():
    df2018=pd.read_csv("valeursfoncieres-2018.txt",sep="|")

    colonne_presque_vide=[colonne for colonne in df2018.columns if df2018[colonne].isnull().sum()>df2018.shape[0]*0.95]
    df2018=df2018.drop(colonne_presque_vide,axis=1)

    df2018=df2018.drop(['No voie'],axis=1)
    df2018=df2018.drop(['Type de voie'],axis=1)
    df2018=df2018.drop(['Code voie'],axis=1)
    df2018=df2018.drop(['Section'],axis=1)
    df2018=df2018.drop(['Voie'],axis=1)
    df2018=df2018.drop(['No plan'],axis=1)
    df2018=df2018.drop(['1er lot'],axis=1)
    df2018=df2018.drop(['2eme lot'],axis=1)
    df2018=df2018.drop(['Nombre de lots'],axis=1)

    df2018['Surface reelle bati']=df2018['Surface reelle bati'].fillna(0)
    df2018['Nombre pieces principales']=df2018['Nombre pieces principales'].fillna(0)
    df2018['Surface terrain']=df2018['Surface terrain'].fillna(0)
    df2018['Valeur fonciere']=df2018['Valeur fonciere'].fillna(0)

    df2018['Valeur fonciere']=df2018['Valeur fonciere'].apply(lambda x : float(str(x).replace(',','.')))
    df2018['Code departement']=df2018['Code departement'].apply(lambda x :str(x))

    df2018["Prix_m"]=df2018["Valeur fonciere"]/df2018['Surface terrain']
    df2018['Surface non batie']=df2018['Surface terrain']-df2018['Surface reelle bati']

    return df2018

option = st.selectbox("Choisissez le visuel à afficher",
                      ("","bar_prix_m2_depart","carte_prix_m2",
                       "nb_types_proprietes","communes_plus_cheres",
                       "top_S_echangee","map_nb_transac_21",
                       "map_nb_transac_20","map_prix_total",
                       "map_prix_total","surf_terrain_moyenne",
                       "surf_totale","surf_NB","surf_dispo",
                       "NB_echange","VF_taille","nat_mutations","types_local",
                       "nat_terrain","nb_types_depart","top_S_avg",
                       "mois_mut","nb_mut_paris","prix_paris",
                       "s_moyenne_paris","nb_pieces_paris","evo_nb_19_21",
                       "evo_types","types_depart","prix_mois","prix_m2_paris",
                       "evo_prix_depart","prop_jardins","evo_appart",
                       "evo_transac"))

data_load_state = st.text('Loading data... ')

df2022 = Load_2022()
df2021 = Load_2021()
df2020 = Load_2020()
df2019 = Load_2019()
df2018 = Load_2018()

data_load_state.text = ('')



# """df2022_0=df2022.copy()
# df2022_0[df2022_0["Surface terrain"]==0.0]
# df2022_0.drop(df2022_0[(df2022_0['Surface terrain']==0.0)].index,inplace=True)"""
df2022_0=df2022.copy()

#df2022_0[df2022_0["Surface reelle bati"]==0.0]

df2022_0.drop(df2022_0[(df2022_0['Surface reelle bati']==0.0)|(df2022_0['Type local']=="Dépendance")].index,inplace=True)


###Fonction d'appel

def plot_hbar(dataframe, col,col1, n,titre,titrex,titrey, hover_data=[]):
    fig = px.bar(dataframe.sort_values(col).tail(n), 
                 x=col,
                 y=col1,
                 color=col,  
                 text=col,
                 orientation='h',
                 width=800,
                 hover_data=hover_data,
                 color_discrete_sequence = px.colors.qualitative.Dark2)
    fig.update_layout(title=titre, xaxis_title=titrex, yaxis_title=titrey, 
                      yaxis_categoryorder = 'total ascending',
                      uniformtext_minsize=8, uniformtext_mode='hide')
    return fig

def barplot_prix_m2_departement():
    df1=df2022_0.copy().dropna()
    df1.drop(df1[(df1['Valeur fonciere']==0.0)].index,inplace=True)
    df1=df1.groupby("Code departement").mean("Prix_m")
    df1["Code departement"]=df1.index
    return plot_hbar(df1,'Prix_m',"Code departement",df1.shape[0],"Prix du mètre carré par département","Prix moyen du mètre carré","Departement")


import json

def carte(dataframe,colonne,titre,couleur,ecart):
    with open("departements_om.geojson") as response:
        carte_france = json.load(response)
    fig = px.choropleth_mapbox(dataframe,
                           center={'lat': 47, 'lon': 2}, #on centre la carte sur la france (longitude/latitude)
                           color= colonne, #ici "No disposition" est le nombre de transaction
                           color_continuous_scale=couleur,
                           featureidkey="properties.code", #correspond au numéro du departement dans le fichier
                           geojson=carte_france,#fichier geojson
                           hover_name=colonne,
                           locations=dataframe.index,  
                           mapbox_style="open-street-map", # le style du fond
                           opacity=1, #opacité de la couleur
                           range_color=ecart,
                           title=titre,
                           zoom=4) #pour afficher seulement la France
    
    return fig

def carte_prix_m2():
    df=df2022_0.copy().drop(["Nature mutation"],axis=1).dropna()
    df=df.groupby(by=["Valeur fonciere","Code postal","Date mutation"]).sum()
    
    df['Date']=df.index.get_level_values(2)
    df["Code Postal"]=df.index.get_level_values(1)
    df["Code Postal"]=df["Code Postal"].apply(lambda x: str(int(x)))
    #df["Prix_m"]=df['Valeur fonciere']/df['Surface reelle bati']
    df["Code departement"]=df.index.get_level_values(1)
    
    df["Code departement"]=df["Code departement"].apply(lambda x : int(x/1000))
    df = df[['Code departement','Prix_m']]
    df7=df.dropna().groupby("Code departement").mean()


    return carte(df7,"Prix_m","Prix au mètre carré par département","matter",(0,7000))

def nb_types_proprietes():
    #df2=df2022_0.copy()
    df2=df2022.copy()
    df2=df2.groupby("Type local").count()
    df2["Type local"]=df2.index
    df2["Nombre"]=df2["Prix_m"]

    return plot_hbar(df2,"Prix_m","Type local",15,"Classement des types de propriété en fonction de leur nombre","Nombre","Type")

def communes_plus_cheres():
    df=df2022_0.copy()
    df=df.groupby(by=["Valeur fonciere","Code postal","Date mutation"]).sum()
    df['Date']=df.index.get_level_values(2)
    df["Code Postal"]=df.index.get_level_values(1)
    df["Code Postal"]=df["Code Postal"].apply(lambda x: str(int(x)))
    
    df["Prix_m"]=df.index.get_level_values(0)/df['Surface reelle bati']
    
    df["Code departement"]=df.index.get_level_values(1)
    df["Code departement"]=df["Code departement"].apply(lambda x : int(x/1000))

    df7= df.copy()[['Prix_m','Commune']].groupby('Commune').mean().sort_values(by="Prix_m",ascending=False)
    
    fig = px.bar(df7, x="Prix_m",y=df7.index,color="Prix_m",text="Prix_m",orientation='h',width=800,hover_data=[],color_discrete_sequence = px.colors.qualitative.Dark2,title="Classement 15 des Communes avec le mètre carré le plus cher dans les mutations")
    return  fig
    #return plot_hbar(df7,"Prix_m",df7.index,15,"Classement des 15 Communes ayant le prix du mètre carré le plus cher","Prix_m","Commune")

def top_S_echangee():
    df16=df2022_0.copy()
    df16=df16.groupby("Commune").sum("Surface terrain")
    df16["Commune"]=df16.index

    return plot_hbar(df16,"Surface terrain","Commune",15,"Classement des 15 Communes ayant la surface totale echangée la plus grande","Prix_m","Commune")

def map_nb_transac_21():
    df3=df2022.copy()
    df3=df3.groupby('Code departement')['No disposition'].count().to_frame()
    return carte(df3,"No disposition",'Nombre de transaction pour chaque département en 2022','matter',(0,100000))
def map_nb_transac_20():
    df3=df2021.copy()
    df3=df3.groupby('Code departement')['No disposition'].count().to_frame()
    return carte(df3,"No disposition",'Nombre de transaction pour chaque département en 2021','matter',(0,100000))

def map_prix_total():
    df6=df2022_0.copy()
    df6=df6.groupby('Code departement').sum()
    df6['Code departement']=df6.index
    return carte(df6,"Prix_m","Prix total echangé dans les transactions par département","matter",(0,250000000))

def surf_terrain_moyenne():
    df7=df2022.copy()[['Surface terrain','Code departement']]
    df7=df7.groupby('Code departement').mean()
    df7['Code departement']=df7.index
    return carte(df7,'Surface terrain',"Surface de Terrain moyenne dans les transactions par département","matter",(0,6000))
def surf_totale():
    df8=df2022.copy()[['Surface terrain','Code departement']]
    df8=df8.groupby('Code departement').sum()
    df8['Code departement']=df8.index
    return carte(df8,'Surface terrain',"Surface de Terrain totale dans les transactions par département","matter",(0,200000000))
def surf_NB():
    df9=df2022.copy()[['Surface non batie','Code departement']]
    df9=df9.groupby('Code departement').sum()
    df9['Code departement']=df9.index
    return carte(df9,"Surface non batie","Surface totale disponible par departement","matter",(0,200000000))
def surf_dispo():
    df10=df2022.copy()[['Surface non batie','Code departement']]
    df10=df10.groupby('Code departement').mean()
    df10['Code departement']=df10.index
    return carte(df10,"Surface non batie","Surface moyenne disponible par departement","matter",(0,6000))

def NB_echange():
    df11=df2022.copy()[['Surface reelle bati','Surface non batie','Code departement']]
    df11.drop(df11[(df11['Surface reelle bati']!=0.0)].index,inplace=True) #correspond à garder les terrains vides
    df11=df11.groupby('Code departement').mean()
    df11['Code departement']=df11.index
    return carte(df11,"Surface non batie","Surface moyenne des terrains non construit échangé par departement","matter",(0,7000))

def VF_taille():
    df9=df2022.copy()[['Surface terrain','Valeur fonciere','Code departement']]
    df9=df9.groupby('Code departement').mean()
    df9['Code departement']=df9.index
    df9.head()
    fig = px.scatter(df9.sort_values('Valeur fonciere', ascending=False).iloc[:100, :], 
                    x='Surface terrain', y='Valeur fonciere', color='Code departement', size='Surface terrain', 
                    height=700, text='Code departement', log_x=True, log_y=True, 
                    title='Valeur fonciere en fonction de la taille')
    fig.update_traces(textposition='top center')
    fig.update_layout(showlegend=False)
    fig.update_layout(xaxis_rangeslider_visible=True)
    return fig

def nat_mutations():
    df16=df2022.copy()[["Nature mutation","No disposition"]]
    df16=df16.groupby("Nature mutation").count()
    fig = px.pie(df16, values="No disposition", names=df16.index, title='Proportion des différentes natures des mutations')
    return fig

def types_local():
    df17=df2022.copy()[["Type local","No disposition"]]
    df17=df17.groupby("Type local").count()
    df17=df17.sort_values(by="No disposition")
    fig = px.pie(df17, values="No disposition", names=df17.index, title='Proportion des différents types de local dans les mutations')
    return fig

def nat_terrain():
    df17=df2022.copy()[["Nature culture","No disposition"]]
    df17=df17.groupby("Nature culture").count()
    df17=df17.sort_values(by="No disposition")
    fig = px.pie(df17, values="No disposition", names=df17.index, title='Proportion des différents Natures de terrain dans les mutations')
    #fig.show()
    return fig

def nb_types_depart():
  
    df3=df2022.copy()
    df3=df3.groupby(by=["Code departement","Nature mutation"]).count()
    df3['Code departement']=df3.index.get_level_values(0)
    tab=[]
    for j in set(df3["Code departement"]):
        tab1=[]
        tab1.append(j)
        r=0
        for i in ["Vente","Vente en l'état futur d'achèvement","Vente terrain à bâtir","Echange","Adjudication"]:
            if i in (df3.loc[j].index):
                a=df3.loc[(j,i),"No disposition"]
                tab1.append(a)
            else:
                a=0
                tab1.append(0)
            r=r+a
        tab1.append(r)
        tab.append(tab1)

    dfA=pd.DataFrame(data=tab,columns=['Code departement',"Vente","Echange","Vente terrain à bâtir","Vente en l'état futur d'achèvement","Adjudication","Count"])
    branches = list(dfA["Code departement"])
    c1= list(dfA["Vente"])
    c2 =list(dfA["Vente en l'état futur d'achèvement"])
    c3 =list(dfA["Vente terrain à bâtir"])
    c4=list(dfA["Echange"])
    c5=list(dfA['Adjudication'])
    trace1 = go.Bar(
    x = branches,
    y = c1,
    name = 'Vente'
    )
    trace2 = go.Bar(
    x = branches,
    y = c2,
    name = "Vente en l'état futur d'achèvement"
    )
    trace3 = go.Bar(
    x = branches,
    y = c3,
    name = 'Vente terrain à bâtir'
    )
    trace4 = go.Bar(
    x = branches,
    y = c4,
    name = 'Echange'
    )
    trace5 = go.Bar(
    x = branches,
    y = c5,
    name = "Adjudication"
    )
    data = [trace1, trace2, trace3,trace4,trace5]
    layout = go.Layout(barmode = 'stack')
    fig = go.Figure(data = data, layout = layout)
    return fig

def top_S_avg():
    df16=df2022.copy()[["Commune","Surface terrain"]]
    df16=df16.groupby("Commune").mean("Surface terrain")
    df16["Commune"]=df16.index

    return plot_hbar(df16,"Surface terrain","Commune",15,"Classement des 15 Communes ayant la surface moyenne du terrain les plus grandes","Prix_m","Commune")

def mois_mut():
    df21=df2022.copy()
    df21["Date mutation"]=df21["Date mutation"].apply(lambda x: x[3:5])
    df21=df21.groupby("Date mutation").count()
    df21["Compte"]=df21["No disposition"]
    df21["Date mutation"]=df21.index
    df21=df21[["Compte"]]
    fig = px.bar(df21, x=df21.index, y='Compte',color="Compte",color_continuous_scale="peach")
    return fig

def carte_paris(dataframe,colonne,titre,couleur,ecart):
    with open("arrondissements.geojson") as response:
        carte_france = json.load(response)
    fig = px.choropleth_mapbox(dataframe,
                           center={'lat': 48.86, 'lon': 2.34}, #on centre la carte sur la france (longitude/latitude)
                           color= colonne, #ici "No disposition" est le nombre de transaction
                           color_continuous_scale=couleur,
                           featureidkey="properties.c_ar", #correspond au numéro du departement dans le fichier
                           geojson=carte_france,#fichier geojson
                           hover_name=colonne,
                           locations=dataframe.index,  
                           mapbox_style="open-street-map", # le style du fond
                           opacity=0.99, #opacité de la couleur
                           range_color=ecart,
                           title=titre,
                           zoom=10) #pour afficher seulement la France
    return fig

def nb_mut_paris():
    df14=df2022.copy()
    df14=df14[(df14["Code postal"]>=75000.0) &(df14["Code postal"]<76000.0)]
    df14["Arrondissement"]=df14["Code postal"]-75000
    df14=df14.groupby("Arrondissement").count()

    return carte_paris(df14,"No disposition","Nombre de mutation par arrondissement","matter",(0,10000))

def prix_paris():
    df=df2022_0.copy()[["Valeur fonciere","Code postal","Code departement",'Surface reelle bati']]
    df=df.groupby(by=["Valeur fonciere","Code postal"]).sum()
    #df['Date']=df.index.get_level_values(2)
    df["Code Postal"]=df.index.get_level_values(1)
    df["Code Postal"]=df["Code Postal"].apply(lambda x: str(int(x)))
    df["Prix_m"]=df.index.get_level_values(0)/df['Surface reelle bati']
    df["Code departement"]=df.index.get_level_values(1)
    df["Code departement"]=df["Code departement"].apply(lambda x : int(x/1000))
    df15=df.copy()
    df15["Code Postal"]=df15["Code Postal"].apply(lambda x:int(x))
    df15=df15[(df15["Code Postal"]>=75000) &(df15["Code Postal"]<76000)]
    df15["Arrondissement"]=df15["Code Postal"]-75000
    df15=df15.groupby("Arrondissement").mean()

    return carte_paris(df15,"Prix_m","Prix du mètre carré par arrondissement","matter",(0,20000))

def s_moyenne_paris():
    df16=df2022.copy()[["Code postal","Surface reelle bati"]]
    df16=df16[(df16["Code postal"]>=75000.0) &(df16["Code postal"]<76000.0)]
    df16["Arrondissement"]=df16["Code postal"]-75000
    df16=df16.groupby("Arrondissement").mean()

    return carte_paris(df16,"Surface reelle bati","Surface moyenne du terrain par arrondissement","matter",(0,100))
def nb_pieces_paris():
    df16=df2022.copy()[["Code postal","Nombre pieces principales"]]
    df16=df16[(df16["Code postal"]>75000.0) &(df16["Code postal"]<76000.0)]
    df16["Arrondissement"]=df16["Code postal"]-75000
    df16["Arrondissement"]=df16["Arrondissement"].apply(lambda x:str(int(x)))
    df16=df16.groupby("Arrondissement").mean()

    return plot_hbar(df16,"Nombre pieces principales",df16.index,30,"Classement des arrondissement en fonction de leur nombre de pièces","Nombre","Arrondissement")
def evo_nb_19_21():
    df1 = df2022.copy().groupby('Code departement')['No disposition'].count().to_frame()
    df2020transactions=df2020.groupby('Code departement')['No disposition'].count().to_frame()
    différence1=df1-df2020transactions
    return carte(différence1,"No disposition",'Evolution du nombre de transactions pour chaque département entre 2020 et 2022','icefire',(-50000,50000))

def evo_types():
    df17=df2022.copy()
    df17=df17.groupby("Type local").count()
    df17=df17.sort_values(by="No disposition")
    df22=df2022.copy()
    dfmutations2020=df2020.copy()
    df22=df17.groupby("Type local").count()
    dfmutations2020=dfmutations2020.groupby("Type local").count()
    df22=df17.sort_values(by="No disposition")
    dfmutations2020=dfmutations2020.sort_values(by="No disposition")

    fig = make_subplots(rows=1, cols=2, specs=[[{"type": "pie"}, {"type": "pie"}]])

    fig.add_trace(go.Pie(values=list(dfmutations2020["No disposition"].to_dict().values()),labels=list(dfmutations2020["No disposition"].to_dict().keys()),
        name="2020"),row=1, col=2)

    fig.add_trace(go.Pie(values=list(df22["No disposition"].to_dict().values()),labels=list(df17["No disposition"].to_dict().keys()),
        name="2022"), row=1, col=1)

    return fig


def types_depart():
    df6=df2022.copy()
    df6=df6.groupby(by=["Code departement","Type local"]).count()
    df6["Compte"]=df6["No disposition"]
    df6['Code departement']=df6.index.get_level_values(0)
    tab=[]
    for j in set(df6["Code departement"]):
        tab1=[]
        tab1.append(j)
        r=0
        for i in [ 'Local industriel. commercial ou assimilé', 'Dépendance', 'Appartement', 'Maison']:
            if i in (df6.loc[j].index):
                a=df6.loc[(j,i),"Compte"]
                tab1.append(a)
            else:
                a=0
                tab1.append(0)
            r=r+a
        tab1.append(r)
        tab.append(tab1)
    
    dfA=pd.DataFrame(data=tab,columns=['Code departement','Local industriel. commercial ou assimilé', 'Dépendance', 'Appartement', 'Maison',"Count"])
    dfA=dfA.sort_values("Count")
    branches = list(dfA["Code departement"])
    c1= list(dfA["Local industriel. commercial ou assimilé"])
    c2 =list(dfA["Dépendance"])
    c3=list(dfA["Appartement"])
    c4=list(dfA['Maison'])
    trace1 = go.Bar(
    x = branches,
    y = c1,
    name = "Local industriel. commercial ou assimilé"
    )
    trace2 = go.Bar(
    x = branches,
    y = c2,
    name = 'Dépendance'
    )
    trace3= go.Bar(
    x = branches,
    y = c3,
    name = 'Appartement'
    )
    trace4 = go.Bar(
    x = branches,
    y = c4,
    name = 'Maison'
    )
    data = [trace1, trace2, trace3,trace4]
    layout = go.Layout(barmode = 'stack')
    fig = go.Figure(data = data, layout = layout)
    return fig

def prix_mois():
    df=df2022_0.copy()[["Code postal","Date mutation","Valeur fonciere",'Surface reelle bati']]
    df=df.groupby(by=["Valeur fonciere","Code postal","Date mutation"]).sum()
    df['Date']=df.index.get_level_values(2)
    df["Code Postal"]=df.index.get_level_values(1)
    df["Code Postal"]=df["Code Postal"].apply(lambda x: str(int(x)))
    df["Prix_m"]=df.index.get_level_values(0)/df['Surface reelle bati']
    df["Code departement"]=df.index.get_level_values(1)
    df["Code departement"]=df["Code departement"].apply(lambda x : int(x/1000))
    df21=df.copy()
    df21.head()
    df21["Date"]=df21["Date"].apply(lambda x: int(x[3:5]))
    df21=df21.groupby("Date").mean()
    df21["Date"]=df21.index
    fig = px.line(df21, x='Date', y='Prix_m')
    return fig

def prix_m2_paris():
    df=df2022_0.copy()[["Code postal","Valeur fonciere",'Surface reelle bati']]
    df=df.groupby(by=["Valeur fonciere","Code postal"]).sum()
    
    
    df["Code Postal"]=df.index.get_level_values(1)
    df["Code Postal"]=df["Code Postal"].apply(lambda x: str(int(x)))
    df["Prix_m"]=df.index.get_level_values(0)/df['Surface reelle bati']
    df["Code departement"]=df.index.get_level_values(1)
    df["Code departement"]=df["Code departement"].apply(lambda x : int(x/1000))
    df15=df.copy()
    
    df15["Code Postal"]=df15["Code Postal"].apply(lambda x:int(x))
    df15=df15[(df15["Code Postal"]>=75000) &(df15["Code Postal"]<76000)]
    df15["Arrondissement"]=df15["Code Postal"]-75000
    df15=df15.groupby("Arrondissement").mean()
    return carte_paris(df15,"Prix_m","Prix du mètre carré par arrondissement","matter",(0,20000))

def evo_prix_depart():
    df=df2022_0.copy()[["Code postal","Valeur fonciere",'Surface reelle bati',"No disposition"]]
    df=df.groupby(by=["Valeur fonciere","Code postal"]).sum()
    #df['Date']=df.index.get_level_values(2)
    df["Code Postal"]=df.index.get_level_values(1)
    df["Code Postal"]=df["Code Postal"].apply(lambda x: str(int(x)))
    df["Prix_m"]=df.index.get_level_values(0)/df['Surface reelle bati']
    df["Code departement"]=df.index.get_level_values(1)
    df["Code departement"]=df["Code departement"].apply(lambda x : int(x/1000))

    df2022PrixM2=df.copy()
    df2022PrixM2["Prix_m"]=df2022PrixM2["Prix_m"]/df2022PrixM2["No disposition"]
    df2022PrixM2=df2022PrixM2.groupby("Code departement").mean()

    df2020_0=df2020.copy()
    #df2020_0[df2020_0["Surface reelle bati"]==0.0]
    df2020_0.drop(df2020_0[(df2020_0['Surface reelle bati']==0.0)|(df2020_0['Type local']=="Dépendance")].index,inplace=True)

    df2020PrixM2=df2020_0.copy()[["Code postal","Valeur fonciere",'Surface reelle bati',"No disposition"]]
    df2020PrixM2=df2020PrixM2.groupby(by=["Valeur fonciere","Code postal"]).sum()
    #df2020PrixM2['Date']=df2020PrixM2.index.get_level_values(2)
    df2020PrixM2["Code Postal"]=df2020PrixM2.index.get_level_values(1)
    df2020PrixM2["Prix_m"]=df2020PrixM2.index.get_level_values(0)/df2020PrixM2['Surface reelle bati']
    df2020PrixM2["Prix_m"]=df2020PrixM2["Prix_m"]/df2020PrixM2["No disposition"]
    df2020PrixM2["Code departement"]=df2020PrixM2.index.get_level_values(1)
    df2020PrixM2["Code departement"]=df2020PrixM2["Code departement"].apply(lambda x : int(x/1000))
    df2020PrixM2=df2020PrixM2.groupby("Code departement").mean()

    df2020PrixM2["Difference"]=df2022PrixM2["Prix_m"]-df2020PrixM2["Prix_m"]
    return carte(df2020PrixM2,"Difference","Evolution du prix moyen du metre carré par département entre 2020 et 2022","icefire",(-2000,2000))


def prop_jardins():
    nbMaisonsJardin2022=df2022.loc[df2022["Surface non batie"]>=10]
    nbMaisonsJardin2022=nbMaisonsJardin2022["No disposition"].loc[nbMaisonsJardin2022["Code type local"]==1].count()
    nbMaisonsApp2022=df2022["No disposition"].loc[df2022["Code type local"]==1].count()+df2022["No disposition"].loc[df2022["Code type local"]==2].count()
    prop2022=(nbMaisonsJardin2022/nbMaisonsApp2022)*100

    nbMaisonsJardin2021=df2021.loc[df2021["Surface non batie"]>=10]
    nbMaisonsJardin2021=nbMaisonsJardin2021["No disposition"].loc[nbMaisonsJardin2021["Code type local"]==1].count()
    nbMaisonsApp2021=df2021["No disposition"].loc[df2021["Code type local"]==1].count()+df2021["No disposition"].loc[df2021["Code type local"]==2].count()
    prop2021=(nbMaisonsJardin2021/nbMaisonsApp2021)*100

    nbMaisonsJardin2020=df2020.loc[df2020["Surface non batie"]>=10]
    nbMaisonsJardin2020=nbMaisonsJardin2020["No disposition"].loc[nbMaisonsJardin2020["Code type local"]==1].count()
    nbMaisonsApp2020=df2020["No disposition"].loc[df2020["Code type local"]==1].count()+df2020["No disposition"].loc[df2020["Code type local"]==2].count()
    prop2020=(nbMaisonsJardin2020/nbMaisonsApp2020)*100

    nbMaisonsJardin2019=df2019.loc[df2019["Surface non batie"]>=10]
    nbMaisonsJardin2019=nbMaisonsJardin2019["No disposition"].loc[nbMaisonsJardin2019["Code type local"]==1].count()
    nbMaisonsApp2019=df2019["No disposition"].loc[df2019["Code type local"]==1].count()+df2019["No disposition"].loc[df2019["Code type local"]==2].count()
    prop2019=(nbMaisonsJardin2019/nbMaisonsApp2019)*100

    nbMaisonsJardin2018=df2018.loc[df2018["Surface non batie"]>=10]
    nbMaisonsJardin2018=nbMaisonsJardin2018["No disposition"].loc[nbMaisonsJardin2018["Code type local"]==1].count()
    nbMaisonsApp2018=df2018["No disposition"].loc[df2018["Code type local"]==1].count()+df2018["No disposition"].loc[df2018["Code type local"]==2].count()
    prop2018=(nbMaisonsJardin2018/nbMaisonsApp2018)*100


    x=[2018,2019,2020,2021,2022]
    y=[prop2018,prop2019,prop2020,prop2021,prop2022]
    d={'Année':x,"Proportion de maisons avec jardin":y}
    df=pd.DataFrame(d)
    fig = px.line(df, x="Année", y="Proportion de maisons avec jardin")
    return fig

def evo_appart():
    App2022=df2022.loc[df2022["Code type local"]==2]
    nbApp2022=App2022.groupby("Code departement").sum()


    App2020=df2020.loc[df2020["Code type local"]==2]
    nbApp2020=App2020.groupby("Code departement").sum()

    nbApp2022["Code departement"]=nbApp2022.index
    nbApp2020["Code departement"]=nbApp2020.index
    difference=nbApp2022["No disposition"]-nbApp2020["No disposition"]
    return carte(difference,"No disposition","Evolution des transactions des appartements entre 2020 et 2022","icefire",(-15000,15000))

def evo_transac():
    df22=df2022.copy()
    df21=df2021.copy()
    df20=df2020.copy()
    df19=df2019.copy()
    df22["Date mutation"]=df22["Date mutation"].apply(lambda x: x[3:5])
    df21["Date mutation"]=df21["Date mutation"].apply(lambda x: x[3:5])
    df20["Date mutation"]=df20["Date mutation"].apply(lambda x: x[3:5])
    df19["Date mutation"]=df19["Date mutation"].apply(lambda x: x[3:5])

    df22=df22.groupby("Date mutation").count()
    df21=df21.groupby("Date mutation").count()
    df20=df20.groupby("Date mutation").count()
    df19=df19.groupby("Date mutation").count()

    dftest=pd.DataFrame()
    dftest["Transactions en 2019"]=df19["No disposition"]
    dftest["Transactions en 2020"]=df20["No disposition"]
    dftest["Transactions en 2021"]=df21["No disposition"]
    dftest["Transactions en 2022"]=df22["No disposition"]
    dftest["Date"]=dftest.index

    fig = px.bar(dftest, x="Date", y=["Transactions en 2019","Transactions en 2020","Transactions en 2021","Transactions en 2022"],barmode="group")
    return fig


def index(option):

    if option == "bar_prix_m2_depart":
        return barplot_prix_m2_departement()
        
            
    elif option == "carte_prix_m2":
        return carte_prix_m2()        
    
    elif option == "nb_types_proprietes":
         
        return nb_types_proprietes()
        
    elif option == "communes_plus_cheres":
         
        return communes_plus_cheres()
        
    elif option == "top_S_echangee":
         
        return top_S_echangee()
        
    elif option == "map_nb_transac_21":
         
        return map_nb_transac_21()
        
    elif option == "map_nb_transac_20":
         
        return map_nb_transac_20()
        
    elif option == "map_prix_total":
         
        return map_prix_total()
        
    elif option == "surf_terrain_moyenne":
         
        return surf_terrain_moyenne()
        
    elif option == "surf_totale":
         
        return surf_totale()
        
    elif option == "surf_NB":
         
        return surf_NB()
        
    elif option == "surf_dispo":
         
        return surf_dispo()
        
    elif option == "NB_echange":
         
        return NB_echange()
        
    elif option == "VF_taille":
         
        return VF_taille()
        
    elif option == "nat_mutations":
         
        return nat_mutations()
        
    elif option == "types_local":
         
        return types_local()
        
    elif option == "nat_terrain":
         
        return nat_terrain()
        
    elif option == "nb_types_depart":
         
        return nb_types_depart()
        
    elif option == "top_S_avg":
         
        return top_S_avg()
        
    elif option == "mois_mut":
         
        return mois_mut()
        
    elif option == "nb_mut_paris":
         
        return nb_mut_paris()
        
    elif option == "prix_paris":
         
        return prix_paris()
        
    elif option == "s_moyenne_paris":
         
        return s_moyenne_paris()
        
    elif option == "nb_pieces_paris":
         
        return nb_pieces_paris()
        
    elif option == "evo_nb_19_21":
         
        return evo_nb_19_21()
        
    elif option == "evo_types":
         
        return evo_types()
        
    elif option == "types_depart":
         
        return types_depart()
        
    elif option == "prix_mois":
         
        return prix_mois()
        
    elif option == "prix_m2_paris":
         
        return prix_m2_paris()
        
    elif option == "evo_prix_depart":
         
        return evo_prix_depart()
        
    elif option == "prop_jardins":
         
        return prop_jardins()
        
    elif option == "evo_appart":
         
        return evo_appart()
        
    elif option == "evo_transac":         
        return evo_transac()

index(option)

display = index(option)
st.plotly_chart(display, use_container_width=True)
