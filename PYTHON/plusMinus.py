def plusMinus(arr):
    # Write your code here
    p_count, n_count, z_count = 0,0,0
    payda = len(arr)
    for i in arr:
        if i > 0:
            p_count +=1
        elif i < 0:
            n_count +=1
        else:
            z_count +=1
    print(p_count/payda, n_count/payda, z_count/payda, sep='\n')