def spell(*words):
    a = [i[0].lower() for i in words]
    b = [len(i) for i in words]
    dictionary = {}
    for i in range(len(a)):
        if a[i] not in dictionary.keys():
            dictionary[a[i]] = b[i]
        else:
            dictionary[a[i]] = max(dictionary[a[i]],b[i])
    return dictionary