import gym[Box2D]
import pygame

env = gym.make("CarRacing-v0")
observation = env.reset()

done = False
while not done:
    observation, reward, done, info = env.step(env.action_space.sample())
    print(env.action_space.sample())

    env.render()