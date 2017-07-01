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

## Rectangular specimen experiment

When I started to build the numerical model for thesis purposes, I knew that a skateboard deck is a lamina made from Canadian Maple (usually 7-9 plies). I was not in comfortable situation because I had not analysed that kind of material before. For that reason, I decided to build a very simple model which allowed me to understand a material behaviour. Luckily, I found at home an old skateboard - that gave me the opportunity to make physical tests on real piece of lamina. The photo was taken during the test performed in professional laboratory built from a home gym set :-) .

{% capture imagesrc %}00_skate/testing_station.jpg{% endcapture %}
{% capture imagetitle %}Testing station{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

The main idea of the physical tests was to find a relation between deck deflection and a value of mass used to weight the deck. In more engineering terms, I was trying to look for a displacement under given loading. I performed the measurements using a ruler, so the obtained data were probably far from being accurate. However, the rough results were enough to judge if my numerical model could be acceptable.
Before I moved to model creation process, I had to find material properties which are crucial in Finite Element Analysis. At that stage, I found a very useful Wood Handbook with Canadian Maple material data (it can be found <a href="https://www.fpl.fs.fed.us/documnts/fplgtr/fpl_gtr190.pdf">here</a>). Using the data from this resource, I built a shell geometry in Abaqus and I applied the lamina material model to it. After that, I put appropriate restrains and loads to imitate the body behaviour from physical tests. The results from experiments are presented below.

{% capture imagesrc %}00_skate/Result_F_U.png{% endcapture %}
{% capture imagetitle %}Abaqus results{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

{% capture imagesrc %}00_skate/TestComparison.png{% endcapture %}
{% capture imagetitle %}Results comparison{% endcapture %}
<a href="{{site.url}}{{site.baseurl}}/assets/images/{{ imagesrc }}">{% picture post_landscape {{ imagesrc }} alt="{{ imagetitle }}" title="{{ imagetitle }}" %}</a>
{: .center-image }

The colourful plots do not show any non-physical behaviour which is a good sign. Also, looking at the force-displacement graph it can be seen that the numerical model results are not far from physical tests. It indicates that both lamina material model and the material properties can be assumed as correct for further investigations.

## Pressure test on skateboard

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

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


