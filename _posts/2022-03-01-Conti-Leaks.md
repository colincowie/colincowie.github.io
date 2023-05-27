---
layout: default
title: Conti Ransomware Leaks
categories: [Threat Intelligence, Ransomware]
tags: [Malware, CTI, Conti, Ransomware]
comments: false
---
# The Conti Ransomware Leaks

## Background
On February 25th 2022 the Conti Ransomware crew declared they support the Russian government:
> “The Conti Team is official announcing a full support of Russian government,” the group said in a very aggressive message posted on Friday.  “If any body will decide to organize a cyberattack or any war activities against Russia, we are going to use our all possible resources to strike back at the critical infrastructures of an enemy.”

Later on the 25th @FellowSecurity and @vxunderground [shared](https://twitter.com/vxunderground/status/1497311023828807682) a screenshot of Conti ransomware groups private chatroom and all of their affiliates.
> "Little did they know some of their "friends" sided with Ukraine." - [@vxunderground](https://twitter.com/vxunderground/status/1497311023828807682)

 Two days later on Feburary 27th a Twitter user @ContiLeaks leaked private conti ransomware communications (Jabber chat logs). Over the course of 3 days additional conti data sets were leaked publicly by @ContiLeaks. A full timeline of the leaked data publishing was curated and [shared by @ex_raritas](https://twitter.com/ex_raritas/status/1498780626148728832)


Originally it was suspected that @ContiLeaks was operated by a pro- Ukrainian disgruntled ransomware affiliate.

As further data was leaked it became clear that @ContiLeaks had fully compromised Conti infrastructure and shared details of their root access. Given the extensive access obtained and data leaked, some people have theorized that a government intelligence agency is responsible for the leaks. The security company HoldSecurity reported that the leaks were from Ukrainian Security Researchers:


> "Conti's systems have been infiltrated by cybercrime researchers for some time. The data was dumped by a Ukrainian cyber security researcher pissed off after Conti expressed support for Russia in the conflict." - [@ransomwarefiles](https://twitter.com/ransomwarefiles/status/1498086108395360256)


This analysis aims to provide a centralized document with links to other resources and analysis.   

> "The #conti case will be studied for years to come. Such a diversion. And the criminal underground will fear forever the cyber ghost from Kyiv who took down Top 1 #Ransomware group in the world 🌎" - [@ddd1ms](https://twitter.com/ddd1ms/status/1498492556560289794)

## The raw data

Originally the leaked data was posted to the file sharing service anonfiles. Fortunately VX Underground took the effort to archive the data on their [website](https://share.vx-underground.org/Conti/).
- [Conti Chat Logs 2020.7z](https://share.vx-underground.org/Conti/Conti%20Chat%20Logs%202020.7z)
- [Conti Documentation Leak.7z](https://share.vx-underground.org/Conti/Conti%20Documentation%20Leak.7z)
- [Conti Internal Software Leak.7z](https://share.vx-underground.org/Conti/Conti%20Internal%20Software%20Leak.7z)
- [Conti Jabber Chat Logs 2021 - 2022.7z](https://share.vx-underground.org/Conti/Conti%20Jabber%20Chat%20Logs%202021%20-%202022.7z)
- [Conti Locker Leak.7z](https://share.vx-underground.org/Conti/Conti%20Locker%20Leak.7z)
- [Conti Pony Leak 2016.7z](https://share.vx-underground.org/Conti/Conti%20Pony%20Leak%202016.7z)
- [Conti Rocket Chat Leaks.7z](https://share.vx-underground.org/Conti/Conti%20Rocket%20Chat%20Leaks.7z)
- [Conti Screenshots December 2021.7z](https://share.vx-underground.org/Conti/Conti%20Screenshots%20December%202021.7z)
- [Conti Toolkit Leak.7z](https://share.vx-underground.org/Conti/Conti%20Toolkit%20Leak.7z)
- [Conti Trickbot Forum Leak.7z](https://share.vx-underground.org/Conti/Conti%20Trickbot%20Forum%20Leak.7z)
- [Conti Trickbot Leaks.7z](https://share.vx-underground.org/Conti%20Trickbot%20Leaks.7z)


## Public analysis and data enrichments
#### Data Enrichment
- [Translated conti leaked comms, shared by @Kostastsale](https://github.com/tsale/translated_conti_leaked_comms)

#### Analysis and Review
- [Twitter thread with interesting findings from @TheDFIRReport](https://twitter.com/TheDFIRReport/status/1498642505646149634)
- [Conti Ransomware taking orders from the FSB regarding Alexey Navalny (Shared by
Christo Grozev on twitter)](https://twitter.com/christogrozev/status/1498386621657493510)
- [MalwareBytes analysis with timeline and IOCs](https://blog.malwarebytes.com/threat-intelligence/2022/03/the-conti-ransomware-leaks/)
- [MAPPING THE CONTI NETWORK by @JGomes_EU](https://public.flourish.studio/visualisation/8851678/)
- [Twitter thread with interesting findings from @res260](https://twitter.com/res260/status/1498103308711518215)
- [TRM Analysis Corroborates Suspected Ties Between Conti and Ryuk Ransomware Groups and Wizard Spider](https://www.trmlabs.com/post/analysis-corroborates-suspected-ties-between-conti-and-ryuk-ransomware-groups-and-wizard-spider)
- [Conti Leaks: Examining the Panama Papers of Ransomware](https://www.trellix.com/en-us/about/newsroom/stories/threat-labs/conti-leaks-examining-the-panama-papers-of-ransomware.html)
- [Leaks Reveal Organizational Structure and Relationships](https://www..com/blog/gold-ulrick-leaks-reveal-organizational-structure-and-relationships)
- ['I can fight with a keyboard': How one Ukrainian IT specialist exposed a notorious Russian ransomware gang](https://www.cnn.com/2022/03/30/politics/ukraine-hack-russian-ransomware-gang/index.html)

## Timezone Analysis

Jabber Logs:

![Jabber Logs](https://github.com/colincowie/HeatMapViz/raw/master/heatmap_viz/example_data/images/example.PNG)

## Notable Quotes  

> 2022-02-23T11:51:30.228Z 2022-02-23-announcements.json rocco:
Happy Holidays, Cyber Troops! Let's bend the Amerians!

> 2021-04-16T21:33:34.025Z 2021-04-11-conti.json rozetka:
need a debag
sophos found who the option to bypass?


> "Hello world. Who can help with the lock of the net? Rights raised, data pumped out. Main domain (175serves online) + 2 trusts (~40 serv online). The problem is that everywhere there is a sophos with a password. You can't find a pass from sophos. Any changes in the settings of sofos are limited, the mount will not be able to lock, although there are cars without AV. You need someone who can cut/stop the sophos. Write in the PM who knows how to deal with sophos."


> 2021-01-20T11:21:01.685Z 2021-01-11-discussion.json VasyaPypkin:
no, there is better not to make noise, but to use something from native utilities, but psexec is clearly locked in sophos and the service itself is not a remote host just does not start
