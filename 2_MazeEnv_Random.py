from mazeEnv import MazeEnv
import random


env = MazeEnv()

random.seed(0)

print("## Frozen Lake ##")
print("Start state:")
env.render()

action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

state = env.reset()
done = False

i = 0
r_all = 0

while not done:
    action = random.randint(0, 3)  # choose a random action
    state, reward, done, _ = env.step(action)
    r_all += reward
    i += 1
    print(f"\nAction:{action2string[action]}, new state:{state}, reward:{reward}")
    env.render()

print(f"\ndone after {i} steps, earned reward of {r_all}!")

