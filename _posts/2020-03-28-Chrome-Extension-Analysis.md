---
layout: default
title: Chrome Extension Analysis
categories: [Malware Research, Browser Hijackers]
tags: [Python, Browser Extensions]
comments: false
---
Chrome extensions have over 1.2 billion installs. Not many people have actually reviewed the authenticity and risk associated with the chrome extensions they use.  This blog post describes some of the tools and techniques that can be used to review chrome extensions for signs of possible malicious activity or user privacy data abuse.

# Static Analysis

Reading the JavaScript used by a chrome extension will often provide the best insight but code obfuscation may make this challenging. Fortunately there are methods for reviewing chrome extension without JavaScript knowledge!

## ExtAnalysis

My go-to tool for reviewing chrome extensions is the Browser Extension Analysis Framework ([ExtAnalysis](https://github.com/Tuhinshubhra/ExtAnalysis)). This open source framework is written in Python 3 and runs as a local web application. I use ExtAnalysis to perform static analysis of extensions and get a better understanding of their functionality.

![extanalysis info](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/ext_info.png)

ExtAnalysis has a lot of useful features such as automatically parsing extension permissions and extracting  information such as urls and domains.

![extanalysis permissions](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/ext_perms.png)

Using Neo4j, ExtAnalysis plots the extensions files and communications in an interactive graph. This feature is good for getting a high-level understanding of the extensions structure. ExtAnalysis has an embedded file viewer with functionality to "beautify" (re-structure/organize) files.

![extanalysis files](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/extanalysis_files.png)   

The "URLs and Domains" tab provides information on network connections that an extension may be making and has integration with VirusTotal and WHOIS records! (Perhaps integration with urlscan.io will be in a future pull request)

![extanalysis domains](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/ext_domains.png)   

The general methodology I use to review extensions with ExtAnalysis is:

> 1) Start analysis on an extensions by submitting the extensions chrome webstore url or ID
>
> 2) Look at the structure of extension files in the file viewer graph
>
> 3) Review the permissions
>
> 4) Review extracted urls and domains
>
> 5) Review javascript used by the extensions
(The section "EXTRACTED URLS FROM FILES" in a ExtAnalysis report can help with finding the right javascript file)

## crxcavator.io

Suppose you don't want to run ExtAnalysis or only have a browser to work with, no worries - there are other tools you can use!  

[crxcavator](crxcavator.io) is an online application owned by DuoSec that can be used to review chrome extensions. Similarly to ExtAnalysis, crxcavator allows users to submit an extension for review and will parse permissions among other things.

My favorite features of crxcavator are the "entry points" and "dangerous functions". These sections will include code segments of risky chrome API calls in use or possible malicious javascript.

![crx entry](https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/crx_entry.png)   


# Dynamic Analysis

Reviewing the source code of an extension can help provide a good understanding of overall functionality but dynamic analysis may be the key in taking your analysis to the next level.

## Chrome Developer Tools

After installing a chrome extension, the chrome developer tools can be leveraged to view whats going on  "behind the scenes". The steps for accessing the runtime environment of an installed chrome extension is:

> 1) Visit `chrome://extensions`
>
> 2) Enable Developer Mode (top right of page)
>
> 3) Click on "Inspect views background page" of the extension you're interested in.
>
> 4) Navigate to the "Network" section of the chrome developer tools
>
> 5) Enable "Preserve Log"

This will record the network request being made by the extension in analysis.

The "Sources" section of the chrome developer tools will show some of the extensions files in use. The chrome developer console can be used to interact with the JavaScript environment of the extension.

## Python and Chrome Webdriver

Using Python, specifically selenium chrome webdriver, you can run extensions in a new instance of chrome with a network proxy intercepting browser traffic.

This can be done in python as followed:

```
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('load-extension=/path/to/extension));
options.add_argument('--proxy-server=127.0.0.1:8080')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.get("chrome://extensions/")
```

So far we've gone over a couple different tools and tricks for taking a look at chrome extensions.

**In a future blog post, I will write more about automating dynamic analysis with python and mitmproxy.**

But in the meantime, feel free to reach out on twitter if you want to discuss further!
