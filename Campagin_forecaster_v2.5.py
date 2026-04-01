    
def get_roas(self):
        # The 'Money Multiplier'
        if self.budget == 0: return 0
        return self.get_revenue() / self.budget

    
def get_cpa(self):
        # Cost Per Acquisition (How much to 'buy' one customer)
        conversions = self.get_clicks() * self.cr
        if conversions == 0: return 0
        return self.budget / conversions
