def sort_dict(dic):
    return [(key, dic[key]) for key in sorted(dic, key=dic.get)]


def incr(key, dic):
    try:
        dic[key] += 1
    except KeyError:
        dic.setdefault(key, 1)


def main():
    resultDict = {}

    # read file
    with open('breakfast.txt', 'rb') as afile:
        for line in afile.readlines():
            # clean up line
            for word in line.split():
                # count words
                incr(word, resultDict)
    sortedKeys = sort_dict(resultDict)

    for item in sortedKeys:
        print '%s: %s' % (item[0], item[1])

if __name__ == '__main__':
    main()
