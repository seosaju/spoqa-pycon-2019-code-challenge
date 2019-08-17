# Python 3.7
patterns = ['*    ', '    *', '*   *', ' * * ', '  *  ', '*****', '**  *', '*  **']
pattern_dict = {'A': '42522', 'C': '50005', 'E': '50505', 'H': '22522', 'I': '54445', 'N': '26572', 'O': '52225',
                'P': '52500', 'S': '50515', 'T': '54444', 'Y': '23444'}


def print_str(string):
    result = [[] for _ in range(5)]
    for i in string:
        index = 0
        alphabet = pattern_dict[i]
        for j in alphabet:
            pattern = patterns[int(j)]
            result[index].append(pattern.replace('*', i))
            index += 1
    for i in result:
        for j in i:
            print(j, end=' ')
        print('')


text = ['CONNECT', 'THE', 'PYTHONISTAS']
for i in text:
    print_str(i)
