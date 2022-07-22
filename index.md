---
layout: default
title: Home
comments: true
---
## Automated discovery of interpretable gravitational-wave population models
**Kaze W.K Wong** (Flatiron Institute), **Miles Cranmer** (Princeton University); (*equal contribution*)

<img src="{{site.baseurl}}/public/image/Figure1.PNG">


## TL;DR
1. There will be more and more gravitational wave (GW) events in the coming decade.
2. To study the GW population, people usually write down simple phenomenological models. 
3. But that's hard to do when you data is getting more complex, so people turn to flexible models like Gaussian Mixture Model. The problem is, these models are not interpretable.
4. Symbolic regression can help distilling interpretable models from the flexible models
5. We apply this to gravitational wave data, but this can be applied to other problems as well!

## Main poster (~2 minutes read)

{% include videos.html %}

## Take home messages

Flexible models are very popular in data analysis due to their capability to fit complex dataset.
However, they are often difficult to interpret due to their large number of parameters in some non-intuitive basis.
SR can be a tool to distill more interpretable out of these flexible models.
Perhaps the coolest part of this work is the result you get out of the pipeline is **a collection of models**, which means you can use these models in typical data analysis tasks such as parameter estimation or model selection (And print it in your paper).
One can surely take the equations fitted by SR and try to make scientific conclusion with them.
But in case the referee ask "What about this robustness check?", just plug it in a traditional data analysis pipeline, and all follows.
After all, what's the difference between a carbon-based ConvNet who look at data and propose equations and a silicon-based one?

## A couple more things

### Showyourwork

<a href="https://github.com/showyourwork/showyourwork">
<img src="https://raw.githubusercontent.com/showyourwork/.github/main/images/showyourwork.png" alt="showyourwork"/>
</a>

Our paper is prepared using the package [showyourwork](https://github.com/showyourwork/showyourwork), which is a workflow management tool for **reproducible**, **extensible**, **transparent**, and **just downright awesome** open source scientific articles (in their own wording). You can find the source code of our latex file, data file and script which generate the figures in this [github repository](https://github.com/kazewong/SymbolicGWPopulation_paper). We welcome comments in the form of github issue. If you think reproducibility and openness are important to scientific publication, give showyourwork a try!

### Manim animation

<a href="https://github.com/ManimCommunity/manim">
<img src="https://raw.githubusercontent.com/ManimCommunity/manim/main/logo/cropped.png">
</a>

The animation in this poster is made using an animation engine for explanatory math videos in python, which is originally developed by Grant Sanderson for his YouTube channel [3Blue1Brown](https://www.youtube.com/c/3blue1brown), then subsequently being developed by the manim community. We use the [community version](https://github.com/ManimCommunity/manim) for the videos in this poster. If you are interested in start making explanatory video in this style, checkout the engine! Also, the source code for creating the animations in this poster can be found in [this repo](https://github.com/kazewong/ManimAnimation/tree/master/SRexplain).

### The authors


<img src="{{site.baseurl}}/public/image/Kaze.jpg"/> 

<img src="{{site.baseurl}}/public/image/Miles.jpeg"/> 


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