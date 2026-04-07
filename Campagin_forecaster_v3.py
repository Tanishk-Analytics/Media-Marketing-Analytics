class Campaign:
    def __init__(self,name,budget,cpc,conv_rate,avg_sale_value):
        self.name = name
        self.budget = budget
        self.cpc = cpc
        self.cr = conv_rate
        self.asv = avg_sale_value

    def get_clicks(self):
        # Adding a Safety check for cpc
        if self.cpc <= 0: return 0
        return self.budget / self.cpc

    def get_conversions(self):
        return self.get_clicks() * self.cr

    def get_revenue(self):
        return self.get_conversions() * self.asv

    def get_roas(self):
        #Safety check to prevent crash if budget is zero
        if self.budget <= 0: return 0
        return self.get_revenue() / self.budget

#Managing a Portfolio
campaign_list = [
    {"name": "Google_Search", "budget": 50000, "cpc": 45, "cr": 0.02, "asv": 10000},
    {"name": "Meta_Ads", "budget": 20000, "cpc": 10, "cr": 0.04, "asv": 1500},
    {"name": "YT_Awareness", "budget": 30000, "cpc": 25, "cr": 0.03, "asv": 8000},
    {"name": "Error_Test", "budget": 0, "cpc": 0, "cr": 0.03, "asv": 8000} # Test case
]

print("--- PORTFOLIO REPORT ---")
# Professional Header
print(f"{'CLIENT NAME':<18} | {'CLICKS':>8} | {'CONV.':>6} | {'REVENUE':>12} | {'ROAS':>8}")
print("-" * 65)

for data in campaign_list:
    c = Campaign(data["name"], data["budget"], data["cpc"], data["cr"], data["asv"])
    
    # Extracting values for clean printing
    clicks = c.get_clicks()
    conv = c.get_conversions()
    rev = c.get_revenue()
    roas = c.get_roas()

    # The "Magic" Formatting:
    # :<18 means left-align with 18 spaces
    # :>12,.0f means right-align, 12 spaces, add commas, and 0 decimals
    print(f"{c.name:<18} | {clicks:>8.0f} | {conv:>6.0f} | ₹{rev:>11,.0f} | {roas:>7.2f}x")

print("-" * 65)


