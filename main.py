# person's who interact with admin.

with open("_chat.txt", 'r', encoding='utf-8') as fp:
    text = fp.readlines()
    
# Create an empty set to store unique user names
user_names = set()

# Iterate through each line in the text
for line in text:
    # Check if the line contains 'sir'
    if 'sir' in line.lower():
        # Extract the user name from the line
        parts = line.split(']')  # Split the line by ']'
        if len(parts) >= 2:
            user_name = parts[1].strip().split(':')[0]
            user_names.add(user_name)
user_names.remove('ThiyagaB')
# Print the unique user names who mentioned 'sir'
for name in user_names:
    print(name)