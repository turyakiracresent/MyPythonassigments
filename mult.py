maxNumber=int(input('Enter your maximum number: '))
for outerLoop  in range (1,maxNumber+1):
        """ 
        innerloop executes completely on each 
        iteration in correspondence with the outer loop
        """
        for innerLoop  in range(1,maxNumber+1,1):
            print(f"{outerLoop}*{innerLoop}={outerLoop*innerLoop}",end=" ")
        print()    
            
            