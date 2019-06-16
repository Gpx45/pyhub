
class Error(Exception):
    pass

class NotEqualLength(Error):
    """Raised when length of arguments are not equal"""
    pass

def same_pattern(txt1,txt2):
    booklet1 = dict()
    booklet2 = dict()
    pattern1 = list(txt1)
    pattern2 = list(txt2)
    compare_table1 = list()
    compare_table2 = list()
    counter = 0

    try:
        if len(txt1) != len(txt2):
            raise NotEqualLength

        for letter in pattern1:
            if letter not in booklet1:
                booklet1.update({letter:counter})
                counter += 1
            compare_table1.append(booklet1[letter])

        counter = 0

        for letter in pattern2:
            if letter not in booklet2:
                booklet2.update({letter:counter})
                counter += 1
            compare_table2.append(booklet2[letter])

        return print(compare_table1 == compare_table2)

    except NotEqualLength:
        print("Length of arguments are not equal")

same_pattern("ABAB", "ZXZXY")
