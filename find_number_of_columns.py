import csv 
def find_number_of_columns(data):
    """
    Find the number of columns in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of columns.
    """
    lst = []
    s = 0
    for i in data:
        lst.append(i) 
    for j in lst[0]:   
        s += 1
        
    return int(s)
 
# Read the csv file
f = open('data.csv')
r = csv.reader(f)
print(find_number_of_columns(r))