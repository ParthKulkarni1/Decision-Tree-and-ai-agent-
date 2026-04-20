def customer_decision(previous_purchase, income, age):
    if previous_purchase == "Yes":
        return "Target Customer"
    else:
        if income > 50000:
            return "Target Customer"
        else:
            if age < 25:
                return "Not Target"
            else:
                return "Maybe Target"

# Example
print(customer_decision("No", 40000, 30))
print(customer_decision("yes", 700000, 10))
print(customer_decision("yes", 200, 10))