# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    # Your code goes here!
    sentence = "I am super excited for this course!"
    message = sentence
    for i in range(0,4):
        message += " "+sentence
    return message

print show_excitement()
