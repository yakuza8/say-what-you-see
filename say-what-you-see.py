# ###### Functions for recursive algorithm ###### #


def merger(l):
    """
    This function takes a list of strings as a parameter and return list of grouped, consecutive strings
    :param l: List of strings
    :return:
    """
    if not l:
        print("Error in merge with empty list")
    elif len(l) == 1:
        return l
    else:
        # Divide the list from half
        half_length = len(l) / 2
        left = merger(l[:half_length])
        right = merger(l[half_length:])
        if left[-1][-1] == right[0][0]:
            # If left and right have common string from ending and beginning respectively, merge them
            return left[:-1] + [left[-1] + right[0]] + right[1:]
        else:
            # Else return directly
            return left + right


def separator(s):
    """
    From any string, return the list composed of each character that are in the string
    :param s:
    :return:
    """
    result = []
    for i in s:
        result.append(i)
    return result


def formatter(l):
    """
    Takes the list in the form ['aaa', 'b', 'ccccc', ...] and return list of tuples which represents
    (length of list element, its composer character)
    In other words, return [(3, 'a'), (1, 'b'), (5, 'c'), ...]
    :param l:
    :return:
    """
    result = []
    for i in l:
        result.append((len(i), i[0]))
    return result


###################################################

# ###### Functions for iterative algorithm ###### #

def get_longest_substring(n):
    """
    Iterates over the string and parses it in order to create list of tuples from length of
    the longest contiguous characters and that character
    :param n:
    :return:
    """
    temp = n
    result = []
    _len = len(temp)
    while temp != "":
        current_element = temp[0]
        times = 1
        while _len > times and current_element == temp[times]:
            times += 1
        _len -= times
        temp = temp[times:]
        result.append((times, int(current_element)))
    return result


###################################################

# ############### Common Functions ############## #

def assembly(l):
    result = []
    for i in l:
        result.append(str(i[0]) + str(i[1]))
    return "".join(result)


###################################################

def say_what_you_see(n):
    """
    :param n: The number of elements that you need to have in the output list
    :return:
    """
    series = [1]
    for i in range(1, n):
        # Iterative string processor
        series.append(assembly(get_longest_substring(str(series[i - 1]))))

        # Recursive divide and conquer algorithm
        # series.append(assembly(formatter(merger(separator(str(series[i-1]))))))

    return series


def main():
    while True:
        a = int(input("Enter the number of elements : "))
        if a <= 0:
            print("Invalid length of sequence")
            break
        for i in say_what_you_see(a):
            print(i)


if __name__ == "__main__":
    main()
