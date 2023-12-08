keywords = ['False', 'True', 'None', 'and', 'with', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except']

new_keywords = [word for word in keywords if len(word) >= 5]

print(new_keywords)
