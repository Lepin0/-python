class Solution(object):
    def rob(self, nums):
        step_1 = 0
        step_2 = 0
        for n in nums:
            maxx = max(step_1 + n, step_2)

            step_1 = step_2
            step_2 = maxx

        return step_2
