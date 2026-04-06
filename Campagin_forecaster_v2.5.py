    
def get_roas(self):
        # The 'Money Multiplier'
        if self.budget == 0: return 0
        return self.get_revenue() / self.budget

    
def get_cpa(self):
        # Cost Per Acquisition (How much to 'buy' one customer)
        conversions = self.get_clicks() * self.cr
        if conversions == 0: return 0
        return self.budget / conversions
# Day 8: Managing a Portfolio
campaign_list = [
    {"name": "Google_Search", "budget": 50000, "cpc": 45, "cr": 0.02, "asv": 10000},
    {"name": "Meta_Ads", "budget": 20000, "cpc": 10, "cr": 0.04, "asv": 1500},
    {"name": "YT_Awareness", "budget": 30000, "cpc": 25, "cr": 0.03, "asv": 8000}
]

print("--- PORTFOLIO REPORT ---")
for data in campaign_list:
    c = Campaign(data["name"], data["budget"], data["cpc"], data["cr"], data["asv"])
    print(f"Client: {c.name} | ROAS: {c.get_roas():.2f}x")
