# Step 1: Create a sample server.log file
sample_logs = [
    "Error at line 1",
    "Warning at line 2",
    "Error at line 3",
    "Warning at line 4",
    "Error at line 5"
]

with open("server.log", "w") as file:
    for log in sample_logs:
        file.write(log + "\n")

# Step 2: Read the file and analyze
with open("server.log", "r") as file:
    lines = file.readlines()

word_count = {}      # dictionary for frequency
unique_words = set() # set for unique words

# Step 3: Process each line
for line in lines:
    words = line.strip().lower().split()  # lowercase + split
    for word in words:
        unique_words.add(word)  # add to set
        word_count[word] = word_count.get(word, 0) + 1  # count words

# Step 4: Sort words by frequency
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Step 5: Print results
print("Top 5 frequent words:")
for word, freq in sorted_words[:5]:
    print(f"{word}: {freq}")

print("Unique words:", unique_words)
print("Total number of lines =", len(lines))
