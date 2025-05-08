from collections import defaultdict
from datetime import datetime

# Sample transaction data
transactions = [
    {"age": 24, "day": "Saturday", "time": "14:30", "amount": 45.20, "category": "groceries", "loyalty": True, "date": "2025-04-26"},
    {"age": 31, "day": "Monday", "time": "09:15", "amount": 12.00, "category": "snacks", "loyalty": False, "date": "2025-04-21"},
    # Add more entries as needed
]

# Buckets
age_groups = {
    "18-25": {"weekday": 0, "weekend": 0},
    "26-30": {"weekday": 0, "weekend": 0},
    "31-39": {"weekday": 0, "weekend": 0}
}
category_totals = defaultdict(float)
time_of_day_totals = {"morning": 0, "afternoon": 0, "evening": 0}
loyalty_totals = {"member": 0, "non_member": 0}
monthly_totals = defaultdict(float)

weekend_days = {"Saturday", "Sunday"}

# Helper functions
def get_age_group(age):
    if 18 <= age <= 25:
        return "18-25"
    elif 26 <= age <= 30:
        return "26-30"
    elif 31 <= age <= 39:
        return "31-39"
    return None

def get_time_bucket(time_str):
    hour = int(time_str.split(":")[0])
    if 5 <= hour < 12:
        return "morning"
    elif 12 <= hour < 17:
        return "afternoon"
    else:
        return "evening"

# Processing loop
for tx in transactions:
    age = tx["age"]
    if age >= 40:
        continue  # skip
    
    group = get_age_group(age)
    if not group:
        continue

    is_weekend = tx["day"] in weekend_days
    amount = tx["amount"]

    # Add to age group weekday/weekend total
    if is_weekend:
        age_groups[group]["weekend"] += amount
    else:
        age_groups[group]["weekday"] += amount

    # Category total
    category_totals[tx["category"]] += amount

    # Time of day
    time_bucket = get_time_bucket(tx["time"])
    time_of_day_totals[time_bucket] += amount

    # Loyalty
    if tx["loyalty"]:
        loyalty_totals["member"] += amount
    else:
        loyalty_totals["non_member"] += amount

    # Monthly trend
    date_obj = datetime.strptime(tx["date"], "%Y-%m-%d")
    month_key = date_obj.strftime("%Y-%m")
    monthly_totals[month_key] += amount

# Output results
print("Spending by Age Group (Weekday vs Weekend):")
for group, totals in age_groups.items():
    print(f"{group} - Weekday: ${totals['weekday']:.2f}, Weekend: ${totals['weekend']:.2f}")

print("\nSpending by Category:")
for cat, total in category_totals.items():
    print(f"{cat}: ${total:.2f}")

print("\nSpending by Time of Day:")
for period, total in time_of_day_totals.items():
    print(f"{period}: ${total:.2f}")

print("\nLoyalty Members vs Non-Members:")
for group, total in loyalty_totals.items():
    print(f"{group}: ${total:.2f}")

print("\nMonthly Spending Trends:")
for month, total in sorted(monthly_totals.items()):
    print(f"{month}: ${total:.2f}")
