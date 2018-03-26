import sys
def main(argv):
    n = int(argv[0])
    pi = 0
    sign = 1
    for i in range(1,n,2):
        pi = pi + sign*1/i
        sign = sign * -1
    pi = pi*4
    print(pi, end="")

if __name__ == "__main__":
   main(sys.argv[1:])
