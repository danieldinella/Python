################################################################################
################################################################################
################################################################################
''' WARNING!!! SAVE THIS FILE AS program.py '''
''' WARNING!!! WRITE BELOW YOUR NAME, SURNAME AND STUDENT ID '''

nome        = "NAME"
cognome     = "SURNAME"
matricola   = "STUDENT ID"

###############################################################################
################################################################################
################################################################################
# DEBUG SUGGESTIONS
#   to run only some of the tests, you can comment rows 288-292 at the end of grade.py
#
#   to check the error stack trace, you can uncomment row 36 of testlib.py 
################################################################################
################################################################################
################################################################################

'''Ex 1:  6 points. 
A file contains some integer numbers written as follows:
- each number is separated by one or more empty lines
- each number is written in one or more consecutive lines, one for
  each digit
- each line with a digit begins with a % sign and has the digit in its
  unary representation, namely, with as many 1's as its value.
- each number is written from the most significant digit to the least
  one.
As an example, file "U1.txt" contains the numbers  5049, 10, 94, 0, 49, 66.
The ones are always consecutive (no white spaces or other char between 1's).
The file always ends with an empty line.

Design the function ex1(pathname) that gets as input the pathname of a
file as described above and returns the list of the numbers written in
it. The list has to be ordered with respect to the number of digits
and, then, to their value.

As an example, for file 'U1.txt', the function has to return the following list:
[5049,10,49,66,94,0]

'''

def ex1(pathname):
    # write your code here
    pass

    
#####################################################################################


'''    
    Ex 2: 8 points
    
    We have a set P containing points, each point is a tuple (x,y)
    with the coordinates of the point.  We want to produce an image
    with the given points and, possibly, some vertical and some
    horizontal segments.


    In particular:
    1) the height h and the width w of the image are the minimum
       values able to contain the coordinates of all points.

    2) The points are drawn in the image with the red color (255,0,0)
       on a black background (0,0,0).

    3) For every point p=(x,y) for which there are two points 
            p1=(x1,y) with x1>x and same y
        and p2=(x,y1) with y1>y and same x
        a white segment (255,255,255) is drawn that joins p to the nearest
        point between p1 and p2 (to p1 if the two distances are equal).

    In other words if to the right of p there is a point p1 with the same
    y-coordinate as p1 and below p there is a point p2 with the same x
    coordinate, in the image will appear
    - a horizontal segment between p and p1, if p1 is less distant
      (or at the same distance) than p2 from p, or
    - a vertical segment between p and p2, if p1 is more distant than
      p2 from p.
    For example the image corresponding to the set 
    P={(20,10),(20,20),(20,40),(40,40),(50,20),(50,70),(60,20)}
    will have height 70 and width 60 and is shown in figure I1.png
    
    Design the function ex2(P, fname) that takes as input the set of
    points P and the address fname of a .png file. The function saves
    at the address fname the image obtained from the set of points P
    and returns the number of horizontal segments in the image.
     
    To load and save PNG files, use the load and save functions of the
    images library.  '''
import images

def ex2(P,fname):
    # insert your code here
    pass

############################################################################


'''
    Ex. 3: 9 points

    Given a node in a tree, the node degree is the number of children
    of the node.
    Design the recursive function ex3(r) (or a function that makes use
    of of recursive function(s) or method(s)) that receives as
    parameter the root r of a tree made by nodes of type Node, as
    defined in the tree.py library. The function returns a dictionary.
    The dictionary contains as keys, the degrees of the nodes in the
    tree. For each key, the associated value is the list of values of
    the nodes in the tree with that degree.  The list must be in
    non-decreasing order.

    As an example, given the following tree:
              16               
      ________|_____________   
     |          |           |  
     2          4           5  
     |     _____|______        
     10   |   |  |  |  |       
          1   2  9  8  2       
            __|__              
           |     |             
           3     6    


   the function ex3 returns the dictionary
   {3: [16], 1: [2], 0: [1, 2, 3, 5, 6, 8, 9, 10], 5: [4], 2: [2]} 

   NOTE: any subfunction, if present, should be defined at the external
          level to pass the recursion check '''

import tree

def ex3(r):
    # insert your code here
    pass

###########################################################################

'''
    Ex. 4: 9 points
    
    Design and implement a recursive function (or a function that uses
    recursive functions or methods) ex4(dirname, s) that receives as
    an input the name of a directory (dirname) and a string (s).  The
    function explores the directory dirname and its subdirectories and
    returns a list of tuples.  There is one tuple for each file with
    extension .txt containing occurrences of the string s
    (case-insensitive) encountered during the visit. The tuples are
    pairs (a,b) where:
      - a is the full name of the file
      - b is the number of times the string was found in that file.
    The list is in alphabetical order, with respect to the first
    coordinate of the tuples.
    Any file or directory starting with '.' or '_' has to be ignored.
    
    As an example, if dirname='dir1' and s='angelo', the function ex4
    returns the list:
    [('dir1/st1/st2/1W.txt', 4), ('dir1/st1/st2/Ncn.txt', 5), ('dir1/zzzEFG.txt', 1)]
    
    NOTE: it is forbidden to use os.walk or similar recursive system
          functions
    NOTE: any subfunction, if present, should be defined at the external
          level to pass the recursion check
'''    

import os

def ex4(dirname, s): 
    # insert your code here
    pass


#################################################################################
