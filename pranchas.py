from os import write
from typing import Text
import pandas as pd
#from pycaret.regression import load_model 
import streamlit as st
#from sklearn.metrics import accuracy_score
from streamlit.proto.RootContainer_pb2 import SIDEBAR
from streamlit.proto.Slider_pb2 import Slider
import joblib
#from PIL.Image import core as _imaging
from PIL import Image


model = joblib.load('modelo_grid_papai.pkl')

#Título do app
st.header("""
**Sistema de Indicações de pranchas** \n
Este Aplicativo utiliza os dados inseridos, para recomendar a melhor prancha para você""")

#Cabeçalho criado
st.subheader('Informações Preenchidas:')


#Dados de preenchimento
sexo = st.sidebar.selectbox('Sexo: ', ('Feminino', 'Masculino'))
st.write('Sexo:', sexo)
escala = ["Iniciante","Medina","Agressivo","Dark_Shneider"]
estilo = st.sidebar.select_slider("Estilo do surf",
            options=escala)
st.write('Estilo no Mar informada:', estilo)
idade = st.sidebar.slider('Qual sua Idade?', 12,80, 20)
st.write('Idade Informada: ', idade)
peso = st.sidebar.slider('Peso', 45,120, 60)
st.write('Peso Informado: ', peso)
altura = st.sidebar.slider('Altura: ', 1.5,2.10, 1.70)
st.write('Altura: ', altura)

#Transformando strings em numerical:
sexo = 1 if sexo == "Masculino" else 0

def change(l):
    if l =="Iniciante":
        return 1
    elif l == "Medina":
        return 2
    elif l == "Agressivo":
        return 3
    elif l == "Dark_Shneider":
        return 4

estilo = change(estilo)

# inserindo um botão na tela
btn_predict = st.sidebar.button("Realizar Recomendação")

# verifica se o botão foi acionado
if btn_predict:
    data_teste = pd.DataFrame()

    data_teste['estilo'] = [estilo]
    data_teste['idade'] = [idade]
    data_teste['peso'] = [peso]
    data_teste['altura'] = [altura]
    data_teste["sexo"] =	[sexo]

    
   # imprime os dados de teste    
   # print(data_teste)

    #realiza a predição
    result = model.predict(data_teste) 
        #model,data = data_teste)["Label"]
    
    st.subheader("A recomendação para o seu tipo de surf é:")
    resultado = f'A Prancha recomendada para você é a de número: {result}.' #if result == [1] else "Negada. Tente entrar em contato com seu gerente de contas."
    st.write(resultado)
    caminho = 'C:/Users/willi/Pictures/'
    p1 = 'Images/prancha22.jpg'
    p2 = 'Images/prancha3.jpg'
    p3 = 'Images/prancha4.png'
    p4 = 'Images/pranchas.jpg'
    p5 = 'Images/surf.jpg'
    
    if result == [6]:
        image = Image.open(f'{caminho}/{p1}')
        st.image(image, caption = 'Prancha Hardcore') 
    elif result == [4]:    
        image = Image.open(f'{caminho}/{p4}')
        st.image(image, caption = 'Prancha top demais')
    elif result == [2]:    
        image = Image.open(f'{caminho}/{p2}')
        st.image(image, caption = 'Prancha top demais')
    elif result == [1]:    
        image = Image.open(f'{caminho}/{p5}')
        st.image(image, caption = 'Prancha top demais') 
    else:
        image = Image.open(f'{caminho}/{p3}')
        st.image(image, caption = 'Outras')
         
        
    
#    caminho = 'C:/Users/willi/Pictures/'
#    p1 = '303828.jpg'#    p2 = 'surf.jpg'    x = result    x = p1 if x == [6] else p2
#    image = Image.open(f'{caminho}/{x}')
#    st.image(image, caption = 'Prancha')
