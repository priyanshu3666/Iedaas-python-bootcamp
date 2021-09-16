'''
This program is simply a bank rate od  different bank
'''

class Bank():
    '''
    This class contain the rates of different bank
    '''
    def __init__(self):
        self.name = "Bank Rates"
    
    def get_SBI(self):   #method about SBI rates 
       return 7

    def get_BOB(self):
        return 10

    def get_PNB(self):
        return 12
