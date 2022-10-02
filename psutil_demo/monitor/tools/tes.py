a = {'a':{'ss':1},
     'b':{'dd':2}
     }
r = {
    dict(
        c=2,
        d=3,
        **a[k]
    ) for k ,v in a.items()
}
print(r)