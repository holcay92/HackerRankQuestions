if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

cuboid = [[x_, y_, z_] for x_ in range(x+1) for y_ in range(y+1) for z_ in range(z+1) if(x_+y_+z_ != n)]
print(cuboid)