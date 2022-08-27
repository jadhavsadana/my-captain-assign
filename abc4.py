def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('sadhna'))




Output:
{'s':1, 'a':2, 'd':1, 'h':1, 'n':1}


