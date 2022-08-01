
from msilib.schema import AdminExecuteSequence
from tkinter import*
from tkinter import Tk, ttk
from turtle import left
from tkinter import messagebox
from webbrowser import get


# cores -----------------------------
co0 = "#f0f3f5"  # Preta / black
co1 = "#feffff"  # branca / white
co2 = "#3fb5a3"  # verde / green
co3 = "#38576b"  # valor / value
co4 = "#403d3d"   # letra / letters

# Janela

janela = Tk()  # Cria a janela
janela.title("Aplicação")  # Cria o titulo da janela
janela.geometry("400x400+750+300")
janela.configure(background="#CE4257")
janela.resizable(width=False, height=False)


# Parte de cima

frame_cima = Frame(
    janela,
    width=400,
    height=90,
    bg="#CE4257",
    relief="flat",



)

frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW,)


# Configurando parte de cima

l_login = Label(
    frame_cima,
    text="LOGIN",
    anchor=NE,
    font="Arial 35",
    bg="#CE4257",
    fg="#6B2737",

)

l_login.place(x=5, y=5)

l_traco = Label(
    frame_cima,
    text="",
    anchor=NW,
    width=375,
    font="Arial 1",
    bg="#6B2737",
    fg="#6B2737",

)

l_traco.place(x=5, y=80)


# Função para verificar o login

credencias = ['Kaue', '123456', 'Ana', '654321',
              'Luciana', '987654', 'Noah', '456456']


def verificar():

    nome = e_nome.get()
    senha = e_senha.get()

    if nome == 'admin' and senha == 'admin':
        messagebox.showinfo('LOGIN', 'Seja bem vindo de volta admin')
    elif credencias[0] == nome and credencias[1] == senha:
        messagebox.showinfo(
            'LOGIN', 'Seja bem vindo de volta ' + credencias[0])
    elif credencias[2] == nome and credencias[3] == senha:
        messagebox.showinfo(
            'LOGIN', 'Seja bem vindo de volta ' + credencias[2])
    elif credencias[4] == nome and credencias[5] == senha:
        messagebox.showinfo(
            'LOGIN', 'Seja bem vindo de volta ' + credencias[4])
    elif credencias[6] == nome and credencias[7] == senha:
        messagebox.showinfo(
            'LOGIN', 'Seja bem vindo de volta ' + credencias[6])
    else:
        messagebox.showwarning('Erro', 'Verifique o nome e a senha')


# Parte de baixo
frame_baixo = Frame(
    janela,
    width=400,
    height=400,
    bg="#CE4257",
    relief="flat",



)
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW,)


l_nome = Label(
    frame_baixo,
    text="Nome:",
    anchor=NW,
    font="Arial 15",
    bg="#CE4257",
    fg="#6B2737",

)

l_nome.place(x=9, y=60)

e_nome = Entry(
    frame_baixo,
    width=28,
    justify="left",
    font=("", 18),
    highlightthickness=1,
    relief="solid",
)

e_nome.place(x=9, y=100)


l_senha = Label(
    frame_baixo,
    text="Senha:",
    anchor=NW,
    font="Arial 15",
    bg="#CE4257",
    fg="#6B2737",

)

l_senha.place(x=9, y=140)

e_senha = Entry(
    frame_baixo,
    width=28,
    justify="left",
    font=("", 18),
    highlightthickness=1,
    relief="solid",
)

e_senha.place(x=9, y=180)


b_confirmar = Button(
    frame_baixo,
    text="Confirmar",
    justify="center",
    width=20,
    height=2,
    font="Arial 15",
    bg="#6B2737",
    fg="black",
    relief=RAISED,
    overrelief=RIDGE,
    command=verificar,

)

b_confirmar.place(x=80, y=230)


janela.mainloop()
