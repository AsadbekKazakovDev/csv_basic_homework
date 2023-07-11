import csv
def get_first_row(data):   
    """
    Get the first row from a CSV file.
    Args:
        data(str): csv file.
    Return:
        list: First row.
    """
    r=data.split()
    return r[0]
    
# Read the csv file
f=open("data.csv")
data=f.read()
print(get_first_row(data))