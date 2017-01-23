
#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that calculate the error rates between the predicted labels my function returns
# and the actual labels
#######
import numpy as np

def calculate_error_rate(predicted_labels, test_data):
    ''' function that calculates the error rate between my predicted labels and the actual ones'''

    #first I will count the number of rows and columns in the test data
    d = len(test_data)
    l = len(test_data[0])

    #This variable will be used to count the number of wrong predictions
    wrong =0


    #for the number of rows in the test data
    for i in range(d):

        #I will get the predicted label from the predicted labels
        predicted_value = predicted_labels[i]

        #and the correct label is the last column of the test data
        correct_value = int(test_data[i,l-1])

        #I will compare both variables, and if they are not the same, I will add one to the wrong variable
        if predicted_value != correct_value:
            wrong += 1
    #The error rate will be the number of wrong predictions over the total number of cases
    error_rate = (wrong/d)

    return error_rate
