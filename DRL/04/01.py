
import matplotlib.pyplot as plt
import numpy as np
from pandas import *
from gym import envs
import gym
import torch



def main():
    env =gym.make('CartPole-v0')
    state1 = env.reset()
    print(state1)
    action = env.action_space.sample()
    state,reward,done,info=env.step(action)
    l1 = 4
    l2 = 150
    l3 = 2
    model = torch.nn.Sequential(
        torch.nn.Linear(l1, l2),
        torch.nn.LeakyReLU(),
        torch.nn.Linear(l2, l3),
        torch.nn.Softmax())
    learning_rate = 0.0009
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
    pred = model(torch.from_numpy(state1).float())
    action = np.random.choice(np.array([0, 1]), p=pred.data.numpy())
    state2, reward, done, info = env.step(action)


if __name__ == '__main__':
    main()
