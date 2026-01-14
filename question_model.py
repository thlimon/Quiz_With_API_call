import random
class question():
    def __init__(self,text,cor_ans,inc_ans):
        self.ques = text
        self.cor_ans = cor_ans
        self.inc_ans = inc_ans

        self.choices = [self.cor_ans]+ self.inc_ans
        random.shuffle(self.choices)
        
        pass
    
        
