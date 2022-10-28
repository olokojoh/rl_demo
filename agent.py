import numpy as np

class Agent():
    def __init__(self, OOXX_index, Epsilon=0.1, Lr=0.1):
        self.value = np.zeros((3, 3, 3, 3, 3, 3, 3, 3, 3))
        self.currentState = np.zeros(9)
        self.previousState = np.zeros(9)
        self.index = OOXX_index
        self.epsilon = Epsilon
        self.alpha = Lr

    def reset(self):
        self.currentState = np.zeros(9)
        self.previousState = np.zeros(9)

    def actionTake(self, State):
        state = State.copy()
        available = np.where(state == 0)[0]
        length = len(available)
        if length == 0:
            return state
        else:
            random = np.random.uniform(0, 1)
            # 如果小于0.1,则触发随机行动
            if random < self.epsilon:
                choose = np.random.randint(length)
                state[available[choose]] = self.index
            # 否则按照价值最大的位置落子（greedy）
            else:
                tmpValue = np.zeros(length)
                # 遍历所有可能的选择，计算value，取最大的做为本次action
                for i in range(length):
                    tempState = state.copy()
                    tempState[available[i]] = self.index
                    tmpValue[i] = self.value[tuple(tempState.astype(int))]
                choose = np.where(tmpValue == np.max(tmpValue))[0]
                chooseIndex = np.random.randint(len(choose))
                state[available[choose[chooseIndex]]] = self.index
        return state

    def valueUpdate(self, State, Reward=0):
        self.currentState = State.copy()
        self.value[tuple(self.previousState.astype(int))] += \
            self.alpha * (Reward + self.value[tuple(self.currentState.astype(int))] - self.value[
                tuple(self.previousState.astype(int))])

        self.previousState = self.currentState.copy()

    def changePara(self, epsilon, lr):
        self.epsilon = epsilon
        self.alpha = lr