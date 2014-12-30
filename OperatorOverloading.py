class Frac:
    def __init__(self, numerator = 0, denominator = 1):
        if type(numerator) == float:                            #If the numerator is a FLOAT convert it to a fraction
            self.convertDec(numerator)
        else:
            self.numer = numerator
            self.denom = denominator
        self.reduce()

    def __str__(self):                                          #Defines a rule on how we want our object printed
        if self.numer == 0:
            return "0"
        answer = "%d/%d" % (self.numer,self.denom)
        return answer
    
    def __add__(self, frac):
        n2 = self.numer
        d2 = self.denom
        
        if type(frac) == str:                                   #If the 2nd argument is STRING
            return str(self) + frac                             #return concatenated string and fraction
        elif type(frac) == float:                               #If the 2nd argument is FLOAT
            self.convertDec(frac)
            n1 = self.numer
            d1 = self.denom
        elif type(frac) == int:                                 #If 2nd argument is INT
            n1 = frac                                           #Set numerator to int
            d1 = 1                                              #Set Denominator to 1
        else:
            n1 = frac.numer
            d1 = frac.denom
            
        total = Frac(d2*n1+d1*n2,d1*d2)
        return total

    def __radd__(self, string):     #radd handles right side addition
        return string + str(self)   #In our case return a concatenated version of the string + fraction

    def __mul__(self,frac):
        n1 = self.numer
        d1 = self.denom
        n2 = frac.numer
        d2 = frac.denom
        total = Frac(n1*n2, d1*d2)
        return total

    def __lt__(self, frac):         #If "<" operator is used this method is called
        if self.denom < frac.denom: 
            return False
        else:
            return True

    def convertDec(self,numerator):
        tempFrac = str(numerator).split('.')                                #Cast it as a string and split before and after decimal point
        self.denom = 10 ** len(tempFrac[1])
        if int(tempFrac[0]) > 0:                                            #Handles deimal numbers 1 or greater (ex: 1.75)
            self.numer = int(tempFrac[0]) * self.denom + int(tempFrac[1])
        else:                                                               #Handles decimal numbers less than 1 (ex: .75)
            self.numer = int(tempFrac[1])
        
    def gcd(self,a,b):              #Greatest Common Denominator
        if b == 0:
            return a
        return self.gcd(b,a%b)
    
    def reduce(self):
        d = 1
        if self.denom != 0 and self.numer != 0:     # Makes sure fraction != 0
            d = self.gcd(self.numer, self.denom)    # Find the greatest common denominator
        if d > 1:                                   # Reduce Numerator and Denominator if gcd is > 1
            self.numer //= d                        # //= Floor division and assigns a value to the left operand
            self.denom //= d


           
f1 = Frac()
print("F1 = Frac(): ", f1)

f2 = Frac(2,6)
print("F2 = Frac(2,6): ", f2)

f3 = Frac(1,2)
print("F3 = Frac(1,2): ", f3)

f4 = Frac(3.75)
print("F4 = Frac(3.75): ", f4)

f5 = f2 + 3
print("F5 = F2 + 3: ", f5)

f6 = f2 + 1.25
print("F6 = F2 + 1.25: ", f6)

f7 = f2 < f3
print("F7 = F2 < F3: ", f7)

f1 = f2 + f3
print("Add: ", str(f2.numer) + "/" + str(f2.denom) + " + " + str(f3.numer) + "/" + str(f3.denom) + " = " + str(f1.numer) + "/" + str(f1.denom))

f1 = f2 * f3
print("Mul: ", str(f2.numer) + "/" + str(f2.denom) + " * " + str(f3.numer) + "/" + str(f3.denom) + " = " + str(f1.numer) + "/" + str(f1.denom))

print("Fraction is " + f1)
print(f1 + " is the fraction")

