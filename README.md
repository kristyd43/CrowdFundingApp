# CrowdFundingApp

MVP Name: ShowBizness

Point of Difference: 
A platform to support schools fund classes
donations made to help businesses will increase the donater's membership with the business. An increase in membership will unlock benefits to redeem within the business. These prizes/benefits are chosen by and specific to each business and will aim to further advertise the company.
For example:
a $50 donation to businessA might reward the donor a free cap. $50 to businessB might get them 10% off a 1st order.
However a $100 donation to businessA could reward the donor a ticket in a raffle for a car. $100 to businessB could reward 15% off and free delivery for the next 3 orders.

Must Have Features:
⦁	A list of Businesses with the option to select each title to see more detail.
⦁	A "Your Profile" page showing previous donations, rewards and current memberships.
⦁	A "Create Business" page that lets the user upload a profile photo, write some "why you should donate" info and the different rewards available.
⦁	A login/logout and create user page
⦁	An info page describing what how 'Get Busyness' works.

Would Be Nice Features:
⦁	Search function to find businesses with key words important to the user.
⦁	A blog feature where business owners could keep customers up to date with progress via latest stories and photos.

Database Schema:
 



API Endpoints:
GET - /posts/ - returns all posts
GET - /profile/ - shows the user profile - user needs to be logged in
POST - /createuser/ - creates user
GET - /login/ - log user in
GET - /logout/ - logs user out.
POST - /post/ - creates a new post - user needs to be logged in. must be owner of project
POST - /pledge/ - creates a pledge - must be logged in.
GET - /project/1/ - returns project with id of 1
GET - /pledge/1/ - returns pledge with id of 1
DELETE - /project/1/ - deletes project with id of 1  - must be logged in and owner of project
DELETE - /pledge/1/ - deletes pledge with id of 1  - must be logged in and owner of pledge
GET - /pledge/ - returns all pledges - must be logged in
GET - /posts/search/x/ - returns all posts containing x
GET - /pledge/search/x/ - returns all pledges containing x - must be logged in  


