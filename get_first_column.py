import csv
def get_first_column(data):
    """
    Get the first column from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First column.
    """
    lst= []
    for i in data:
        lst.append(i[0])   
    return lst
    
# Read the csv file
data = open('data.csv')
reader = csv.reader(data)
print(get_first_column(reader))