'''We are given two arrays that represent the arrival and departure times of trains, the task is to find the minimum number of platforms required so that no train waits. 
Examples: 
Input: arr[] = {9:00, 9:40, 9:50, 11:00, 15:00, 18:00}, dep[] = {9:10, 12:00, 11:20, 11:30, 19:00, 20:00} 
Output: 3 
Explanation: There are at-most three trains at a time (time between 9:40 to 12:00) 
Input: arr[] = {9:00, 9:40}, dep[] = {9:10, 12:00} 
Output: 1 
Explanation: Only one platform is needed. 
'''
arr = ['9:00', '9:40', '9:50', '11:00', '15:00', '18:00']
dep = ['9:10', '12:00', '11:20', '11:30', '19:00', '20:00']

#arr = ['9:00', '9:40']
#dep = ['9:10', '12:00']

arr_mins = [int(t.split(':')[0]) * 60 + int(t.split(':')[1]) for t in arr]
dep_mins = [int(t.split(':')[0]) * 60 + int(t.split(':')[1]) for t in dep]

arr_mins.sort()
dep_mins.sort()

platforms = 1
res = 1

i = 1
j = 0

while i < len(arr_mins) and j < len(dep_mins):
    if arr_mins[i] <= dep_mins[j]:
        platforms += 1
        i += 1
    elif arr_mins[i] > dep_mins[j]:
        platforms -= 1
        j += 1
    res = max(res, platforms)
print('output:', res)