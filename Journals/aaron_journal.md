# Journal For Aaron Bradfield
## 1/24/2020
Setup initial repo, added readme, added journal directory, added my journal.
Note, are text files okay for our journals? 

## 1/25/2020
Corrected journal to use .md format, adding more material for setup of python, flask, etc., and started feasability study.

## 1/26/2020
Continued working on feasability study, do we write the study as if we are our own company? Started new branch for Pycket landing page, haven't pushed that branch yet though.

## 1/27/2020
Worked on the feasability study, added that to the google drive, updated the landing page, etc. 

## 1/29/2020
Finished feasability study, played around with flask, started URCA abstract

## 1/30/2020
Finished URCA abstract and added to the drive. Met with Eric to get him setup.

## 1/31/2020
Met with Trevor and Qingzhong, helped them setup their dev environments, met with Eric to finish setting up Eric his dev environment. 

## 2/3/2020
Met with Trevor and Aingzhong, helped them understand HTML/CSS, provided resources to learn HTML/CSS, worked on mock-up for Friday, etc.

## 2/4/2020
Met with Eric, discussed HTML and CSS, cut the meeting short as I wasn't feeling well.

## 2/5/2020
Met with Qingzhong and Eric to flesh out more of the home page, finished the mockup on Figma, created and finished our presentation, began our progress report, met with Eric after Algorithms to discuss our presentation and which parts he will be presenting. 

## 2/7/2020
Team TODO had our presentation today, met after class to dicuss how we think that went, what our goals are for the next progress report, finished the progress report.

## 2/8/2020
Started Flask tutorial to gain a better understanding of Flask, worked through the majority of the front-end components and started the back-end stuff.

## 2/9/2020
Finished the Flask tutorial (including unit testing) and have gained a better knowledge of how Flask is used to run the back-end, database, etc. We will be implementing ideas and concepts from the tutorial into our own project.

## 2/10/2020
Met with trevor and Qingzhong at 10, started templating out the base page, walked them through a simple Flask project, and showed them some of the things we will have to change with templating, our static pages, etc.

## 2/11/2020
Met with Eric at 12:30, finished creating the base template together, Eric is going to try creating the login page by himself, and we will work on that together on Thursday.

## 2/12/2020
Met with Trevor and Qingzhong at 9, got Trevor and Qingzhong started on the content for the home page, I started working on the back-end.

## 2/13/2020
Met with Eric, hooked up auth.py with login/setup html pages. Trevor and Qingzhong are supposed to be working on the landing page content.

## 2/14/2020
Worked on back-end for login page, started reorganization of bootstrap/css/js.

## 2/16/2020
Updated signup/login pages and added client-side password verification. Changed to a login page as opposed to a login modal. A login page works better and is easier to integrate/maintain

## 2/17/2020
Creating base template and extended templates for ticket section of software such as create/edit ticket.

## 2/18/2020
Worked on ticket section, started base template and began extension for other templates mentioned above. I am stuck on an error with 'ticket.index' not being recognized as a URL endpoint, but I am able to access it as a method. I am unsure why it is not being recognized as an endpoint.

## 2/20/2020
Worked on ticket section, attempting to route between landing page and our main ticketing page, unable to correctly route and receiving an error 'unable to builtd url endpoint for 'ticket.index'. This error makes it seem as though index is not defined within the ticket blueprint, but it is? Unsure of where this error is coming from.

Edit: I'm stupid. The ticket blueprint was improperly named as 'app' and not 'ticket'. Routing now operating as expected to our ticketing side of our app. The goal is to try and finish the landing page and ticketing pages prior to our next class meeting, but we will see what happens over the next week.

## 2/29/2020
Continued wokring on the ticketing page routes. I am now able to add some simple styling to the main ticket page. Eric mentioned possibly adding a 'forgot password' functionality to our project. I tasked him with doing some research for what it would take to add that functionality. Maybe it'll be something we can add. 

## 3/31/2020
Team meeting today. We talked about adding the 'forgot password' functionality, but I think it is beyond the scope of this project. It would require either significant edits to the existing back-end and database functionality and/or the implementation of an email server. Both of which I do not think we will have time for.

## 4/01/2020
Found a cool Flask library called Flask-WTF. This is a flask implementation of the WTForms library. Apparently this is to protect against some cross-site-scripting and sql-injection attacks. I am going to try and replace our existing forms to use the WTForms.

