import sys
def main(argv):
    n = int(argv[0])
    pi = 0
    for i in range(0,n):
        pi = pi + (pow(-1,i)/pow(2,10*i)) * ((-1*pow(2,5)/((4*i)+1)) + (-1/((4*i)+3)) + (pow(2,8)/((10*i)+1)) + (-1*pow(2,6)/((10*i)+3)) + (-1*pow(2,2)/((10*i)+5))  + (-1*pow(2,2)/((10*i)+7)) + (1/((10*i)+9)) )                         
    pi = pi/pow(2,6)
    print(pi,end="")

if __name__ == "__main__":
   main(sys.argv[1:])
