# brain
brain simulator

## Background
1. Nervous system consists of neuron.
1. Each neuron communicate by neurotransmitters at synapses.
1. Total number of neurons is fixed or decrease from the beginning of initial creation.
1. Number of synapses between two neurons is dynamically changed.

## Hypothesis
1. Type of neurotransmitter determines type of information to be sent.
1. All calculation in neuron are determined by amount, type, and threshold value of transmitters.
1. All calculation in neuron return approximated value and the calculation is a kind of Markov process.<br>
Each neuron is a Markov chain that affects an input of next chain.