---
layout: default
title: Home
comments: true
---
## Automated discovery of interpretable gravitational-wave population models

**Kaze W.K Wong** (Flatiron Institute), **Miles Cranmer** (Princeton University); (*equal contribution*)


We present an automatic approach to discover analytic population models for gravitational-wave (GW) events from data.
As more gravitational-wave (GW) events are detected, flexible models such as Gaussian Mixture Models have become more important in fitting the distribution of GW properties due to their expressivity.
However, flexible models come with many parameters that lack physical motivation, making interpreting the implication of these models challenging.
In this work, we demonstrate symbolic regression can complement flexible models by distilling the posterior predictive distribution of such flexible models into interpretable analytic expressions.
We recover common GW population models such as a power-law-plus-Gaussian, and find a new empirical population model which combines accuracy and simplicity.
This demonstrates a strategy to automatically discover interpretable population models in the ever-growing GW catalog, which can potentially be applied to other astrophysical phenomena.

{% include videos.html %}

<!-- <iframe src="/SymbolicGWPopulation_paper/public/video/FitMassFunction.mp4" frameborder="0" allowfullscreen></iframe> -->


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