## 4/02/2020
I broke the login and signup pages and I am not sure what I am doing wrong. I am moving these to use the WTForms library. I think I am not correctly labeling the front-end components to match what is on our back-end.

Edit: I was correct, because 'Login' was on the front-end but was 'Log in' on the back-end. There were a few others also named like this.

## 4/03/2020
Finally transitioned to use the WTForms for the login and signup pages. I have yet to do the ticket creation page as Eric is working on that page right now. My changes should not break any of the styling he is doing to them.

## 04/05/2020
Met with the team (no Qingzhong) on Discord/Zoom. We did a practice presentation on our current project state so we can properly present tomorrow. Eric, Trevor, and I also talked about the lack of effort from Qingzhong and our frustration. We are unsure what, if anything, Qingzhong will present tomorrow.  

## 4/06/2020
Progress report presentation went well. I tried to have everyone else do a little more talking as I know I tend to talk more than everyone else. I think I managed to do better with that.

## 4/07/2020
Created the base Webstore routes and started on the back-end functionality. This webstore is going to be like a very stripped down version of an ecommerce site.

## 4/08/2020
Adding the Product table to the database. This class is going to need so many helper methods for us to properly get/post any information from this table. 

## 4/09/2020
I broke the database trying to update the Product table. The Alembic and Flask-SQLAlchemy tools don't have the best documentation for trying to fix this.

## 4/10/2020
I got frustrated with the database and wiped everything. Hopefully I won't have this issue again making any changes to the DB, but its nice that we didn't have a lot of information in our DB as of yet.

## 4/14/2020
We had a team meeting to practice for our URCA presentation tomorrow. We figured out how we are going to present and practiced our presentation a few times through. We also decided on who is going to do what next. I am starting the webstore, Eric is working on the Create Ticket page, and Trevor is going to work on the Main Ticket page.

## 4/15/2020
URCA is cancelled because of people Zoom-bombing he URCA meeting. Information hasn't been sent out yet about any makeup event.

## 4/16/2020
Still no information for any URCA makeup info. Nothing else done today.

## 4/17/2020
Dr. Swanson sent out some makeup info for the URCA presentations. We can record our presentation that can then be posted for others to see what we have been working on. 


## 4/28/2020
I broke the database... again. I tried updating the Product table, but it seems that SQLite3 doesn't support updating existing columns in a table, which seems strange to me. Basically, I had to delete all the data in that table of the db, make the update, and then add new data to that table.

## 5/1/2020
Continued work on the base template for the webstore. I am trying to fix some URL errors for the navbar. I am trying to set the URL for the webstore.index route, but I am getting an error saying, "webstore.index does not exist."

Edit: Found the error, the webstore blueprint was named Webstore. The capitol 'W' was causing the error.

## 5/2/2020
Worked on the webstore main page and add product page. The main ticket page now extends a base template, as well as the add product page. The product page has a form, but that form does not currently do anything. The products displayed on the main page are all mocked data that needs to be transitioned to pulling from the database. 

## 5/3/2020
We were all supposed to meet to record our URCA presentation today, but Trevor has been having issues with his internet. I chatted with Eric for a couple of hours as we worked through the main ticket page. The main page now correctly lists out existing tickets and relevant info for each ticket. Users can also click the ticket number to navigate to the edit ticket page for that ticket. We will meet tomorrow to record our URCA presentation.

## 5/4/2020
Met with the team from ~7-8:30pm to record our URCA presentation. I think our presentation went pretty smoothly after practicing a couple of takes. Each of us talked for a fairly equal amount of time as we conducted a demo of our project. I also made sure there was no extra feedback coming through my mic.

## 5/5/2020
Final meeting with the team. We are practicing our presentation for our final progress report that is tomorrow. I spent some time earlier today finalizing the add and edit pages for the webstore. Users can now add a new product and edit an existing product. Also, the main webstore page now correctly lists out the products added to the store.

## 5/6/2020
We had out final progress report presentation today. I think the presentation went well and we should be proud of how much we accomplished in the time we worked on this. I hope each of us learned something about programming, web development, and working with teams as a whole. I know I learned how I need to improve on delegating tasks, setting up proper documentation, and a better need for project management as a whole.