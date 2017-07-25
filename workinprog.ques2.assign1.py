mass_dict = {'A': 71.03711360, 'a': 71.03711360, 'C': 103.0091854, 'c': 103.0091854, 'D': 115.0269428, 'd': 115.0269428,
             'E': 129.0425928, 'e': 129.0425928, 'F': 147.0684136, 'f': 147.0684136, 'G': 57.02146360, 'g': 57.02146360,
             'H': 137.0589116, 'h': 137.0589116, 'I': 113.0840636, 'i': 113.0840636, 'K': 128.0949626, 'k': 128.0949626,
             'L': 113.0840636, 'l': 113.0840636, 'M': 131.0404854, 'm': 131.0404854, 'N': 114.0429272, 'n': 114.0429272,
             'P': 97.05276360, 'p': 97.05276360, 'Q': 128.0585772, 'q': 128.0585772, 'R': 156.1011106, 'r': 156.1011106,
             'S': 87.03202820, 's': 87.03202820, 'T': 101.0476782, 't': 101.0476782, 'V': 99.06841360, 'v': 99.06841360,
             'W': 186.0793126, 'w': 186.0793126, 'Y': 163.0633282, 'y': 163.0633282}
list_aa = list(mass_dict.keys())
p_z_dict = {'ACACIMED': 2, 'acacimed': 2, 'ELEMYRATNE': 1, 'elemyratne': 1, 'wapwop': 3, 'WAPWOP': 3, 'zeittsieg': 2,
            'ZEITTSIEG': 2, 'desfbirc': 1, 'DESFBIRC': 1, 'ALTAATSIV': 3, 'altaatsiv': 3, 'MEINWOHC': 2, 'meinwohc': 2}
# p_z_dict for protein: charge
list_p_seq = list(p_z_dict.keys())  # list of protein seq for this assignment


def main():
    while True:
        aa_seq = input('Enter amino acid sequence:\t')
        for letter in aa_seq:
            if letter not in list_aa:
                print(letter, 'is an invalid amino acid thus', aa_seq, 'is an invalid protein sequence.\n')
                break
            elif letter in list_aa and aa_seq not in list_p_seq:
                print('Amino acid sequence is a valid protein but is not part of HW Assignment Question 2.')
                break
            elif letter in list_aa and aa_seq in list_p_seq:
                print('\n')
                print(aa_seq, 'is valid.')
                break
            elif letter in list(aa_seq) and letter in mass_dict.keys():
                n = len(aa_seq)

                m = mass_dict[letter]
                for num in list(m):
                sum_p = 0
                sum_p = sum_p + num
                print('Mass:\t', sum_p)
                if aa_seq in p_z_dict.keys():
                ch = p_z_dict[aa_seq]  # charge = p_z_dict[pro for protein seq for assignment]
                print('Charge (z):\t', ch)
                mow = 18.010564684  # mass of water (mow)
                sum_aa = mow + sum_p
                m_z = sum_aa / ch
                print('Mass (m):\t', '{:.2f}'.format(sum_aa))  # formatted to two decimal places
                print('m/z:\t', '{:.2f}'.format(m_z), '\n')


main()

# mass(A) = 71.03711360
# mass(C) = 103.0091854
# mass(D) = 115.0269428
# mass(E) = 129.0425928
# mass(F) = 147.0684136
# mass(G) = 57.02146360
# mass(H) = 137.0589116
# mass(I) = 113.0840636
# mass(K) = 128.0949626
# mass(L) = 113.0840636
# mass(M) = 131.0404854
# mass(L) = 113.0840636
# mass(M) = 131.0404854
# mass(N) = 114.0429272
# mass(P) = 97.05276360
# mass(Q) = 128.0585772
# mass(R) = 156.1011106
# mass(S) = 87.03202820
# mass(T) = 101.0476782
# mass(V) = 99.06841360
# mass(W) = 186.0793126
# mass(Y) = 163.0633282
