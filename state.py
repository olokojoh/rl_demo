def win(s, win_state):
    for i in win_state:
        if 1 == s[i[0]] == s[i[1]] == s[i[2]]:
            # print('p1 win!')
            return True, 1
        if 2 == s[i[0]] == s[i[1]] == s[i[2]]:
            # print('p2 win!')
            return True, 2
    return False, 0