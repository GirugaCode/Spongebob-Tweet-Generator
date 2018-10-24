import random
import sys

# print ('Number of arguments:', len(sys.argv), 'arguments.')
# print ('Argument List:', str(sys.argv))

# print(sys.argv[1:])


def random_arrangement():
    inputs_list = sys.argv[1:]
    result_list = []
    for i in inputs_list:
        rand_index = random.randint(0, len(inputs_list) -1)
        list = inputs_list[rand_index]
        result_list.append(list)
        str1 = ' '.join(result_list)
    return str1
    # pass


if __name__ == '__main__':
    arrange = random_arrangement()
    print(arrange)







#
# quotes = ("It's just a flesh wound.",
#           "He's not the Messiah. He's a very naughty boy!",
#           "THIS IS AN EX-PARROT!!")
#
#
# def random_python_quote():
#     rand_index = random.randint(0, len(quotes) - 1)
#     return quotes[rand_index]
#
# if __name__ == '__main__':
#     quote = random_python_quote()
#     print (quote)
