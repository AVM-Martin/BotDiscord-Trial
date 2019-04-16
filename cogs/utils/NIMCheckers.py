class NIM:
    def __init__(self, NIM):
        self._NIM = NIM;

    def isValid(self):
        nums = [int(c) for c in self._NIM if("0" <= c <= "9")];
        # check length
        if(len(nums) != 10):
            return False;
        # check last digit
        if(nums[9] > 6):
            return False;
        # check sum digit
        for i in range(9):
            if(i%2 == 0):
                nums[i] = (4*nums[i]) % 7;
            if(i%2 == 1):
                nums[i] = (14-nums[i]) % 7;
        res = 0;
        for num in nums:
            res = (res + num) % 7;
        return res == 4;

    def __str__(self):
        nums = [c for c in self._NIM if("0" <= c <= "9")];
        return "".join(nums);
