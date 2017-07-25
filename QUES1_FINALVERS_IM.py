
seq_list = []  # initial seq list
rev_list = []  # reversed list
new_list = []  # new list
fin_list = []  # final list


def reverse(seq_li):  # seq_li is variable
    for i in seq_li:
        rev_list.append(i[::-1])
    return rev_list


def swap(rev_comp):  # swap function replacing bases with their compliments
    for x in rev_comp:  # rev_comp for reverse compliment
        rev_comp = x.replace('A', '{}').replace('T', 'A').replace('{}', 'T').replace('C',
                                '{}').replace('G', 'C').replace('{}', 'G').replace('a', '{}').replace('t',
                                'a').replace('{}', 't').replace('c', '{}').replace('g', 'c').replace('{}', 'g')
    return rev_comp


def stats(fin_li):  # fin_li is another name used in the definition of this function
    nos = len(fin_li)  # nos stands for number of sequences
    print('\nNumber of valid sequences:', nos)
    for j in fin_li:  # j is each output in final list
        for i in list(j):  # i is for each letter inside list of all the final outputs
            new_list.append(i)
    ax = new_list.count('A')  # x is for capital base
    ay = new_list.count('a')  # y is for lower case base
    axy = ax + ay   # total number of base both capital and lower case
    cx = new_list.count('C')
    cy = new_list.count('c')
    cxy = cx + cy
    tx = new_list.count('T')
    ty = new_list.count('t')
    txy = tx + ty
    gx = new_list.count('G')
    gy = new_list.count('g')
    gxy = gx + gy
    total = (axy + txy + cxy + gxy)    # includes all bases entered
    asl = total / nos  # asl stands for average sequence length
    print('Average sequence length:', '{:.1f}'.format(asl))  # # 1 tab and limiting decimal to tenth place
    max1 = len(new_list)  # max1 is the total number of bases in all reverse complements
    print('\nBase frequencies in reverse complements:')
    print('\t\tA/a\t', '{}/{}'.format(axy, max1))    # 4 tabs and formatting ratio
    print('\t\tC/c\t', '{}/{}'.format(cxy, max1))
    print('\t\tT/t\t', '{}/{}'.format(txy, max1))
    print('\t\tG/g\t', '{}/{}'.format(gxy, max1))
    print('\n\t\t\t\t\t\t**END OF RESULTS**\n')


def main():
    while True:
        dna_seq = input('Enter DNA Sequence (Enter DONE or done to finish capturing sequences):\t')
        if dna_seq == 'done' or dna_seq == 'DONE':
            print('\n\t\t\t\t\t\t**************')
            print('\nValid sequences:\t\t', seq_list)    # 2 tabs
            print('Reverse complements:\t', fin_list)   # 1 tab
            print('\n\t\t\t\t\t\t**STATISTICS**')  # 6 tabs
            stats(fin_list)
            break
        elif dna_seq in seq_list:
            print('Sequence is already in list.\n')
            continue
        else:
            for letter in list(dna_seq):  # letter in list of input dna seq
                if letter not in ['A', 'a', 'C', 'c', 'G', 'g', 'T', 't']:
                    print(letter, 'is an invalid character thus', dna_seq, 'is an invalid DNA seq.\n')
                    break
            else:
                seq_list.append(dna_seq)
                rl = reverse(seq_list)  # rl for reversed sequence list
                print('Above sequence and its reverse complement have been stored and added to lists.\n')
                fin_list.append(swap(rl))


main()
