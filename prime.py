__author__ = 'andaro'
#!/bin/python


def is_prime(integer):
    """Determines weather integer is prime, returns a boolean value"""
    # add logic here to make sure number < 2 are not prime
    if integer < 2:
        return True

    for i in range(2, integer):
        if integer % i == 0:
            return False
    return True


# Your code below:
for i in range(100):
    if is_prime(i):
        print "%i is prime" %i

