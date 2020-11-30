# Lab 2

In the second lab, we continue working on the  [FrozenLake environment](https://gym.openai.com/envs/FrozenLake-v0/)
and implement the concept of Q-value prediction.


### Task 1:
1. Play episodes in the 4x4 environment using a random policy until a reward is earned (you can use `solutions/S1_FrozenLake_Random.py` on GitHub as
starting point).
2. After step 1 is finished, calculate the Q-values of all visited state-action pairs using every-visit MC
prediction.
3. Repeat step 1 and 2 for 10 times and print the updated Q-values after each successful episode.
4. Play an episode in which the agent greedily decides in every time step of the action with the hightest Q-value.

### Task 2:
- Do the same as in Task 1 but now use TD-Prediction to update the Q-values.
