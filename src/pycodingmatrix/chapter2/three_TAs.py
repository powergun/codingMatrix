import random


# source:
# what is the inverse of XOR
# https://stackoverflow.com/questions/14279866/what-is-inverse-function-to-xor
def xor_secr(lhs: [int], rhs: [int]) -> [int]:
    return [(l ^ r) for (l, r) in zip(lhs, rhs)]


# b = T ^ c ^ a
# T = b ^ a ^ c
def do_split(plaincode: [int]) -> ([int], [int], [int]):
    c = [random.randint(0, 1) for _ in plaincode]
    a = [random.randint(0, 1) for _ in plaincode]
    plaincode_ = xor_secr(plaincode, c)
    b = xor_secr(plaincode_, a)
    return a, b, c


def do_merge(a: [int], b: [int], c: [int]) -> [int]:
    return xor_secr(xor_secr(b, a), c)


def str_to_code(s: str) -> [int]:
    def c_to_code(ch: str) -> [int]:
        code = [int(b) for b in '{:b}'.format(ord(ch)).rjust(8, '0')]
        return code

    l = []
    for c in s:
        l.extend(c_to_code(c))
    return l


def code_to_str(code: [int]) -> str:
    def segment_to_c(segement: [int]) -> str:
        return chr(int(''.join([str(b) for b in segment]), base=2))

    s = ''
    for num_segment in range(len(code) // 8):
        segment = code[num_segment * 8:num_segment * 8 + 8]
        c = segment_to_c(segment)
        s = s + c
    return s


if __name__ == '__main__':
    code = str_to_code('there')
    s = code_to_str(code)
    print(s)
    a, b, c = do_split(code)
    # s_ = code_to_str(xor_secr(b, c))
    # print(s_)
    # s_ = code_to_str(xor_secr(a, c))
    # print(s_)
    # s_ = code_to_str(xor_secr(a, b))
    # print(s_)
    s_ = code_to_str(do_merge(a, b, c))
    print(s_)