#Write a Python function called max_num()to find the maximum of three numbers.

def max_number(max1,max2,max3):
    return max([max1,max2,max3])

print(max_number(8,26,3))
print(max_number(10,20,30))
print(max_number(465,546,654))

#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(list):
    #if theirs nothing in the list
    if len(list)==0:
        return 0
    #start with first on list
    prod = list[0]   

    if len(list)>1:
    #multiply together
        for i in list[1]:
            prod = prod * i    
    return prod

print(mult_list[20,25,30])
print(mult_list([]))
print(mult_list([10]))

#Write a Python function called rev_string() to reverse a string.

def rev_string(my_str):
    return my_str[-1]

print(rev_string(""))
print(rev_string("chocolate"))
print(rev_string("currupt file"))

#Write a Python function called num_within() to check whether a number falls in a given range.
#The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
#Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.

def num_within(a,b,c):
    return a in range (b, c+1)

print(num_within(8,7,6))
print(num_within(58,8747,61))
print(num_within(8532,7435,656))

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
#The function accepts the number n, the number of rows to print
#Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.