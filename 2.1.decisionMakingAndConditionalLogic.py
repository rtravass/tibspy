# Get customer input
age = int(input("Enter customer age: "))
monthly_income = float(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
employment_status = input("Enter employment status (employed/unemployed): ").lower()
existing_loan = input("Does the customer have an existing loan? (yes/no): ").lower()

#Evaluate booleans and print
age_eligible = age >=21
income_eligible = monthly_income >= 30000
credit_eligible = credit_score >= 650
currently_employed = employment_status == "employed"
no_existing_loan = existing_loan == "no"

print("Age eligible: ", age_eligible)
print("Income eligible: ",income_eligible)
print("Credit eligible: ", credit_eligible)
print("Currently employed: ", currently_employed)
print("No existing loan: ", no_existing_loan)

basic_eligiblity = (age_eligible and income_eligible and currently_employed)
print("Basic eligiblity: ", basic_eligiblity)

if (not age_eligible):
    print("\nResult: Rejected")
    print("Reason: Customer must be atleast 21 years old")
else:
    if basic_eligiblity:
        print("Customer passed the basic eligiblity check")
        if credit_score >= 750:
            decision = "Approved"
            risk_level = "Low Risk"
        
        elif credit_score>= 700:
            decision = "Approved"
            risk_level = "Moderate Risk"
        
        elif credit_score >= 650:
            decision = "Review"
            risk_level = "Medium Risk"

        else:
            decision = "Rejected"
            risk_level = "High Risk"

        print("Credit assessment: ", risk_level)
        print("Decision: ", decision)
    
    else:
        print("\nCustomer failed the basic eligiblity check")

        if not income_eligible:
            print("Reason: Monthly income is below Rs. 30000")
        elif not currently_employed:
            print("Reason: Customer is not currently employed")
        else:
            print("Reason: Customer does not meet the basic criteria")


print("\n -------------- Short-Circuit Evaluation----------")
if age >= 21 and credit_score >= 650:
    print("Customer satisfies age and credit requirements")

if age < 21 or credit_score < 650:
    print("Customer fails age or credit requirements")
        




