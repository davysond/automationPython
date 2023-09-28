#1: Inserir o sistema da empresa 'https://dlp.hashtagtreinamentos.com/python/intensivao/login';
#2: Realizar login;
#3: Importar a base de dados;
#4: Cadastrar 1 produto;
#5: Repetir o processo de cadastro.

import pyautogui
import time

# pyautogui.click -> Clicar com o mouse
# pyautogui.write -> Escrever 
# pyautogui.press -> Pressionar 1 tecla
# pyautogui.hotkey -> Atalho (combinação de teclas)

pyautogui.PAUSE = 0.5

# Entrar no site:
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
url_site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(url_site)
pyautogui.press("enter")

time.sleep(1.5)

# Inserir o login:
pyautogui.click(x=412, y=376)
pyautogui.write("davysonguimares74@gmail.com")
pyautogui.click(x=488, y=469)
pyautogui.write("admin")
pyautogui.click(x=476, y=524, clicks=2)

# Lendo base de dados:

import pandas

tabela = pandas.read_csv("tabelaprodutos.csv")
print(tabela)

# Cadastrando um produto:

for linha in tabela.index:
    time.sleep(2)
    pyautogui.click(x=583, y=269)

    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]

    if not pandas.isna(obs):
        pyautogui.write(str(obs))
        
    pyautogui.click(x=411, y=865, clicks=2)