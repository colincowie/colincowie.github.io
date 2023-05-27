---
layout: default
title: Tweetdeck for Threat Intel
categories: [Threat Intelligence, Resources & Guides]
tags: [CTI, Malware, Social Media]
comments: false
---
<meta name="twitter:image" content="https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/tweetdeck/tweetdeck_cover.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:description" content="Setting up Tweetdeck for threat intelligence and information security.">

Twitter is undeniably a great resource for learning about security. A lot of people share information on malware, phishing, new vulnerabilities, exploits and more. Sometimes it can be difficult to filter out the non-security social media content. This blog post walks through setting up Tweetdeck for threat intelligence so that you can stay informed without giving up your Twitter memes!

# Tweetdeck
[Tweetdeck](https://tweetdeck.twitter.com/) is a dashboard application for management of Twitter accounts. It was originally an independent app and was acquired by Twitter in 2011. Tweetdeck is composed of columns that you can customize to show different content.

![tweetdeck](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/tweetdeck/tweetdeck.png)

There are a few different types of columns you can create with the "Add column" button. The search feature is what I use for a threat intelligence focused setup.

![columns](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/tweetdeck/column.png)

# Search Filters
Searching can be used to find text or hashtags and has 3 search modifies, AND/OR/NOT. More information the search filter syntax can be found in the [Twitter Documentation](https://help.twitter.com/en/using-twitter/twitter-advanced-search). Below are the search filters I use with Tweetdeck:

### Malware and Phishing

"Open directories" are listing of files on a web server. Sometimes directories are intentionally left open but mostly are an outcome of laziness. Threat actors sometimes leave directories open with malware or phishing kits hosted. `#opendir` is a gold mine of good intel on twitter.

![opendir](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/tweetdeck/opendir.png)

Phishing sites shared on urlscan.io:
```
urlscan.io AND phishing
```

Phishing Kits:
```
#PhishingKit
```

Online malware & sandboxes:
```
virustotal.com OR app.any.run OR hybrid-analysis
```

Indicators of Compromise:
```
malware AND IOC
```

### Vulnerabilities and Exploits

Common vulnerabilities and exposures (cve) and proof of concept (poc):
```
"cve-" AND poc
```

Open source exploits:
```
exploit AND (gitlab.com OR github.com)
```

### Other Good Queries
```
#bugbountytip OR #bugbountytips
```


Hopefully this post has shown how powerful tweetdeck can be with the right searches! Have any cool/useful tweetdeck search queries? Let me know on twitter! - @th3_protoCOL
