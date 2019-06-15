---
title:  "Eaton Capstone Project Summary"
date:   2019-5-10 08:11:03 +0930
categories: CMU
tags: Python
---


We worked on Eaton’s requirement of analysing customer behavior by leveraging the web-click activity on Eaton’s website. Another requirement was to assess the customers’ reputation through sentiment analysis of news articles. A secondary requirement was to develop an anonymizer tool that can encrypt and decrypt user-selected columns in a file, to allow sharing of confidential data with external vendors.

<!-- more -->
Our client, Eaton, is a power management company with sales of $21.6 billion in 2018 and 99,000 employees around the world. It provides B2B energy-efficient solutions for electrical, hydraulic and mechanical power management. Finally, we integrated the scores obtained from the existing model, web-click behavior model and the trigger terms model to arrive at a final score in the range of 0-4 for every customer.

Eaton utilizes a scoring model to identify customers with highest sales conversion potential from a set of 4500+ customers that it has identified. It wishes to validate and improve this existing model along with adding additional features such as customer behavior and online reputation to this model. It also requires a tool that can anonymize confidential data before sharing it externally.

Eaton’s current scoring model captures five (5) different factors. Our team performed statistical analysis in R to determine the performance of this model and found that the current model is not a good predictor of sales. We did further analysis and suggested improvements in the model.

 ![Eaton1](\img\posts\eaton1.png "process flow")

We worked on Eaton’s requirement of analysing customer behavior by leveraging the web-click activity on Eaton’s website. This activity could be used to flag customers with high activity to the sales team, assuming they would be interested in buying Eaton’s products. We developed a model that analyzes the recency and frequency of the web click activities of these customers on Eaton.com site and generates a ‘web-click score’ in the range of 0-4.

Another requirement was to assess the customers’ reputation through sentiment analysis of news articles. We developed a model that fetches top 10 news articles from past 6 months for every customers and performs a sentiment analysis on them using trigger terms such as bankruptcy, increase in sales, etc.. These are then used to generate a ‘Trigger Terms Score’ in the range of 1-4.

Finally, we integrated the scores obtained from the existing model, web-click behavior model and the trigger terms model to arrive at a final score in the range of 0-4 for every customer. We made use of R, Python and Microsoft Excel in developing these models. This integrated scoring model will be used by the sales team of Eaton to prospect customers. Eaton’s sales team is enthusiastic about these models as they feel that this will immediately improve their sales by providing real-time information about a customer’s interest in Eaton’s products. They will also be able to track real-time changes in their customers’ corporate/ financial/ managerial set-up, which may have an impact on Eaton’s sales.

A secondary requirement was to develop an anonymizer tool that can encrypt and decrypt user-selected columns in a file, to allow sharing of confidential data with external vendors. We developed this tool in Python using the libraries wxPython for UI and PyCrypto for encryption. We used AES encryption alongside a password and it can also support two-factor authentication.


![Eaton2](\img\posts\eaton2.png "process flow")
