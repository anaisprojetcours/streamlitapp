import streamlit as st 
st.title("S'cool")
st.subheader("Trouver l'école idéale pour vos enfants n'a jamais été aussi facile! ")



#############Libraries########################## 
#Dataframe 
import pandas as pd 
import numpy as np 
#Wab app 
import streamlit as st 

#Plot thing 
#import plotly.express as px 

#Map 
from folium.plugins import StripePattern
#import geopandas as gpd

#Web app map 
from streamlit_folium import st_folium
import folium
#from folium.plugins import MarkerCluster


######################################################################################################

#############################################Data base################################################

######School
data_school= pd.read_csv("/Users/anaisdias/Desktop/dataetablissement.csv", sep=";")
school = data_school.copy()
#Drop unuseful columns
school = school.drop(['patronyme_uai','lieu_dit_uai','boite_postale_uai','coordonnee_x','coordonnee_y','localisation','position','appellation_officielle','localite_acheminement_uai','libelle_commune','code_commune'], axis=1)
#rename UAI
school = school.rename(columns={'numero_uai':'UAI'})

#####IPS
#Indice sur la position sociale des parents
data_ips = pd.read_csv("/Users/anaisdias/Desktop/ips.csv", sep=";")
ips= data_ips.copy()


######Pollution
#Indice de pollution
data_pollution = pd.read_csv("/Users/anaisdias/Desktop/yy.csv", sep=",", encoding = 'utf8')
pollution = data_pollution.copy()
#rename UAI
pollution = pollution.rename(columns={'ID':'UAI'})
#drop NaN value
pollution = pollution.dropna(axis=0)



#####Sector
data_sector= pd.read_csv("/Users/anaisdias/Desktop/secteurs.csv", sep=";")
sector = data_sector.copy()

#####Nb_student
data_student= pd.read_csv("/Users/anaisdias/Desktop/nbeleves.csv", sep=";")
nbstudent= data_student.copy()
#keep on insteressting columns
nbstudent= nbstudent[['numero_ecole','nombre_total_classes','nombre_eleves_elementaire_hors_ulis', 'nombre_eleves_ulis',
       'nombre_eleves_cp_hors_ulis', 'nombre_eleves_ce1_hors_ulis',
       'nombre_eleves_ce2_hors_ulis', 'nombre_eleves_cm1_hors_ulis',
       'nombre_eleves_cm2_hors_ulis' ]]
#rename UAI
nbstudent = nbstudent.rename(columns={'numero_ecole':'UAI'})

######DataMerge
#merge df on uai column
school_ips = pd.merge(school,ips, on="UAI", how="inner")
school_ips_pollution = pd.merge(school_ips,pollution, on="UAI", how="inner")
data = pd.merge(school_ips_pollution,nbstudent, on="UAI", how="inner")


#Change type
data['latitude'] = data['latitude'].astype(float)
data['longitude'] = data['longitude'].astype(float)

#Data on Paris only
df=data[data['Nom de la commune'].str.contains('PARIS')]
df = df.drop_duplicates(subset=['UAI'])


#########################Web#####################################
###import image
import PIL 
from PIL import Image

#image = Image.open('Images/school.jpg')
#st.image(image,use_column_width=True)



#######################streamlitselection####################################
school_category = df['denomination_principale'].unique().tolist()
school_sector = df['secteur_public_prive_libe'].unique().tolist()
school_cp = df['CP'].unique().tolist()
s_ips= df['IPS'].unique().tolist()

ips_selection = st.slider('IPS:', 
                        min_value=min(s_ips), 
                        max_value=max(s_ips), 
                        value=(min(s_ips), max(s_ips)))

school_category_selection=st.multiselect('Catégorie spécifique:', 
                                        school_category, 
                                        default=school_category)

school_sector_selection=st.multiselect('Secteur:', 
                                        school_sector, 
                                        default=school_sector)

school_cp_selection=st.multiselect('Code Postal:', 
                                        school_cp, 
                                        default=school_cp)

######Filter dataframe based on selection

mask=(df['IPS'].between(*ips_selection)) & (df['denomination_principale'].isin(school_category_selection)) & (df['secteur_public_prive_libe'].isin(school_sector_selection)) & (df['CP'].isin(school_cp_selection))                                   
number_of_results=df[mask].shape[0]
st.markdown(f'*Avialable results: {number_of_results}*')

st.dataframe(df[mask])


######test map #######
m = folium.Map(location = [48.856578, 2.351828], zoom_start = 12)
for (index, row) in df[mask].iterrows():
    if row.loc['secteur_public_prive_libe']=='Privé':
        color='red'
    else: 
        color='blue'
    folium.Marker(location=[row.loc['latitude'], row.loc['longitude']],icon=folium.Icon(color=color), popup = row.loc["Nom de l'établissment"], zoom_start = 12).add_to(m)


st_data = st_folium(m, width = 725)

print(pd.__version__)
