from math import sqrt

def main():
    my_dict = {i: i**3 for i in range(1, 101) if i % 3 != 0}
    # for i in range(1, 101):
    #     if i % 3 == 0:
    #         continue
    #     my_dict[i] = i**3
    # print(my_dict)
    challenge = {i: sqrt(i) for i in range(1, 1001)}
    print(challenge)
if __name__ == '__main__':
    main()