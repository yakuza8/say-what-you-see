#####################################
#        Powered by Yakuza          #
#####################################
#
# Say What You See series where ith
# element of series is composed of the
# immediate previous element's lenght
# of the contiuous substring of different
# character followed by that character
#
# The first 10 elements of the series:
# 1
# 11
# 21
# 1211
# 111221
# 312211
# 13112221
# 1113213211
# 31131211131221
# 13211311123113112211

def getLongestSubs(n):
    temp = n
    result = []
    l = len(temp)
    while temp != "":
        currentElement = temp[0]
        times = 1
        while l > times and currentElement == temp[times]:
            times += 1
        l -= times
        temp = temp[times:]
        result.append((times, int(currentElement)))
    return result


def assembly(l):
    result = []
    for i in l:
        result.append(str(i[0]) + str(i[1]))
    return "".join(result)


def sayWhatYouSee(n):
    series = [1]
    for i in range(1, n):
        # Iterative string processor
        series.append(assembly(getLongestSubs(str(series[i - 1]))))

        # Recursive divide and conquer algorithm
        # series.append(assembly(formatter(merger(seperator(str(series[i-1]))))))
    return series


####### Functions for recursive algorithm #######
def merger(l):
    if l == []:
        print
        "Error in merge"
    elif len(l) == 1:
        return l
    else:
        halfLength = len(l) / 2
        left = merger(l[:halfLength])
        right = merger(l[halfLength:])
        if left[-1][-1] == right[0][0]:
            return left[:-1] + [left[-1] + right[0]] + right[1:]
        else:
            return left + right


def seperator(s):
    result = []
    for i in s:
        result.append(i)
    return result


def formatter(l):
    result = []
    for i in l:
        result.append((len(i), i[0]))
    return result


#################################################


while True:
    a = int(input("Enter the number of elements : "))
    if a <= 0:
        print("Invalid number")
        break
    for i in sayWhatYouSee(a):
        print(i)