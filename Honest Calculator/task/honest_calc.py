# write your code here
import sys
memory = 0
msg_ = ["Enter an equation", "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...", "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):", " ... lazy", " ... very lazy",
        " ... very, very lazy", "You are", "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]


def repeat_process():
    while True:
        print(msg_[5])
        response = input().lower()
        if response == "y":
            main()
        elif response == "n":
            sys.exit()


def is_one_digit(value):
    if -10 < value < 10 and value.is_integer():
        return True
    else:
        return False


def check(x, y, oper):
    msg = ""
    if is_one_digit(x) and is_one_digit(y):
        msg += msg_[6]
    if (x == 1 or y == 1) and oper == "*":
        msg += msg_[7]
    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


def calculate(x, y, oper):
    if oper == "+":
        return x + y
    elif oper == "-":
        return x - y
    elif oper == "*":
        return x * y
    elif oper == "/" and y != 0:
        return x / y


def main():
    global msg_index
    global memory
    global msg_

    while True:
        print(msg_[0])
        calc = input()
        x, oper, y = calc.split()
        if x == "M":
            x = memory
        if y == "M":
            y = memory
        try:
            x = float(x)
            y = float(y)
            break
        except (TypeError, ValueError):
            print(msg_[1])

    check(x, y, oper)
    if oper not in ["+", "-", "*", "/"]:
        print(msg_[2])
        main()
    elif oper == "/" and y == 0:
        print(msg_[3])
        main()
    else:
        result = calculate(x, y, oper)
        print(result)
        print(msg_[4])
        response = input().lower()
        if response == "y":
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(f"{msg_[msg_index]}")
                    resp = input().lower()
                    if resp == 'y':
                        if msg_index < 12:
                            msg_index += 1
                        else:
                            memory = result
                            break
                    elif resp == 'n':
                        msg_index = 10
                        break
            else:
                memory = result

        repeat_process()


if __name__ == '__main__':
    main()
