# process_file.py

# Step 1: Read the contents of input.txt
with open("input.txt", "r") as infile:
    content = infile.read()
print(content)
# Step 2: Count the number of words
words = content.split()
word_count = len(words)

# Step 3: Convert all text to uppercase
upper_content = content.upper()

# Step 4: Write processed text + word count to output.txt
with open("output.txt", "w") as outfile:
    outfile.write("Processed Text:\n")
    outfile.write(upper_content + "\n\n")
    outfile.write(f"Word Count: {word_count}\n")

# Step 5: Print success message
print("✅ output.txt has been created successfully!")
