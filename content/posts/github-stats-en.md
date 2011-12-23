Title: GitHub in Numbers
Slug: github-stats
Date: 2011-10-15 09:20
Category: texts
Tags: git, github
Lang: en

Some times ago, I had got an idea — to create a new service around the GitHub. In the first place it will be useful to those users who have many repositories or following/watching many users and repositories.

My basic GitHub usage pattern is: to follow other coders to see in the News Feed which other coders they are following and which projects they are watching. This way I'm able to discover interesting people and projects on the GitHub. But this approach works only to a paritcular moment, while amount of data is not very big. When I had got a lot of items in my News Feed, I stoped to read it.

The idea is to aggregate items from the news feed and pop out interesting projects. For example, people who you are following instest can be used or people from the 2nd circle.

Moreover, this service should be useful for watching on the changes in your repositories forks. This feature will be useful for those guys who have tens public repositories. I already implemented this functionality for myself as a simple script. This script generates a RSS feed with new commits from the forks.

Also, there will be a funny medals and ratings. Push a dozen commits at the midnight and you'll become a "Midnight code warrior" :)

But before actual implementation of the idea, I decided to calculate some stats about GitHub's usage. I have to estimate how many people will be interested in such project, because I hate to create useless things.

Progress
--------

At first, I wrote a GitHub's profiles and reps fetcher. It takes one login and downloads a his profile and add all users who he follows to the queue. Then it repeats the process for every login in the queue.

Because the rate limit in 5000 reqeusts a hour, my script worked about 2 days.

Totally about **57 thousand** profiles were downloaded and **500 thousand** repositories were fetched. I expected that there are much more users, but probably these numbers are correct. After all, if my script didn't download somebody then nowbody follows hib and his account probably abandoned.

This graph depicts a fetching progress. At this graph is well seen the moment when queue stopped to grow and started to fall down.

