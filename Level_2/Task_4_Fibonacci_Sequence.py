def fibonacci_sequence():
    terms = int(input("Enter number of terms: "))

    first = 0
    second = 1

    print("Fibonacci Sequence:")

    for i in range(terms):
        print(first, end=" ")

        next_term = first + second
        first = second
        second = next_term


fibonacci_sequence()