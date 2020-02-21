#Given January 30th, 2020

#Compute the running median of a sequence of numbers.
#That is, given a stream of numbers, print out the median of the list so far
#on each new element.

#Recall that the median of an even-numbered list is the average
#of the two middle numbers.

#For example, given the sequence [2, 1, 5, 7, 2, 0, 5],
#your algorithm should print out:

#2
#1.5
#2
#3.5
#2
#2
#2

def binary_search(sorted_sequence : list, sequence_length : int, value: int) -> int:
    '''returns the first index of the value you are looking for
    '''
    left_index = 0
    right_index = sequence_length

    while left_index < right_index:
        middle_index = (left_index + right_index) // 2

        if sorted_sequence[middle_index] < value:
            left_index = middle_index + 1
        else:
            right_index = middle_index

    #this accounts for if the value is not actually in the array
    if sorted_sequence[left_index] != value:
        return -1
    
    return left_index


def median(sequence : [int]):
    lst = []
    median = 0
    length = 0
    
    for i in sequence:
        if length == 0:
            lst.append(i)
            length += 1
        

        elif i < lst[0]:
            lst = [i] + lst
            length += 1

        elif i > lst[-1]:
            lst.append(i)
            length += 1

        #do a binary search for the index to insert...
        elif i > lst[0] and i < lst[-1]:
            index = binary_search(lst, length, i)
            lst.insert(index, i)
            length += 1

        #print(lst)

        #print median
        if length % 2 == 1:
            print (lst[length // 2])
           

        elif len(lst) % 2 == 0:
            print( (lst[(length // 2) - 1] + lst[length // 2]) / 2 )
       

if __name__ == '__main__':
    #case 1
    print(binary_search([1,2,3], 3, 2), 'index should be 1')
    #case 2
    print(binary_search([1,2,3], 3, 0), 'index should be -1')    
    #case 3
    print(binary_search([1,1,1], 3, 1), 'index should be 0')
    #case 4
    print(binary_search([1, 1, 2, 2, 2, 3], 6, 2), 'index should be 2')
    print()
    
    median([2, 1, 5, 7, 2, 0, 5])
    
    #print(binary_search([1,2,3,4,5,6,7,8,9,10], 1))
    #print(binary_search([1,2,3,4,4,4,5,6,7,8,9,10], 4))
    #print(binary_search([1,2,3,4,5,6,7,8,8,8,8,9,10], 8))
    
