'''
Created on Feb 23, 2018

@author: Sagar Bayar
'''
def pairsum(arr,k):
    if len(arr)<2:
        return
    seen=set()
    output=set()
    for num in arr:
        target=k-num
        if target in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)),max(num,target)))
    print('\n',join(map(str,list(output))))
pairsum([1,3,2,2,8],4)