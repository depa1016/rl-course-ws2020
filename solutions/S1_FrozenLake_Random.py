import gym
import random

env = gym.make("FrozenLake-v0", is_slippery=False)

random.seed(0)

print("## Frozen Lake ##")
print("Start state:")
env.render()

no_of_actions = env.env.nA
action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}


def play_episode(env, policy=None):
    state = env.reset()
    done = False
    all_reward = 0
    states = [state]
    actions = []
    while not done:
        if policy is None:
            action = random.randint(0, no_of_actions-1)  # choose a random action
        else:
            action = policy[state]

        actions.append(action)
        state, reward, done, _ = env.step(action)
        states.append(state)
        all_reward += reward

    return states, actions, all_reward


# Task 1:
print(f"\n ### TASK 1 ### ")

count = 0
converged = False
s, a = [], []
while not converged:
    s, a, r = play_episode(env)
    count += 1
    if r > 0:
        converged = True

print(f"Converged after {count} episodes.")
print(f"Took {len(s)} steps.")


policy = {}
for i, v in enumerate(s[:-1]):
    policy[v] = a[i]

print(policy)
s, a, r = play_episode(env, policy)
if r > 0:
    print(f"Success: New policy took {len(s)} steps.")
else:
    print("New policy failed!")


# Task 2:
print(f"\n ### TASK 2 ### ")

env_8x8 = gym.make("FrozenLake-v0", is_slippery=False, map_name="8x8")

count = 0
converged = False
s, a = [], []
while not converged:
    s, a, r = play_episode(env_8x8)
    count += 1
    if r > 0:
        converged = True

print(f"Converged after {count} episodes.")
print(f"Took {len(s)} steps.")

policy_8x8 = {}
for i, v in enumerate(s[:-1]):
    policy_8x8[v] = a[i]

print(policy_8x8)
s, a, r = play_episode(env_8x8, policy_8x8)
if r > 0:
    print(f"Success: New policy took {len(s)} steps.")
else:
    print("New policy failed!")

# Task 3:
print(f"\n ### TASK 3 ### ")
env_slippery = gym.make("FrozenLake-v0")
s, a, r = play_episode(env_slippery, policy)
if r > 0:
    print(f"Success: New policy took {len(s)} steps.")
else:
    print("New policy failed!")


