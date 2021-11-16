import math 
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

    x = (l1+ l2 * cos(theta2)+ l3 * cos(theta2+theta3)) * cos(theta1)         #formule pour obtenir la coordonnée du point 'x' en P3, en bout de bras
    y = ((l1 + l2 * cos(theta2 ) + l3 * cos (theta2 +theta3 )) * sin(theta1)) #formule pour obtenir la coordonnée du point 'y' en P3
    z = -((l2*sin(theta2)+l3*sin(theta2+theta3)))                             #formule pour obtenir la coordonnée du point 'z' en P3

    return [x, y, z]                                                          #On retourne les coordonnées numériques des points (x,y,z)

def alkashi (a,b,c):                                                          # Définition du thèoréme d'Al-Kashi pour l'utiliser ultérieurement
    

    return  -acos ((a**2+b**2-c**2)/(2*a*b))                                   #Formule de Al-Kashi avec les variables (a,b,c)


def computeIK(x, y, z, l1=constL1, l2=constL2, l3=constL3):
    

    dp = sqrt(x**2 + y**2 )                                                   #Correspond à 'dproj' soit la distance entre P0 et P3proj du schéma en bas à gauche du fichier 'leg_proj.pdf'
    d1 = dp -l1                                                               #correspond  à 'd13', la distance entre P1 et P3proj du même schéma


    if d1<0:                                                                  #cette condition sert à ne pas faire intérompre le simulateur

        d1 = 0.001
    d= sqrt(d1**2+z**2)                                                       #'d' est l'hypothénuse du triangle (P1, P3, P3proj) du même schéma précédemment présenté
    
    if d > l2+l3 :                                                            #'l2+l3' est la longueur maximum que peut prendre 'd' 

        d = l2+l3
    a = atan(z/d1)



    if x ==0:

        theta1 = atan(y/0.1)                                                #formule de l'angle 'theta1'si x=0 pour éviter d'intérompre le simulateur
        theta2 = -a +alkashi(l2,d,l3)                                       #formule de l'angle 'theta2' si x=0
        theta3 = alkashi(l2,l3,d)- pi                                       #formule de l'angle 'theta3' si x=0
    
        
    else :
        
        theta1 = atan(y/ x)                                                   #formule générale de l'angle 'theta1' sauf si x=0
        theta2 = -a +alkashi(l2,d,l3)                                         #formule générale de l'angle 'theta2'
        theta3 = alkashi(l2,l3,d)-pi                                         #formule générale de l'angle 'theta3'
    
    

    return [theta1, theta2, theta3]                                           #on retourne la valeur des 3 angles

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

