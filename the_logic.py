import requests
import html

import random


class Quiz_manager():
    def __init__(self):
       self.ques_data = None
       pass
     
 
    def fetch_data(self):
       url = "https://opentdb.com/api.php?amount=1&type=multiple"
       response = requests.get(url)
      
       if response.status_code == 200:
            data = response.json() 
            self.ques_data = data['results'][0] 
            return True
       else:
           quit()
    def Get_ques(self):
       
        ques = html.unescape(self.ques_data['question'])
        return ques
    
    def Get_cor_ans(self):
        
        self.cor_ans = html.unescape(self.ques_data['correct_answer'])
        return self.cor_ans
    
    def Get_in_ans(self):
       self.incorrects = [html.unescape(ans) for ans in self.ques_data['incorrect_answers']]
       
           
       return self.incorrects
    
    def get_all_ans(self):

        self.cor_ans = html.unescape(self.ques_data['correct_answer'])

        self.incorrects = self.incorrects = [html.unescape(ans) for ans in self.ques_data['incorrect_answers']]
        
        self.all_ans = [self.cor_ans] + self.incorrects
        random.shuffle(self.all_ans) 
        
        return self.all_ans          
       
       

    




