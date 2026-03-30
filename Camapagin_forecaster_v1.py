class Campaign:
    def __init__(self, name, budget, cpc):
        self.name = name
        self.budget = budget
        self.cpc = cpc

    def estimate_clicks(self):
        return self.budget / self.cpc

# Create an object (your first "Campaign" data point)
my_ad = Campaign("Google_Search_India", 5000, 25)
my_ad2= Campaign("Meta_Search_India",10000,25)
#print(f"Estimated Clicks for {my_ad.name},: {my_ad.estimate_clicks()}")

#print(f"Estimated Clicks for {my_ad2.name},:{my_ad2.estimate_clicks()}")

# Use \n for a new line and \t for a tab space
print(f"REPORT: {my_ad.name}\n\tTotal Budget:\t₹{my_ad.budget}\n\tEst. Clicks:\t{my_ad.estimate_clicks()}")
print("-" * 30)
print(f"REPORT: {my_ad2.name}\n\tTotal Budget:\t₹{my_ad2.budget}\n\tEst. Clicks:\t{my_ad2.estimate_clicks()}")
