import numpy as np
from agent import Agent
from state import *
from tqdm import tqdm

def main():
    p1 = Agent(1, Epsilon=0.1, Lr=0.1)
    p2 = Agent(2, Epsilon=1, Lr=0)

    times = 10000
    record = {0: 0, 1: 0}
    # 0,1,2,
    # 3,4,5,
    # 6,7,8
    win_state = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 4, 8), (2, 4, 6), (0, 3, 6), (1, 4, 7), (2, 5, 8)]
    record = []
    state = np.zeros(9)

    for i in tqdm(range(times * 3)):
        while True:
            pS = state.copy()
            state = p1.actionTake(state)
            # 终局或者赢
            if (state == pS).all() or win(state, win_state)[0]:
                p1.valueUpdate(state, 1)
                p2.valueUpdate(state, -1)
                break
            p1.valueUpdate(state)

            pS = state.copy()
            state = p2.actionTake(state)
            # 终局或者赢
            if (state == pS).all() or win(state, win_state)[0]:
                p1.valueUpdate(state, -1)
                p2.valueUpdate(state, 1)
                break

            p2.valueUpdate(state)

        record.append(win(state, win_state)[1])
        p1.reset()
        p2.reset()
        state = np.zeros(9)

    result = {0: 0, 1: 0, 2: 0}
    for i in record:
        result[i] += 1
    print(f'p1胜率：{result[1] / len(record) * 100}%')
    print(f'p2胜率：{result[2] / len(record) * 100}%')
    print(f'和棋率：{result[0] / len(record) * 100}%')
if __name__ == '__main__':
    main()

