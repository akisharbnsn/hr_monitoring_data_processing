def filter_nondigits(data: list) -> list:
    """
    This function filters out nondigit elements from the given data and returns a list of digits.
    
    Args: 
    - data: (list): User inputs a list of strings
    
    Returns: 
    - new_list: A new list containing only digits from Test 1, Test 2, Test 3, Test 4, and Test 5.
    
    Example:
    og_list= ((['1\n','ap\nple','2\n,'mang\no','3','f\nly','4\n','5\n','che\nese','6\n','7\n',]))
    new_list= [1,2,3,4,5,6,7]

    """
    new_list = [] # created new list
    for i in data: # looping through each element in the data
        if "\n" in i: # checking if the string "\n" is in the string (i)
            i = i.replace("\n", "") # replace "\n" with an empty string
        if i.isdigit() == True: # isdigit() returns True or False, if isdigit () returns True
            i = int(i) # converting the digit string type to an int type
            new_list.append(i) #adding the converted i into the new list
    return new_list # returns a list with only intergers after looping throught all elements in "data"