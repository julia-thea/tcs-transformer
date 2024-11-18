import csv

# Initialize lists to store test case data
titles, preconditions, test_steps, expected_results = [], [], [], []

# Read file and populate lists
with open("chat.txt", "r") as f:
    title, precondition, test_step, expected_result = "", "", "", ""
    current_section = None  # Tracks the current section being processed
    
    for line in f:
        line = line.strip()
        
        # Skip empty lines
        if not line:
            continue
        
        # Identify the section of the test case
        if line.startswith("Test Case"):
            # If there's already a test case being processed, save it
            if title:
                titles.append(title)
                preconditions.append(precondition.strip())
                test_steps.append(test_step.strip())
                expected_results.append(expected_result.strip())
            
            # Start a new test case
            title = line.replace("Test Case: ", "")
            precondition, test_step, expected_result = "", "", ""  # Reset for the new test case
            current_section = None  # Reset section tracker
        
        elif line.startswith("Preconditions:"):
            current_section = "Preconditions"
        elif line.startswith("Test Steps:"):
            current_section = "Test Steps"
        elif line.startswith("Expected Result:"):
            current_section = "Expected Result"
        
        # Append content to the relevant section
        elif current_section == "Preconditions":
            precondition += line + "\n"
        elif current_section == "Test Steps":
            test_step += line + "\n"
        elif current_section == "Expected Result":
            expected_result += line + "\n"
    
    # Append the last test case (if the file ends without another Test Case)
    if title:
        titles.append(title)
        preconditions.append(precondition.strip())
        test_steps.append(test_step.strip())
        expected_results.append(expected_result.strip())

# Write all data to CSV with headers
with open("target.csv", "w", newline="") as csvfile:
    mywriter = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    
    # Write column headers
    mywriter.writerow(["Title", "Precondition", "Test Steps", "Expected Result", "Automated", "References"])
    
    # Write the data rows
    for title, precondition, test_step, expected_result in zip(titles, preconditions, test_steps, expected_results):
        # Populate the empty columns "Automated" and "References" with default values
        mywriter.writerow([title, precondition, test_step, expected_result, "No", ""])
