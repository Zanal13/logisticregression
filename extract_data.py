def extract_values(text, digit_number):
    entries = text.split("\n")
    for entry in entries:
        if digit_number in entry:
            values = entry.split(",")
            before = values[values.index("D") - 3]
            after = values[values.index("D") + 1]
            return before, after

    return None

digit_number = input("Enter the 16-digit number: ")

values = extract_values(text, digit_number)

if values:
    print(f"Before: {values[0]}, After: {values[1]}")
else:
    print("The 16-digit number does not exist in the text.")
