import requests
import streamlit as st 

def buscar_letra(artista, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{artista}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra
    

st.image("https://i.imgur.com/SmktDIH.png")
st.title("Letras de músicas")

banda = st.text_input("Artista ou banda: ", key = "banda")
musica = st.text_input("Nome da música: ", key = "musica")
pesquisar = st.button("Pesquisar")

if pesquisar: 
    letra = buscar_letra(artista, musica)
    if letra:
        st.success("Encontramos a letra da música")
        st.text(letra)
    else:
        st.error("Não foi possível encontrar a letra dessa música")    
