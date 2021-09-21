"""The 401k Shuffle."""

# 1. @TODO: Use the following dictionary or paste the dictionary to a new python script:
accounts = {"Schwab": 2000, "Fidelity": 8000, "Merrill": 3000, "Wells Fargo": 0.01}

# 2. @TODO: Using dictionary syntax, print the amount of the Fidelity 401k.
print(f" The balance in Fidelity 401k : $")
print(accounts["Fidelity"])

# 3. @TODO: What’s up with that one penny Wells Fargo account?
# Delete that account from the dictionary.
del accounts["Wells Fargo"]
print(accounts)

# Add the new 401k account (this one’s with SoFi)
# to the list of existing accounts.
accounts["SoFi"]=2000
print(accounts)

# 5. @TODO: Create a new dictionary to store the new 401k rollover
# First copy the following list:
new_accounts={}

# 6. @TODO: Sum up your money from the `old_account_amounts` list
# Save this total amount to a new variable called `total_amount`.
old_account_amounts=[2000, 8000, 3000, 2000]
total_amount=sum(old_account_amounts)

# 7. @TODO: Finally, create a new dictionary called `new_accounts`.
new_accounts["WealthFront"]=total_amount

# Store the new 401k as a new entry.
# YOUR CODE HERE!

# Print the new_accounts dictionary
print(new_accounts)
