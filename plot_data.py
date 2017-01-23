#########

#Name; Felipe Marujo Grabowsky
#UNI: fm2579


# This program contains a function that plots all graphs available by
#matching the columns for a numpy matrix




import matplotlib.pyplot as plt
from create_data import *

def plot_data(data):
    ''' function that plots different graphs using matplotlib'''


    #To start with, I will create lists for all the different options of
    #plants and hteir features
    d = len(data)
    sepal_length_setosa =[]
    sepal_width_setosa = []
    petal_length_setosa = []
    petal_width_setosa = []

    sepal_length_versicolor = []
    sepal_width_versicolor = []
    petal_length_versicolor = []
    petal_width_versicolor = []

    sepal_length_virginica = []
    sepal_width_virginica = []
    petal_length_virginica = []
    petal_width_virginica = []




    #For all rows in the test data
    for i in range(d):

        #For every row that has an information of the plant Iris Setosa, I
        #will append its features to the correct list
        if data[i,-1] == "Iris-setosa":
            sepal_length_setosa.append((data[i,0]))
            sepal_width_setosa.append((data[i,1]))
            petal_length_setosa.append((data[i,2]))
            petal_width_setosa.append((data[i,3]))

        # For every row that has an information of the plant Iris Versicolor,
        #I will append its features to the correct list
        elif data[i,-1] == "Iris-versicolor":
            sepal_length_versicolor.append((data[i,0]))
            sepal_width_versicolor.append((data[i,1]))
            petal_length_versicolor.append((data[i,2]))
            petal_width_versicolor.append((data[i,3]))


        # For every row that has an information of the plant Iris Virginica,
        #I will append its features to the correct list
        elif data[i,-1]== "Iris-virginica":
            sepal_length_virginica.append((data[i,0]))
            sepal_width_virginica.append((data[i,1]))
            petal_length_virginica.append((data[i,2]))
            petal_width_virginica.append((data[i,3]))



    #Then, I will create two dictionaries, one with all features of each plant,
            #and the other with the plotting styles
    data_2 = {
            "Iris Setosa": [sepal_length_setosa, sepal_width_setosa,
                            petal_length_setosa,petal_width_setosa],
            "Iris Versicolor": [sepal_length_versicolor, sepal_width_versicolor,
                                petal_length_versicolor, petal_width_versicolor],
            "Iris Virginica": [sepal_length_virginica, sepal_width_virginica,
                               petal_length_virginica,petal_width_virginica]
            }
    styles = {
        "Iris Setosa": "ro",
          "Iris Versicolor": "o",
              "Iris Virginica": "x"
            }


    #These two variables will be used for me to iterate through the plant
    #dictionary when plotting
    i = 0
    d =1


    # For this graph, I will subplot each plants Sepal Length with its plant
    #Sepal Width
    fig, ax = plt.subplots()
    for group, data in data_2.items():
                ax.plot(data[i], data[d], styles[group], label=group)


    #To customize the graphs, I will always yse 0.5 margins, and the appropriate
                #labels and titles
    ax.margins(0.5)
    plt.title("Sepal Length Versus Sepal Width!")  # Add a title
    plt.xlabel('Sepal Length')  # Add axis labels
    plt.ylabel('Sepal Width')  # Add axis labels

    #The legend will be added according to the plant dictionaries. i will
    #also then save the graphs, clear the axes and
    #close them
    ax.legend()
    plt.savefig("sepal_length_vs_sepal_width")
    plt.show()
    plt.cla()
    plt.close()

    # For this graph, I will subplot each plants Sepal Length with its plant
    #Petal Length
    fig, ax = plt.subplots()

    for group, data in data_2.items():
        ax.plot(data[i], data[d+1], styles[group], label=group)

    # To customize the graphs, I will always yse 0.5 margins, and the
    #appropriate labels and titles
    ax.margins(0.5)
    plt.title("Sepal Length Versus Petal Length!")  # Add a title
    plt.xlabel('Sepal Length')  # Add axis labels
    plt.ylabel('Petal Length')  # Add axis labels

    # The legend will be added according to the plant dictionaries.
    #i will also then save the graphs, clear the axes and
    # close them
    ax.legend()
    plt.savefig("sepal_length_vs_petal_length")
    plt.show()
    plt.cla()
    plt.close()

    # For this graph, I will subplot each plants Sepal Length with its plant
    #Petal Width
    fig, ax = plt.subplots()

    for group, data in data_2.items():
        ax.plot(data[i], data[d+2], styles[group], label=group)

    # To customize the graphs, I will always yse 0.5 margins, and the
    #appropriate labels and titles
    ax.margins(0.5)
    plt.title("Sepal Length Versus Petal Width!")  # Add a title
    plt.xlabel('Sepal Length')  # Add axis labels
    plt.ylabel('Petal Width')  # Add axis labels

    # The legend will be added according to the plant dictionaries.
    #i will also then save the graphs, clear the axes and
    # close them
    ax.legend()
    plt.savefig("sepal_length_vs_petal_width")
    plt.show()
    plt.cla()
    plt.close()

    # For this graph, I will subplot each plants Sepal Width with its
    #plant Petal Length
    fig, ax = plt.subplots()

    for group, data in data_2.items():
        ax.plot(data[i+1], data[d+1], styles[group], label=group)

    # To customize the graphs, I will always yse 0.5 margins, and the
    #appropriate labels and titles
    ax.margins(0.5)
    plt.title("Sepal Width Versus Petal Length!")  # Add a title
    plt.xlabel('Sepal Width')  # Add axis labels
    plt.ylabel('Petal Length')  # Add axis labels

    # The legend will be added according to the plant dictionaries.
    #i will also then save the graphs, clear the axes and
    # close them
    ax.legend()
    plt.savefig("sepal_width_vs_petal_length)
    plt.show()
    plt.cla()
    plt.close()

    # For this graph, I will subplot each plants Sepal Width with its
    #plant Petal Width
    fig, ax = plt.subplots()

    for group, data in data_2.items():
        ax.plot(data[i+1], data[d+2], styles[group], label=group)

    # To customize the graphs, I will always yse 0.5 margins, and the
    #appropriate labels and titles
    ax.margins(0.5)
    plt.title("Sepal Width Versus Petal Width!")  # Add a title
    plt.xlabel('Sepal Width')  # Add axis labels
    plt.ylabel('Petal Width')  # Add axis labels

    # The legend will be added according to the plant dictionaries.
    #i will also then save the graphs, clear the axes and
    # close them
    ax.legend()
    plt.savefig("sepal_width_vs_petal_width")
    plt.show()
    plt.cla()
    plt.close()

    # For this graph, I will subplot each plants Petal Length with its
    #plant Petal Width
    fig, ax = plt.subplots()

    for group, data in data_2.items():
        ax.plot(data[i+2], data[d+2], styles[group], label=group)

    # To customize the graphs, I will always yse 0.5 margins, and the
    #appropriate labels and titles
    ax.margins(0.5)
    plt.title("Petal Length Versus Petal Width!")  # Add a title
    plt.xlabel('Petal Length')  # Add axis labels
    plt.ylabel('Petal Width')  # Add axis labels

    # The legend will be added according to the plant dictionaries.
    #i will also then save the graphs, clear the axes and
    # close them
    ax.legend()
    plt.savefig("petal_length_vs_petal_width")
    plt.show()
    plt.cla()
    plt.close()



    return None




