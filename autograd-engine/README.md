# Autograd Engine

An autograd engine is a small system for automatic differentiation: it records operations in a computational graph and backpropagates gradients without writing the derivative formulas by hand.

## Good sources to look up
- Andrej Karpathy's micrograd implementation and blog notes
- PyTorch autograd documentation
- JAX autodiff documentation
- Theoretical material on automatic differentiation and computational graphs

## Handy math concepts
- Calculus: derivatives and chain rule
- Multivariate differentiation
- Computational graphs
- Forward mode vs reverse mode autodiff
- Linear algebra for tensor operations and matrix shapes
- Gradient descent and optimization basics

## Typical things to practice
- Implementing scalar values with a gradient field
- Backpropagation through simple neural nets
- Handling broadcasting and shape rules
- Checking gradients numerically with finite differences
- Understanding why reverse-mode autodiff is efficient for deep networks
