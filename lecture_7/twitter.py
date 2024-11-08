import re

url = input("Enter the URL: ").strip();

#? re.sub(pattern, repl, string, count=0, flags=0)
new_url = re.sub(r"https?://", "", url);
print(new_url);

#? walrus operator (:=) is a short-hand for assigning a value to a variable and using it in the same line
if matches := re.search(r"^https?://(?:www\.)?twitter\.com/(.+)$", url, re.IGNORECASE):  
    print(f"Username:", matches.group(1))