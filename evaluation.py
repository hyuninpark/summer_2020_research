from simulation import run_simulation
import numpy as np
from policies import *
from environment import Servers
from estimators import Evaluation
import sys

if __name__ == "__main__":
    # Initialize basic variables
    num_requests = 15#int(input("num_requests: "))
    num_servers = 4#int(input("num_servers: "))
    num_trajectories_list = [0] + [10 ** i for i in range(1, 7)]
    start_trajectory_index = 0
    num_boot = 5
    # end_trajectory_index = 1

    # Initialize policies
    behavior_policy = ('UniRan', UniRan(num_servers))
    target_policy1 = ('LeastLoad_0.3', LeastLoad(num_servers, epsilon=0.3))
    target_policy2 = ('LeastLoad_0', LeastLoad(num_servers, epsilon=0))
    target_policy3 = ('EpsilonGreedy', EpsilonGreedy(num_servers, epsilon=0.3))
    target_policy4 = ('UCB1', UCB1(num_servers))

    # behavior_policy = ('EpsilonGreedy', EpsilonGreedy(num_servers, epsilon=0.3))
    # target_policy1 = ('LeastLoad_0.3', LeastLoad(num_servers, epsilon=0.3))
    # target_policy2 = ('LeastLoad_0', LeastLoad(num_servers, epsilon=0))
    # target_policy3 = ('UniRan', UniRan(num_servers))
    # target_policy4 = ('UCB1', UCB1(num_servers))


    target_policies = [target_policy1, target_policy2, target_policy3, target_policy4]
    num_target_policies = len(target_policies)

    policies = [target_policy1, target_policy2, target_policy3, target_policy4, behavior_policy]
    num_policies = 1 + num_target_policies

    target_policy_names = [policy[0] for policy in policies if policy != policies[-1]]

    # Initialize environment (servers)
    servers = Servers(num_policies=num_policies, num_servers=num_servers)

    # Initialize evaluation for each seed
    evaluations = [Evaluation(horizon=num_requests,
                              num_target_policies=num_target_policies,
                              num_actions=num_servers)
                   for _ in range(num_boot)]

    # Iterate over random seed
    for i in range(5):
        # bootstrap
        np.random.seed(seed)

        # Set a particular evaluation for the seed
        seed_evaluation = evaluations[seed - seed_add]

        # Iterate over trajectories of the given number to run simulation
        for trajectory_index in range(num_trajectories_list[num_trajectories_index - 1], num_trajectories_list[num_trajectories_index]):
            print(f"seed:{seed - seed_add} / trajectory: {seed_evaluation.num_trajectories}", end='\r')

            # Run simulation and get trace & true performances of every target policy
            total_latency_for_each_policy, trace = \
                run_simulation(policies=policies, num_requests=num_requests, servers=servers)

            # Get the estimate of every target policy on the trajectory. 


    # After finishing iterating over every random seed,
    # display the estimate of each target policy for the given number of trajectories
    for seed_evaluation in evaluations:
                """
                Implement
                """




