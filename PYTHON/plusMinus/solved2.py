def plusMinus(arr):
    payda = len(arr)
    print (sum(1 if i > 0 else 0 for i in arr)/payda)
    print (sum(1 if i < 0 else 0 for i in arr)/payda)
    print (sum(1 if i == 0 else 0 for i in arr)/payda)


# We have other method as below;

def plusMinus(arr):
    payda = len(arr)
    print (len([i for i in arr if i>0 ])/payda)
    print (len([i for i in arr if i<0 ])/payda)
    print (len([i for i in arr if i==0 ])/payda)

    