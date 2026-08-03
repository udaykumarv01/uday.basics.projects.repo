
for i in range(1,4):
    print(f"your trial number is : {i}")
    a,b = map(int ,input("enter the order of matrix A : ").split())
    c,d = map(int ,input("enter the order of matrix B : ").split())
    if b==c:
        none=[]
        def elements(x):
            for i in range (0,x+1):
               matrix=none
               if i <x:
                  row= list(map(int,input(f"enter the elements of {i+1} row: ").split())) 
                  i+=1 
                  matrix.append(row)   
               else :
                  break   
            print(none)     
        print("for the matrix A")
        elements(int(a))
       
        matrix_A=none
    
        print("for the matrix B")
        elements(int(c))
        matrix_B=none

        resultant = [[0 for _ in range(d) ] for _ in range (a)]
        for i in range(a):
            for j in range(d):
                for k in range(c):
                    resultant[i][j]=matrix_A[i][k]*matrix_B[k][j]
            print(f"the resultant matrix after multiplying A and B is : {resultant}")
        break
    
    elif b!=c:
        print("enter the valid input of b and c it naccesary that b=c ")
        print("\n")