def print_given(*args,**kwargs):
    for i in args:
         print(i, type(i))
    for i,j in sorted(kwargs.items()):
        print(i,j,type(j))