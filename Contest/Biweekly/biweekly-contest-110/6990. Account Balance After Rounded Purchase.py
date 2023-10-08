class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if purchaseAmount < 10 and purchaseAmount >= 5:
            return 90
        elif 1 < purchaseAmount < 5:
            return 100
        elif purchaseAmount % 10 == 0: # multiple of 10
            return 100-purchaseAmount
        else:
            if purchaseAmount % 10 < 5:
                return 100 - 10*(purchaseAmount // 10)
            else:
                return 100 - 10*(purchaseAmount // 10 + 1)


s = Solution()
purchaseAmount = 2
print(s.accountBalanceAfterPurchase(purchaseAmount))