import pyautogui
import time
pyautogui.PAUSE = 1.5

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(7)
print(pyautogui.position())

pyautogui.click(x=510, y=360)
pyautogui.write("Brendo213@outlook.com")

pyautogui.press("tab")
pyautogui.write("i6x8h5c9@")

pyautogui.press("tab")
pyautogui.press("enter") 


pyautogui.click(x=493, y=253)   

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]

    codigo= 'MOLO000251'

pyautogui.write("codigo") 

pyautogui.press("tab")

pyautogui.write("marca")

pyautogui.press("tab")

pyautogui.write("tipo")

pyautogui.press("tab")

pyautogui.write("categoria")

pyautogui.press("tab")

pyautogui.write("preco")

pyautogui.press("tab")

pyautogui.write("custo")

pyautogui.press("tab")

pyautogui.write("obs")

pyautogui.press('tab')

pyautogui.press("enter")

time.sleep(4)
import pandas as pd

tabela = pd.read_csv("produtos.csv")



print (tabela)


time.sleep(5)
print(pyautogui.position())

pyautogui.scroll(5000)



