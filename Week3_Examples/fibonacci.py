
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == "__main__":

    nth_term = 36

    print(f"The {nth_term}th term of the Fibonacci sequence is {fibonacci(nth_term)}")