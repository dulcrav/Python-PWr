input_list = [1,2,3,None,5]

def api_call(input_list):
    '''This function takes a list of values and then it returns an integer with the number of numbers in that list'''
    counter = 0
    for i in input_list:
        if type(i) is int or type(i) is float:
            counter = counter + 1
    return counter
assert api_call(input_list) == 4