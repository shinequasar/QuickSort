import random

def quick_sort_after(arr):
    if(len(arr)>1):
	    pivot = arr[random.randint(0, len(arr)-1)] 
	    right = [i for i in arr if i > pivot]
	    left = [i for i in arr if i < pivot]
	    middle = [i for i in arr if i == pivot]
	    return quick_sort_after(left) + middle + quick_sort_after(right)
    else:
	    return arr