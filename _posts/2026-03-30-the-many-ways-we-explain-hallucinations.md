---
title: "The Many Ways We Explain Hallucinations"
date: 2026-03-30
categories:
  - thinking-aloud
  - research
  - tech
tags:
  - hallucinations
  - ai
  - llm
---

<p>Original Medium post: <a href="https://medium.com/@nityaakalra5/the-many-ways-we-explain-hallucinations-810385835566" target="_blank" rel="noopener">The Many Ways We Explain Hallucinations</a>.</p>

<p>Last year, I started reading about hallucinations in LLMs. Every time I came across a new explanation, I would note it down. Not in a very structured way, just small fragments of how different people seemed to understand them. A few days ago, I went back to those notes and realised something interesting. The explanations were not actually competing with each other. Instead, they seemed to be describing the same phenomenon from different parts of the system.</p>

<h2>Evaluation shapes behaviour</h2>

<p>One of the first explanations I came across was in the paper <em>Why Language Models Hallucinate</em> (Kalai et al., 2025). The central argument is that hallucinations are not just random mistakes but are shaped by how we train and evaluate models. Most benchmarks are binary.</p>

<p>An answer is either correct or incorrect, and there is little to no reward for expressing uncertainty or saying “I don’t know.” In such a setup, a model that always attempts an answer, even when uncertain, can perform better than one that refuses to answer. The authors draw a parallel with competitive exams such as JEE or NEET, where students are often incentivised to guess rather than leave a question unanswered. In both cases, the system not only evaluates knowledge but also encourages risk-taking.</p>

<p>From this perspective, hallucinations begin to look less like accidents and more like a natural outcome of the incentives built into evaluation.</p>

<h2>Learning to sound confident</h2>

<p>Another perspective comes from how these models are trained. As Andrej Karpathy has pointed out in his talks, instruction-tuned models learn from large collections of human-written conversations. If human trainers consistently provide direct and confident answers, the model learns that pattern. This behaviour is further reinforced through methods like reinforcement learning from human feedback (RLHF), where responses that appear helpful and complete are preferred (Ouyang et al., 2022).</p>

<p>As a result, even when the model does not actually know something, it still knows what a “good” response is supposed to sound like and is likely to produce an answer that appears complete and confident.</p>

<p>In this sense, hallucination is not only about missing knowledge, but also about learned patterns of communication.</p>

<h2>Generation and the snowball effect</h2>

<p>A different but closely related explanation comes from the generation process itself. As discussed in <em>AI Engineering</em> by Chip Huyen, language models generate text one token at a time, conditioning each new token on everything that has already been produced. This includes both the original input and the model’s own previous outputs.</p>

<p>Because of this, the model builds on its own assumptions as it generates a response. It does not explicitly verify or ground its intermediate outputs, and instead treats them as part of the context for future predictions. Once an early part of the answer deviates slightly, the rest of the response continues under that assumption. The result is often text which is coherent and fluent, but not necessarily grounded in accurate information.</p>

<p>This compounding effect is sometimes referred to as the snowball effect.</p>

<h2>Intrinsic and extrinsic hallucinations</h2>

<p>The literature also distinguishes between intrinsic and extrinsic hallucinations. Intrinsic hallucinations arise when the model generates outputs that are inconsistent with the input or reasoning process, such as in tasks involving counting. Extrinsic hallucinations involve introducing information that is not grounded in the input or external sources. Approaches such as retrieval-augmented generation (RAG) aim to address extrinsic hallucinations by grounding responses in external data.</p>

<p>However, they do not fully eliminate intrinsic ones, since those are tied to how the model processes and generates information rather than what it has access to.</p>

<h2>Putting it all together</h2>

<p>Hallucinations mirror our own cognitive shortcuts. As humans, we often fill in gaps in memory to maintain a coherent story. We may overconfidently guess under pressure in situations like exams, and once we commit to a narrative in conversation, our reasoning can “snowball” as we build on earlier assumptions.</p>

<p>Similarly, evaluation methods, training procedures, and generation are not separate causes but interconnected parts of the same system. Models are trained to produce human-like responses, evaluated in ways that reward answering over abstaining, and generate outputs by predicting the most likely continuation of a sequence. Taken together, these factors create a system that prioritises fluency and plausibility, even in the absence of certainty.</p>

<p>Maybe the more useful question is not just why hallucinations occur, but what they reveal about the systems we value. As we continue to build, we have to decide: are we building a tool for truth, or a mirror of our own confident, creative, and sometimes beautifully flawed selves?</p>

<h2>References</h2>

<ul>
  <li>Kalai, A. T., Nachum, O., Vempala, S. S., &amp; Zhang, E. (2025). <em>Why Language Models Hallucinate</em></li>
  <li>Ouyang, L. et al. (2022). <em>Training language models to follow instructions with human feedback</em> (InstructGPT)</li>
  <li>Chip Huyen, <em>AI Engineering</em></li>
</ul>
