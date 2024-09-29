def print_params(a = 1, b = 'строка', c = True):
    print (a,b,c)

print_params()
print_params(1,2,3)
print_params(4, 5)
list_ = (2,3,[4,5,6,7])
print_params (*list_)

values_list = ('string', False, 10)
print_params (*values_list)
values_dict = {'c':'symbol', 'a':True, 'b':22 }
print_params (**values_dict)

values_list_2 = (list_, True)
print_params (*values_list_2, 42)