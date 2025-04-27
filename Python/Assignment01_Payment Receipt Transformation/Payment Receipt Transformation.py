import os

cust_id = "125322"
cust_fname = "John"
cust_lname = "O'Connor"
address_line1 = "123 Main St"
address_line2 = "unit 203"
city = "Vancouver"
province = "BC"
country = "Canada"
postal_code = "V4X3A2"
principal = 5000 # Loan principal amount 
apr = 34.5 # Annual Percentage Rate 
lp = 12.5 # Loan Protection Premium 
payment_amount = 100 # Payment amount made by the customer 
payment_date = "2025-03-30" # Date of payment

# calculations
interest_paid = round(((principal * apr / 100) / 26),2)
total_mandatory_amount = round((interest_paid + lp),2)
balance_applied_toPrincipal = round((payment_amount - total_mandatory_amount),2)
latest_principal_balance = round((principal - balance_applied_toPrincipal),2)
next_min_payment_amount = round(((latest_principal_balance * apr / 100) / 26 + lp),2)

#output formatting
receipt_content = f"""From,
XXX Financials
Vancouver

To,
{cust_lname}, {cust_fname}
{address_line1} - {address_line2},
{city},
{province},
{country} {postal_code}

Dear {cust_fname},

We have received the payment of $round(payment_amount,2) on {payment_date}. Thank you for your payment. Attached is the breakdown of your payment.

Interest paid = ${interest_paid}
Loan Protection Premium = ${lp:.2f}
Total mandatory amount = ${total_mandatory_amount}
Balance (applied to principal) = ${balance_applied_toPrincipal}
Latest Principal balance = ${latest_principal_balance}

Next minimum payment amount = ${next_min_payment_amount}
"""

#folder to save receipts
folder_name = f"receipts/{payment_date[:4]}_{payment_date[5:7]}"
os.makedirs(folder_name, exist_ok=True)

#generate file to save receipt  receipt_125322_2025-03-30
file_name = f"receipt_{cust_id}_{payment_date[:4]}-{payment_date[5:7]}-{payment_date[8:10]}.txt"
file_path = os.path.join(folder_name, file_name)

# Write formatted output to the file
with open(file_path, "w") as receipt_file:
    receipt_file.write(receipt_content)

print(f"Receipt saved as {file_path}")
