"""
Author:
Purpose:
Date："""
import argparse
import gym
import numpy as np
import keras
import tensorflow as tf


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
      # print(obs)
       angle = obs[2]
       #print(angle)
       return 0 if angle < 0 else 1



def get_model():
    """

    :return:
    """
    n_inputs = 4  # == env.observation_space.shape[0]
    model = keras.models.Sequential([
        keras.layers.Dense(5, activation="elu", input_shape=[n_inputs]),
        keras.layers.Dense(1, activation="sigmoid"),
    ])



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
            if isinstance(obs,tuple):
                obs=obs[0]
            action = basic_policy(obs)
            obs, reward, terminated,truncated , info = env.step(action)
            episode_rewards += reward
            if terminated:
                break
    totals.append(episode_rewards)
    print(np.max(totals))





if __name__ == '__main__':
    main()
