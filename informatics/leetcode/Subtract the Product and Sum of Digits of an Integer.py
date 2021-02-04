class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product = 1
        sum = 0
        for digit in str(n):
            product *= int(digit)
        for digit in str(n):
            sum += int(digit) 
        return product - sum