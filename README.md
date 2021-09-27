# Q-pathplanning
## Q-Learning Path Planning for Multi-Agent System in Traffic Networks

In this project, I developed a path planning method based on reinforcement learning algorithm in multi-agent system (MAS). The path planning is based on the real-time updated Q value, the agent selects the path with the smallest Q value, and the Q value is updated by the Q-learning algorithm. During the running of the vehicle, congestion will be uploaded to the management center in time, and the management center will update the Q value according to the congestion level, thereby alleviating road congestion. In this project, a simulation model is built. The simulated roads are grid-like. It is assumed that there are eight routes (OD). Each starting point will generate vehicles through Poisson distribution to simulate the actual road conditions. This project tested three parameters: learning rate, discount factor, and greedy exploration, to figure out which combination have the best performance. At the same time, three evaluation parameters are selected to analyze algorithm performance: driving time on each route, driving time from starting point to destination point, and road congestion degree. Finally, I simulate this model at different level of traffic flow and compare the performace. Observing the simulation results, we can see that the algorithm can use traffic information to reduce road congestion.

### Algorithm pseudocode：

![image](https://github.com/liguanlue/Q-pathplanning/blob/main/IMG/pathplanning.png)


