#######################
#     包括的两个函数:    #
#     1.jiami（加密）   #
#     2.jiemi（解密）   #
#  都要传入”yi“（移位值） #
########################
def jiami(ming, yi):
    mi = ''
    ming_old_list = list(ming)
    ''
    for y in range(0, yi):
        for i in ming_old_list:
            if i == 'a':
                mi += 'b'
            elif i == 'A':
                mi += 'B'

            elif i == 'b':
                mi += 'c'
            elif i == 'B':
                mi += 'C'

            elif i == 'c':
                mi += 'd'
            elif i == 'C':
                mi += 'D'

            elif i == 'd':
                mi += 'e'
            elif i == 'D':
                mi += 'E'

            elif i == 'e':
                mi += 'f'
            elif i == 'E':
                mi += 'F'

            elif i == 'f':
                mi += 'g'
            elif i == 'F':
                mi += 'G'

            elif i == 'g':
                mi += 'h'
            elif i == 'G':
                mi += 'H'

            elif i == 'h':
                mi += 'i'
            elif i == 'H':
                mi += 'I'

            elif i == 'i':
                mi += 'j'
            elif i == 'I':
                mi += 'J'

            elif i == 'j':
                mi += 'k'
            elif i == 'J':
                mi += 'K'

            elif i == 'k':
                mi += 'l'
            elif i == 'K':
                mi += 'L'

            elif i == 'l':
                mi += 'm'
            elif i == 'L':
                mi += 'M'

            elif i == 'm':
                mi += 'n'
            elif i == 'M':
                mi += 'N'

            elif i == 'n':
                mi += 'o'
            elif i == 'N':
                mi += 'O'

            elif i == 'o':
                mi += 'p'
            elif i == 'O':
                mi += 'P'

            elif i == 'p':
                mi += 'q'
            elif i == 'P':
                mi += 'Q'

            elif i == 'q':
                mi += 'r'
            elif i == 'Q':
                mi += 'R'

            elif i == 'r':
                mi += 's'
            elif i == 'R':
                mi += 'S'

            elif i == 's':
                mi += 't'
            elif i == 'S':
                mi += 'T'

            elif i == 't':
                mi += 'u'
            elif i == 'T':
                mi += 'U'

            elif i == 'u':
                mi += 'v'
            elif i == 'U':
                mi += 'V'

            elif i == 'v':
                mi += 'w'
            elif i == 'V':
                mi += 'W'

            elif i == 'w':
                mi += 'x'
            elif i == 'W':
                mi += 'X'

            elif i == 'x':
                mi += 'y'
            elif i == 'X':
                mi += 'Y'

            elif i == 'y':
                mi += 'z'
            elif i == 'Y':
                mi += 'Z'

            elif i == 'z':
                mi += 'a'
            elif i == 'Z':
                mi += 'A'

            else:
                mi += i
        ming_old_list = list(mi)
        mi_str = mi
        mi = ''
    return mi_str


def jiemi(mi, yi):
    ming = ''
    mi_old_list = list(mi)
    ''
    for y in range(0, yi):
        for i in mi_old_list:
            if i == 'a':
                ming += 'z'
            elif i == 'A':
                ming += 'Z'

            elif i == 'b':
                ming += 'a'
            elif i == 'B':
                ming += 'A'

            elif i == 'c':
                ming += 'b'
            elif i == 'C':
                ming += 'B'

            elif i == 'd':
                ming += 'c'
            elif i == 'D':
                ming += 'C'

            elif i == 'e':
                ming += 'd'
            elif i == 'E':
                ming += 'D'

            elif i == 'f':
                ming += 'e'
            elif i == 'F':
                ming += 'E'

            elif i == 'g':
                ming += 'f'
            elif i == 'G':
                ming += 'F'

            elif i == 'h':
                ming += 'g'
            elif i == 'H':
                ming += 'G'

            elif i == 'i':
                ming += 'h'
            elif i == 'I':
                ming += 'H'

            elif i == 'j':
                ming += 'i'
            elif i == 'J':
                ming += 'I'

            elif i == 'k':
                ming += 'j'
            elif i == 'K':
                ming += 'J'

            elif i == 'l':
                ming += 'k'
            elif i == 'L':
                ming += 'K'

            elif i == 'm':
                ming += 'l'
            elif i == 'M':
                ming += 'L'

            elif i == 'n':
                ming += 'm'
            elif i == 'N':
                ming += 'M'

            elif i == 'o':
                ming += 'n'
            elif i == 'O':
                ming += 'N'

            elif i == 'p':
                ming += 'o'
            elif i == 'P':
                ming += 'O'

            elif i == 'q':
                ming += 'p'
            elif i == 'Q':
                ming += 'P'

            elif i == 'r':
                ming += 'q'
            elif i == 'R':
                ming += 'Q'

            elif i == 's':
                ming += 'r'
            elif i == 'S':
                ming += 'R'

            elif i == 't':
                ming += 's'
            elif i == 'T':
                ming += 'S'

            elif i == 'u':
                ming += 't'
            elif i == 'U':
                ming += 'T'

            elif i == 'v':
                ming += 'u'
            elif i == 'V':
                ming += 'U'

            elif i == 'w':
                ming += 'v'
            elif i == 'W':
                ming += 'V'

            elif i == 'x':
                ming += 'w'
            elif i == 'X':
                ming += 'W'

            elif i == 'y':
                ming += 'x'
            elif i == 'Y':
                ming += 'X'

            elif i == 'z':
                ming += 'y'
            elif i == 'Z':
                ming += 'Y'

            else:
                ming += i
        mi_old_list = list(ming)
        ming_str = ming
        ming = ''
    return ming_str
