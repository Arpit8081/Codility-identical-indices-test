from itertools import combinations

arr = [ 1,1,1,2 ]
mydict = {}
for i, j in enumerate(arr):
    if j not in mydict:
        mydict[j] = [i]
    else:
        mydict[j].append(i)
    for k, v in mydict.items():
        if len(v) > 1:
        	print(list(combinations(v, 2)))  