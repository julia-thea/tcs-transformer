import csv

# Initialize lists to store data
titles, preconditions, expected_results = [], [], []

# Read file and populate lists
with open("chat.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line.startswith("Test Case"):
            titles.append(line.replace("Test Case: ", ""))
        elif line.startswith("Precondition"):
            preconditions.append(line.replace("Precondition: ", ""))
        elif line.startswith("Expected result"):
            expected_results.append(line.replace("Expected result: ", ""))

# Write all data to CSV with headers
with open("target.csv", "w", newline="") as csvfile:
    mywriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    
    # Write column headers
    mywriter.writerow(["Title", "Precondition", "Test Steps", "Expected Result", "Automated", "References"])
    
    # Write the data rows
    for title, precondition, expected_result in zip(titles, preconditions, expected_results):
        # Populate the empty columns "Test Steps" and "References" with empty strings
        mywriter.writerow([title, precondition, "", expected_result, "No", "", ""])
