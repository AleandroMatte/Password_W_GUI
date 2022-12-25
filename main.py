from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from randompass import password


def gerar():
    entry_password.insert(0, password)
    entry_password.clipboard_clear()
    entry_password.clipboard_append(password)
    entry_password.update()


# ---------------------------- SAVE PASSWORD ------------------------------- #
import tkinter.filedialog


def savethings():
    website = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    if len(email) < 12 and len(password) > 8:
        messagebox.showerror(title="email", message="your email is invalid")
    else:emailcheck=True

    if len(password) < 8 and len(email) > 12:
        messagebox.showerror(title="Password", message="your password_entrada needs to be atleas 8 characters long")
    else:senhacheck=True
    if len(password) < 8 and len(email) < 12:
        messagebox.showerror(title="passsword and email",
                             message="your password_entrada needs to be atleast 8 characters long"
                                     " and your e-mail is invalid")
    else:senha_e_email_check=True
    if len(website) < 4:
        messagebox.showwarning(title='website', message="voce nao inseriu o nome do site,Corrija seu erro mero mortal")
    else:website_check=True

    if senhacheck and senha_e_email_check and  website_check and emailcheck:
        aceitou = messagebox.askokcancel(title=website,
                                         message=f"Are you sure you want to save {password} as standard password_entrada for {website}")
        if aceitou:
            with open(file=tkinter.filedialog.askopenfilename(), mode='a') as file:
                file.write("\n" + website + '||' + email + "||" + password + "\n")
            entry_password.delete(first=0, last=END)
            entry_website.delete(first=0, last=END)


# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

window = Tk()
window.title("Password Manager almateon")
window.config(padx=50, pady=50)

canvas = Canvas(width=150, height=150, highlightthickness=0)
imagem = PhotoImage(file="logo.png")
canvas.create_image(80, 100, image=imagem)
canvas.grid(column=1, row=1, pady=20, padx=20)
canvas.config()
##
label_website = Label(text="Website:", padx=0)
label_website.grid(column=0, row=2, pady=5)
entry_website = Entry(width=50)
entry_website.grid(column=1, row=2, columnspan=2, pady=5, sticky='w')
entry_website.focus()

label_email = Label(text="email/username:", padx=10)
label_email.grid(column=0, row=3, pady=5)
entry_email = Entry(width=50)
entry_email.insert(0, "aleandrogostoso@outlook.com")
entry_email.grid(column=1, row=3, columnspan=2, pady=5, sticky='w')

label_pssw = Label(text="password_entrada:", padx=10)
label_pssw.grid(column=0, row=4, pady=5)
entry_password = Entry(width=30)
entry_password.grid(column=1, row=4, columnspan=2, pady=5, sticky='w')
botao_gerar = Button(text="gerar", width=15, command=gerar)
botao_gerar.grid(column=2, row=4, pady=5, columnspan=2)

botao_finalizar = Button(text="Adicionar", command=savethings, width=30)
botao_finalizar.grid(column=1, row=6, columnspan=2, pady=10, sticky='w')

window.mainloop()
