###importar bibiliotecas ##################
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import Database

###criar janela #########################
jan = Tk()
jan.title("DP Systema - Access Panel")
jan.geometry("600x300")
jan.configure(background="white")
jan.resizable(width=False,height=False)
jan.attributes("-alpha", 0.9)
jan.iconbitmap(default="img/LogoIcon.ico")

##### CARREGANDO IMAGENS #########################
logo = PhotoImage(file="img/logo.png")


##### CRIANDO WIDGETS LOGIN #########################
LeftFrame = Frame(width=200,height=300,bg="MIDNIGHTBLUE",relief="raise")
LeftFrame.pack(side=LEFT)

RightFrame = Frame(width=397,height=300,bg="MIDNIGHTBLUE",relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LeftFrame, image=logo,bg="MIDNIGHTBLUE")
LogoLabel.place(x=50,y=100)

UserLabel = Label(RightFrame,text="Username:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="White")
UserLabel.place(x=5,y=100)

UserEntry = ttk.Entry(RightFrame,width=30)
UserEntry.place(x=150,y=114)

PassLabel = Label(RightFrame,text="Password:",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
PassLabel.place(x=5,y=150)

PassEntry = ttk.Entry(RightFrame,width=30, show="*")
PassEntry.place(x=150,y=160)

##### FUNÇÃO LOGIN #########################
def Login():
    
    User = UserEntry.get()
    Password = PassEntry.get()
    
    Database.cursor.execute("""
    SELECT User, Password FROM Users
    WHERE (User = ? AND Password = ?)
    """,(User, Password))
    
    VerifyLogin = Database.cursor.fetchone()
    try:
        if(User in VerifyLogin and Password in VerifyLogin):
            messagebox.showinfo(title="Info Login", message="Acesso Confirmado. Bem vindo !")
    except:
        messagebox.showinfo(title="Info Login", message="Acesso inválido. Verifique usuário/senha")

LoginButton = Button(RightFrame,text="Login", width=20, command=Login)
LoginButton.place(x=50,y=220)


def ForgotToPassword():
    ##### REMOVENDO WIDGETS LOGIN #########################
    UserEntry.place(x=5000)
    UserLabel.place(x=5000)
    PassEntry.place(x=5000)
    PassLabel.place(x=5000)
    LoginButton.place(x=5000)
    ResetButton.place(x=5000)
    SignupButton.place(x=5000)
    
    ##### CRIANDO WIDGETS PARA VALIDAR E-MAIL #########################
    EmailResetLabel = Label(RightFrame,text="E-mail:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="White")
    EmailResetLabel.place(x=0,y=65)

    EmailResetEntry = Entry(RightFrame,width=49)
    EmailResetEntry.place(x=95,y=78)

    NewPassLabel = Label(RightFrame,text="New Password:",font=("Century Gothic", 20), bg="MIDNIGHTBLUE",fg="White")
    NewPassLabel.place(x=0,y=118)

    NewPassEntry = Entry(RightFrame,width=30, show="*")
    NewPassEntry.place(x=210,y=130)
   
    def ResetPassword():
        Email = EmailResetEntry.get()
        NewPass = NewPassEntry.get()

        Database.cursor.execute("""
        SELECT * FROM Users
        WHERE (Email = ?)
        """,(Email,))
        VerifyEmail = Database.cursor.fetchone()

        try:
            if(Email in VerifyEmail):
                Database.cursor.execute("""
                UPDATE Users
                SET Password = ?
                WHERE Email = ?
                """,(NewPass,Email))
                Database.conn.commit()
                messagebox.showinfo(title="Info Reset Password", message="Senha atualizada")
        except:
            messagebox.showinfo(title="Info Reset Password", message="E-mail não localizado na base de dados")        

    VerifyemailButton = Button(RightFrame, text="Reset Password", width=20, command=ResetPassword)
    VerifyemailButton.place(x=30, y=220)

    def Back():
        ##### REMOVENDO WIDGETS VERIFICA E-MAIL #########################
        VerifyemailButton.place(x=5000)
        BackButton.place(x=5000)
        EmailResetLabel.place(x=5000)
        EmailResetEntry.place(x=5000)
        NewPassEntry.place(x=5000)
        NewPassLabel.place(x=5000)
        
        ##### VOLTANDO WIDGETS LOGIN #########################
        UserLabel.place(x=5)
        UserEntry.place(x=150)
        PassLabel.place(x=5)
        PassEntry.place(x=150)
        LoginButton.place(x=50)
        SignupButton.place(x=220)
        ResetButton.place(x=100)

    BackButton = Button(RightFrame, text="Back", width=20, command=Back)
    BackButton.place(x=210, y=220)

ResetButton = Button(RightFrame, text="Forgot To Password", width=30, command=ForgotToPassword)
ResetButton.place(x=100, y=256)

def Register():
    #Removendo Widgets de Login
    LoginButton.place(x=5000)
    SignupButton.place(x=5000)

    #Adicionado Widgets de cadastro
    NameLabel = Label(RightFrame, text="Name:", font=("Century Gothic", 20), bg="MIDNIGHTBLUE", fg="White")
    NameLabel.place(x=5,y=15)

    NameEntry = ttk.Entry(RightFrame, width=30)
    NameEntry.place(x=150,y=29)

    EmailLabel = Label(RightFrame,text="Email:",font=("Century Gothic",20), bg="MIDNIGHTBLUE", fg="White")
    EmailLabel.place(x=5,y=55)
    
    EmailEntry = ttk.Entry(RightFrame,width=30)
    EmailEntry.place(x=150,y=70)

    def RegisterToDatabase():
        Name = NameEntry.get()
        Email = EmailEntry.get()
        User = UserEntry.get()
        Password = PassEntry.get()

        if (Name == "" and Email == "" and User == "" and Password == ""):
            messagebox.showerror(title="Register Error", message="Não deixe nenhum campo vazio. Preecnha todos os campos")
        else:
            Database.cursor.execute("""
            INSERT INTO Users(Name, Email, User,Password) VALUES(?, ?, ?, ?)
            """,(Name, Email, User, Password))
            Database.conn.commit()
            messagebox.showinfo(title="Register Info", message="Account Created Sucessfull")

    RegisterButton = Button(RightFrame,text="Register",command=RegisterToDatabase, width=20)
    RegisterButton.place(x=50,y=220)
    
    def BackToLogin():
        #Removendo Widgets de cadastro
        NameLabel.place(x=5000)
        NameEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        RegisterButton.place(x=5000)
        BackButton.place(x=5000)

        #Trazendo de volta Widgets de Login
        LoginButton.place(x=50)
        SignupButton.place(x=220)

    BackButton = Button(RightFrame,text="Back", width=20,command=BackToLogin)
    BackButton.place(x=220,y=220)

SignupButton = Button(RightFrame,text="Sign Up",command=Register, width=20)
SignupButton.place(x=220,y=220)

jan.mainloop()  