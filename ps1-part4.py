prior_arrests = int(input("Prior arrests: "))
prior_arrest_local_ordinance = input("Prior arrests for local ordinance (Y/N): ")
age_release = int(input("Age at release: "))
risk_score = 0
if prior_arrests >= 2:
    risk_score += 1
elif prior_arrests >= 5:
    risk_scrore += 1
    
if prior_arrest_local_ordinance.strip().upper() == "Y":
    risk_score += 1
pass
if age_release > 18 and age_release < 24:
    risk_score += 1
elif age_release >= 40:
    risk_score -= 1
print(f"The recidivism risk score is {risk_score}")
