
def same_pattern(txt1,txt2):
    booklet = dict()
    compare_table1 = list()
    compare_table2 = list()
    counter = 0

    if len(txt1) != len(txt2):
        print("Strings are NOT SAME LENGTH")

    else:
        pattern = list(txt1)
        for letter in pattern:
            if letter not in booklet:
                booklet.update({letter:counter})
                counter += 1
            compare_table1.append(booklet[letter])

        counter = 0
        pattern = list(txt2)
        booklet.clear()

        for letter in pattern:
            if letter not in booklet:
                booklet.update({letter:counter})
                counter += 1
            compare_table2.append(booklet[letter])

        return print(compare_table1 == compare_table2)

