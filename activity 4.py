def format_column(title, width=20):
    """Format the column title to a fixed width."""
    return title[:width].ljust(width)# Prompt the user for the number of columns

num_columns = int(input("How many columns do you want in the table? "))# Prompt the user for column titles

column_titles = []
for i in range(num_columns):
    title = input(f"Enter title for column {i + 1}: ")
    column_titles.append(format_column(title))

header = "|".join(column_titles)# Print the table header
print(header)
print("-" * len(header))


sample_data = [
    ["Data 1", "Data 2", "Data 3"],  # Row 1
    ["Sample", "Example", "Demo"],   # Row 2
    ["Row 3", "Info", "Details"]     # Row 3
]# Sample data for demonstration

for row in sample_data:
    formatted_row = "|".join(format_column(item) for item in row)
    print(formatted_row)# Print the sample data rows
