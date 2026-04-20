def attrition_risk(satisfaction, overtime, salary, years):
    if satisfaction == "Low":
        if overtime == "Yes":
            return "High Risk"
        else:
            if salary == "Low":
                return "High Risk"
            else:
                return "Medium Risk"
    else:
        if years < 2:
            return "Medium Risk"
        else:
            if salary == "High":
                return "Low Risk"
            else:
                return "Medium Risk"

# Example
print(attrition_risk("Low", "Yes", "Low", 1))
print(attrition_risk("Low", "No", "High", 4))