import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python fib.py number")
        exit(1)

    n = int(sys.argv[1])
    print(fibo(n))

#optimised fibonacci function
def fibo(n):
    fibo = []
    fibo.append(0)
    fibo.append(1)
    for i in range(2, n + 1):
        fibo.append(fibo[i-1] +  fibo[i-2])
    return (fibo[n])

if __name__ == "__main__":
   main()
