# Vamos criar função que vai gerar uma frase usando o chat GPT
import openai

frase = ''

# Criando uma função de geração de frase
def gerador_de_frases()->str:
    """
    Uma função que gera uma frase reflexiva usando a api do ChatGPT

    Return:
        str: Retorna a frase reflexiva
    """
    
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages=[{
            "role": 'system', 'content':'Voçê deve gerar frase lindas e reflixas, perfeitas para enviar para um amigo, amiga, pais, e irmãos, familiares e amigos.'
        },
        {
            'role':'user','content':'Gera uma nova frase reflexiva!'
        }],
        max_tokens=200,
        temperature=0.8
    )

    global frase 
    frase = response.choices[0].message.content.strip()
    return response.choices[0].message.content.strip()