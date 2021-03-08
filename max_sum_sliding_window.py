"""
Given an array of integers of sizi 'n', calculate the maximum sum of 'k' consecutieve elements in the array.
Hint: Use the sliding window technique.
"""
def max_sum(arr, k):
    n = len(arr)
    if n < k:
        print("Invalid")
        return -1
    window_sum=sum(arr[:k]) # starting window
    max_sum = window_sum
    for i in range(len(arr) - k ):
        window_sum = window_sum - arr[i] + arr[i+k] # reduce the ith element from the window sum, add the next element to the sum
        max_sum = max(max_sum, window_sum)
    return max_sum

if __name__ == "__main__":
    arr=[5,1,18,-1,6,-3,29,2,7,-2,7,14,6,21,12,1,-5,-45,20]
    arr=[1,4,2,10,2,3,1,0,20]
    print(max_sum(arr,4))