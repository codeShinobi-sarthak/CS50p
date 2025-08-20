import os
from datetime import datetime

filename = "journal.txt"
header = "Date          Time        Entry\n---------------------------------------\n"

# --- The New Logic ---
# Check if the file exists BEFORE we open it
file_exists = os.path.exists(filename)
# --------------------

try:
    # Use append mode 'a'. It creates the file if it doesn't exist.
    with open(filename, 'a') as file:
        # If the file did NOT exist, then we are creating it for the first time.
        # So, we should write the header.
        if not file_exists:
            file.write(header)
        
        # Now, continue with the normal process
        entry = input("Enter your journal entry: ")
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        
        file.write(f"{date_str}    {time_str}    {entry}\n")

except IOError:
    print("Error: Could not write to the journal file.")

else:
    print("Journal entry saved successfully!")

finally:
    print("Journal program finished.")