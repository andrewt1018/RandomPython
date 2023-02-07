import sys


def check_prime(num):
    divisor = 0
    prime = True
    for i in range(2, num):
        if num % i == 0:
            divisor = i
            prime = False
            break
    return prime, divisor


if __name__ == "__main__":
    try:
        while True:
            print("What prime number do you want to check?")
            print("Type 'exit' to exit")
            num = input()
            if num == "Exit" or num == "exit":
                break

            num = int(num)
            prime, divisor = check_prime(num)
            if prime:
                print(f"{num} is prime!\n")
            else:
                print(f"{num} is not prime!")
                print(f"{divisor} is a divisor\n")
    except KeyboardInterrupt:
        sys.exit()
