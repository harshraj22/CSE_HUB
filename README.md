# CSE-HUB

Based on [php version](https://github.com/harshraj22/contest)

##### Idea :
To have a website that caters all needs that a CSE UG has.

##### What works ?

* adding problems (login_required)
* adding testcase (for now we can only add one test case at a time, also only author of a problem can add testcase for the problem)
* login/logout
* adding solution (checks if user is logged in or not)
* evaluation of solution
* updation of table for problems upon adding solution by the user(successful/total submissions), ie. each problem stores count of AC/ WA to itself
* adding predefined tags to problems
* We've got a discussion forum with comments functioning !!
* User can now edit profile !! (but currently we don't store anything editable)
* Now user can see/download all submited codes. How cool is that !!

##### What lacks ?

* Only mode of submission is through file upload
* No work is done for creating a contest
* frontend for various pages
* Editing of: problem/ added testcase
* User registration (signUp)

##### Mapped urls :

* ```admin/```
* ```''```
* ```profile/<username>```
* ```profile/<username>/edit```
* ```problems/add```
* ```problems/display/<int:problem_id>```
* ```problems/add/testcase```
* ```problems/submit/<int:problem_id>```
* ```submit/<int:id>/```
* ```submissions/<str:username>/```
* ```submissions/<str:username>/view/<int:id>/```
* ```submissions/download/<int:id>/```
* ```problems```
* ```login```
* ```logout```
* ```forum```
* ```forum/post/<int:post_id>/```

##### Installation :

* create a virtual environment and activate it (google it)
* Install dependencies into it ```pip3 install -r requirements.txt``` or ```python -m pip install -r requirements.txt```.
* Make sure if you are using virtual environment, you have all dependencies installed (mentioned in ```requirements.txt```). ```python3 manage.py migrate --run-syncdb ``` [read here](https://stackoverflow.com/a/37799885/10127204) (p.s. all migration files are being ignored, see .gitignore) , ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```. This will update database with tables as we describe in models.py. Then ```python3 manage.py runserver``` and play around testing what all has been developed.
use ```python3 manage.py createsuperuser``` to create admin credentials and then go to ```localhost:8080/admin``` after ```python3 manage.py runserver``` to log-in as admin. Create some user accounts/ profile pages/ question tags etc and play along with them, logging in from ```localhost:8080``` (you may use credentials of user you just created, but make sure you've created his/her profile as well from admin pannel)

##### Screenshots :
![Screenshot from 2019-12-04 02-29-03](https://user-images.githubusercontent.com/46635452/70089367-f0fab600-163d-11ea-81d9-fa1441ac95ac.png)

![Screenshot from 2019-12-04 03-31-38](https://user-images.githubusercontent.com/46635452/70093670-ed1f6180-1646-11ea-9b39-3c318603edbe.png)


#### Further Reading :
* [Writing tests](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
