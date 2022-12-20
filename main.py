from tkinter import *
from tkinter import messagebox
from mydb import Database
from myapi import API




class NLPApp:

    def __init__(self):
        #create db object
        self.dbo = Database()
        self.apio = API()
        #Create GUI
        self.root = Tk()
        self.root.title('NLP App')
        self.root.geometry('500x700')
        self.root.configure(bg='#70B2CF')

        self.login_gui()
        self.root.mainloop()

    def login_gui(self):
        self.clear_page()
        head = Label(self.root,text = 'NLPApp',bg='#70B2CF',fg='white')
        head.pack(pady=(30,30))
        head.configure(font=('Ariel',28,'bold'))

        label1 = Label(self.root,text='Enter Email',bg='#70B2CF',fg='white')
        label1.pack(pady=(10,10))
        label1.configure(font=('Ariel',15,'bold'))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=5)

        label2 = Label(self.root, text='Enter Password', bg='#70B2CF', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('Ariel', 15, 'bold'))

        self.password_input = Entry(self.root, width=50,show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        login_btn = Button(self.root,text='Login',width=14,height=2,command=self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root, text='Not a Member?', bg='#70B2CF', fg='white')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root,text='Register',command = self.register_gui)
        redirect_btn.pack(pady=(10,10))

    def register_gui(self):
        self.clear_page()

        head = Label(self.root, text='Register Here For NLPApp', bg='#70B2CF', fg='white')
        head.pack(pady=(30, 30))
        head.configure(font=('Ariel', 28, 'bold'))

        label0 = Label(self.root, text='Enter Your Name', bg='#70B2CF', fg='white')
        label0.pack(pady=(10, 10))
        label0.configure(font=('Ariel', 15, 'bold'))

        self.name_input = Entry(self.root, width=50)
        self.name_input.pack(pady=(5, 10), ipady=5)

        label1 = Label(self.root, text='Enter Email', bg='#70B2CF', fg='white')
        label1.pack(pady=(10, 10))
        label1.configure(font=('Ariel', 15, 'bold'))

        self.email_input = Entry(self.root, width=50)
        self.email_input.pack(pady=(5, 10), ipady=5)

        label2 = Label(self.root, text='Enter Password', bg='#70B2CF', fg='white')
        label2.pack(pady=(10, 10))
        label2.configure(font=('Ariel', 15, 'bold'))

        self.password_input = Entry(self.root, width=50, show='*')
        self.password_input.pack(pady=(5, 10), ipady=5)

        register_btn = Button(self.root, text='Register', width=14, height=2,command=self.perform_registration)
        register_btn.pack(pady=(10, 10))

        label3 = Label(self.root, text='Already a Member?', bg='#70B2CF', fg='white')
        label3.pack(pady=(20, 10))

        redirect_btn = Button(self.root, text='Login Here', command=self.login_gui)
        redirect_btn.pack(pady=(10, 10))



    def clear_page(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)
        if response:
            messagebox.showinfo('Success','Registration Successful. Login Now')
        else:
            messagebox.showerror('Error','Email Already Exists')

    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)
        if response:
            messagebox.showinfo('Success','WELCOME')
            self.dashboard_gui()
        else:
            messagebox.showerror('Error','Invalid Details')

    def dashboard_gui(self):
        self.clear_page()

        head = Label(self.root, text='Analyse various Sentiments ', bg='#70B2CF', fg='white')
        head.pack(pady=(30, 30))
        head.configure(font=('Ariel', 27, 'bold'))

        sentiment_btn = Button(self.root, text='Sentiment Analysis',width=30,height=4, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20, 20))

        ner_btn = Button(self.root, text='Abuse Analysis',width=30,height=4 ,command=self.abuse_gui)
        ner_btn.pack(pady=(20, 20))

        emotion_btn = Button(self.root, text='Emotion Analysis',width=30,height=4, command=self.emotion_gui)
        emotion_btn.pack(pady=(20, 20))

        logout_btn = Button(self.root, text='Logout', command=self.login_gui)
        logout_btn.pack(pady=(10, 10))

    def sentiment_gui(self):
        self.clear_page()

        head = Label(self.root, text='Sentiment Analysis ', bg='#70B2CF', fg='white')
        head.pack(pady=(30, 30))
        head.configure(font=('Ariel', 27, 'bold'))

        label1 = Label(self.root, text='Enter Text', bg='#70B2CF', fg='white')
        label1.pack(pady=(20, 10))
        label1.configure(font=('Ariel', 15, 'bold'))

        self.sentiment_input = Entry(self.root, width=50)
        self.sentiment_input.pack(pady=(5, 10), ipady=20)

        sentiment_btn = Button(self.root, text='Analyse', command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10, 10))

        self.sentiment_result = Label(self.root, text='', bg='#70B2CF', fg='white')
        self.sentiment_result.pack(pady=(20, 10))
        self.sentiment_result.configure(font=('verdana', 16))

        go_back_btn = Button(self.root, text='Go Back', command=self.dashboard_gui)
        go_back_btn.pack(pady=(7, 7))

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)
        txt = ''
        for i in result['sentiment']:
            txt = txt + i + '-->' + str(result['sentiment'][i]) + '\n'
        print(txt)
        self.sentiment_result['text'] = txt

    def abuse_gui(self):

        self.clear_page()

        head = Label(self.root, text='Abuse Analysis ', bg='#70B2CF', fg='white')
        head.pack(pady=(30, 30))
        head.configure(font=('Ariel', 27, 'bold'))

        label1 = Label(self.root, text='Enter Text', bg='#70B2CF', fg='white')
        label1.pack(pady=(20, 10))
        label1.configure(font=('Ariel', 15, 'bold'))

        self.abuse_input = Entry(self.root, width=50)
        self.abuse_input.pack(pady=(5, 10), ipady=20)

        abuse_btn = Button(self.root, text='Analyse', command=self.abuse_analysis)
        abuse_btn.pack(pady=(10, 10))

        self.abuse_result = Label(self.root, text='', bg='#70B2CF', fg='white')
        self.abuse_result.pack(pady=(20, 10))
        self.abuse_result.configure(font=('verdana', 16))

        go_back_btn = Button(self.root, text='Go Back', command=self.dashboard_gui)
        go_back_btn.pack(pady=(7, 7))

    def abuse_analysis(self):

        text = self.abuse_input.get()
        result = self.apio.abuse_analysis(text)
        self.abuse_result['text'] = result
        print(result)

    def emotion_gui(self):

        self.clear_page()

        head = Label(self.root, text='Emotion Analysis ', bg='#70B2CF', fg='white')
        head.pack(pady=(30, 30))
        head.configure(font=('Ariel', 27, 'bold'))

        label1 = Label(self.root, text='Enter Text', bg='#70B2CF', fg='white')
        label1.pack(pady=(20, 10))
        label1.configure(font=('Ariel', 15, 'bold'))

        self.emotion_input = Entry(self.root, width=50)
        self.emotion_input.pack(pady=(5, 10), ipady=20)

        emotion_btn = Button(self.root, text='Analyse', command=self.emotion_analysis)
        emotion_btn.pack(pady=(10, 10))

        self.emotion_result = Label(self.root, text='', bg='#70B2CF', fg='white')
        self.emotion_result.pack(pady=(20, 10))
        self.emotion_result.configure(font=('verdana', 16))

        go_back_btn = Button(self.root, text='Go Back', command=self.dashboard_gui)
        go_back_btn.pack(pady=(7, 7))

    def emotion_analysis(self):
        text = self.emotion_input.get()
        result = self.apio.emotion_analysis(text)
        self.emotion_result['text'] = result
        print(result)























NLPApp()