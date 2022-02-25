subscript = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")

def examples():
    print("\nIMPORTANT!! Enter ONLY the factors of the unknowns at the same sequence.")
    print("\n\nEX:")
    
    s = 0
    temp = []
    
    # loop for 2 equation in ex
    for i in range(2):
        s += 1
        print("eq" + str(i + 1) + ": ", end=(""))
        temp.append([])
        
        # loop for the elements in each equation
        for j in range(2):
            unknown = "x" + str(s).translate(subscript)
            factor = "a" + str(s).translate(subscript)
            temp[i].append(factor) # store the factors to print them again as an ex for input
            print(factor + unknown, end=(""))
            
            if j < 1:
                print(" + ", end=(""))
            
            else:
                print(" = ", end=(""))
                absolute = "a" + str(s + 1).translate(subscript)
                temp[i].append(absolute)
                print(absolute)
                
            s += 1
                
    
    print("\n\nYour input MUST be like this:\n")
    for i in range(2):
        print(*temp[i], sep=(" "))
        


def get_equations():
    equations = []
    
    while True:
        try:
            t = int(input("\nEnter the number of equations: "))
            if t > 1: # to get at least 2 equations
                break
            else:
                print("INVALID! Enter a number greater than 1, please")
        except:
            print("INVALID! Enter a number, please")    


    temp = 0
    while t > temp:
        try:
            lst = list(map(int, input("\n\nEnter the factors of eq" + str(temp + 1) + ": ").split()))
            
            # make sure that the number of factors is right
            if len(lst) != t + 1:
                print("\nINVALID! It MUST be " + str(t + 1) + " seprated-numbers")
                print("HINT: If an unkown isn't exist in an equation, it is factor is 0")
                print("Take a look above to see how to input equations and try again, please")
            
            else:
                equations.append(lst)
                temp += 1
        except:
            print("INVALID! Enter ONLY numbers(The factors)!! ")
            
        
    return t, equations




def gaussian_elimination(t, equations):
    
    status = True
    for i in range(t):
        
        # make sure that the equation[i][i] not equals to 0
        while status:
            
            for j in range(i + 1, t):
                if equations[i][i] != 0:
                    status = False
                    break
                
                equations[i] = [a + b for a, b in zip(equations[i], equations[j])]
                
        # if all unknowns in the last equation equal to 0
        if equations[i][i] == 0:
            if equations[i][-1] == 0: # infinite number of solution
                return 1
            else: # no solution
                return 0
            
        else: 
            equations[i] = [num / equations[i][i] for num in equations[i]]
            
            for j in range(t):
                if j == i:
                    continue
                
                factor = -equations[j][i]
                temp = [element * factor for element in equations[i]]
                equations[j] = [a + b for a, b in zip(temp, equations[j])]
    
    
    solution = []
    for i in range(t):
        solution.append(round(equations[i][-1], 3))
        
    return solution
            
    
    
def main():
    
    examples()
    var = get_equations()
    solution = gaussian_elimination(var[0], var[1])
    
    print("\n\n")
    
    if solution == 0:
        print("There is no solution.")
        
    elif solution == 1:
        print("There is infinite number of solutions.")
        
    else:
        for i in range(var[0]):
            template = "x" + str(i + 1).translate(subscript) + " = "
            
            if solution[i] == -0: # to aviod the ugly sign if a very small negative number rounded to 0
                print(template, 0.0)
            else:
                print(template, solution[i])
        


main()