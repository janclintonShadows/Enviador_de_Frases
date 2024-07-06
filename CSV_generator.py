# importando o modulo pandas
import pandas as pd
from datetime import date

def carregar_dados_csv(path:str, type:str, sep:str=',')->pd.DataFrame:
    """
    Função que Gera um dataframe do arquivo csv existente, 
    caso não exista, ele cria um dataframe.

    O Dataframe tem o seguinte formato, cod_frase, frase_reflexiva, data para o ficheiro do tipo 'f'
    cod_frase, pessoa_enviada, data para ficheiro do tipo 'p'

    Args:
        path (str) Caminho do arquivo no formato csv ou tsv ou txt
        type (str, 'p','f') O tipo de ficheiro a ser carregado ('f' -> dataframe de frase; 'p' -> Dataframe para armazenar mensagens enviadas as pessoas)
        sep (str, opcional) O tipo de separador do ficheiro CSV, por padrão considera a ',' como separador

    Returns:
        pd.Dataframe: Retorna um dataframe pandas
    """
    # Verificar qual daframe foi selecionado
    if type == 'p':
        try:
            df = pd.read_csv(filepath_or_buffer=path,sep=sep)
        except:
            df = pd.DataFrame(columns=['cod_frases','pessoa_enviada','data'])
            df.to_csv('datasets/Dados_Pessoa.csv', index=False)
        finally:
            return df
    elif type == 'f':
        try:
            df = pd.read_csv(filepath_or_buffer=path,sep=sep)
        except:
            df = pd.DataFrame(columns=['cod_frases','Frase_reflexiva','data'])
            df.to_csv('datasets/Dados_Frases.csv', index=False)
        finally:
            return df
    else:
        raise ValueError("Valor do tipo somente pode ser 'f' ou 'p'")
    
    
# função de adicionar novos dados ao dataframe
def add_valor(df:pd.DataFrame, type:str, valor:str,cod_frases:str=None)->None:
    """
    O Dataframe e a Frase que vai ser concatenado nela

    Args:
        path (str) Caminho do arquivo no formato csv ou tsv ou txt
        type (str, 'p','f') O tipo de ficheiro a ser carregado ('f' -> dataframe de frase; 'p' -> Dataframe para armazenar mensagens enviadas as pessoas)
        valor (str) A frase a ser armazenada, se for o dataframe do type 'f', ou nome da pessoa para o dataframe de type 'p'
        cod_frases (str, if type == 'p':) o código da frase, somente se estiver sendo enviado para a pessoa, recebe o código da frase enviada

    Returns:
        None: Não retorna nada
    """
    if type == 'p':
        if not cod_frases:
            raise SyntaxError('Se o tipo do Dataframe é "p" esse valor é obrigatorio')
        if len(df):
            new_df = pd.DataFrame(data={'cod_frases':[cod_frases],'pessoa_enviada':[valor],'data':[str(date.today())]})
        else:
            new_df = pd.DataFrame(data={'cod_frases':[cod_frases],'pessoa_enviada':[valor],'data':[str(date.today())]})
        pd.concat([df,new_df]).to_csv('datasets/Dados_Pessoa.csv', index=False)
    elif type == 'f':
        if len(df):
            last_num = gerador_cod()
            new_df = pd.DataFrame(data={'cod_frases':[last_num],'Frase_reflexiva':[valor],'data':[str(date.today())]})
        else:
            last_num = gerador_cod()
            new_df = pd.DataFrame(data={'cod_frases':[last_num],'Frase_reflexiva':[valor],'data':[str(date.today())]})
        pd.concat([df,new_df]).to_csv('datasets/Dados_Frases.csv', index=False)


def e_vazio(path:str)->bool:
    '''
    Está função recebe um ficheiro verifica se o ficheiro conjunto de dados está vazio ou não, e retorna um valor lógico.
    Se estiver vazio retorna verdadeiro

    Args:
        path (str) O caminho ate o ficheiro csv

    Returns:
        bool: Retorna um valor booleano True or False
    '''
    df = pd.read_csv(path)
    try:
        if len(df):
            return False
        else:
            return True
    except:
        return True
    

def gerador_cod():
    num = int(len(carregar_dados_csv('datasets/Dados_Frases.csv',type='f')) + 1)
    return 'cod_'+str(num)
