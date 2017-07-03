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

In my life I had so many hobbies that it would be hard to count them. Skateboarding was definitely the one which I remember the most and it is still my favourite sport. It has fascinated me so much that I wrote my Bachelors Thesis about it. In this thesis, I did a computer simulation of a skater landing on a skateboard. That was especially interesting for me as I could have done an experiment on a skateboard without physically destroying it. 

The disserartion was split into the three stages and the complexity of the model was increasing throughout them. In this blog, I will try to describe the process of model creation without getting into details. By details, I mean not providing any complicated equations, terms and all bunch of things which may scare a person who has no knowledge of simulations. 

Before I moved further, I have to admit that for purpose of this article, I recreated the models in Abaqus Student version. The software is available free of charge to students, educators, and researchers for personal and educational use - I believe the educational blog fits well to these requirements.

## Simple specimen experiment

Analysis of a skateboard is not an easy task due to its' complicated geometry and unusual material used to built the deck. Traditionally, manufacturers are using a composite material made from Canadian Maple layers, usually 7-9 plies. I decided to build a very simple plate model on computer to understand this composite behaviour. Luckily, at home I found an old skateboard from which I cut an analogue real sample. After that, I utilised it in a bending test performed in the professional laboratory built from a home gym set :-) .

{% capture imagesrc %}00_skate/testing_station.jpg{% endcapture %}
{% capture imagetitle %}Testing station{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

The main idea of the physical tests was to find a relation between deck deflection and a value of mass used to weight the deck. In more engineering terms, I was trying to look for a displacement under given loading. I performed the measurements using a ruler, so the obtained data were probably far from being accurate. However, the rough results were enough to judge if my numerical model could be acceptable.
Before I moved to model creation process, I had to find material properties which are crucial in Finite Element Analysis. At that stage, I found a very useful Wood Handbook which presents Canadian Maple material data (it can be found <a href="https://www.fpl.fs.fed.us/documnts/fplgtr/fpl_gtr190.pdf">here</a>). Using the data from this resource, I built a shell geometry in Abaqus and I applied the lamina material model to it. After that, I put appropriate restrains and loads to imitate the body behaviour from physical tests. The results from experiments are presented below.

{% capture imagesrc %}00_skate/Result_F_U.png{% endcapture %}
{% capture imagetitle %}Abaqus results{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

{% capture imagesrc %}00_skate/TestComparison.png{% endcapture %}
{% capture imagetitle %}Results comparison{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

The colourful plots do not show any non-physical behaviour which is a good sign. Also, looking at the force-displacement graph it can be seen that the numerical model results are not far from physical tests. It indicates that both lamina material model and the material properties can be assumed as correct for further investigations.
At this point, it is worth showing how easy is to get results for different material data. In case of physical tests, I would have to cut few different samples to use them in experiment. For the numerical simulation, it is only matter of changing few variables.

## Skateboard pressure test

Another stage was to perform skateboard pressure test simulation. It allowed to check the strength of the skateboard under the static loading. That is also a stage when real geometry was introduced. When writing thesis I found some data from physical experiments which seems not to be available anymore (<a href="link">link</a>). Fortunately, I saved a laboratory test photo and the original results (<a href="link">here</a>).  

{% capture imagesrc %}00_skate/LabTest_photo.jpg{% endcapture %}
{% capture imagetitle %}Testing station{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

<div style='position:relative;padding-bottom:57%'><iframe src='https://gfycat.com/ifr/WigglyHardtofindBlackpanther' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0;' allowfullscreen></iframe></div>

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

{% capture imagesrc %}00_skate/LaboratoryPlot.png{% endcapture %}
{% capture imagetitle %}Abaqus results{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

{% capture imagesrc %}00_skate/LaboratoryPlot_plasticity.png{% endcapture %}
{% capture imagetitle %}Results comparison{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

## 'Real' drop test
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

{% capture imagesrc %}00_skate/Skateboard.jpg{% endcapture %}
{% capture imagetitle %}Results comparison{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

<div style='position:relative;padding-bottom:56%'><iframe src='https://gfycat.com/ifr/MiserlyHatefulIndianrockpython' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0;' allowfullscreen></iframe></div>


