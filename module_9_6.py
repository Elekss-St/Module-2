def all_variants(text):
    # for i in len(text)
    for _i in range(len(text)):
        for _j in range(len(text) - _i):
            yield text[_j:_j + 1 + _i]


a = all_variants("abc")
for i in a:
    print(i)