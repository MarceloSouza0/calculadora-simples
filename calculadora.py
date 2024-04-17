# Etapa 1
# importando biblioteca tkinter
from tkinter import *
from tkinter import ttk
# (Etapa 3)
cor1 = '#141414'  # black/preta
cor2 = '#feffff'  # white/branca
cor3 = '#38576b'  # blue/azul
cor4 = '#ECEFF1'  # gray/cinza
cor5 = '#FFAB40'  # orange/laranja

# Etapa 2
# Criar janela e fazer configurações basicas da janela
janela = Tk()
janela.title('Calculadora do Celo garoto de programa')
janela.geometry('235x310')
janela.config(bg=cor1)

# Etapa 3
# definir a cor do background da primeira janela
frame_tela = Frame(janela, width=235, height=50, bg=cor3)

# definir tamanho e expessura do background da primeira janela
frame_tela.grid(row=0, column=0)

# tem dois widgets, um acima do outro. Um deles servindo de background

# definir a cor background da janela maior
frame_corpo = Frame(janela, width=235, height=268)

# definir o tamanho e expessura do backgroud da janela maior
frame_corpo.grid(row=1, column=0)

# variavel todos valores
todos_valores = ''
valor_texto = StringVar()

#criando função, etapa 6
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)

    
    # passando valor para tela
    valor_texto.set(todos_valores)


#função para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(resultado)


# função limpar tela
def limpar_tela():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')


# criando label

app_label = Label(frame_tela, textvariable=valor_texto , width=16, height=2, padx=7,
                  relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 18'), bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# etapa 4 Criando botões e etapa 5 cofigurando e colocando cor
b_1 = Button(frame_corpo, command= limpar_tela,text='C', width=11, height=2, bg=cor4, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)  # criar o botao
b_1.place(x=0, y=0)  # posicionar o botão

b_2 = Button(frame_corpo, command= lambda: entrar_valores('%'), text='%', width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

b_3 = Button(frame_corpo, command= lambda: entrar_valores('/'), text='/', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)  # para mudar a cor da letra, use fg
b_3.place(x=177, y=0)

# parte 2

b_4 = Button(frame_corpo, command= lambda: entrar_valores('7'), text='7', width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)

b_5 = Button(frame_corpo, command= lambda: entrar_valores('8'), text='8', width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)

b_6 = Button(frame_corpo, command= lambda: entrar_valores('9'), text='9', width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)

b_7 = Button(frame_corpo, command= lambda: entrar_valores('*'), text='*', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),
             relief=RAISED, overrelief=RIDGE)  # para mudar a cor da letra, use fg
b_7.place(x=177, y=52)

# parte 3

b_8 = Button(frame_corpo, command= lambda: entrar_valores('4'), text='4', width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)

b_9 = Button(frame_corpo, command= lambda: entrar_valores('5'), text='5', width=5, height=2, bg=cor4,
             font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)

b_10 = Button(frame_corpo, command= lambda: entrar_valores('6'), text='6', width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)

b_11 = Button(frame_corpo, command= lambda: entrar_valores('-'), text='-', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE)  # para mudar a cor da letra, use fg
b_11.place(x=177, y=104)

# parte 4

b_12 = Button(frame_corpo, command= lambda: entrar_valores('1'), text='1', width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)

b_13 = Button(frame_corpo, command= lambda: entrar_valores('2'), text='2', width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)

b_14 = Button(frame_corpo, command= lambda: entrar_valores('3'), text='3', width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)

b_15 = Button(frame_corpo, command= lambda: entrar_valores('+'), text='+', width=5, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'),
              relief=RAISED, overrelief=RIDGE)  # para mudar a cor da letra, use fg
b_15.place(x=177, y=156)

# parte 5

b_16 = Button(frame_corpo, command= lambda: entrar_valores('0'), text='0', width=11, height=2, bg=cor4, font=(
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)  # criar o botao
b_16.place(x=0, y=208)  # posicionar o botão

b_17 = Button(frame_corpo, command= lambda: entrar_valores('.'), text='.', width=5, height=2, bg=cor4,
              font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)

b_18 = Button(frame_corpo, command= calcular, text='=', width=5, height=2, bg=cor5, fg=cor2, font=(
    # para mudar a cor da letra, use fg
    'Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=177, y=208)


# (Etapa 2)
janela.mainloop()  # essas linhas acima servem para criar um janela