from create_data import *
import numpy as np
from integerize_labels import *
from split import *

#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that returns a numpy matrix with the k
#nearest neighbors of a test point

#######

def find_k_nearest_neighbors(test_point, train_data, k):
    ''' function that returns the k nearest neigbors of a test point'''
    #Your code here
    #test point is numpy matriiz [1,2,3,4,5]
    #test_data is numpy matrix with 105 rows
    #k is an integer

    #First, I will create the variables that will be used to find the nearest
    #neighbors
    rows = len(test_point)
    rows_train_data = len(train_data)
    dict_of_train_data ={}
    number = 0

    k_nearest_neighbours_list =[]
    list_of_order=[]
    k_nearest_neighbours_list_final=[]
    list_correct =[]


    #This loop will run for every row in the train data
    for p in range(rows_train_data):

        #This w
        for i in range(rows - 1):  #calculate individual distances
            number += (((int(float(test_point[i]))) - int(float(train_data[p,i]))) ** 2)

        distance = ((number) ** (1 / 2))
        k_nearest_neighbours_list.append(distance)
        dict_of_train_data.update({p:distance})

        number = 0

    k_nearest_neighbours_list.sort()



    for i in range(k): #Iterate sorted list only up to k to find nearest
        #neighbours values
        for name, age in dict_of_train_data.items():
            if age == k_nearest_neighbours_list[i]:
                order =  name
                list_of_order.append(order)

    for number in list_of_order:
        if number not in list_correct:
            list_correct.append(number)

    #Now I have a list with all the orders but without duplicates



    for number in range(k): #even if my loop before gives more than k orders,
        #this loop will make sure only
                            #a k number of points are selected
        nearest_neighbour = train_data[list_correct[number]]
        k_nearest_neighbours_list_final.append(nearest_neighbour)



    k_nearest_neighbors = np.array(k_nearest_neighbours_list_final)


    #create a list with all the distances, sort them and get the smallest k ones


    return k_nearest_neighbors






