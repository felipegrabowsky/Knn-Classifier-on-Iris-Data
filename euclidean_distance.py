#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that calculates the euclidean distance
#between two test points

#######



import numpy as np

def euclidean_distance(x1,x2):
    '''function that calculates the euclidean distrance between two test points'''


    # To start with, I will assign a varible to the number of features the
    #entry has
    d = len(x1)
    number = 0

    #This loop will run until the penultinum feature, as the last feature
    #corresponds to the label of the entry.
    #It will calculate the difference squared between the respective features
    #of the entries
    for i in range (d-1): #ate i ser 4 vai rodar de 0,1,2,3
        number += (((x1[i])-(x2[i]))**2)

    #Then, the euclidean distance is the square root of all the differences
        #squared added together
    distance = ((number)**(1/2))




    return distance


