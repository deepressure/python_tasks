#add multiple values to a dictionary key with other rules provided
def update_dictionary(d, key, value):
    if key in d.keys():
        d[key].append(value)
    elif 2 * key in d.keys():
        d[2 * key].append(value)
    else:
        d[2 * key] = [value]
     
def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
