import tkinter as tk
from tkinter import messagebox
from the_logic import Quiz_manager
from question_model import question
import html


class GUI:
    def __init__(self):
        #the window/canvas and its property
        self.window = tk.Tk()
        self.window.title("A Quiz game")
        self.window.geometry("900x700")
        self.window.config(padx=20,pady=10,bg="#0B4C6E")
        
        #the worker(object of class Quiz_manager) who can use all the function of Quiz_manger
        self.worker = Quiz_manager()
        
        #the widgets(buttons, labels, ans box etc all cretated on a seperate function, but part of window thus ran here )
        self.create_widgets()
        self.window.mainloop()
        

        pass
    def create_widgets(self):

        self.score_label= tk.Label(self.window, text="score :",fg="white",bg="#0B4C6E", font=("arial",10))
        self.score_label.grid(row=1,column=2,sticky="E",padx=30,pady=30)

        self.score_label_point= tk.Label(self.window, text="0",fg="black",bg="white", font=("arial",10))
        self.score_label_point.grid(row=1,column=2,sticky="E",padx=20,pady=20)
                                                                                                                                        #pressing this btn generates ques
        self.btn_for_ques= tk.Button(self.window,text="get question",height=2,width=10,command = self.print_ques)
        self.btn_for_ques.grid(row=6,column=0,sticky="N",padx=10,pady=10)
                                                                                                                                        #on this label(Not text box, as it can be edited by user)
        self.ques_label = tk.Label(self.window, text="Qustion : ",height=4,width=70,fg="black",bg="#29AD9C", font=("arial",10))
        self.ques_label.grid(row=6,column=1, sticky="N",padx=20,pady=20)
        #a function that contantly checks for radiobtn activity. will return 1,2,3 etc. int
        self.user_choice = tk.IntVar()

        #radio buttons for all options
        self.button_1 = tk.Radiobutton(text="",variable=self.user_choice,value = 1,bg="white",fg="black",font=("arial",15,"bold"))
        self.button_1.grid(row=7,column=1,padx=2,pady=2,sticky="N")

        self.button_2 = tk.Radiobutton(text="",variable=self.user_choice,value = 2,bg="white",fg="black",font=("arial",15,"bold"))
        self.button_2.grid(row=8,column=1,padx=2,pady=2,sticky="N")

        self.button_3 = tk.Radiobutton(text="",variable=self.user_choice,value = 3,bg="white",fg="black",font=("arial",15,"bold"))
        self.button_3.grid(row=9,column=1,padx=2,pady=2,sticky="N")

        self.button_4 = tk.Radiobutton(text="",variable=self.user_choice,value = 4,bg="white",fg="black",font=("arial",15,"bold"))
        self.button_4.grid(row=10,column=1,padx=2,pady=2,sticky="N")
        
        #the JUDGE
        self.ans_label = tk.Label(self.window, text="Ans: ",height=4,width=70,fg="black",bg="#50D811", font=("arial",10))
        self.ans_label.grid(row=11,column=1, sticky="N",padx=20,pady=20)
        
        # to check ans
        self.btn_ans = tk.Button(self.window,height=2,width=10,bg="white",fg="black",text="Finalize ans",font=("arial",10),command=self.check_correct)
        self.btn_ans.grid(row=11,column=0,padx=5,pady=5)

    def print_ques(self):
        self.q = self.worker.next_ques()
        all_ans= self.q.choices
        ques = self.q.ques
        
        self.ques_label.config(text=ques)
        
        self.button_1.config(text=f"{all_ans[0]}")
        self.button_2.config(text=f"{all_ans[1]}")
        self.button_3.config(text=f"{all_ans[2]}")
        self.button_4.config(text=f"{all_ans[3]}")

        self.ans_label.config(text="")

    




    def check_correct(self):
    
        a = self.user_choice.get()

        if a == 1:
            text1 = self.button_1.cget("text")
        elif a == 2:
            text1 = self.button_2.cget("text")
        elif a == 3:
            text1 = self.button_3.cget("text")
        elif a == 4:
            text1 = self.button_4.cget("text")
        
        cor_ans = self.q.cor_ans
        

        if text1 == cor_ans:
            self.ans_label.config(text="its Correct")

            current_score = int(self.score_label_point.cget("text")) 
            new_score = current_score+5

            self.score_label_point.config(text=new_score)
        else:
            self.ans_label.config(text = "wrong")


        

        














        

        


        

        



app = GUI()