def check_answer(answers: dict[str, str]) -> str:
    correct_answer = ['c', 'b', 'a', 'b', 'a']
    message = ''
    for i, ans in enumerate(answers.values()):
        message += '\n'
        if ans[0] == correct_answer[i]:
            message += f'{i + 1} - {ans} ✅'
        else:
            message += f'{i + 1} - {ans} ❌'
    return message
