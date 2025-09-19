# File Read & Write Program

# Step 1: Read from the input file
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Modify the content (convert to uppercase)
modified_content = content.upper()

# Step 3: Write the modified content to a new file
with open("output.txt", "w") as outfile:
    outfile.write(modified_content)

# Step 4: Print success message
print("✅ File has been read and modified. Output saved to 'output.txt'")



