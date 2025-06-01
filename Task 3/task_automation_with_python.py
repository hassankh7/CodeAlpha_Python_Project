

import re


# Step 1: input.txt 
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Email address find karna using regular expression
emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", content)

# Step 3: Emails Add New fills 
with open("emails_output.txt", "w") as output_file:
    for email in emails:
        output_file.write(email + "\n")

print("✅ All email addresses extracted and saved to 'emails_output.txt'")