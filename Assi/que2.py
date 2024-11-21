'''2.	Write a Python program to plot two or more lines on same plot with suitable legends of each line. output shown in the following screenshot:'''

import matplotlib.pyplot as plt

# Function to read data from the text file and split into x and y values
def read_data_from_file(test):
    x_values = [2,4,6,8]
    y_values = [3,5,7,9]
    
    with open(test, 'r') as file:
        for line in file:
            x, y = map(float, line.split())
            x_values.append(x)
            y_values.append(y)
    
    return x_values, y_values

# Main function to plot the graph
def plot_graph_from_file(filename):
    # Step 1: Read data from the file
    x_values, y_values = read_data_from_file(filename)
    
    # Step 2: Plot the data
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')
    
    # Step 3: Add labels and title
    plt.xlabel('X Axis')  # Label for X Axis
    plt.ylabel('Y Axis')  # Label for Y Axis
    plt.title('Line Graph from File Data')  # Title of the graph
    
    # Step 4: Display the plot
    plt.grid(True)  # Adding a grid for better readability
    plt.show()

# Test the program with the file 'test.txt'
plot_graph_from_file('test.txt')