<center>
![](http://chart.apis.google.com/chart?cht=lxy&chs=800x300&chd=e:AAApBSB7CkDND2EfFIFxGaHDHrIUI9JmKPK4LhMKMzNcOFOuPXQAQpRSR7SkTNT1UeVHVwWZXCXrYUY9ZmaPa4bhcKczdceFeufXgAgohRh6ijjMj1kelHlwmZnCnroUo9pmqPq4rhsKsztbuEutvWv.woxRx6yjzMz10e1H1w2Z3C3r4U495m6O637g8J8y9b-E-t.W..,FtSbbKjQmuqvthvwxU0D043Z5o5d7N-I8X8K9B9X-V...e.8-z-z.Y.o.A-K-J9w736D7Q6C425S3P23000dzuyMy-y2ySy1xyw6wcuyuFtFrQrAqGpPphomnNmpnsmQmSkhjVh9hTfselfjecczeVcPbfavZMcRbUaIYgXnWwV4UyUTSCRLPIN4MaKrJJHpGIEzDSCJAH&chtt=Fetching%20progress&chxt=y,x,y,x&chxl=2:%7cqueue%7c3:%7cnumber%20of%20fetched%20profiles&chxr=0,0,3707%7c1,0,57001&chxp=2,50%7c3,50&chg=25,25,1,0)
</center>

Watch & Follow
--------------

One of the most impotent stats for my project is portion of users who are watching a large amount of repositories or following many other coders:

<center>

![](http://chart.apis.google.com/chart?cht=p3&chs=500x150&chd=s:EbZFAA&chtt=Num%20watched%20repositories&chco=208020&chl=%3C1000%20%287.0%25%29%7c%3C100%20%2843.7%25%29%7c%3C10%20%2841.7%25%29%7cnot%20watching%20%287.4%25%29%7c%3C10000%20%2852%29%7c%3E10000%20%281%29) | ![](http://chart.apis.google.com/chart?cht=p3&chs=500x150&chd=s:NdTA&chtt=Number%20of%20followed%20users&chco=208020&chl=%3C100%20%2820.5%25%29%7c%3C10%20%2847.3%25%29%7cnot%20following%20%2831.4%25%29%7c%3E100%20%28410%29)
  
</center>

Here we see that about 50% of users are watching more than 10 repositories and 7% (~ 4000) — are watching more than 100. Also I'm interested in those 20% (~11000), who are following more than 10 people, definitely they are unable to read through all their news feeds. And certanly those 410 users who follow more then hungred other coders will fall in love with aggregation feature. Myself is in the latter category as I'm following about 331 users.

A number of repositories
------------------------

Average amount of public repositories is **8**, **3** of them are forks of someone's else repository.

<center>

![](http://chart.apis.google.com/chart?cht=p3&chs=500x150&chd=s:PlJA&chtt=Number%20of%20public%20repositories&chco=208020&chl=%3C100%20%2824.4%25%29%7c%3C10%20%2860.1%25%29%7cno%20reps%20%2815.2%25%29%7c%3E100%20%28158%29) | ![](http://chart.apis.google.com/chart?cht=p3&chs=500x150&chd=s:mIPA&chtt=Number%20of%20public%20repositories%20%28except%20forks%29&chco=208020&chl=%3C10%20%2862.1%25%29%7c%3C100%20%2813.4%25%29%7cno%20reps%20%2824.4%25%29%7c%3E100%20%2854%29)

</center>

This graph shows that 60% of users have less than 10 public repositories and 15% does not have repositories at all. But about a quarter of users have from 10 to 100 public repositories. They will appreciate a fork watching feature of my project.

Also, I calculated a part of active repositories. Only 10% of repositories had been pushed at last month.

And more…
---------

As I said before, totally about **500 thousand** repositories were downloaded and **40%** of them are forks. It is amazing! I thought this number should be much much bigger.

In addition, I estimated how much a 2nd cirle is. Average GitHub user follows 9 people and watches at 33 repositories. But his 2nd circle contains 230 people and 800 repositories. This is average number, but for geeks like me they are much bigger. I have in 2nd cirle 11548 people and 42882 repositories. It is about 1/5 of all GitHub!

And here is how many **organisations** relative to **users**:

<center>

![](http://chart.apis.google.com/chart?cht=p3&chs=500x150&chd=s:7C&chtt=User%20types&chco=208020&chl=User%20%2896.41%25%29%7cOrganization%20%283.59%25%29)

</center>


And some tops, I know, you like them!
-------------------------------------

<style>
  div.top {width: 40%; float: left; margin-right: 10%;}
  br.clear {border: 0px; clear: both;}
</style>

<div class="top">

### Top 20 Companies

Company     |Users
------------|------
            |37965 
ThoughtWorks|75    
Google      |65    
Mozilla     |61    
Red Hat     |58    
Freelance   |56    
Twitter     |40    
Japan       |40    
Yandex      |39    
Freelancer  |36    
Globo.com   |35    
Yahoo!      |33    
Intridea    |31    
Facebook    |30    
GitHub      |29    
Student     |26    
Emergya     |26    
Pivotal Labs|24    
Microsoft   |23    
Engine Yard |23

</div>

<div class="top">

### Top 20 Cities

City         |Users
-------------|------
             |23657 
San Francisco|1441  
London       |962   
New York     |578   
Paris        |474   
Chicago      |458   
Seattle      |457   
Tokyo        |430   
Berlin       |423   
Germany      |417   
Portland     |346   
Toronto      |317   
Boston       |288   
Austin       |280   
Sydney       |272   
Stockholm    |261   
Japan        |244   
Los Angeles  |230   
Brooklyn     |226   
Melbourne    |221

</div>

<div class="top">

### Top 20 "followers"
Login         |Follows
--------------|------------
snytkine      |3242        
mtsoerin      |1983        
webiest       |1903        
superfeedr    |1710        
charlenopires |1236        
stonegao      |1205        
Marak         |1068        
speedygonzalez|1059        
tyru          |1022        
esneko        |867         
josegonzalez  |640         
c9s           |556         
kanzure       |555         
take-cheeze   |517         
elliottcable  |495         
Sannis        |475         
mattn         |462         
j2labs        |453         
dpree         |446         
rkh           |444

</div>

<div class="top">

### Top 20 "who followed"
Login           |Followers
----------------|--------------
defunkt         |4005          
torvalds        |3803          
jeresig         |3466          
mojombo         |3248          
ryanb           |2737          
schacon         |2429          
paulirish       |2316          
dhh             |2170          
wycats          |2044          
ry              |2032          
rails           |1946          
facebook        |1802          
jquery          |1767          
technoweenie    |1572          
pjhyett         |1563          
visionmedia     |1554          
cyanogen        |1410          
douglascrockford|1380          
tpope           |1369          
android         |1317

</div>

<div class="top">

### Top 20 repository owners
Login          |Repositories
---------------|------------
gitpan         |21976       
vim-scripts    |3735        
emacsmirror    |3101        
Epictetus      |911         
panega         |612         
jenkinsci      |602         
dev2dev        |504         
wave2future    |411         
CyanogenMod    |342         
MechanisM      |329         
rjbs           |325         
tokuhirom      |297         
rwldrn         |297         
aculich        |287         
rainly         |282         
albertobraschi |278         
idega          |272         
rafl           |266         
apache         |258         
kristianmandrup|244

</div>

<div class="top">

### Top 20 "watchers"
Login          |Watches
---------------|------------
gitpan         |21976       
vim-scripts    |3736        
emacsmirror    |3588        
stonegao       |2789        
abecciu        |2474        
igrigorik      |2415        
charlenopires  |2339        
stan           |2318        
matagus        |2160        
smtlaissezfaire|1955        
rmetzler       |1916        
shanlalit      |1897        
willi          |1896        
Epictetus      |1821        
filipeamoreira |1812        
arden          |1783        
andrew         |1746        
methodmissing  |1665        
rkh            |1571        
lgs            |1511

</div>

The end
-------

Certanly, some other interesting metrics could be calculated, using my database. If you have any ideas feel comment this post or send me an email.

P.S. — I think that my project have a chance to take off and will be useful for few thousand of people around the world. One more thing to think about is how to monetize it to pay rent for servers.