# Pythonista
This repository contains my experiments with Python. 

#####1) Website crawler to access particular data
This is a program which goes to www.thenewboston.com and accesses the points earned by each user, displaying it with the usernames. Currently it accesses 40 people's profile points.

#####2) Youtube Playlist length calculator
Using this program you can calculate the length of any Youtube playlist. It takes the URL of the Youtube playlist as command line argument and displays the length in the form of hours, minutes and seconds.

`$ python3 Youtube-playlist-time-calculator.py "https://www.youtube.com/playlist?list=PL6gx4Cwl9DGAcbMi1sH6oAMk4JHw91mC_" `

To make it work you need to install 2 modules.
 
######-Requests
 `pip install requests`
 
######-BeautifulSoup4
`pip install beautifulsoup4`

#####3) Coding clock
According to Malcolm Gladwell 10,000 hours is what it takes to be an expert in any field. Are you on a spree to become the best coder on the planet? This timer will help you track the amount of time you spent coding. 
Just start the timer when you are coding. Pause it when you take a break. Stop it when you are done. 

#######Caution: It creates a file called timer.txt. Make sure you don't tamper it or delete it. It stores the number of seconds you have coded so far.
