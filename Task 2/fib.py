import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python fib.py number")
        exit(1)

    n = int(sys.argv[1])
    if n < 0:
        print("negative numbers not accepted!")
        exit(2)
    print(fibo(n))


def fibo(n):
    """ optimised fibonacci function with dynamic programming technique
        takes integer n and returns fibonacci(n)
    """
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(2, n + 1):
        fibo.append(fibo[i-1] +  fibo[i-2])
    return (fibo[n])

if __name__ == "__main__":
   main()
