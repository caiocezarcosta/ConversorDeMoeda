
import requests
import json
from tkinter import *
from tkinter import ttk

def pegar_cotacao():
    
    try:
        rq = requests.get(f'https://economia.awesomeapi.com.br/last/{cb_moeda1.get()}-{cb_moeda2.get()}')
        rq = rq.json()
        cotacao = rq[f'{cb_moeda1.get()}{cb_moeda2.get()}']["bid"]
        mostrarResultado["text"] = f'{cb_moeda2.get()} {cotacao}'
    except: 
       mostrarResultado["text"] = "Não foi possivel realizar a conversão"
        
root = Tk()
root.title("Conversor de moeda")
root.geometry("400x400")
#primeiro label
desc = Label(root, text= "Aplicativo para realizar a conversão de moedas")
desc.pack()

#moeda1
moedas = ["BRL","USD","BTC"]
lb_moeda1 = Label(root,text="Moedas")
lb_moeda1.pack()

cb_moeda1=ttk.Combobox(root, values = moedas,state="readonly")
cb_moeda1.set("")
cb_moeda1.pack()

#moeda2 
lb_moeda2 = Label(root,text="Moeda")
lb_moeda2.pack()

cb_moeda2 =ttk.Combobox(root, values = moedas,state="readonly")
cb_moeda2.set("")
cb_moeda2.pack()

#botao
btn_rodar = Button(root,text="Buscar", command=pegar_cotacao)
btn_rodar.pack()

#Mostrar resultado
mostrarResultado = Label(root, text="")
mostrarResultado.pack()

root.mainloop()




