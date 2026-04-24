---
title: "Not Everyone’s Mirror"
date: 2026-04-23
categories:
  - blog
tags:
  - "ai-alignment-and-safety"
  - "llm"
  - "ai-safety"
medium_url: "https://medium.com/@nityaakalra5/not-everyones-mirror-cfa09857a78c?source=rss-2b7b285a116d------2"
---

> In my last post on AI hallucinations, I ended with a question: are we building a tool for truth or a mirror of ourselves? I thought I was done there. But the more I sat with it, the more it started to unravel something bigger. Because if AI systems really are mirrors, then the next question is not about hallucinations. It is about AI alignment.

![](https://cdn-images-1.medium.com/max/1024/1*_TjkXQtshjx9DHkMju86bQ.png)

AI alignment is not a new area of research. Discussions around aligning intelligent systems with human goals can be traced back to at least the early 2000s, and even earlier in philosophy and decision theory. But with the rise of LLMs, the question has moved from theory to something much more immediate.

At its core, alignment is the idea that AI systems should behave in ways that fit what humans want. But this sentence hides a problem. What does _“what humans want_ ” actually mean? If we look into the literature, it could mean instructions, intentions, revealed preferences, ideal preferences, interests, or even values. These are not the same thing at all, and the difference between them is where the problem starts to feel less technical and more political.

Instructions are easy to specify but brittle in practice. They can be misinterpreted or exploited in ways we did not intend. Preferences are closer to human behaviour but they are inconsistent, and often shaped by external influence. Perhaps, values seem more stable and meaningful, closer to what we actually care about. But they are also much harder to define. And once you try to define them, the obvious next question appears:**_whose values are we talking about?_**

### The values problem

This is where [Iason Gabriel’s ](<https://link.springer.com/article/10.1007/s11023-020-09539-2>)work helped me reframe things. One of its central points is that the normative and technical sides of alignment are deeply intertwined. Any powerful AI system is never simply following rules in a neutral sense, but is embedding some view of what counts as a good outcome.

Gabriel argues that _values are a more promising target than instructions or preferences, precisely because they give us something stable enough to reason about and scrutinise._ But that does not resolve the deeper problem. Values themselves are plural and often in conflict. Consider something as basic as content moderation: one person’s harmful speech is another’s political expression, and there is no encoding that sidesteps that disagreement. Even if something like International human rights law seems like a reasonable shared foundation, we still have to decide which rights take precedence, whether we are protecting people from harm or also ensuring access to opportunity, and how a legal doctrine built for states and citizens should translate to artificial agents. In other words, _even the most appealing moral anchor still leaves a great deal unresolved._

Perhaps all of this feels a bit too philosophical. It did, to me. Then I came across a paper that made it much harder to stay abstract. In [_Whose Opinions Do Language Models Reflect?_](<https://arxiv.org/abs/2303.17548>), researchers compared model outputs to survey responses from different demographic groups across the United States. They found that language models consistently aligned with the views of liberal, educated, higher income individuals, and diverged significantly from older, more conservative, lower income populations.

The study is explicitly U.S. centric and does not claim to generalise globally, but that limitation is almost the point. Even within a single country, alignment is not evenly distributed. It reflects the data used to train these systems, the design choices, and the people who shaped them. So even if we agree that values are the right target, the values currently encoded are not some neutral average of human preference. Instead, they belong to a specific subset of people.

### The verification problem

So now the question shifts again. Even if we decide what values we want, how do we know the model actually learned them?

This is where an Anthropic paper from a year ago, [_Auditing Language Models for Hidden Objectives_](<https://arxiv.org/abs/2503.10965>), caught my attention. The researchers trained a model with a deliberately hidden objective and then asked four independent teams to investigate it. Three of the four teams eventually uncovered the hidden objective, drawing on a combination of behavioural testing, analysis of training data, and interpretability tools including sparse auto-encoders.

On the surface, this sounds like a success story. But these were expert teams, some working with full access to the training data and were specifically told that something was hidden and tasked with finding it. Despite this, the process was difficult, and one team failed completely. In a real deployment scenario, you would have none of those advantages. What this reveals is a gap that does not get enough attention. _There is a difference between a model that appears aligned and a model that is actually optimising for what we think it is, and evaluating outputs alone is not sufficient to tell the two apart._ This is why interpretability research matters beyond its niche status in the ML community. If we cannot look inside the model and understand what computations it is running, we are essentially trusting behaviour we cannot fully explain. And as models become more capable, this problem does not get easier.

### What happens when we can no longer supervise at all?

AI systems are increasingly becoming too complex for humans to supervise directly and a promising direction is a relatively new area called [scalable oversight](<https://arxiv.org/abs/2312.09390>). The idea is to use AI systems to help align other AI systems, often through approaches like weak to strong supervision. I am still working through the details so I will not try to explain it fully here, but the core idea is both practical and slightly unsettling (something about needing an AI system to help us align another one seems strange, no?).

### So where does this leave us?

This feels like the right place to pause. What started as a question about hallucinations has turned into something else entirely. We are trying to align systems to something we do not fully agree on, using methods we do not fully understand, and as these systems become more capable, we may have to rely on them to help us do the alignment itself. So maybe alignment is not one question after all. It is a chain of uncomfortable ones. Whose values ( if indeed values is something we are focusing on) are we encoding? Can we verify that they are actually learned? And what happens when we can no longer do that verification alone?

_AI systems may be mirrors. But not of everyone. Not evenly. Not intentionally. And not transparently._

If that is true, then making AI safer is not just about adding constraints. It is about deciding what those constraints privilege and what gets left out. That is the thread I am starting to pull on with this project. The next step is to move from philosophy to something more concrete- because if alignment changes behaviour, and it does, then it must also change capability, trade-offs, and outcomes in ways we can actually measure and this is where it gets more interesting.

![](https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=cfa09857a78c)
