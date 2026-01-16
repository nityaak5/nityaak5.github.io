---
title: "Reading NeurIPS 2025- Nested Learning: The Illusion of Deep Learning Architecture"
date: 2026-01-12
categories:
  - thinking-aloud
  - research
tags:
  - nested learning
  - deep learning
  
---

In NeurIPS 2025, Google Research introduced [Nested Learning: The Illusion of Deep Learning Architecture](https://abehrouz.github.io/files/NL.pdf). At first glance, it is quite dense. The kind of paper where you know you won’t absorb everything in one sitting, but the title alone makes you curious enough to try.
The title immediately caught my attention. The illusion of deep learning architecture is a strong claim. Why do they call it an illusion? Have we been thinking about deep learning systems the wrong way all this time? Well, not exactly wrong, but according to the paper, maybe incomplete.

The paper starts from a familiar problem: catastrophic forgetting. In simple terms, catastrophic forgetting is when a model learns something new and, in the process, forgets what it learned before. This becomes painful in settings like continual learning, long-context reasoning or multi-task learning, where we want models to accumulate knowledge over time instead of constantly overwriting it. The paper argues that simply designing bigger or fancier architectures may not be enough to solve this. More layers, more parameters, and better attention mechanisms do not automatically give us better long-term learning. Instead, they suggest we need to rethink what a learning system actually is, and this is where Nested Learning comes in.

### What is Nested Learning?

Now, this is not a new architecture in the usual sense. Instead, it is a new way of looking at learning systems. Traditionally, we think of the neural network as the learner and the optimizer as a tool that updates its weights. The model learns and the optimizer just does math. But the paper argues that this separation is artificial.

A real learning system is not just a neural network. It is the entire pipeline: the model, the optimizer, the memory mechanisms, the update rules, the training process, and even what happens at inference time. In other words, learning is happening at multiple levels at once. Some learning happens slowly, like weight updates during training that shape long-term representations. Some learning happens very fast, like in-context learning when a language model adapts its behaviour based on the prompt. And some learning is implicit, like when optimizers such as Adam store statistics about past gradients and use that information to change future updates.

This is one of the central ideas of the paper: that optimizers are not just update rules, but learners too. So instead of seeing a deep learning model as a single learner, the paper suggests we should see it as a hierarchy of learners nested inside one another, each operating at a different time scale. A deep learning system is not just a model that learns; it is a system that learns how to learn. This perspective also connects naturally to ideas from associative memory systems (the paper discusses it in detail), where memory is not just a passive store of information but an active component that participates in reasoning and learning. Memory becomes part of the learning loop rather than something bolted on afterwards.

At this point in the paper, I found myself wondering:

### Does Nested Learning actually solve catastrophic forgetting?

The honest answer is no, and the authors are very clear about this. They do not claim to have solved continual learning. Instead, they present Nested Learning as a shift in perspective. The real contribution is not a breakthrough result, but a reframing of how we think about learning systems. The suggestion is that progress in continual learning may come less from inventing new architectures and more from explicitly modeling learning itself as a hierarchy of nested processes operating across multiple time scales. That is both refreshing and in a way, slightly underwhelming. Refreshing because it feels honest. Underwhelming because we all secretly want a clean solution, right?

That said, the paper does not stay purely theoretical. The authors introduce an architecture called Hope (loved the name haha), built on top of a model called Titans. Titans is a long-context architecture designed to handle extremely long sequences using explicit memory modules. Instead of relying purely on attention, it introduces persistent memory components that can store and retrieve information over long horizons. You can think of it as giving the model an external memory it can read from and write to.

Hope takes this one step further. While Titans focuses on memory, Hope focuses on learning from that memory over time. It introduces nested learners: fast learners for short-term adaptation and slow learners for long-term knowledge. In other words, Titans gives the system memory, and Hope turns that memory into something the model can actively learn from.
In their experiments, they show modest but encouraging improvements on long-context reasoning and memory-intensive tasks. The results are not dramatic, but they suggest that making this nested learning structure explicit does help, at least a little.

While reading, I kept thinking:
### How is this different from Meta-Learning? Isn’t this also just learning to learn?

A helpful way I started thinking about it is through a human analogy. Meta-learning is like explicitly teaching someone how to study. You give them strategies and shortcuts so they can adapt faster to new subjects. Nested Learning is about recognising that learning is already happening at many levels at once. You slowly build long-term knowledge. You adapt quickly during a conversation. You subconsciously change habits over time. You accumulate intuition without realizing it. So the difference is not whether the system learns to learn. It is where and when learning is assumed to happen.

What I personally liked most about this paper is that it pushes us to stop treating training and inference as two completely separate worlds. In practice, modern models already blur this line. In-context learning is a form of fast adaptation. Memory-augmented models blur the boundary between parameters and data. Optimizers accumulate history. But we rarely talk about these pieces as parts of a single learning system. Nested Learning gives a language to talk about all of this in a unified way. While I skipped many of the technical details on my first read, but even at a high level, the paper made me rethink how I mentally picture a deep learning system.

If nothing else, the paper succeeds in doing what research should do: it makes you question assumptions you didn’t even realize you had. Maybe that is the real contribution here. Not a new architecture. Not a new benchmark. But a new way of seeing what deep learning systems already are.


Good to checkout: [Paper video explanation](https://youtu.be/uX12aCdni9Q?si=GIepX0uq4xG5rynN)

