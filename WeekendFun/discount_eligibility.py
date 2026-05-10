total_bill = float(input("Enter total bill amount: "))
is_member = input("Are you a member? (yes/no): ").strip().lower()

if total_bill >= 1000 and is_member == "yes":
    discount = total_bill * 0.10
    print("You get 10% discount")

elif total_bill >= 1000 and is_member == "no":
    discount = total_bill * 0.05
    print("You get 5% discount")

else:
    discount = 0
    print("No discount")

final_amount = total_bill - discount

print("Discount =", discount)
print("Final Amount =", final_amount)
