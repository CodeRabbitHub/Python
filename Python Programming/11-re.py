# Introduction to Regular Expressions

# Regular expressions are a powerful tool for matching patterns in text data.
# They are used for tasks such as validating input, searching for information, and manipulating text.
# Regular expressions are made up of characters and meta-characters, which have special meanings.
# The characters are used to match literal characters in the text, while the meta-characters are used to specify patterns.
# The re (regular expression) module in Python provides functions for working with regular expressions.
# It allows you to search for patterns in text, replace text, and split text into parts.
# Regular expressions can be complex and difficult to read, but with practice and experience, you can create very powerful
# expressions for text data analysis.
# In this tutorial, we will cover the basics of regular expressions, including syntax, special characters, character classes,
# anchors, quantifiers, and grouping.

# Basic Syntax in Regular Expressions

import re

# 1. Literal Characters
# A literal character matches exactly the same character in the text:
text = "Hello, World!"
result = re.findall("Hello", text)
print(result)  # Output: ['Hello']

# 2. Meta-Characters
# Meta-characters have special meanings in regular expressions. Some of the most commonly used meta-characters are:
# . ^ $ * + ? { } [ ] \ | ( )

# 3. Character Classes
# A character class allows you to match any one character from a set of characters:
text = "Hi 123 Hello 456"
result = re.findall("[0-9]+", text)
print(result)  # Output: ['123', '456']

# 4. Anchors
# Anchors are used to match the position of characters, rather than the characters themselves:
text = "Hello\nHi"
result = re.findall("^H.*", text, re.MULTILINE)
print(result)  # Output: ['Hello', 'Hi']

# 5. Quantifiers
# Quantifiers are used to specify the number of occurrences of a character:
text = "Go Goa Gone"
result = re.findall("Go+", text)
print(result)  # Output: ['Goa', 'Gone']

# 6. Grouping
# Grouping allows you to apply a quantifier to a group of characters:
text = "Hi 123 Hello 456"
result = re.findall("[0-9]+", text)
print(result)  # Output: ['123', '456']

# Understanding the basic syntax of regular expressions is important in order to create powerful and accurate expressions to extract information from text data.

# Special Characters in Regular Expressions

import re

# 1. Dot (.)
# Matches any character except a newline character:
text = "Hello, World!"
result = re.findall("He.llo", text)
print(result)  # Output: ['Hello']

# 2. Star (*)
# Matches zero or more occurrences of the preceding character:
text = "Go Goa Gone"
result = re.findall("Go*", text)
print(result)  # Output: ['Go', 'Go', 'Go', 'Gone']

# 3. Plus (+)
# Matches one or more occurrences of the preceding character:
text = "Go Goa Gone"
result = re.findall("Go+", text)
print(result)  # Output: ['Go', 'Goa', 'Gone']

# 4. Question Mark (?)
# Matches zero or one occurrence of the preceding character:
text = "Color color"
result = re.findall("Colou?r", text)
print(result)  # Output: ['Color', 'color']

# 5. Brackets ([])
# Matches any character within the brackets:
text = "Hi 123 Hello 456"
result = re.findall("[0-9]+", text)
print(result)  # Output: ['123', '456']

# 6. Caret (^)
# Matches the start of the line:
text = "Hello\nHi"
result = re.findall("^H.*", text, re.MULTILINE)
print(result)  # Output: ['Hello', 'Hi']

# 7. Dollar Sign ($)
# Matches the end of the line:
text = "Hello\nHi"
result = re.findall(".*i$", text, re.MULTILINE)
print(result)  # Output: ['Hi']

# 8. Pipe (|)
# Matches either the expression before or after the pipe:
text = "Hi 123 Hello 456"
result = re.findall("Hi|Hello", text)
print(result)  # Output: ['Hi', 'Hello']

# These are some of the most commonly used special characters in regular expressions. Understanding how to use these
# special characters can help you create complex and powerful regular expressions to extract information from text data.

# Using the re module in Python
# To use regular expressions in Python, you can use the `re` module, which provides several functions for pattern matching and substitution.
# Here's an example of using `re.search` to search for a pattern in a string:

text = "The quick brown fox jumps over the lazy dog."

# Search for the pattern "fox" in the string
match = re.search("fox", text)

# Check if a match was found
if match:
    print("Match found!")
    # Print the start and end indices of the match
    print("Start index:", match.start())
    print("End index:", match.end())
else:
    print("Match not found.")

# In addition to searching for patterns, the `re` module also allows you to replace matched patterns with new text.
# Using `re.sub` to replace patterns
# The `re.sub` function replaces all occurrences of a pattern in a string with a new string.
# Here's an example:

text = "The quick brown fox jumps over the lazy dog."

# Replace the pattern "fox" with "cat"
new_text = re.sub("fox", "cat", text)
print(new_text)  # Output: The quick brown cat jumps over the lazy dog.

