#Define function,Get coloumn names from a csv file
import csv
#Define function,Get coloumn names from a csv file
def get_column_names(data):
    """ 
    Get column names from a csv file
    Parameters:
        data(str): csv file
    Returns:
        column_names: list of column names
    """
    lst= []
    for i in data:
        lst.append(i)   
        
        
    return lst[0]
    
# Read the csv file
data = open('data.csv')
reader = csv.reader(data)
print(get_column_names(reader))