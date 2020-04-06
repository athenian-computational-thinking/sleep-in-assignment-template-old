def sleep_in(weekday, vacation):
    return not weekday or vacation


if __name__ == '__main__':
    # Test your code here. Change the argument to try different values
    print(sleep_in(True, True))