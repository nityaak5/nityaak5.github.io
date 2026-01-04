---
title: "Thinking Aloud"
layout: single
permalink: /thinking-aloud/
---

Ideas in progress and exploratory notes live here. Filter by category to skim the threads that interest you.

<div class="filter-chip-bar" id="thinking-filter">
  <button class="filter-chip is-active" data-filter="all">All</button>
  <button class="filter-chip" data-filter="research">Research</button>
  <button class="filter-chip" data-filter="tech">Tech</button>
  <button class="filter-chip" data-filter="life">Life</button>
</div>

{% assign thinking_posts = site.posts | where_exp: "post", "post.categories contains 'thinking-aloud'" %}

{% if thinking_posts.size > 0 %}
<div class="post-card-grid" id="thinking-posts">
  {% for post in thinking_posts %}
  {% assign downcase_categories = post.categories | join: ' ' | downcase %}
  <article class="post-card" data-categories="{{ downcase_categories }}">
    <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
    <p class="post-card-meta">{{ post.date | date: "%B %d, %Y" }}</p>
    {% if post.excerpt %}
    <p>{{ post.excerpt | strip_html | truncate: 180 }}</p>
    {% endif %}
    {% if post.categories %}
    <p class="post-card-tags">Categories: {{ post.categories | join: ", " }}</p>
    {% endif %}
  </article>
  {% endfor %}
</div>
{% else %}
<p class="notice">No Thinking Aloud entries yet. Add posts categorized with <code>thinking-aloud</code> to show them here.</p>
{% endif %}

<script>
  (function () {
    const container = document.getElementById('thinking-posts');
    const filterBar = document.getElementById('thinking-filter');
    if (!container || !filterBar) return;

    const cards = Array.from(container.querySelectorAll('.post-card'));
    const buttons = Array.from(filterBar.querySelectorAll('[data-filter]'));

    const setActive = (value) => {
      buttons.forEach((btn) => btn.classList.toggle('is-active', btn.dataset.filter === value));
    };

    const applyFilter = (value) => {
      cards.forEach((card) => {
        const categories = (card.dataset.categories || '').split(/\s+/).filter(Boolean);
        const matches = value === 'all' || categories.includes(value);
        card.style.display = matches ? '' : 'none';
      });
      setActive(value);
    };

    buttons.forEach((button) =>
      button.addEventListener('click', () => applyFilter(button.dataset.filter))
    );

    applyFilter('all');
  })();
</script>
