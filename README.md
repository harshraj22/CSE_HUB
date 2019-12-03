# CSE-HUB

Based on [php version](https://github.com/harshraj22/contest)

##### Idea :
To have a website that caters all needs that a CSE UG has.

##### What works ?

* adding problems
* adding testcase (for now we can only add one test case at a time)
* login/logout
* adding solution (checks if user is logged in or not)
* evaluation of solution
* updation of table for problems upon adding solution by the user(successful/total submissions)
* adding predefined tags to problems

##### What lacks ?

* Only mode of submission is through file upload
* No work is done for uploading a contest
* frontend
* can add only one tag to each problem
* Display all solutions by a user and for a question

##### Mapped urls :

* ```admin/```
* ```''```
* ```profile```
* ```problems/add```
* ```problems/display/<int:problem_id>```
* ```problems/add/testcase```
* ```problems/submit/<int:problem_id>```
* ```problems```
* ```login```
* ```logout```

##### Installation :

* create a virtual environment and activate it (google it)
* Install dependencies into it ```pip3 insall -r requirements.txt```

##### Screenshots :
![Screenshot from 2019-12-04 02-29-03](https://user-images.githubusercontent.com/46635452/70089367-f0fab600-163d-11ea-81d9-fa1441ac95ac.png)
