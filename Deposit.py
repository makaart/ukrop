class Deposit:
    def compound(self, sum, rate, period):
        if period == 0:
            return sum
        else:
            return self.compound(sum * (1 + rate), rate, period - 1)

    def accumulativeCompound(self, sum, rate, period, accumulative_amount):
        if period == 0:
            return sum - accumulative_amount
        else:
            return self.accumulativeCompound(accumulative_amount + sum * (1 + rate), rate, period - 1, accumulative_amount)