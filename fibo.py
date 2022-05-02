def recursive_nth_fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return recursive_nth_fibo(n-1) + recursive_nth_fibo(n-2)

def main():
    count = int(input('How many numbers?'))
    fib_seq = []
    for n in range(count):
        fib_seq.append(recursive_nth_fibo(n))
    print(fib_seq)


if __name__ == "__main__":
    main()
