import requests
import html
from question_model import question
import random


class Quiz_manager():
    def __init__(self):
       
       url = "https://opentdb.com/api.php?amount=10&type=multiple"
       response = requests.get(url)
      
       if response.status_code == 200:
            data = response.json() 

       else:
           quit()
       
       self.question_bank = [] 
       
       for item in data['results']:
        
        ques_data = item
           
        ques = html.unescape(ques_data['question'])
        cor_ans = html.unescape(ques_data['correct_answer'])
        inc_ans = html.unescape(ques_data['incorrect_answers'])

        questions = question(ques,cor_ans,inc_ans)
        self.question_bank.append(questions)
        self.ques_num= 0
       pass
    def next_ques(self):
       current_q = self.question_bank[self.ques_num]

       self.ques_num +=1

       return current_q
          
       
 

        


       
       

    




