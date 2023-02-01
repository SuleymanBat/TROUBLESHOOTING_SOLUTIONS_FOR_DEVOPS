def miniMaxSum(arr):
    # Write your code here
    top1 = sum(arr)-max(arr)
    top2 = sum(arr)-min(arr)
    print(top1,top2)