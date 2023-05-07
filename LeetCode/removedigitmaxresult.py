# first draft 
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        dig = int(digit)
        nums = []
        for i,m in enumerate((number)):
            nums.append(m)
        for i in range(len(nums)):
            if nums[i] == dig:
                if i < len(nums)-1 and nums[i] < nums[i+1]:
                    del(nums[i])
                break
            return nums
        # Convert the list of numbers to a string of numbers
        number_string = ''.join(str(i) for i in nums)
        return number_string
    
    # chat GPT answer, note use of nums=list(number)
    class Solution:
        def removeDigit(self, number: str, digit: str) -> str:
            dig = int(digit)
            nums = list(number)
            for i in range(len(nums)):
                if int(nums[i]) == dig:
                    del(nums[i])
                    break
            # Convert the list of numbers to a string of numbers
            number_string = ''.join(nums)
            return number_string
# this answer doesnt maximize the integer
# didnt have the second conditional and didnt append ints to the first list 
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        dig = int(digit)
        nums = []
        for m in number:
            nums.append(int(m))
        for i in range(len(nums)):
            if nums[i] == dig:
                if i < len(nums)-1 and nums[i] < nums[i+1]:
                    del(nums[i])
                    break
            # return statement should be outside the for loop
        # Convert the list of numbers to a string of numbers
        number_string = ''.join(str(i) for i in nums)
        return number_string
    
#answer that worked --- didnt pass submit 
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        dig = int(digit)
        nums = []
        for m in number:
            nums.append(int(m))
        for i in range(len(nums)):
            if nums[i] == dig:
                del nums[i] # i think this line by itseld made it not work
                break
        # Convert the list of numbers to a string of numbers
        number_string = ''.join(str(i) for i in nums)
        return number_string

#finally worked 
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_number = -1
        for i in range(len(number)):
            if number[i] == digit:
                new_number = number[:i] + number[i+1:]
                max_number = max(max_number, int(new_number))
        return str(max_number)

