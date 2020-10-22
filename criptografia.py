import tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from Crypto.Cipher import AES
from Crypto.Hash  import SHA256
from unicodedata import normalize

janela = tkinter.Tk()
janela.title("Trabalho APS CC2020")

janela["bg"] = "gray15"

#Tamanho da Janela LarguraxAltura - Distância da esquerda do monitor e do Topo em pixel
janela.geometry("1000x700+300+300")


#Biblioteca 

#Senha fixa
senha = "Essa é minha Senha Fixa"

# normalmente hash é padrão  diferente do sals fiz só para mostra que senha a pessoa pode escolher ;
# no arquivos de criptografia explica oque hash e sals 
#condifica com hash para tamanho fixo
hash_obj = SHA256.new(senha.encode('utf-8'))
hkey = hash_obj.digest()
cifra = AES.new(hkey)







#pad é para verificar se a palavra é do tamanho 16 for menor completa com '{'

def pad(s):
    return s + ((16 -len(s) % 16) * '{')

#encrypt vai pegar a msg verificada com tamanho    
def encrypt(plaintext):
    global cifra
    return cifra.encrypt(pad(plaintext))

#vai decriptografa com separado os { da palavra original
def decrypt(ciphertext):
    global cifra
    dec = cifra.decrypt(ciphertext).decode('utf-8')
    l = dec.count('{')
    return dec[:len(dec)-l]


#cop vai retorna a palavra criptografada e descriptografada 


def cop(msg):
    msgR = normalize('NFKD', msg).encode('ASCII','ignore').decode('ASCII')
    a = encrypt(msgR)
    b = decrypt(a)
  

    return a,b



#cripto é o botão que vai criptografa, ele pega a palavra escrita na textbox passa para uma variavel que é criptografada e retornada o valor da criptografia 

def cripto ():
    
    entrada1.config(state = 'normal')
    entrada2.config(state = 'normal')
    msg = entrada.get()
    c,d = cop(msg)
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada1.insert(0,str(c))
    entrada1.config(state = 'disable')
    entrada2.config(state = 'disable')

#Descrip é botão que vai retorna a descriptografia

def descrip():
    entrada2.config(state = 'normal')
    msg = entrada.get()
    c,d = cop(msg)
    entrada2.delete(0, END)
    entrada2.insert(0,str(d))
    entrada2.config(state = 'disable')

#limpa vai tira todas as escrita das textbox
def limpa():
    entrada1.config(state = 'normal')
    entrada2.config(state = 'normal')
    entrada.delete(0,END)
    entrada1.delete(0, END)
    entrada2.delete(0, END)
    entrada1.config(state = 'disable')
    entrada2.config(state = 'disable')
    



#Entrada 1
entrada = Entry(janela,width = 150)
entrada.place(x=30,y=50)


#botãoLimpar
#Acrescentar Command = FunçãoLimpar
bt1 = Button(janela, width = 100, text = "CRIPTOGRAFAR TEXTO", fg = "black", bg = "yellow2", font = "Helvetica,80", command= cripto)
bt1.place(x=30, y=100)

#MensagemCrirptografada
#Acrescentar Command = FunçãoCriptografar

entrada1 = Entry(janela,width = 150,state = 'disable')
entrada1.place(x=30,y=150)


#BotãoCriptografar
bt2 = Button(janela, width = 100, text = "DESCRIPTOGRAFAR TEXTO", fg = "black", bg = "chartreuse2", font = "Helvetica,80",command= descrip)
bt2.place(x=30, y=200)


#MensagemDescriptpografada
#Acrescentar Command = FunçãoDescriptografar
entrada2 = Entry(janela,width = 150,state = 'disabled')
entrada2.place(x=30,y=250)

#BotãoDescriptografar
bt3 = Button(janela, width = 100, text = "Limpar", fg = "black", bg = "red2", font = "Helvetica,80",command= limpa)
bt3.place(x=30, y=300)







janela.mainloop()





