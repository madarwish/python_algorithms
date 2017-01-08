# Uses python3
import sys

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
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
