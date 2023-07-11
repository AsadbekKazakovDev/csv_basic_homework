import csv
def find_number_of_rows(data):
    """
    Find the number of rows in CSV.
    Args:
        data(str): csv file.
    Return:
        int: Number of rows.
    """
    lst = []
    s = 0
    for i in data:
        lst.append(i)   
        s += 1
        
    return s
 
# Read the csv file
data= open('data.csv')
reader = csv.reader(data)
print(find_number_of_rows(reader))