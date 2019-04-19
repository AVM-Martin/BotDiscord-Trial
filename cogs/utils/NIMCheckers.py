"""NIM Checkers"""

# class StudentId:
class NIM:
    def __init__(self, student_id):
        self._student_id = student_id;

    def is_valid(self):
        nums = [int(num) for num in self._student_id if '0' <= num <= '9'];

        # check length
        if(len(nums) != 10):
            return False;

        # check last digit
        if(nums[9] > 6):
            return False;

        # check sum digit
        for idx in range(9):
            if(idx%2 == 0):
                nums[idx] = (4*nums[idx]) % 7;
            if(idx%2 == 1):
                nums[idx] = (14-nums[idx]) % 7;
        sum_ = 0;
        for num in nums:
            sum_ = (sum_ + num) % 7;
        return sum_ == 4;

    def __str__(self):
        nums = [num for num in self._student_id if '0' <= num <= '9'];
        return "".join(nums);
