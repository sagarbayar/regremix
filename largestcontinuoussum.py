'''
Created on Feb 23, 2018

@author: Sagar Bayar
'''
def large_cont_sum(arr):
    if len(arr)==0:
        return 0
    max_sum=cur_sum=arr[0]
    for num in arr[1:]:
        cur_sum=max(cur_sum+num,num)
        max_sum=max(cur_sum,max_sum)
    return max_sum
print(large_cont_sum([1,2,5,78,-98,-89]))
