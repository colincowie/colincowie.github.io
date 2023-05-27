---
layout: default
title: Minecraft & IT software targeted with fake websites & Remote Access Trojans
categories: [Malware Research, Loaders & Other Commodity Malware]
tags: [Malware, CTI, Malvertising]

comments: false
---
<meta name="twitter:image" content="https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/graphs/Targets.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title"  content="Minecraft & IT software targeted with fake websites & Remote Access Trojans">
<meta name="twitter:description" content="Malicious advertising -> Malware download -> Scheduled Task Creation -> Download of Remote Access Trojans & CryptoMiners">

# Minecraft & IT software targeted with fake websites & Remote Access Trojans

## Background research
In January of 2022 Félix Aimé from SEKOIA shared a [detailed twitter thread](https://mobile.twitter.com/felixaime/status/1481312381028478977) about a threat actor targeting open source projects. Some of the domains that Félix proactively shared were hosted and abused. Bleeping Computer published an article about this campaign titled: [Trojanized dnSpy app drops malware cocktail on researchers, devs](https://twitter.com/BleepinComputer/status/1479899697972133888)  

In June of 2022 I [tweeted](https://twitter.com/th3_protoCOL/status/1534530079975346176) about malicious advertising targeting OpenBroadcastSoftware leading to remote access trojans.    

In July of 2022 Twitter users @felixaime and @_yannis2707
[discussed](https://twitter.com/_yannis2707/status/1543557122612494338) new domains operated by this threat actor. This blog post aims to summarize the existing research and observations about this threat actor

![Graph](https://pbs.twimg.com/media/FI5i66vXwAE4N-m?format=jpg&name=4096x4096)

*Source: @felixaime on twitter, Threat Intel at SEKIO. Janurary 2022.*

## Attack Overview
Malicious advertising -> Malware download -> Scheduled Task Creation -> Download of Remote Access Trojans & CryptoMiners

This blog post is primarily focused on documenting the network infrastructure used and will not feature full malware analysis (at least for now).

## Active Targeting as of July 3rd
![Targets](/assets/img/graphs/Targets.png)

All of the following domains were setup by this threat actor to distribute malware. In some cases search engine adverting is leveraged to increase inbound web traffic.  

### Apache
- apachefriends[.]co

### Minecraft
- minecraft-launcher[.]net
- tlauncherminecraft[.]net
- optifine[.]app

### Open Broadcast Software (OBS)
- obsproject[.]app

### Notepad++
- notepad-plus-plus[.]co

### dnSpy .NET debugger and assembly editor
- dnspy[.]dev

### CPU Diagnostics Tools
- cpu-z[.]org
- gpu-z[.]org

## Online, but not active yet
### Minecraft
- minecraft-download[.]win   
- minecraft-java[.]com
- minecraftfree[.]net  
- minecraftz[.]net

## Historical Targets
### Open Broadcast Software (OBS)
- streamlabsobs[.]net
- obs-studio[.]net

### Apache
- xampp[.]download

### Tor Browser
- tor-browser[.]co

### Other Security & IT Tools
- cmder[.]co
- sandboxies[.]net
- mingw64[.]net
- dev-c[.]net
- de4dot[.]net
- dnspy[.]net

### Other Historical Threat Actor Websites
- combolist[.]cloud
- windows-software[.]co
- toolbase[.]co
- torfiles[.]net
- coolmint[.]net
- filesr[.]net
- windows-software[.]net
- tools-utilities[.]net
- carbonblackz[.]art


## Second Stage & C2 Indicators
### Threat Actor Cloud Hosting
- s3.us-west-1.wasabisys[.]com/cdnfiles/obs/
- s3.us-west-1.wasabisys[.]com/cdnfiles/minecraft/

### Threat Actor Malware Scripts
- codenote[.]org/raw/6mhzh0nqmg
- notepadd[.]net/raw/b4ym7
- codenote[.]org/raw/xhwv8nqthh
- notepadd[.]net/raw/obsx

### Command and Control Servers
- xiiideath[.]com
- inject1byte[.]com
- black-crystal[.]net
- 4api[.]net
- 4bash[.]net
- 4need[.]net
- 4perl[.]net
- duck[.]black
- l96[.]org

## Related Files

- OBS-Studio-27.2.4-Full-Installer-x64.exe
  - 1689db24be08cc680864338e57088c784d141187
- obs64.exe
  - 2735c8a59d391cbc7377bd0eabc846462b110acd
- n.exe
  - 8e6c31409562dae2beaeaee873de14fc98caba7a
- TLauncher-2.841-Installer-0.9.9.exe
  - ecb3b9b63b226cfe1534260f63165bdc5730d136
- s.exe
  - d6a142337788d09e98af6665ea44899b248e46fd
