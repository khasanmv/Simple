num_of_array = int(input('How many numbers do you want? '))
number=[]

for i in range(num_of_array):
    num=int(input(f'{i+1} Entered numbers: '))
    number.append(num)
count=0
sum=0
largest_so_far = -1
smallest_so_far = None
for i in number:
    count=count+1
    sum=sum+i
    if i > largest_so_far:
        largest_so_far = i
    if smallest_so_far is None:
        smallest_so_far = i 
    elif smallest_so_far >i:
        smallest_so_far = i

print('Here we go: ')
print('Total Counted numbers: ', count)
print('Largest number: ', largest_so_far)
print('Smallest number: ', smallest_so_far)
print('Sum: ', sum/count) 
