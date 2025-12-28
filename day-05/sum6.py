string="The quick brown fox jumps over the lazy dog"
alphabet="abcdefghijklmnopqrstuvwxyz"
if set((string)) >= set(alphabet):
    print("Pangram")
else:
    print("Not pangram")