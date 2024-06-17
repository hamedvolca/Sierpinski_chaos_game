"""
This code is written and shared by hamedvolca, 2024
This code creates the Sierpinski triangle using the chaos game.


The chaos game algorithm:
1) Create a random point in an equilateral triangle as the new current point
2) Select the current point
3) Select one of the corners randomly
4) Create a new point (as the point) at the middle of the selected corner and the selected point (at step 2)
5) Go to the step 2
"""
import numpy as np
import matplotlib.pyplot as plt
import random

# To select a point randomly in a triangle
# The function is adopted from the stackoverflow
# https://stackoverflow.com/questions/47410054/generate-random-locations-within-a-triangular-domain
def point_on_triangle(pt1, pt2, pt3):
    """
    Random point on the triangle with vertices pt1, pt2 and pt3.
    """
    x, y = sorted([random.random(), random.random()])
    s, t, u = x, y - x, 1 - y
    return np.array([s * pt1[0] + t * pt2[0] + u * pt3[0],
            s * pt1[1] + t * pt2[1] + u * pt3[1]])

# To define the vertices of the triangle            
pnt_A = np.array([[-0.5,0]])
pnt_B = np.array([[0.5,0]])
pnt_C = np.array([[0,np.sin(np.pi/3)]])

# To plot the triangle points
fig, ax = plt.subplots()
ax.scatter(pnt_A[0,0],pnt_A[0,1],s=1.5,c='k')
ax.scatter(pnt_B[0,0],pnt_B[0,1],s=1.5,c='k')
ax.scatter(pnt_C[0,0],pnt_C[0,1],s=1.5,c='k')
ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

# To create an array that contains all points
pnt_all = np.append(np.append(pnt_A,pnt_B,axis=0),pnt_C,axis=0)

# To select the first random point
pnt_1 = point_on_triangle(pnt_A[0], pnt_B[0], pnt_C[0])
pnt_1 = np.reshape(pnt_1,(1,2))
pnt_all = np.append(pnt_all, pnt_1,axis=0)

# To set the number of iteration
N = 100000

# To run the algorithm
for i in range(0,N):
    ind = random.randint(0,2)
    ind_end = random.randint(3,pnt_all.shape[0]-1)
    pnt_i = np.array([[0.5 * (pnt_all[ind,0] + pnt_all[ind_end,0]), 
                       0.5 * (pnt_all[ind,1] + pnt_all[ind_end,1])]])
    pnt_all = np.append(pnt_all, pnt_i,axis=0)
    
    if i==0 : pnt_all = np.delete(pnt_all,3,axis=0) 
    
# To plot the final set of points    
fig, ax = plt.subplots()
ax.scatter(pnt_all[:,0],pnt_all[:,1],s=5,c='k', marker='^')
ax.set_aspect('equal')
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)