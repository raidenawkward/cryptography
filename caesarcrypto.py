
_ALPHABET = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

def alpha_shift(ch, shift=0):
    if ch is None:
        return None

    if len(ch) > 1:
        return None

    if ch.isalpha() is False:
        return None

    islower = ch.islower()
    lower = ch.lower()

    index = _ALPHABET.index(lower)
    newindex = index + shift
    newindex = newindex % len(_ALPHABET)

    convertee = _ALPHABET[newindex]

    if not islower:
        convertee = convertee.capitalize()

    return convertee


_NUMBER = [
    '0',
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9'
]

def number_shift(n, shift=0):
    if n is None:
        return None

    if len(n) > 1:
        return None

    if not n.isnumeric():
        return None

    index = _NUMBER.index(n)
    newindex = index + shift
    newindex = newindex % len(_NUMBER)

    convertee = _NUMBER[newindex]

    return convertee


def encrypt(ori, shift=0):
    if ori is None:
        return None

    encryptedtext = ''

    for ch in ori:
        e = None
        if ch.isalpha():
            e = alpha_shift(ch, shift)
        elif ch.isnumeric():
            e = number_shift(ch, shift)
        else:
            e = ch
        encryptedtext = encryptedtext + e

    return encryptedtext

def decrypt(enc, shift=0):
    if enc is None:
        return None

    decryptedtext = ''
    for ch in enc:
        o = None
        if ch.isalpha():
            o = alpha_shift(ch, shift)
        elif ch.isnumeric():
            o = number_shift(ch, shift)
        else:
            o = ch
        decryptedtext = decryptedtext + o

    return decryptedtext



if __name__ == '__main__':
    enc = 'ZW PFL NREK KF CVRIE DFIV RSFLK TIPGKFXIRGYP Z IVTFDDVEU RE FECZEV TFLIJV ZEJKILTKVU SP GIFWVJJFI URE SFEVY WIFD JKREWFIU LEZMVIJZKP ALJK JVRITY TIPGKFXIRGYP RK TFLIJVIR.FIX'
    for shift in range(1, 26):
        ori = decrypt(enc, shift)
        print('[shift=' + str(shift) + ']\t\t' + ori)