import pyautogui
import pyperclip
from time import sleep

# tempo de carregar do pyautogui
pyautogui.PAUSE = 0.5

def enviar_msg_whatsapp(nome:str,frase:str)->None:
    """
    Essa função envia a frase para a pessoa de nome {nome} pelo whatsapp.
    Para essa função funcionar há a necessida que a pessoa em questão tenha o Whatsapp instalado em sua maquina, ou irá gerar um erro

    Args:
        nome (str) Nome de quem se vai enviar a mensagem
        frase (str) A frase reflexiva que vai ser enviada

    Returns:
        None:
    """
    # abrindo a barra de procura do windows e escrever whatsapp
    pyautogui.press('win')
    sleep(2) # esperar 2 segundos
    # Escrever o nome do aplicativo
    pyautogui.write('whatsapp')
    sleep(2) # esperar 2 segundos e clicar Enter
    pyautogui.press('enter')
    sleep(3) # esperar 3 segundos ate o whatsapp carregar, esse valor é determinado assim caso o computador esteja lento
    # procurar pela pessoa desejada
    # Clica na caixa de pesquisa
    pyautogui.click(x=111,y=119)
    # Escreve o nome da pessoa
    pyautogui.write(nome)
    sleep(1) #processa por 1 segundo
    # Clica na primeira pessoa que aparece nas sugestões
    pyautogui.leftClick(x=122,y=184)
    sleep(3) # dorme 3 segundos
    # Escreve a mensagem desejada
    pyperclip.copy(text=frase)
    pyautogui.hotkey('ctrl','v') # cola a mensagem copiada
    pyautogui.press('enter') # Envia a mensagem
    # sai da conversa
    pyautogui.press('esc')

    

