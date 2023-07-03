from typing import List

#Function that divides a postive number by 2 if its even or multiplies it by 3 and adds 1 to it if its odd.
#It then returns a list of all the intermediate values of n.
def collatz(n: int) -> List[int]:
    #Initializing the sequence with an initial value of n
    sequence = [n]

    while n != 1:
        #If n is even, divide it by 2 and it becomes the new n
        if n % 2 == 0:
            n //= 2
        else:
            #If n is odd, mutiply it by 3 and add 1,it becomes the new n
            n = ((n * 3) + 1)

        #Appending the new value of n to the sequence
        sequence.append(n)
    return sequence

#Testing the function when n=6
n = 6
print(collatz(n))


#Function to calculate the number of distinct/unique values in the list.
def distinct_numbers(numbers: List[int]) -> int:
    #The set function returns unique values
    unique_numbers = set(numbers)
    length = len(unique_numbers)
    return length

#Testing the function
integers = [1,2,3,2,3,4,6,5,5,5,6]
print(distinct_numbers(integers))

even = []
print(distinct_numbers(even))