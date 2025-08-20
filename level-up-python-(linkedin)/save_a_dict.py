"""
here pickling function can be used

see here : https://docs.python.org/3/library/pickle.html
"""

import os


def save_a_dict(data_dict, file_path):
    header = "key  value"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(header + "\n")
        for key, value in data_dict.items():
            f.write(f"{key}  {value}\n")

    print("Dictionary saved to", file_path)


def retrieve_a_dict(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        print(f.read())


data = {"key1": "value1", "key2": "value2", "key3": "value3"}

if __name__ == "__main__":
    # Build path next to this script, not under the script file name
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dict.txt")
    save_a_dict(data, path)
    retrieve_a_dict(path)
    print(data)
