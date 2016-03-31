# version code 988
# Please fill out this stencil and submit using the provided submission script.

from matutil import *
from GF2 import one
from collections import OrderedDict


## Problem 1
# Write each matrix as a list of row lists

echelon_form_1 = [[  1,2,0,2,0 ],
                  [  0,1,0,3,4  ],
                  [  0,0,2,3,4  ],
                  [  0,0,0,2,0  ],
                  [  0,0,0,0,4   ]]

echelon_form_2 = [[   0,4,3,4,4  ],
                  [   0,0,4,2,0  ],
                  [   0,0,0,0,1  ],
                  [   0,0,0,0,0   ]]

echelon_form_3 = [[   1,0,0,1  ],
                  [   0,0,0,1   ],
                  [   0,0,0,0]]

echelon_form_4 = [[   1,0,0,0   ],
                  [   0,1,0,0  ],
                  [   0,0,0,0   ],
                  [   0,0,0,0 ]]

def first_non_zero_index(L):
    for l in L:
        if type(l) is list:
            raise Exception("these are not lists")
    if all(v==0 for v in L):# or all(v!=0 for v in L):
        return -1
    index=0
    for i,v in enumerate(L):
        if v!=0:
            index=i
            break
    return index 

def to_the_right(i,j):
    return i>j



def all_zeros(L):
    t=[]
    for i,l in enumerate(L):
        for j in l:
            t.append(j)
    return all(v==0 for v in t)

## Problem 2
def is_echelon(A):
    '''
    Input:
        - A: a list of row lists
    Output:
        - True if A is in echelon form
        - False otherwise
    Examples:
        >>> is_echelon(a=[[1,1,1],[0,1,1],[0,0,1]])
        True
        >>> is_echelon([[0,1,1],[0,1,0],[0,0,1]])
        False
    '''
    if all_zeros(A):
        return True
    for i in range(1,len(A)):
        pivot=first_non_zero_index(A[i-1])
        if pivot==-1 and all(v!=0 for v in A[i]):
            return False
        if pivot!=-1 and not to_the_right(first_non_zero_index(A[i]),pivot):
            return False
            for el in A[i][pivot]:
                if el==0:
                    return True
    return True



## Problem 3
# Give each answer as a list

echelon_form_vec_a =[1,0,3,0]
echelon_form_vec_b = [-3,0,-2,3]
echelon_form_vec_c = [-5,0,2,0,2]



## Problem 4
# If a solution exists, give it as a list vector.
# If no solution exists, provide "None".

solving_with_echelon_form_a = None
solving_with_echelon_form_b = [21,0,2,0,0]

def non_zero_vec(v):
    if not isinstance(v,Vec):
        raise Exception("This is not a vector")
    if all(v==0 for v in v.f.values()):
        return -1
    i=0
    for k,v in sorted(v.f.items()):
        if v!=0:
            i=k
            break
    return i


def zeros(L):
    for i,el in enumerate(L):
        if el==0:
            return True
    return False




def mine_zero_vec(v):
    return all(i==0 for i in v.f.values())


## Problem 5
def echelon_solve(rowlist, label_list, b):
    '''
    Input:
        - rowlist: a list of Vecs
        - label_list: a list of labels establishing an order on the domain of
                      Vecs in rowlist
        - b: a vector (represented as a list)
    Output:
        - Vec x such that rowlist * x is b
    >>> D = {'A','B','C','D','E'}
    >>> U_rows = [Vec(D, {'A':one, 'E':one}), Vec(D, {'B':one, 'E':one}), Vec(D,{'C':one})] 
    >>> b_list = [one,0,one]>>> cols = ['A', 'B', 'C', 'D', 'E']
    >>> echelon_solve(U_rows, cols, b_list)
    Vec({'B', 'C', 'A', 'D', 'E'},{'B': 0, 'C': one, 'A': one})
    '''
    result=Vec(rowlist[0].D,{})
    for i in reversed(range(len(rowlist))):
        if not mine_zero_vec(rowlist[i]):
            pivot=non_zero_vec(rowlist[i])
            result[pivot]=(b[i]-result*rowlist[i])/rowlist[i][pivot]
    return result


## Problem 6
cols= ['C', 'B', 'A', 'D'],

rowlist = [Vec({'A', 'C', 'B', 'D'},{'A': one, 'C': 0, 'B': one, 'D': one}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': 0, 'B': one, 'D': 0}), Vec({'A', 'C', 'B', 'D'},{'A': 0, 'C': one, 'B': 0, 'D': 0}), Vec({'A', 'C', 'B', 'D'},{'A': one, 'C': one, 'B': one, 'D': 0})]
 
   # Provide as a list of Vec instances
label_list = sorted(cols) # Provide as a list
b = [ one,0,one,0 ]          # Provide as a list



## Problem 7
null_space_rows_a = {3,4} # Put the row numbers of M from the PDF



## Problem 8
null_space_rows_b = {4}



## Problem 9
# Write each vector as a list
closest_vector_1 = [1.6,3.2]	
closest_vector_2 = [0,1,0]
closest_vector_3 = [ 3 , 2,  1, -4]



## Problem 10
# Write each vector as a list

def project_along(b, a):
    sigma = (b*a)/(a*a) if a*a != 0 else 0
    return sigma * a

def project_orthogonal(b,a):
    return b-project_along(b,a)

project_onto_1 = [2,0]   
projection_orthogonal_1 =  [0,1]

project_onto_2 = [-0.16666666666666666, -0.3333333333333333, 0.16666666666666666]
projection_orthogonal_2 =[ 1.1666666666666667, 1.3333333333333333,  3.8333333333333335]

project_onto_3 =  [1.0, 1.0, 4.0]
projection_orthogonal_3 =[0.0, 0.0,0.0	]



## Problem 11
norm1 = 3
norm2 = 4
norm3 = 1

