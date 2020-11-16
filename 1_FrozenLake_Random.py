import gym
import random

env = gym.make("FrozenLake-v0", is_slippery=False)

random.seed(0)

print("## Frozen Lake ##")
print("Start state:")
env.render()

no_of_actions = env.env.nA
action2string = {0: "Left", 1: "Down", 2: "Right", 3: "Up"}

# Example execution of an random episode

state = env.reset()
done = False

while not done:
    action = random.randint(0, no_of_actions-1)  # choose a random action
    state, reward, done, _ = env.step(action)
    print(f"\nAction:{action2string[action]}, new state:{state}, reward:{reward}")
    env.render()

print("\ndone!")


# Task 1:
# - Run episodes using the random policy until the agent reaches the goal (reward > 0).
# - Print how many runs it took to get a successful trial.
# - Remember the states and actions that were taken in this trial. How many actions did it take to reach the goal?
# - Given these results, write an algorithm that generates a policy that reaches the goal faster.
# - Run one episode using this new policy and compare the results.

# Task 2:
# - Increase the map size using the 8x8 env:
#   env_8x8 = gym.make("FrozenLake-v0", is_slippery=False, map_name="8x8")
# - Compare the results to task 1.

# Task 3:
# - Use the learned policy from Task 1 and execute it in an 4x4 env that is slippery:
#   env_slippery = gym.make("FrozenLake-v0", is_slippery=False)
# - What is the problem with the learned policy?
# - How can we learn a good policy in such an environment?



