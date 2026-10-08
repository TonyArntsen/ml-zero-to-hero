# ==============================================================================
# TODO 1: DEFINE GENOME & NETWORK STRUCTURES
# ==============================================================================
# - TODO: Define a NodeGene data structure (ID, type: input/hidden/output, bias, activation function).
# - TODO: Define a ConnectionGene data structure (in_node, out_node, weight, enabled/disabled flag, innovation_number).
# - TODO: Define a Genome class holding a list/dict of NodeGenes and ConnectionGenes.
# - TODO: Implement a function to decode/build a feedforward (or recurrent) neural network from a Genome to perform inference.


# ==============================================================================
# TODO 2: TRACK GLOBAL INNOVATION NUMBERS
# ==============================================================================
# - TODO: Maintain a global innovation counter for connection tracking.
# - TODO: Create a lookup table (e.g., hash map of (in_node, out_node) -> innovation_number) to ensure identical structural mutations in the same generation receive the same innovation number.


# ==============================================================================
# TODO 3: IMPLEMENT GENOME MUTATION OPERATORS
# ==============================================================================
# - TODO: Implement weight mutation (randomly perturb existing weights or assign new random values).
# - TODO: Implement "add connection" mutation (select two unconnected nodes and link them with a new ConnectionGene with a new/cached innovation number).
# - TODO: Implement "add node" mutation (split an existing enabled connection by disabling it, inserting a new hidden node, and creating two new connection genes).
# - TODO: Implement toggle mutation (randomly enable/disable existing connections).


# ==============================================================================
# TODO 4: IMPLEMENT GENOMIC CROSSOVER (REPRODUCTION)
# ==============================================================================
# - TODO: Implement a crossover function taking two parent genomes and their respective fitness scores.
# - TODO: Align parent genes by matching innovation numbers.
# - TODO: Inherit matching genes randomly from either parent.
# - TODO: Inherit disjoint and excess genes exclusively from the fitter parent (or randomly/both if fitness is equal).


# ==============================================================================
# TODO 5: IMPLEMENT SPECIATION & DISTANCE METRICS
# ==============================================================================
# - TODO: Implement compatibility distance function: $d = \frac{c_1 E}{N} + \frac{c_2 D}{N} + c_3 \bar{W}$
#         (where E = excess genes, D = disjoint genes, W = average weight difference, N = genome size).
# - TODO: Maintain a list of active Species, each represented by a designated representative genome.
# - TODO: Assign each genome in the current population to an existing species if its distance is below threshold $\delta_t$, or create a new species if no match is found.


# ==============================================================================
# TODO 6: FITNESS EVALUATION & EXPLICIT FITNESS SHARING
# ==============================================================================
# - TODO: Evaluate raw fitness for each genome using your target environment/problem domain.
# - TODO: Calculate adjusted fitness for each genome to share fitness within species: $f_i' = \frac{f_i}{\text{species\_size}}$.
# - TODO: Calculate average adjusted fitness per species to determine the number of offspring each species is allowed to reproduce for the next generation.
# - TODO: Track species stagnation (generations without fitness improvement) and purge stagnant species.


# ==============================================================================
# TODO 7: EVOLUTIONARY RUN LOOP
# ==============================================================================
# - TODO: Initialize a population of minimal initial genomes (inputs connected directly to outputs).
# - TODO: Loop for N generations:
#     1. Decode genomes into networks and compute raw fitness.
#     2. Group population into species based on compatibility distance.
#     3. Compute adjusted fitness and offspring quotas for each species.
#     4. Remove low-performing genomes within each species.
#     5. Produce new generation via asexual reproduction (mutation only) and sexual reproduction (crossover + mutation).
#     6. Update species representatives and advance global generation counter.