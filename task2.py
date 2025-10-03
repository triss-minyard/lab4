lst = [1, 2, [True, False,["a","ra"]],3]
res =[]
for i in lst:
    if type(i) != list:
        res.append(i)
    else:
        for j in i:
            if type(j) != list:
                res.append(j)
            else:
                for x in j:
                    res.append(x)
print(res)

