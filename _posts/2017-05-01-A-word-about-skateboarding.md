---
layout: post
title: "A word about skateboarding"
categories: Daily Physics
tags: [FEA, simulation]
comments: true
categories: Personal
image:
  feature: skate.jpg
  teaser: skate-teaser.jpg
  credit:
  creditlink:
---

Skateboarding was one of my favourite sports when I was younger. It has changed my life so much that I even wrote a Bachelors Thesis about it. In this thesis, I tried to analyse what is happening with a skateboard deck when a skater lands on it. Looking back in time, I feel that picking this particular topic was a really good move. I was at the very beginning of the simulation learning curve and each tiny step towards my goal took ages. However, having practical experience in skateboarding helped me more than I would have imagined. First of all, I knew where the skateboard usually breaks so it was easier to understand the results. Secondly, I felt like I was contributing somehow to the development of skateboarding and that gave me a lot of satisfaction.

The simulation of skateboard is such a nice example of situation when hobby meets engineering that I decided to present it in my first blog. Unfortunately, I cannot use the model I built for Bachelors Thesis purposes as it was created in software that I currently don't have access to. I created new one in Abaqus Student version which is available free of charge to students, educators, and researchers for personal and educational use - I believe the educational blog fits well to these requirements.

# Rectangular specimen experiment
When I started to build the numerical model for thesis purposes, I knew that skateboard deck is a lamina made from Canadian Maple (usually 7-9 plies). The fact that it is a type of material I had not analyse before made my situation a bit problematic. For that reason, I decided to build a model of rectangular specimen at first to see how it behaves. Luckily, I found an old skateboard at home - that allows me to make an experiment on real piece of lamina. The photo was taken during the test performed in professional laboratory built from a home gym set :-) .

{% capture imagesrc %}testing_station.jpg{% endcapture %}
{% capture imagetitle %}Testing station{% endcapture %}
<a href="{{site.url}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

# Pressure test on skateboard
# 'Real' drop test
