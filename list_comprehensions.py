# Let's learn about list comprehensions! You are given three integers x,y  and z representing the dimensions of a cuboid along' \
#    ' with an integer n. Print a list of all possible coordinates given by [i,j,k]  on a 3D grid where the sum of it  is not equal to n.' \
#    ' Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

cuboid = [[x_, y_, z_] for x_ in range(x+1) for y_ in range(y+1) for z_ in range(z+1) if(x_+y_+z_ != n)]
print(cuboid)