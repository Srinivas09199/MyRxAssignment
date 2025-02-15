'''Given a sorted array of positive and negative numbers. You have to Square it and sort it. Constraint : Time complexity O(n) 
Example: 
Input: [-12, -8 , -7, -5, 2, 4, 5, 11, 15] 
Output : [4, 16, 25, 25, 49, 56, 121, 144, 225] 
'''
arr = [-12, -8 , -7, -5, 2, 4, 5, 11, 15]

n = len(arr)
res = [0] * n
l, r = 0, n - 1

pos = n - 1

while l <= r:
    
    l_sqa = arr[l] ** 2
    r_sqa = arr[r] ** 2
    
    if l_sqa > r_sqa:
        res[pos] = l_sqa
        l += 1
    else:
        res[pos] = r_sqa
        r -= 1
    
    pos -= 1

print(res)