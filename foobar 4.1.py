def deepCopy(array):
    return_array = []
    for element in array:
        return_array.append(element)
    return return_array

def powerSet(size):
    #Return an array with all the power sets of size size-1
    #twice, with 0 or 1 appended to the end
    if (size == 1):
        return [[1],[0]]
    else:
        prev_power_set = powerSet(size-1)
        new_power_set = []
        for i in range(len(prev_power_set)):
            prev_power_set_element = deepCopy(prev_power_set[i])
            prev_power_set_element.append(1)
            new_power_set.append(prev_power_set_element)
        for i in range(len(prev_power_set)):
            prev_power_set_element2 = deepCopy(prev_power_set[i])
            prev_power_set_element2.append(0)
            new_power_set.append(prev_power_set_element2)
    new_power_set.sort(reverse=True)
    return new_power_set

#Functions for combinatorics
def factorial(a):
    if (a == 1):
        return 1
    if (a == 0):
        return 1
    return a*factorial(a-1)

def comb(a, b):
    return factorial(a)/factorial(b)/factorial(a-b)

def solution(num_buns, num_required):
    #Each bunny in a set with this many bunnies
    #must have exactly one key in common
    common_set_size = num_buns-num_required+1

    #Number of keys required
    #(Number of sets of size common_set_size)
    num_keys = comb(num_buns, common_set_size)

    #Define empty return matrix to populate with keys
    keys = []
    for _ in range(num_buns):
        keys.append([])

    #Iterate through every subset of size common_set_size
    #Since 2^9 is small, we can use a power set for this
    power_set = powerSet(num_buns)
    current_key = 0
    for subset in power_set:
        if (sum(subset) == common_set_size):
            #Add the current_key to each bunny in this subset
            for i in range(len(subset)):
                if (subset[i] == 1):
                    keys[i].append(current_key)
            current_key+=1

    return keys


    
        
