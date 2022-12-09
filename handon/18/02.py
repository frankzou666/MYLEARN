"""
Author:
Purpose:
Date："""
import argparse
import gym
import numpy as np


def getargs():
    """
    :arg
    :return   programare guemnts
    :date
    """
    argparser = argparse.ArgumentParser(description='say')
    argparser.add_argument('--name', default='world!', help='name message')
    return argparser.parse_args()


def basic_policy(obs):
       angle = list(obs[0])[2]
       print(angle)
       return 0 if angle < 0 else 1





def main():
    """the entrance of this file"""
    env =gym.make("CartPole-v1")
    obs= env.reset()
    action=1
    env.step(action)
    totals = []
    obs, reward, terminated,truncated , info = env.step(action)
    for episode in range(500):
        episode_rewards = 0
        obs = env.reset()
        for step in range(200):
            action = basic_policy(obs)
            obs, reward, terminated,truncated , info = env.step(action)
            episode_rewards += reward
            if terminated:
                break
    totals.append(episode_rewards)


if __name__ == '__main__':
    main()
