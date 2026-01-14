---
title: "Blog"
layout: single
permalink: /blog/
---

Welcome to the blog. Posts here cover updates, notes, and reflections. Use the filters to jump to what you need.

<div class="filter-chip-bar" id="blog-filter">
  <button class="filter-chip is-active" data-filter="all">All</button>
  <button class="filter-chip" data-filter="thinking-aloud">Thinking Aloud</button>
  <button class="filter-chip" data-filter="research">Research</button>
  <button class="filter-chip" data-filter="tech">Tech</button>
  <button class="filter-chip" data-filter="life">Life</button>
</div>

{% capture blog_cards %}
  {% for post in site.posts %}
    {% if post.categories contains "blog" or post.categories contains "thinking-aloud" %}
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
    {% endif %}
  {% endfor %}
{% endcapture %}

{% if blog_cards | strip != "" %}
<div class="post-card-grid" id="blog-posts">
  {{ blog_cards }}
</div>
{% else %}
<p class="notice">No blog posts yet. Add new posts under <code>_posts</code> with a <code>blog</code> or <code>thinking-aloud</code> category to have them appear here.</p>
{% endif %}

<script>
  (function () {
    const container = document.getElementById('blog-posts');
    const filterBar = document.getElementById('blog-filter');
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
