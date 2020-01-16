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
        half_length = int(len(l) / 2)
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
    :param s: String to be separated character by character like '121211'
    :return: Separated list of characters where one can look like ['1', '2', '1', '2', '1', '1']
    """
    result = []
    for i in s:
        result.append(i)
    return result


def formatter(list_of_strings_of_unique_characters):
    """
    Takes the list in the form ['aaa', 'b', 'ccccc', ...] and return list of tuples which represents
    (length of list element, its composer character)
    In other words, return [(3, 'a'), (1, 'b'), (5, 'c'), ...]
    :param list_of_strings_of_unique_characters: List of strings
    where each string expected as combination of one character
    :return: Tuple for each string in the given list where tuple represents the count of the characters
    in each string and the first character of that string
    """
    result = []
    for i in list_of_strings_of_unique_characters:
        result.append((len(i), i[0]))
    return result


###################################################

# ###### Functions for iterative algorithm ###### #

def get_longest_substring(n):
    """
    Iterates over the string and parses it in order to create list of tuples from length of
    the longest contiguous characters and that character
    :param n: String to be parsed and processed in order to find out longest substring and count tuples
    :return: List of (count, character) tuples
    """
    result = []
    current_char = n[0]
    current_char_count = 0
    for ch in n:
        if ch == current_char:
            current_char_count += 1
        elif current_char is not None:
            result.append((current_char_count, int(current_char)))
            current_char = ch
            current_char_count = 1
    result.append((current_char_count, int(current_char)))
    return result


###################################################

# ############### Common Functions ############## #

def assembly(l):
    """
    List of tuples assembler where each tuple represents the count of a character and that character in it
    :param l:  List of tuples where any instance can look like [(1, 2), (1, 1)]
    :return: Merged string of the list of tuples where the above instance can be returned as '1211'
    """
    result = []
    for i in l:
        result.append(str(i[0]) + str(i[1]))
    return "".join(result)


###################################################

def say_what_you_see(n):
    """
    >>> list(say_what_you_see(1))
    [1]
    >>> list(say_what_you_see(2))
    [1, 11]
    >>> list(say_what_you_see(3))
    [1, 11, 21]
    >>> list(say_what_you_see(4))
    [1, 11, 21, 1211]
    >>> list(say_what_you_see(5))
    [1, 11, 21, 1211, 111221]
    >>> list(say_what_you_see(6))
    [1, 11, 21, 1211, 111221, 312211]

    :param n: The number of elements that you need to have in the output list
    :return: Generator for each element in the expected series
    """
    # Initial series element
    series = [1]
    yield int(series[0])
    for i in range(1, n):
        # Iterative string processor
        element = assembly(get_longest_substring(str(series[i - 1])))

        # Recursive divide and conquer algorithm
        # element = assembly(formatter(merger(separator(str(series[i-1])))))

        series.append(element)
        yield int(element)


def main():
    for i in say_what_you_see(10):
        print(i)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
