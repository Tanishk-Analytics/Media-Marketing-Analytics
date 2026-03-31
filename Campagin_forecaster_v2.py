class Campaign:
    def __init__(self, name, budget, cpc, conv_rate, avg_sale_value):
        self.name = name
        self.budget = budget
        self.cpc = cpc
        self.cr = conv_rate  # e.g., 0.03 for 3%
        self.asv = avg_sale_value

    def get_clicks(self):
        return self.budget / self.cpc

    def get_conversions(self):
        return self.get_clicks() * self.cr

    def get_revenue(self):
        return self.get_conversions() * self.asv

    def get_roas(self):
        # The ultimate "Money Metric"
        return self.get_revenue() / self.budget

# Test it for a Delhi-based E-commerce client
my_ad = Campaign("Delhi_Electronics_Sale", 50000, 25, 0.02, 5000)
print(f"CLIENT: {my_ad.name}")
print("-" * 30)
print(f"Total Clicks:\t{my_ad.get_clicks():.0f}")
print(f"Total Revenue:\t₹{my_ad.get_revenue():,.2f}")
print(f"Projected ROAS:\t{my_ad.get_roas()}x")
