---
layout: default
title: Using ChatGPT to Visualize Ransomware Leak Site Data  
categories: [Threat Intelligence, Ransomware]
tags: [CTI, Ransomware, ChatGPT, Plotly]

comments: false
---
<meta name="twitter:image" content="https://github.com/colincowie/colincowie.github.io/raw/master/assets/img/ChatGPT/graphic_1year.png">

# Using ChatGPT to Visualize Ransomware Leak Site Data  

Recently I wanted to test out if I could use [OpenAI's ChatGPT](https://chat.openai.com/chat) to assist with analyzing trends around ransomware leak site postings.

## Project Setup

### The Raw Data

RansomWatch is a publicly accessible project that monitors ransomware leak sites and posts metadata to [their website](https://ransomwatch.telemetry.ltd/#/README). Technical details on RansomWatch can be [found on Github](https://github.com/joshhighet/ransomwatch#ransomwatch--).

For the sake of this project I downloaded a recent copy of all the RansomWatch postings [from their github in .json format](https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json)

### Python Data Visualization Library

To visualize this data I'll be asking ChatGPT to write python3 code using the [plotly library](https://plotly.com/python/). Plotly is open source graphing library for python. The plotly library can be installed via pip, the python package manager.

![Plotly website](/assets/img/ChatGPT/plotly.png)

### Working with ChatGPT

ChatGPT is a chatbot built on top of OpenAI's GPT-3.5 family of large language models. One important thing to note is that ChatGPT works in "conversations". If you feel like ChatGPT has gotten stuck or isn't giving you the results you're looking I've found it's beneficial to start a new conversation with no chat history that might influence the output.
OpenAI has [blog post](https://openai.com/blog/chatgpt/) that explains more in depth how it works - here's one of the provided limitations:
> "Ideally, the model would ask clarifying questions when the user provided an ambiguous query. Instead, our current models usually guess what the user intended."

![ChatGPT website](/assets/img/ChatGPT/chatgpt.png)

## ChatGPT Prompts

**Initial Prompt**

> Given a json file ("posts.json") containing multiple posts, provide python3 plotly code to demonstrate the posting frequency of each group ("group_name") over time, the json data contains timestamps data in the "discovered" field

ChatGPT Output:

![Base Output](/assets/img/ChatGPT/base_output.png)

Code Result:

![Initial Plotly Graph](/assets/img/ChatGPT/base_graph.png)

**Additional Filters**

Within the same conversation I asked ChatGPT to filter the data to only the past 365 days.

> What code is needed to filter the above json data to the past year only?

ChatGPT Output:

![DateTime Filtering](/assets/img/ChatGPT/datetime_filter.png)

Code Outcome:

![1 year scatter graph](/assets/img/ChatGPT/graphic_1year.png)

**Cleaning up the graphics**

Now that we've filtered the results down to the past year, lets try to make it easier to look at and understand.

> There are a large amount "group_name" values, the y-axis is hard to read on the Plotly graphic, how can I update the code to make the y values easier read and sorted by most postings?

ChatGPT Output:

![Chat GPT Output (part 1 of 2)](/assets/img/ChatGPT/update_part1.png)
*\<snipped to save space\>*

![Chat GPT Output (part 2 of 2)](/assets/img/ChatGPT/update_part2.png)

At this point ChatGPT has provided us with a few different solid code examples to work with. Not all of them are perfect but with some minor adjustments I was able to get some pretty nice results!

![Bar graph of 1 year](/assets/img/ChatGPT/bar_graph_1_year.png)

**Changing data graphing formats**

Plotly has a wide breadth of different graphing capabilities, lets ask ChatGPT to change things up a bit!

> How can I modify this code to use a density heatmap

![Heatmap ChatGPT Results (part 1 of 2)](/assets/img/ChatGPT/heaptmap_output_p1.png)
*\<snipped to save space\>*

![Heatmap ChatGPT Results (part 2 of 2)](/assets/img/ChatGPT/heaptmap_output_p2.png)

Code Outcome:

![1 year heatmap graph](/assets/img/ChatGPT/heatmap_1yr.png)


**Some final touches**

To make things more modular I asked ChatGPT to wrap the code into a function

> Can you wrap the above code into a python function? The function should have a variable parameter for the number of days to filter, with a default of 365

![ChatGPT Output](/assets/img/ChatGPT/function.png)

I also wanted to see what color customization options exist.

> What other plotly color palette could I use for this?

![ChatGPT Output](/assets/img/ChatGPT/colors_part1.png)
*\<snipped to save space\>*

![ChatGPT Output](/assets/img/ChatGPT/colors_part2.png)


## Closing Thoughts

Overall ChatGPT is very powerful tool to augment small development projects. ChatGPT saved me a significant amount of time I otherwise would have spent web searching and reading Plotly documentation.  I believe that it's still important to have the programming fundamentals required to modify the ChatGPT output if needed. Hopefully this blog post provided some ChatGPT inspiration!

### Final Code

The final scripts have been uploaded to a new Github repository:
- [https://github.com/colincowie/LeakSiteAnalytics](https://github.com/colincowie/LeakSiteAnalytics)
