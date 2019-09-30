# Political trends in Europe

This code is part of an investigation into long term political trends in Europe by De Correspondent.

## Aim of the project

The aim of this project is to find the big trends in the European political landscape by using data sources commonly used by political scientists, but not by journalists. 

Many people seem to have the feeling that the political landscape is changing rapidly in Europe (and beyond) and that far right parties are gaining ground. In stead of looking at separate elections, we try to get a bird's eye view.

We would like to give you insight into the methods that we have used so you can tag along. You can reach me by e-mail: reinier at decorrespondent.nl

## Data sources

An important source is the [ParlGov database](http://www.parlgov.org/) from Holger Döring and Philip Manow of the University of Bremen.

You will find a collection of csv files of ParlGov in the [data folder.](https://github.com/Respondens/politics/tree/master/data/source_data).

## Stories (in Dutch)

You can read the [first story here.](https://decorrespondent.nl/9541/maakt-europa-een-enorme-ruk-naar-rechts-dit-zeggen-de-data/464618077-897d7fd4)

The  [second story here](https://decorrespondent.nl/10323/de-tijd-van-de-grote-partijen-is-voorbij-dus-laten-we-de-volgende-verkiezingsstrijd-anders-bekijken/5356576734993-fb20c8ea)

And the [third story here]()

## Method of the last story

In the python files in politics/src you can find the code for last two stories. Especially the last one. Especially read the verplintering_EU.pynb. This gives you a guide through the thought process. 

The most important method that I have used is the Effective Number of Parties. This is a ratio based on a formula developed by  Laakso and Taagepera. You can find more about it [here](https://en.wikipedia.org/wiki/Effective_number_of_parties). 

The key is that you weight the amount of parties by their size. This is calculated by employing the following formula:
ENPP=1/Σsi²
where vi/si is the proportion of votes/seats of the ith party. 

To calculate the the average I have used the mean. This is important because the amount of countries in the dataset differs due to fact that new countries became a democracy. One could also argue to take the median because of potential outliers (like Great Britain) but i find it important to keep these as well. The idea is that even with countries with different electoral systems, the ENP grows. By looking at the individual countries as well, one can see which ones influence the slope of the graph. 

## Recommendation
I would urge you to first look at the versplintering_EU file. After that, you can find many more calculations, variables and functions in the fragmentatie.py file. Play along and see if you understand the steps that I make and let me know what else you have found in the dataset! 

I am not a full learned programmer / data scientist (is one ever?), so there are probably many improvements to make that I am keen to learn from! 