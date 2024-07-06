# Importando os modulos importantes para o projecto
import numpy as np
import streamlit as st
import openai
from gerador_ia import gerador_de_frases, frase
from enviar_whatsapp import enviar_msg_whatsapp
from CSV_generator import add_valor, carregar_dados_csv, e_vazio
from grafico import top_enviados


# Carregando o Token da Api do ChatGPT
#openai.api_key = ''

# Colocar a pagina todo no centro
st.set_page_config(layout='centered')

# Criando um logo paraa página
st.image(image="imgs\\images.png", width=150)

# Titulo da Página
st.title("Gerador de Frases Reflexivas")

# Importando os nossos conjuntos de dados
df_frases = carregar_dados_csv('datasets/Dados_Frases.csv',type='f')
df_pessoas = carregar_dados_csv('datasets/Dados_Pessoa.csv',type='p')


# Vamos criar o botão de geração de frases
btn = st.button(label='Gerar uma Frase')
# Se o botão for clicado
if btn:
    # A Frase é exibida
    frase_gerada = gerador_de_frases()
    st.info(frase_gerada)

    # atualizando o conunto de dados
    add_valor(df_frases,type='f',valor=frase_gerada)
    df_frases = carregar_dados_csv('datasets/Dados_Frases.csv',type='f')
    cod_frases = np.array2string(df_frases['cod_frases'].tail(1).values).strip('[]')


# Aqui vamos adicionar a Opção de enviar a mensagem a alguém pelo whatsapp
st.write('Deseja enviar a mensagem para aquela especial no whatsapp? Escreva o nome e clica no botão enviar')
# Caixa para escrever o nome da pessoa
nome = st.text_input('Você!',)
# botão para enviar a mensagem
if nome:
    cod = np.array2string(carregar_dados_csv('datasets/Dados_Frases.csv',type='f')['cod_frases'].tail(1).values).strip('[]')
    st.header('Enviar Mensagem Para o whatsapp')
    # cadastrar no ficheiro a mensagem enviada
    add_valor(df=df_pessoas,type='p',valor=nome,cod_frases=cod)
    # enviar a frase pelo whatsapp
    enviar_msg_whatsapp(nome=nome,frase=frase)
    
        



# Aqui vai a parte correspondente a Analise de dados

if not e_vazio(path='datasets/Dados_Pessoa.csv'):
    st.header('Analise de Dados')
    st.subheader('Top 5 Pessoas que mais Lhe enviaram mensagens')
    top5_enviados = df_pessoas['pessoa_enviada'].value_counts(ascending=False).to_frame(name='contagem').reset_index().head(5)
    st.dataframe(top5_enviados)

    st.subheader('Grafico top 5 de pessoas que mais receberam mensagens')
    st.plotly_chart(top_enviados(top5_enviados=top5_enviados))


# Aqui vai a parte correspondente a Analise de Dados para a mensagens enviadas
if not e_vazio('datasets/Dados_Frases.csv'):
    st.header('Mensagens Geradas Recentemente')
    st.subheader('Ultimas Mensagens Enviadas')
    st.dataframe(df_frases.tail(5))


