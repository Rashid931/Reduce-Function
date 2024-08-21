from functools import reduce

l = [1,2,3,4,5]

sum = reduce (lambda a,b: a+b, l)
print (f"Sum of {len(l)} Nos is", sum)

product = reduce (lambda a,b: a*b, l)
print (f"Product of {len(l)} Nos is", product)

greatest = reduce (lambda x,y: x if x>y else y, l)
print (f"Greatest of {len(l)} Nos is", greatest)

smallest = reduce (lambda x,y: x if x<y else y, l)
print (f"Smallest of {len(l)} Nos is", smallest)