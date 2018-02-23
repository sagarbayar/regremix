'''
Created on Feb 23, 2018

@author: Sagar Bayar
'''
def Miss(arr1,arr2):
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)
    """for num in zip(arr1,arr2):
        print(num)""" 
    for n1,n2 in zip(arr1,arr2):
        if n1!=n2:
            print(n1)
            return
            
Miss([1,2,3,5,6,7],[1,2,6,7,3])