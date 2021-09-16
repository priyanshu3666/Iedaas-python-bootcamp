'''
this is  a temperature class 
'''
class Temprature():
    '''
    this class  is used to contains method regading temperatur conversion'''
    def  convertFahrenhiet(self,celsius):
        '''
        convert celcius to fahrenhiet'''
        return (celsius*(9/5))+32
    def convertCelsius(self,fahrenhiet):
        '''
        this convert fahrenhiet to celcius '''
        return (fahrenhiet-32)*(5/9)


