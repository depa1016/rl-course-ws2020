# Lab 2

In the second lab, we continue working on the  [FrozenLake environment](https://gym.openai.com/envs/FrozenLake-v0/)
and implement the concept of Q-value prediction with Monte Carlo prediction.


### Task 1:
- Download and execute `2_FrozenLake_Prediction.py` on GitHub.
This file plays episodes in the 4x4 lake environment using a random policy until a reward is earned.
This is repeated for 100 iterations.
- After every episode, calculate the Q-values with every-visit MC prediction using the average mean method and no discount on the reward.
- After every successful episode, print out the current Q-values.

### Task 2:
We use now the learned Q-values to simulate episodes:

- After every successful episode, in addition to printing the Q-values run 100 episodes using a greedy policy on the current Q-values.
- Print the average reward per episode for those 100 episodes.