import inflect

result = 0
engine = inflect.engine()
for i in range(1, 1001):
    number_str = engine.number_to_words(i)
    result += sum(char != " " and char != "-" for char in number_str)
print(result)

