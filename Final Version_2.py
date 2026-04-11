import csv

# --- THE LOGIC ENGINE ---
class Campaign:
    def __init__(self, name, budget, cpc, conv_rate, avg_sale_value):
        self.name = name
        self.budget = float(budget)
        self.cpc = float(cpc)
        self.cr = float(conv_rate)
        self.asv = float(avg_sale_value)

    def get_clicks(self):
        if self.cpc <= 0: return 0
        return self.budget / self.cpc

    def get_conversions(self):
        return self.get_clicks() * self.cr

    def get_revenue(self):
        return self.get_conversions() * self.asv

    def get_roas(self):
        if self.budget <= 0: return 0
        return self.get_revenue() / self.budget

# --- SPECIALIST UTILITIES ---
def flag_underperformers(campaign_list, threshold=2.0):
    """Flags campaigns that are underperforming for immediate review."""
    return [f"ALERT: {c.name} is below target (ROAS: {c.get_roas():.2f}x)" 
            for c in campaign_list if c.get_roas() < threshold]

def get_portfolio_summary(campaign_list):
    total_budget = sum(c.budget for c in campaign_list)
    total_revenue = sum(c.get_revenue() for c in campaign_list)
    overall_roas = total_revenue / total_budget if total_budget > 0 else 0
    return total_budget, total_revenue, overall_roas

# --- THE AUTOMATED PIPELINE ---
def run_audit():
    all_campaigns = []
    
    try:
        # Opening both files: Reading data and Writing the final report
        with open('client_data.csv', mode='r') as infile, \
             open('Final_report.csv', mode='w', newline='') as outfile:
            
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)
            writer.writerow(['Campaign Name', 'Revenue', 'ROAS', 'Status'])
            
            print(f"{'CLIENT':<20} | {'REVENUE':<12} | {'ROAS':<8}")
            print("-" * 45)

            for row in reader:
                c = Campaign(row['name'], row['budget'], row['cpc'], row['conv_rate'], row['avg_sale_value'])
                all_campaigns.append(c)
                
                rev = c.get_revenue()
                roas = c.get_roas()
                status = "PASS" if roas >= 2.0 else "FAIL"
                
                # Terminal Print
                print(f"{c.name:<20} | ₹{rev:>10,.0f} | {roas:>7.2f}x")
                
                # CSV Write
                writer.writerow([c.name, round(rev, 2), round(roas, 2), status])

        # 1. Portfolio Summary
        t_budget, t_rev, t_roas = get_portfolio_summary(all_campaigns)
        print("\n" + "="*45)
        print(f"TOTAL REVENUE: ₹{t_rev:,.2f} | OVERALL ROAS: {t_roas:.2f}x")
        print("="*45)

        # 2. Performance Alerts
        alerts = flag_underperformers(all_campaigns)
        if alerts:
            print("\n--- ATTENTION REQUIRED ---")
            for a in alerts: print(a)

    except FileNotFoundError:
        print("Error: 'client_data.csv' not found. Please ensure the file exists.")

if __name__ == "__main__":
    run_audit()
