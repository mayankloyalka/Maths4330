
def vandermode(arg1):
    # What does the Vandermode function do?
    # It takes a list of vectors and raise it to the power of [0,1,2,3,4]
    
    # Arguments:
    # args1 :Arg1 is a list of vectors, that is entered by the user
    result=[]
    for i in range(5):
        new_list=[]
        for element in range(len(arg1)):
            new_list.append(arg1[element]**i)
        result.append(new_list)
    # Final Result of our function?
    # We get a list of matrix that is represented as a coloumn vector
    return result








def transpose(arg1):
        # What does the transpose function do?
    # It takes a matrix and change its rows to coloumns
    
    # Arguments:
    # args1 :Arg1 is a matrix represented as a coloumn vector
    result=[]
    for i in range(len(arg1)):
        new_list=[]
        for element in range(len(arg1)):
            new_list.append(arg1[i][element])
        result.append(new)
    # Final Result of our function?
    # We get a transpose matrix
    return result


def matrix_saclor(arg1,scalor):
        # What does the matrix function do?
    # It takes the coloumns of a matrix and then multiply them to a scalor
    
    # Arguments:
    # args1 :Arg1 is a matrix which is represented as a coloumn vector
    # scalor: It is any complex number
    result=arg1[::]
    for index in range(len(arg1)):
        result[index]=scalor*arg1[index]
     # Final Result of our function?
    # We get a matrix
    return result


def conjuagte(arg1):
        # What does the conjugate function do?
    # It takes an complex number as an argument and changes the sign of the imaginery part
    
    # Arguments:
    # args1 :Arg1 is a list of complex number
    result=0
    for index in range(len(arg1)):
        result[index]=-result[index]
    # Final Result of our function?
    # The sign of the imaginery part is changed
    return result




def conjugate_transpose(arg1):
        # What does the conjugate function function do?
    # It takes the rows of a matrix change them to a coloumn and take their conjugate
    
    # Arguments:
    # args1 :Arg1 is a matrix that is represented as a coloumn vector
    result=transpose(arg1)
    for i in range(len(arg1)):
        for element in range(len(arg1)):
            result[i][element]=conjugate(result[i][element])
    # Final Result of our function?
    # We get a matrix 
    return result
            

def normalisation(arg1):
        # What does the normalisation function do?
    # It takes a singular matrix and then find the absolute value of each raise to the power of 1/2
    
    # Arguments:
    # args1 :Arg1 is a matrix, that is given by a coloumn vector
    result=0
    for i in range(len(arg1)):
        for j in range(len(arg1[i])):
           result=result+ (abs(arg1[i][j]))**2
    result=result**(1/2)
    # Final Result of our function?
    # We a vector norm of our given matrix
    return result            




def gram_Schmitt(arg1):
    # What does the Vandermode function do?
    # It takes a matrix and does an orthogonal decomposition and normalisation
    # on the matrix to find matrix Q and R, such that Matrix= Q*R
    
    # Arguments:
    # args1 :Arg1 is a matrix represented as a coloumn vectore, obtained from
    # doing function vandermode
    V=[]
    for i in range(len(arg1)):
        V.append(arg1[i])
        
    for i in range(len(arg1)):
            R[i][i]=normalisation(V[i])
            Q[i]=V[i]/(R[i])

            for j in (i+1,len(arg1)+1):
                R[i][j]=transpose(Q[i])*V[j]
                V[j]=V[j]- V[i][j]*Q[j]
    # Final Result of our function?
    # We get a unitary matrix Q and a upper triangular matrix R
    return Q,R




def backsub(R,y):
        # What does the bacsub function do?
    # It solves the value of a for the equation
    # R*a=Q*y
    
    # Arguments:
    # R: It is an upper triangular matrix
    # y : It is a vector that will be entered by the user
    result=y
    for i in range(len(R[0])):
        a=len(R)
        result[i]=(b*[i]-matrix_scalor(R[i+1:a],result[i+1:a])*(1/(R[i][i])))
        # Final Result of our function?
    # We get the final values of a
    return result



Beta=backsub(R,Q*y)

def degree4(Beta,x):
        # What does the degree4 function do?
    # It gives us an interpolyating polynomial
    
    # Arguments:
    # Beta: The result obtained after the backsub function
    # x: It is vector that will be entered by the user
    return (Beta[0]+Beta[1]*x+Beta[2]*(x**2)+Beta[3]*(x**3)+Beta[4]*(x**4))



        
        








