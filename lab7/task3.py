import re


def fun(s):
    print(s)
    if not re.match("^[A-Za-z0-9_-]+@[A-Za-z0-9]+\.[A-Za-z0-9_-]{,3}$", s):
        return False
    return True


def filter_mail(emails):
    return list(sorted(filter(fun, emails)))


def main():
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())
    filtered_emails = filter_mail(emails)
    print(filtered_emails)


def get_input_output(inp_f, out_f):
    f1 = open(inp_f, 'r')
    f2 = open(out_f, 'r')
    inp = f1.readlines()
    out = f2.readlines()
    f1.close()
    f2.close()
    inp = list(map(lambda x: x[:-1] if x[-1] == '\n' else x, inp))
    out = list(map(lambda x: x[1: -1], out[0][1: -1].split(', ')))
    if out == ['']:
        out = []
    return inp, out


def test_1():
    inp, out = get_input_output("./emails/input/input00.txt", "./emails/output/output00.txt")
    assert filter_mail(inp[1:]) == out


def test_2():
    inp, out = get_input_output("./emails/input/input01.txt", "./emails/output/output01.txt")
    assert filter_mail(inp[1:]) == out


def test_3():
    inp, out = get_input_output("./emails/input/input02.txt", "./emails/output/output02.txt")
    assert filter_mail(inp[1:]) == out


def test_4():
    inp, out = get_input_output("./emails/input/input03.txt", "./emails/output/output03.txt")
    assert filter_mail(inp[1:]) == out


def test_5():
    inp, out = get_input_output("./emails/input/input04.txt", "./emails/output/output04.txt")
    assert filter_mail(inp[1:]) == out


def test_6():
    inp, out = get_input_output("./emails/input/input05.txt", "./emails/output/output05.txt")
    assert filter_mail(inp[1:]) == out


def test_7():
    inp, out = get_input_output("./emails/input/input06.txt", "./emails/output/output06.txt")
    assert filter_mail(inp[1:]) == out


def test_8():
    inp, out = get_input_output("./emails/input/input07.txt", "./emails/output/output07.txt")
    assert filter_mail(inp[1:]) == out


def test_9():
    inp, out = get_input_output("./emails/input/input08.txt", "./emails/output/output08.txt")
    assert filter_mail(inp[1:]) == out


def test_10():
    inp, out = get_input_output("./emails/input/input09.txt", "./emails/output/output09.txt")
    assert filter_mail(inp[1:]) == out


if __name__ == '__main__':
    get_input_output("./emails/input/input00.txt", "./emails/output/output00.txt")
