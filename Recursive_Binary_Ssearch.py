def recursion_binary_search(list, target):
    if len(list)==0:
        return False    
    else:
        midpoint = (len(list))//2
        
        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                """" #since list[1:]  inlcude all the values starting at position 1, 
                we use midpoint plus 1 to only include those apprearing after midpoint index"""
                return recursion_binary_search(list[midpoint+1:],target)
            else:
               """" #since list[:7] only inlcude the value before position 
               7 we use midpoint as last index """
               return recursion_binary_search(list[:midpoint],target)

def verify(result):
    print("Result found:", result)
    

numbers = [1,2,3,4,5,6,8,9,10,11,12]
results = recursion_binary_search(numbers,5)
result2 = recursion_binary_search(numbers,7)
verify(results)
verify(result2)