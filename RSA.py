#Samuel Parmer
#sap18bq

from math import sqrt
from itertools import count, islice

class RSA:
    def __init__(self):
        self.messages = []
        self.e = 0
        self.d = 0
        self.n = 0


    def isPrime(self, num):
        if num < 2:
            return false
        for x in islice(count(2), int(sqrt(num) - 1)):
            if num % x == 0:
                return False
        return True


    def extendedGcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = self.extendedGcd(b % a, a)
            return g, y - (b // a) * x, x


    def modInverse(self, a, m):
        g, x, y = self.extendedGcd(a, m)
        return x % m


    def inputFunc(self):
        entries = input("Enter the number of messages: ")
        print(entries)
        self.messages.append(input("Enter the messages: "))

        for x in range(1, entries):
            self.messages.append(input())

    def printFunc(self, number):
        print("message is %d", number)


    def primeGen(self, minValue):
        for x in range(minValue, minValue+50):
                res = x + 1
                if(self.isPrime(res)):
                    yield res

    def keyGen(self, minValue):
        generator = self.primeGen(minValue)
        primes = []

        for x in generator:
            primes.append(x)

        p = primes[0]
        q = primes[1]
        self.n = p*q
        totient = (p-1)*(q-1)


        self.e = totient - 1

        GCDCheck = True
        while(GCDCheck):
            self.e -= 1
            g, x, y = self.extendedGcd(self.e,totient)
            if(g == 1):
                GCDCheck = False

        ModCheck = True

        self.d = self.modInverse(self.e,totient)


        print(self.d)

    def encrypt(self, message):
        #return ((message)^e)%n
        return pow(message,self.e,self.n)

    def decrypt(self, cipher):
        #return ((cipher)^d)%n
        return pow(cipher,self.d,self.n)

    def printFunc(self, num):
        return ("message is " + str(num))


    def encryptiondecorator(self, func):
        def func_wrapper(name):
            return "The encrypted " + func(name)
        return func_wrapper

    def decrytiondecorator(self, func):
        def func_wrapper(name):
            return "The decrypted " + func(name)
        return func_wrapper

def main():


    mRSA = RSA()

    mRSA.inputFunc()

    mRSA.keyGen(input("Enter the minimum value for the prime numbers: "))
    print "N is ", mRSA.n
    print "e is ", mRSA.e


    cipherlist = []
    decryptList = []

    for x in mRSA.messages:
        cipherlist.append(mRSA.encrypt(x))

    for x in cipherlist:
        decryptList.append(mRSA.decrypt(x))

    ePrint = mRSA.encryptiondecorator(mRSA.printFunc)
    dPrint = mRSA.decrytiondecorator(mRSA.printFunc)

    for x in cipherlist:
        print (ePrint(x))

    for x in decryptList:
        print (dPrint(x))

if __name__ == "__main__":
        main()


