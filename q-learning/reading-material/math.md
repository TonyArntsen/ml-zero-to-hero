# Bellman equation

A Bellman equation, named after Richard E. Bellman, is a technique in dynamic programming which breaks an optimization problem into a sequence of simpler subproblems, as Bellman's "principle of optimality" prescribes. It is a necessary condition for optimality. The "value" of a decision problem at a certain point in time is written in terms of the payoff from some initial choices and the "value" of the remaining decision problem that results from those initial choices. The equation applies to algebraic structures with a total ordering; for algebraic structures with a partial ordering, the generic Bellman's equation can be used.

## Application in q-learning

```math
Q(s,a)\leftarrow Q(s,a)+\alpha \left[R(s,a)+\gamma \max _{a^{\prime }}Q(s^{\prime },a^{\prime })-Q(s,a)\right]
```

Variable Breakdown:

• α (Learning Rate): Set between 0 and 1. Dictates how much new information overrides old information.

• γ (Discount Factor): Set between 0 and 1. Dictates how much future rewards are valued compared to immediate rewards (a value close to 0 makes the agent short-sighted, while a value close to 1 makes it long-term focused).

```math
\max_{a'} Q(s', a')
```
The maximum expected Q-value for the next state (s') across all possible future actions (a').

## Markov Decision Process
A Markov decision process (MDP) is a formal mathematical framework used to model sequential decision-making in environments where outcomes are partly random and partly under the control of a decision-maker. It serves as the foundational blueprint for reinforcement learning (RL).
Core Components
An MDP is formally defined as a tuple $(S, A, P, R, \gamma)$

• States (S): The set of all possible situations or configurations the agent can find itself in.

• Actions (A): The set of all possible choices or moves available to the agent in a given state.

• Transition Function (P): The rules of the environment defining the probability \(P(s' \mid s, a)\) of moving to a new state s' after taking action a in state s.

• Reward Function (R): The immediate numerical feedback R(s, a, s') received after transitioning between states.

• Discount Factor (γ): A value between 0 and 1 that determines the present value of future rewards versus immediate gratification.