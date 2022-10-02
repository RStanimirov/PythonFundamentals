import re

text = input()

valid_emails_list = []

pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"
# 1. (^|(?<=\s)) - check if there's a start of a string OR ( " | ") if there's space (what the first group does).
# 2. ([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@) - check : (word which contains letters and numbers);
# (then check some of the allowed symbols IF there is, hence we use "?");
# (then again word which contains letters and numbers); the words number can be 1.
# 3. (include the symbol @)
# 4. ([a-zA-Z]+([\.\-_][A-Za-z]+)+) - search for word;
# but after the word there SHOULD be any of the allowed symbols ".", "-" or "_";
# otherwise the string will be faulty with having only one word;
# because the problem says there should be at least 2 words;
# finally the domain - a (.bg, .net and so on), for example @mail.uu.net;
# ([a-zA-Z]+([\.\-_][A-Za-z]+)+) - the plus sign is crucial for group 8,
# as it seeks two more matches ... you can mark more words, but they SHOULD
# start with any of the allowed symbols.
# 5. (\b|(?=\s)) the same as 1. - checks for boundary \b or positive lookahead
# to check if there is a white space.

match = re.finditer(pattern, text)

for x in match:
    valid_emails_list.append(x.group())

# print(valid_emails_list)
print('\n'.join(valid_emails_list))