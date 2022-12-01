
def main():
    '''
    read through the file a line at a time.
    When an empty line is encountered check the current calories, and update the max calories if needed.
    The code reports part 1 and part 2 of the day1 advent puzzle.
    :return:
    '''
    # most cals
    max_calories0 = 0
    # mid cals
    max_calories1 = 0
    # least cals
    max_calories2 = 0
    # current cals
    curr_calories = 0

    with open('input.txt', "rU") as f:
        for l in f:
            line = l.strip()
            if not line:
                max_calories0, max_calories1, max_calories2 = update_max_calories(curr_calories, max_calories0,
                                                                                  max_calories1, max_calories2)
                curr_calories = 0
            else:
                curr_calories += int(line)
    max_calories0, max_calories1, max_calories2 = update_max_calories(curr_calories, max_calories0,
                                                                      max_calories1, max_calories2)

    print("max calories of 1: {}".format(max_calories0))
    print("max calories of 3: {}".format(max_calories0+max_calories1+max_calories2))


def update_max_calories(curr_calories, max_calories0, max_calories1, max_calories2):
    '''
    Convenience function to update the max calories
    :param curr_calories:
    :param max_calories0:
    :param max_calories1:
    :param max_calories2:
    :return: tuple of latest max calorie assignments
    '''
    if curr_calories > max_calories0:
        max_calories2 = max_calories1
        max_calories1 = max_calories0
        max_calories0 = curr_calories
    elif curr_calories > max_calories1:
        max_calories2 = max_calories1
        max_calories1 = curr_calories
    elif curr_calories > max_calories2:
        max_calories2 = curr_calories
    return max_calories0, max_calories1, max_calories2


main()