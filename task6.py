def count(word):
    result=dict()
    for line in word:
        local=word.count(line)
        result[line]=local
    return result

print(count("Mississippi"))

