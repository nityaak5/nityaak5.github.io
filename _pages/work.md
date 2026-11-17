---
title: "Projects + Research"
layout: single
permalink: /work/
---

Currently, I teach Technical AI Safety at SAIN and work on AI Safety evaluations. Publications and citations are on
<a href="https://scholar.google.com/citations?user=e7DfQkUAAAAJ&hl=en" target="_blank" rel="noopener">Google Scholar</a>.

<h2>Recent work</h2>
<div class="post-card-grid featured-grid">
  <article class="post-card is-featured">
    <span class="feature-tag">Ongoing · AI evaluation</span>
    <h3>Refusal Calibration: Does a Model Refuse What It Should, and Only That?</h3>
    <p>An end-to-end safety evaluation of four language models (GPT-5.6, Llama 3.1 8B, Ministral 8B, Qwen3.5 9B) on 450 XSTest prompts, run with Inspect and scored by an LLM judge. It measures both over-refusal and under-refusal.</p>
    <p>I then audited the judge itself by hand-labelling 100 responses. The audit overturned most of its under-refusal flags and changed my headline results. A good reminder that an evaluation is only as trustworthy as its scorer.</p>
    <p>
      <a href="https://github.com/nityaak5/LLM-evals/tree/main/projects/refusal-calibration" target="_blank" rel="noopener">GitHub</a> ·
      <a href="{% post_url 2026-09-19-evals-from-the-ground-up %}">Part 1: why evals</a> ·
      <a href="{% post_url 2026-10-07-evals-from-the-ground-up-part-2 %}">Part 2: building the eval</a> ·
      <a href="{% post_url 2026-10-24-evals-from-the-ground-up-part-3-judging-the-judge %}">Part 3: judging the judge</a>
    </p>
  </article>

  <article class="post-card is-featured">
    <span class="feature-tag">Completed · Published at NLP4PI @ EMNLP 2026</span>
    <h3>Where Do Predictions Go? Class-Level Shifts and Carbon Cost in Stance Detection</h3>
    <p class="post-card-meta">With Jisk J. Attema and Dimitar Shterionov · Tilburg University</p>
    <p>Stance detection is used to summarise public opinion, but aggregate scores like macro-F1 can hide how a model spreads its predictions across support, opposition and neutral. We compare language models and supervised baselines on three stance datasets with different definitions of neutrality, looking at accuracy, class-level behaviour and environmental impact.</p>
    <p>Language models don't consistently beat supervised baselines, some keep the same class-level biases across datasets and prompts, and gains saturate at around 4B to 8B parameters.</p>
    <p>
      <a href="https://aclanthology.org/2026.nlp4pi-1.43/" target="_blank" rel="noopener">Paper</a> ·
      <a href="https://aclanthology.org/2026.nlp4pi-1.43.pdf" target="_blank" rel="noopener">PDF</a> ·
      <a href="https://github.com/nityaak5/slm-topic-modeling" target="_blank" rel="noopener">Code</a>
    </p>
  </article>
</div>

<h2>Earlier research</h2>
<div class="post-card-grid">
  <article class="post-card">
    <h3>Master's Thesis: Thematic Bias in Book Recommender Systems</h3>
    <p class="post-card-meta">Radboud University · 2025</p>
    <p>Explored thematic bias in book recommender systems and its impact on users.</p>
    <p><a href="https://www.cs.ru.nl/masters-theses/2025/N_Kalra___Reading_Between_the_Lines%EA%9E%89_A_Study_of_Thematic_Bias_in_Book_Recommender_Systems.pdf" target="_blank" rel="noopener">Read the thesis</a> or read the shorter version <a href="https://arxiv.org/abs/2508.15643" target="_blank" rel="noopener">here</a>.</p>
  </article>

  <article class="post-card">
    <h3>OSAI Index</h3>
    <p class="post-card-meta">Open Source AI Index · 2025</p>
    <p>Contributed to a community-driven resource on model openness, licensing, and EU regulation for generative AI systems.</p>
    <p><a href="https://osai-index.eu" target="_blank" rel="noopener">Visit OSAI Index</a></p>
  </article>
</div>

<h2>Projects</h2>
<div class="post-card-grid">
  <article class="post-card">
    <h3>An AI Story Blueprint Generator</h3>
    <p class="post-card-meta">Jun 2025 - Present</p>
    <p>Built an end-to-end RAG pipeline that turns book metadata into creative story blueprints using Groq LLM and Qdrant.</p>
    <p>Deployed a modular Streamlit app with a responsive, accessible interface.</p>
    <p class="post-card-tags">Skills: RAG, vector databases, Python, NLP</p>
    <p>
      <a href="https://github.com/nityaak5/vibe-story-creator" target="_blank" rel="noopener">GitHub</a> ·
      <a href="https://vibe-story-creator.streamlit.app/" target="_blank" rel="noopener">Live demo</a>
    </p>
  </article>

  <article class="post-card">
    <h3>An Open-Source Conversational AI Agent</h3>
    <p class="post-card-meta">Sep 2024 - Dec 2024 </p>
    <p>Built a modular conversational AI pipeline with speech recognition, dialogue management, and text-to-speech using Rhasspy.</p>
    <p>Integrated APIs for external data and a T5 paraphrasing model to improve response fluency.</p>
    <p class="post-card-tags">Skills: Rhasspy, LLMs, speech recognition, text-to-speech, Python</p>
    <p><a href="https://github.com/Conversational-AI-graduate-course/Open-Source-Conversational-AI-group-project" target="_blank" rel="noopener">GitHub</a></p>
  </article>

  <article class="post-card">
    <h3>REFLECT: Self-Regulation and Mental Contrasting</h3>
    <p class="post-card-meta">Jan 2024 - Jun 2024 </p>
    <p>Built a mobile application to help students set goals, reflect weekly, and receive AI-driven feedback.</p>
    <p>Inspired by the Comenius project on self-regulated learning.</p>
    <p class="post-card-tags">Skills: JavaScript, React Native, usability testing, GPT-3</p>
    <p><a href="https://www.ru.nl/en/research/research-projects/reflect-for-self-regulated-learning" target="_blank" rel="noopener">Project reference</a></p>
  </article>

  <article class="post-card">
    <h3>Beyond Medical Records: Endometriosis Storytelling on Reddit</h3>
    <p class="post-card-meta">Sep 2023 - Jan 2024</p>
    <p>Analyzed Reddit discussions using emotion classification and topic modeling to surface themes of struggles, pain, and surgery.</p>
    <p>Validated themes with coherence analysis and compared results to existing research.</p>
    <p class="post-card-tags">Skills: NLP, deep learning, Python, LLMs</p>
    <p><a href="https://github.com/nityaak5/Endometriosis-Storytelling-on-Reddit" target="_blank" rel="noopener">GitHub</a></p>
  </article>
</div>
