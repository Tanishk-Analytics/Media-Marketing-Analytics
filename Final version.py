import csv
from Campagin_forecaster_v3 import Campaign 

def run_audit():
    # 1. Open BOTH files at the same time
    with open('client_data.csv', mode='r') as infile, \
         open('Final_report.csv', mode='w', newline='') as outfile:
        
        reader = csv.DictReader(infile)
        writer = csv.writer(outfile)
        
        # 2. Write the header to the CSV file ONLY ONCE (outside the loop)
        writer.writerow(['Campaign Name', 'Revenue', 'ROAS'])
        
        print(f"{'CLIENT':<20} | {'REVENUE':<12} | {'ROAS':<8}")
        print("-" * 45)

        # 3. Now loop through the data
        for row in reader:
            c = Campaign(
                row['name'], 
                float(row['budget']), 
                float(row['cpc']), 
                float(row['conv_rate']), 
                float(row['avg_sale_value'])
            )
            
            # Print to Terminal (For you to see)
            print(f"{c.name:<20} | ₹{c.get_revenue():>10,.0f} | {c.get_roas():>7.2f}x")
            
            # Write to CSV (For the Client/L&F to see)
            writer.writerow([c.name, round(c.get_revenue(), 2), round(c.get_roas(), 2)])

run_audit()

