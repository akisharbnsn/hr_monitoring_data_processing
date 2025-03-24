def average(data: list) -> float:
    """
    Calculate average value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the average of this list
    """
    ### Average is the sum of all numbers divided by the length of numbers
    if data:
        total = 0  # set default value to 0
        count = 0 # set default value to 0
        for number in data:
            total += number # add each number to total
            count += 1 # keep a record of how many numbers are in the list
        mean = total / count # sum of all numbers / total count of numbers
        mean = round(mean, 2) # rounding two decimal points
    else: # if list empty, return empty list
        mean = []
    return mean


def maximum(data: list) -> float:
    """
    Extracts the maximum value from the list.
    
    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the maximum of this list
    """
    if data: # if there is data in the list
        max_value = data [0] # max value starting will be the number at the 0 index position
        for number in data:
            if number > max_value: # if number is greater than the current max value
                max_value = number # update max value if the number was greater than previous max value
        max_value = round(max_value, 2) # rounding to 2 decimal points
    else: # if list empty, return empty list
        max_value = []
    return max_value


def variance(data: list) -> float:
    """
    Calculate the variance value of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the variance of this list
    """
    if data: # if list empty, return empty list
        count = len(data)
        if count <= 1:
            return [] # can't calculate sample variance for 0 or 1 item
        mean = average (data) # calculate the average from the "average" function
        squared_diffs_list = [] # empty list to store values
        for number in data:
            squared_diff = (number - mean) ** 2 # calcuting the squared diffs for each number
            squared_diffs_list.append(squared_diff) # adding the squared diffs into new list
            variance = sum(squared_diffs_list) / count # variance calculation
            variance = round(variance, 2) # round to 2 decimal points
    else:
        variance = []
    return variance


def standard_deviation(data: list) -> float:
    """
    Calculate the standard deviation of the list.

    Args:
        data (list[int]): list of integers representing heart rate samples
    Returns:
        float: a floating point value representing the standard deviation of this list
    """
    if data: # if list empty, return empty list
        _variance = variance(data) # calculating variance from the "variance" function
        sd = _variance ** 0.5 # Calculating the standard deviation of this list
        sd = round(sd, 2) # Rounding the standard deviation float value
    else: # if list empty, return empty list
        sd = []
    return sd
