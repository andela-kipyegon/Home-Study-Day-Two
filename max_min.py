"""find max and min num from a list of integers"""
def find_max_min(numbers):
    """fxn to get max & min"""
    #gets max fro list numbers
    max_number = max(numbers)
    #gets min fro list numbers
    min_number = min(numbers)
    #creates an array
    list_array = []
    #checks if max and min same
    if max_number == min_number:
        #returns len of list numbers
        list_array.append(len(numbers))
    else:
        #returns [max,min] resp
        list_array.append(min_number)
        list_array.append(max_number)
    return list_array
