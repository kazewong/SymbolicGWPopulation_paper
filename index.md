---
layout: default
title: Home
comments: true
---

![Article status](https://github.com/kazewong/SymbolicGWPopulation_paper/actions/workflows/build.yml/badge.svg) ![Article tarball](https://img.shields.io/badge/article-tarball-blue.svg?style=flat) ![Read the article](https://img.shields.io/badge/article-pdf-blue.svg?style=flat)

## Automated discovery of interpretable gravitational-wave population models

**Kaze W.K Wong** (Flatiron Institute), **Miles Cranmer** (Princeton University); (*equal contribution*)


We present an automatic approach to discover analytic population models for gravitational-wave (GW) events from data.
As more gravitational-wave (GW) events are detected, flexible models such as Gaussian Mixture Models have become more important in fitting the distribution of GW properties due to their expressivity.
However, flexible models come with many parameters that lack physical motivation, making interpreting the implication of these models challenging.
In this work, we demonstrate symbolic regression can complement flexible models by distilling the posterior predictive distribution of such flexible models into interpretable analytic expressions.
We recover common GW population models such as a power-law-plus-Gaussian, and find a new empirical population model which combines accuracy and simplicity.
This demonstrates a strategy to automatically discover interpretable population models in the ever-growing GW catalog, which can potentially be applied to other astrophysical phenomena.

<div id="start">
    <video controls>
        <source src="/SymbolicGWPopulation_paper/public/asset/FitMassFunction.mp4" type="video/mp4">
    </video>
</div>

{% if page.comments %}
<div id="disqus_thread"></div>
<script>
    (function() { // DON'T EDIT BELOW THIS LINE
    var d = document, s = d.createElement('script');
    s.src = 'https://symbolic-gw-paper.disqus.com/embed.js';
    s.setAttribute('data-timestamp', +new Date());
    (d.head || d.body).appendChild(s);
    })();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
{% endif %}