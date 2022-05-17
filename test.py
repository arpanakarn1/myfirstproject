# name = input("Enter you name")
# abc = name.lower()
# print(abc)

#print sum of members in a list, nums = [5,7,13,2,25,50,3]
#calculate the percentage obtained by a student from a list of
#individual marks=[70,78,82,89,67]
#print largest number in a list,nums=[5,7,13,2,25,50,3]
nums = [5,7,13,2,25,50,3]
#sum = sum(nums)
#print (sum)
sum = 0
for i in nums:
    sum = sum + i
print(sum)

marks = [70,78,82,89,67]
obtained = 0
for i in marks:
    obtained = obtained + i

print(obtained/500 * 100)

#largest number in a list
nums=[5,7,13,2,25,50,3]
largest = nums[0]
for i in nums:
    if i > largest:
        largest = i

print(largest)

