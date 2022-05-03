#submitted by Keren Or Hadad 208025205

def group_by(func, iter):
    """

    :param func:function
    :param iter:iterablr
    :return:The function will return a dictionary, in which:
The keys are the values returned from the function passed as the first parameter.
The value corresponding to a particular key is a list of all the organs for which the value appearing in the key is repeated.
    """
    dict = {}
    for item in iter:
        key = func(item)
        if key not in dict.keys():
            dict[key] = []
        dict[key].append(item)
    return dict


words = ["hi", "bye", "yo", "try"]
print(group_by(len, words))

""" 
output:
{2: ['hi', 'yo'], 3: ['bye', 'try']}

"""
