def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print((sum(arr)-arr[-1]),(sum(arr)-arr[0]))