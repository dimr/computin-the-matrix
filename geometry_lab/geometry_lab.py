from mat import Mat
import math
from vec import Vec




def fix_mat(d):
    result={}
    for k,v in d.items():
        if v!=0:
            result[k]=v
    return result


## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    m=Mat( (labels,labels),{} )
    for i in labels:
        for j in labels:
            if(i==j):
                m[i,j]=1
    return m

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    labels = {'x','y','u'}
    m2=Mat((labels,labels),{ ('x','x'):1, ('y','y'):1,('u','u'):1,('x','u'):x,('y','u'):y  })
    result = m2*identity()
    return Mat( (labels,labels),fix_mat(result.f))

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    labels = {'x','y','u'}
    I=identity()
    scale_matrix= Mat( I.D, {('x','x'):a,('y','y'):b,('u','u'):1})
    result = scale_matrix*I
    return Mat( (result.D),fix_mat(result.f))

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    I=identity()
    rot=Mat(I.D, { ('x','x'):math.cos(angle),('y','x'):math.sin(angle),('x','y'):-math.sin(angle),('y','y'):math.cos(angle),('u','u'):1 })
    result = I*rot
    return Mat(I.D,fix_mat(result.f))

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    result=translation(x,y)*rotation(angle)*translation(-x,-y)
    return Mat(identity().D,fix_mat(result.f))

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    I=identity()
    I[ 'x','x']=-1
    result = identity()*I
    return Mat(I.D,fix_mat(result.f))

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    I=identity()
    I[ 'y','y']=-1
    result = identity()*I
    return Mat(I.D,fix_mat(result.f))


def fix_col(d):
    result={}
    for k,v in d.items():
        if v!=0 or (v==0 and k[0]==k[1]):
            result[k]=v
    return result
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    I=identity(labels = {'r','g','b'})
    scale_matrix= Mat( I.D, {('r','r'):scale_r,('g','g'):scale_g,('b','b'):scale_b})
    result = scale_matrix*I
    return Mat(I.D,fix_col(result.f))

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    labels = {'r','g','b'}
    m=Mat( (labels,labels),{} )
    for i in labels:
        for j in labels:
            m[i,j]=1
    t=Mat(m.D, {('r','r'):77/255,('g','g'):151/255,('b','b'):26/255})
    result=m*t
    return result

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


