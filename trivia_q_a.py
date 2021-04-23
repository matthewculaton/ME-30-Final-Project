trivia_dictionary = {
    "What is the capital of California?":"Sacramento",
    "What year was SJSU founded":"1857"
}

def trivia():
    q_pair = key, val = random.choice(list(trivia_dictionary.items()))
    ques = q_pair[0]
    answer = q_pair[1]
    return ques
