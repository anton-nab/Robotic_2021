from math import *
from math import cos, sin, pi, sqrt, acos, asin, atan

# Dimensions used for the PhantomX robot :
#constL1 = 54.8
#constL2 = 65.3
#constL3 = 133
theta2Correction = 0  # A completer
theta3Correction = 0  # A completer

# Dimensions used for the simple arm simulation
bx = 0.07
bz = 0.25
constL1 = 0.085
constL2 = 0.185
constL3 = 0.250


def computeDK(theta1, theta2, theta3, l1=constL1, l2=constL2, l3=constL3):
    # A completer


    x = (l1+ l2 * cos(theta2)+ l3 * cos(theta2+theta3)) * cos(theta1)
    y = ((l1 + l2 * cos(theta2 ) + l3 * cos (theta2 +theta3 )) * sin(theta1))
    z = -((l2*sin(theta2)+l3*sin(theta2+theta3)))

    return [x, y, z]

def alkashi (a,b,c):
    

    return acos ((a**2+b**2-c**2)/(2*a*b))


def computeIK(x, y, z, l1=constL1, l2=constL2, l3=constL3):

 
    d=sqrt((sqrt(x**2 + y**2 )- l1)**2+z**2)



    theta1 = atan(y/x)
    theta2 = atan(-z/(sqrt(x**2 + y**2 ))+alkashi(l2,d,l3))
    theta3 = alkashi(l2,l3,d)+ pi

    return [theta1, theta2, theta3]

def main():
    print("Testing the kinematic funtions...")

    print(
        "computeDK(0, 0, 0) = {}".format(
            computeDK(0, 0, 0, l1=constL1, l2=constL2, l3=constL3)
        )
    )
    print(
        "computeDK(0, 0, 0) = {}".format(
            computeDK(50, 90, 50, l1=constL1, l2=constL2, l3=constL3)
        )
    )
    print(
        "computeDK(0, 0, 0) = {}".format(
            computeDK(90, 50, 0, l1=constL1, l2=constL2, l3=constL3)
        )
    )
    print(
        "computeDK(0, 0, 0) = {}".format(
            computeDK(0, 0, 50, l1=constL1, l2=constL2, l3=constL3)
        )
    )
    print(
        "computeIK(0, 0, 0) = {}".format(
            computeIK(0, 0, 0, l1=constL1, l2=constL2, l3=constL3)
        )
    ) 

if __name__ == "__main__":
    main()
