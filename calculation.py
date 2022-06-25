from unittest import result
from celery import Celery
import time

app=Celery('calculation',backend='redis://127.0.0.1',broker='redis://127.0.0.1')

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def palindrome(n):
    return str(n)==str(n)[::-1]

@app.task()
def prime_index(n):
    print("Prime function is called by celery worker..")
    counter=0
    number=2
    while counter!=int(n):
        if is_prime(int(number)):
            counter+=1
        number+=1
    result={
        "result":number-1
    }
    return result




@app.task()
def palindrome_prime_index(n):
    print("Palindrome prime function is called by celery worker..")
    print("Asumption: 1 digit prime number is not considered as palindrome")
    counter=0
    number=10
    while counter!=int(n):
        if is_prime(int(number)) and palindrome(int(number)):
            counter+=1
        number+=1
    result={
        "result":number-1
    }
    return result