# Finding all matches using `re.findall` and `re.finditer`
# The `re.findall` function returns a list of all non-overlapping matches in the string as a list of strings.
# The `re.finditer` function returns an iterator yielding match objects for all non-overlapping matches.

# Here's an example of using `re.findall`:
text = "The quick brown fox jumps over the lazy dog."

# Find all occurrences of the pattern "o"
occurrences = re.findall("o", text)
print(occurrences)  # Output: ['o', 'o', 'o']

# Here's an example of using `re.finditer`:

# Find all occurrences of the pattern "o"
occurrences = re.finditer("o", text)
for match in occurrences:
    print("Match found!")
    # Print the start and end indices of the match
    print("Start index:", match.start())
    print("End index:", match.end())

# Grouping with `re.match` and `re.search`
# You can group parts of a pattern using parentheses. This allows you to extract specific parts of a match.
# For example:

text = "The quick brown fox jumps over the lazy dog."

# Use parentheses to group the pattern "brown fox"
match = re.search("(brown fox)", text)
if match:
    print("Match found!")
    # Extract the matched group
    print("Group:", match.group(1))

# Alternatives with the `|` character
# You can match multiple patterns by using the `|` character, which represents an "or" operator.
# For example:

text = "The quick brown fox jumps over the lazy dog."

# Use the `|` character to match either "fox" or "dog"
match = re.search("fox|dog", text)
if match:
    print("Match found!")

# Quantifiers with `*`, `+`, `?`, and `{}`

# You can specify the number of times a pattern should occur using quantifiers.
# For example:

text = "The quick brown fox jumps over the lazy dog."

# Use the `*` quantifier to match zero or more occurrences of "o"
occurrences = re.findall("o*", text)
print(occurrences)

# Use the `+` quantifier to match one or more occurrences of "o"
occurrences = re.findall("o+", text)
print(occurrences)

# Use the `?` quantifier to match zero or one occurrences of "o"
occurrences = re.findall("o?", text)
print(occurrences)

# Use the `{}` quantifier to match a specific number of occurrences of "o"
occurrences = re.findall("o{2}", text)
print(occurrences)

# There are many more advanced features in the `re` module, but these are some of the most commonly used. With these tools, you should be able to perform most regular expression tasks in Python.

# Commonly Used Regular Expressions Patterns

# 1. Matching any character
# Use the dot `.` to match any character except newline:
text = "hello world"
result = re.findall("h.llo", text)
print(result)  # Output: ['hello']

# 2. Matching digits
# Use the `\d` to match any digit:
text = "The number is 42"
result = re.findall("\d+", text)
print(result)  # Output: ['42']

# 3. Matching whitespaces
# Use the `\s` to match any whitespace character (spaces, tabs, etc.):
text = "The quick\tbrown\nfox jumps over the lazy dog."
result = re.findall("\s+", text)
print(result)  # Output: ['\t', '\n']

# 4. Matching word characters
# Use the `\w` to match any word character (letters, digits, underscores):
text = "Python_is_fun"
result = re.findall("\w+", text)
print(result)  # Output: ['Python_is_fun']

# 5. Matching non-word characters
# Use the `\W` to match any non-word character:
text = "Python! is fun."
result = re.findall("\W+", text)
print(result)  # Output: ['! ', ' is ', '.']

# 6. Matching start and end of a line
# Use the `^` to match the start of a line, and the `$` to match the end of a line:
text = "The quick brown\nfox jumps over\nthe lazy dog."
result = re.findall("^The.*dog.$", text, flags=re.MULTILINE)
print(result)  # Output: ['The quick brown\nfox jumps over\nthe lazy dog.']

# 7. Matching Phone Numbers
# Use the following pattern to match phone numbers in the format xxx-xxx-xxxx:
text = "My phone number is 123-456-7890."
result = re.findall("\d{3}-\d{3}-\d{4}", text)
print(result)  # Output: ['123-456-7890']

# 8. Matching URLs
# Use the following pattern to match URLs:
text = "The website is https://www.google.com."
result = re.findall("https?://[\w.-]+\.[\w]+", text)
print(result)  # Output: ['https://www.google.com']

# 9. Matching Email Addresses
# Use the following pattern to match email addresses:
text = "My email is john.doe@example.com."
result = re.findall("[\w._%+-]+@[\w.-]+\.[\w]+", text)
print(result)  # Output: ['john.doe@example.com']

# 10. Matching Prices
# Use the following pattern to match prices in the format $x.xx:
text = "The price is $5.99."
result = re.findall("\$\d+\.\d{2}", text)
print(result)  # Output: ['$5.99']

# 11. Matching Dates
# Use the following pattern to match dates in the format yyyy-mm-dd:
text = "The date is 2022-01-01."
result = re.findall("\d{4}-\d{2}-\d{2}", text)
print(result)  # Output: ['2022-01-01']
