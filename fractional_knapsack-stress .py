# Uses python3
import sys
from random import randint

def get_optimal_value(capacity, weights, values):
    value = 0
    occupiedWieght = 0 
    largestItemVal = max(values)
    largestItemWeight = weights[values.index(largestItemVal)]
    while len(values) > 0 :
    	maxItemVal = max(values)
    	# get the weight of the most valuable item
	maxItemWeight = weights[values.index(maxItemVal)]
	# Constraints: value of valuable item , weight of valuable item , capacity of the knapsack , weigh of knapsack
	# capacity of knapsack is not exceeded we are checking it in the main while loop 
	# remaining three constraints , value of items , Weight and knapsack capacity 
	while (occupiedWieght < capacity ):
		if occupiedWieght + maxItemWeight <= capacity:
			occupiedWieght = occupiedWieght + maxItemWeight
			value = value + maxItemVal
		else:
                    break
	values.remove(maxItemVal)
	weights.remove(maxItemWeight)
		
	
	# write your code here

    if occupiedWieght < capacity:
        remainingCapacity = capacity - occupiedWieght
        value = value + ( remainingCapacity* largestItemVal / float(largestItemWeight) ) 
    return value


if __name__ == "__main__":
    n = 1000
    capacity = 2000000
    values = []
    weights = []
    for i in range (0 , 1000):
        values.append(randint(1,capacity/2))
        weights.append(randint(1,capacity/2))
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
