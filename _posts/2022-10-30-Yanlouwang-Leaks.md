---
layout: default
title: Yanlouwang Ransomware Leaks
categories: [Threat Intelligence, Ransomware]
tags: [Malware, CTI, Yanlouwang, Ransomware]
comments: false
---

# Yanlouwang Ransomware Leaks Analysis

On October 31st the twitter account [@yanluowangleaks](https://twitter.com/yanluowangleaks) published communication data from Yanlouwang ransomware. The data appear to be leaked from matrix chat servers.

## Overview of Leaked Data

### Leaked Data File Names
- hello1.json
- hello2.json
- hello3.json
- hello4.json
- coder-saint.json
- stealer-felix.json

### All unique matrix usernames:

```
'@killanas', '@saint', '@stealer', '@djonny', '@calls', '@felix', '@win32', '@nets', '@seeyousoon', '@shoker', '@coder', '@ddos', '@gykko', '@loader1', '@guki', '@shiwa', '@zztop', '@al', '@coder0'
```

### Message Sender Frequency

- 1031 @saint
- 762 @killanas
- 338 @guki
- 293 @felix
- 159 @stealer
- 64 @djonny
- 27 @coder
- 20 @calls
- 2 @coder0
- 6 @ddos
- 19 @win32
- 15 @loader1
- 13 @zztop
- 3 @nets
- 2 @shiwa
- 1 @shoker
- 1 @al

## Interesting Chats

**Reaction to REvil FSB Arrest**

The username *saint* shared a link to an article in Russian: [Daily Storm publishes profiles of suspects in the case of the REvil group](https://dailystorm.ru/rassledovaniya/blesk-i-nishcheta-koroley-hakerskogo-mira-daily-storm-publikuet-profayly-podozrevaemyh-po-delu-gruppirovki-revil)
> "the five people involved are former classmates"

> "Пятеро фигурантов — бывшие одноклассники"

\- *Tue 1 February 2022*

## Timestamp HeatMap Analysis

I leveraged python and plotly to generate timestamp heat maps for the 5 most frequent usernames observed in the leaked data. More information about the methodology used can be found in my article:
- [HeatMap Visualization with Python](https://th3protocol.com/2022/HeatMap-Viz)

{% include plotly/all.html%}
{% include plotly/saint.html%}
{% include plotly/killanas.html%}
{% include plotly/guki.html%}
{% include plotly/felix.html%}
{% include plotly/stealer.html%}
