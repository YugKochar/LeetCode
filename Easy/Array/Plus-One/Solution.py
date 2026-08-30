class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # for i in range(len(digits)-1,-1,-1):
        #     if digits[i] < 9:
        #         digits[i]+= 1
        #         return digits
        #     digits[i] = 0
        # return [1]+ digits

        # string = ""
        # for i in range(len(digits)):
        #     string = string + str(digits[i])
        # value = int(string)
        # value = str(value+1)
        # arr = []
        # for i in range(len(value)):
        #     arr.append(int(value[i]))
        # return arr

        value = 0
        digits = digits[::-1]
        for i in range(len(digits)):
            value += digits[i] * (10 ** i)
        value = str(value + 1)
        arr = []
        for i in range(len(value)):
            arr.append(int(value[i]))
        return arr

        

