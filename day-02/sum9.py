string=input("Enter a string: ").lower()
alphabets="abcdefghijklmnopqrstuvwxyz"
if set(string) >= set(alphabets):
    print("Pangram")
else:
    print("Not pangram")