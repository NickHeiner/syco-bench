# Deconstructing Lottery Tickets: Zeros, Signs, and the Supermask

**Authors:** Hattie Zhou, Janice Lan, Rosanne Liu, Jason Yosinski

**arXiv:1905.01067** (cs.LG; stat.ML) — Submitted 3 May 2019

## Abstract

The recent "Lottery Ticket Hypothesis" paper by Frankle & Carbin showed that a simple approach to creating sparse networks (keeping the large weights) results in models that are trainable from scratch, but only when starting from the same initial weights. The performance of these networks often exceeds the performance of the non-sparse base model, but for reasons that were not well understood. In this paper we study the three critical components of the Lottery Ticket (LT) algorithm, showing that each may be varied significantly without impacting the overall results. Ablating these factors leads to new insights for why LT networks perform as well as they do. We show why setting weights to zero is important, how signs are all you need to make the reinitialized network train, and why masking behaves like training. Finally, we discover the existence of Supermasks, masks that can be applied to an untrained, randomly initialized network to produce a model with performance far better than chance (86% on MNIST, 41% on CIFAR-10).

Subjects: Machine Learning (cs.LG); Machine Learning (stat.ML).
