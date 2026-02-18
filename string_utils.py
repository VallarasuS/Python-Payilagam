def split(data, delimiter, skip):
    li = data.split(delimiter)

    return li[skip : len(li) : 1]
