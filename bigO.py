import timeit
def sum(n):
    final_sum=0
    for x in range(n+1):
        final_sum+=x
    return final_sum
print(sum(10))