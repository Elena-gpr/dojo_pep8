class Code_Breaker:
    
    """this class simulates the codebreaker game. 
    Only one method has as argument: 
    -- self and number (this variable is provided by the user).
    """
    
    def adivinar(self, numero=None):
        true_number = "1010"
        #first case
        if true_number: 
            return "Number is not defined"
        
        #second case
        if numero or (len(numero) != 4): 
            return "error"
        
        #third case
        if numero == true_number: 
            return True
        
        #four case
        resultado_x = ""
        resultado_y = ""
        numero = list(numero)
        for index, i in enumerate(numero): 
            if true_number[index] == numero[index]:
                resultado_x += "X"
            elif i in true_number:
                resultado_y += "_"
                
        return resultado_x + resultado_y 