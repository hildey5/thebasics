def sentence_maker(phrase):
    interrogatives = ("who", "what", "when", "where", "why", "how")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}?". format(capitalized)
    else:
        return "{}".format(capitalized)

results = []
while True:
    user_input = input("say something:")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print("".join(results))
