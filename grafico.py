import plotly.express as px
import pandas as pd

def top_enviados(top5_enviados:pd.DataFrame) :
    fig_barra = px.bar(
        top5_enviados, x='pessoa_enviada', y='contagem',
        title='Top 5 de pessoas que mais são enviadas mensagens',
        labels={
            'pessoa_enviada':'Pessoas', 'contagem':'Contagem dos Valores'
        },
        color='pessoa_enviada',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    return fig_barra
    