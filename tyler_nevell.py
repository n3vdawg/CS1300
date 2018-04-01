def tempToEmote(x, y):
    if x < 100:
        if y <= 100:
            return "Brrr!"
        elif y < 100:
            return "Mixed Bag."
    elif x == 100:
        if y < 100 or y > 100:
            return "Good."
        elif y == 100:
            return "Just Right!"
    elif x > 100:
        if y < 100:
            return "Mixed Bag."
        elif y >= 100:
            return "Hot Hot!"
        
def unfairTax(income):
    if income <= 25000:
        tax_rate = .5
    elif income <= 50000 and income > 25000:
        tax_rate = .4
    elif income <= 100000 and income > 50000:
        tax_rate = .3
    elif income > 100000:
        tax_rate = .2
    
    tax_bill = income * tax_rate
    return tax_bill

def getColor(num):
    if num % 3 == 0:
        if num % 2 == 0:
            return "Gamboge"
        else:
            return "Puce"
    else:
        if num % 2 == 0:
            return "Mauve"
        else:
            return "Wenge"
        
def gameMove(myScore, yourScore, scoreToWin, feelingLucky):
    if yourScore > myScore:
        if feelingLucky == True:
            return "Red"
        else:
            if yourScore - myScore > 5:
                return "Green"
            else:
                return "Blue"
    else:
        if scoreToWin - yourScore < 7:
            return "Green"
        else:
            if myScore - yourScore > 3:
                return "Blue"
            else:
                return "Red"