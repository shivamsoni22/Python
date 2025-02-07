#  String Manipulation - Reverse Words in a String
# Question:
# Ek string di gayi hai, tumhe words ko reverse karna hai bina extra spaces add kiye.
def reverse_words(s):
    return " ".join(s.strip().split()[::-1])

# Example
print(reverse_words("  hello   world  "))  # Output: "world hello"
