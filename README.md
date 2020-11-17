# CSE-HUB

Based on [php version](https://github.com/harshraj22/contest) &nbsp; Website under development. Can be accessed [here](https://harshraj22.pythonanywhere.com/)

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
* User Registration, Now user can SignUp, so no need to go to admin section to create user.(will be implementing verification soon).
* We've got a good editor built ! It can do a lot of things (see details [here](https://github.com/harshraj22/CSE_HUB/pull/57))

<details>
<summary> What lacks ? </summary>

* Only mode of submission is through file upload
* No work is done for creating a contest
* frontend for various pages
* Editing of: problem/ added testcase
</details>

<details>
<summary> Mapped urls :</summary>

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
* ```editor/```
</details>

##### Installation :

* create a virtual environment and activate it (google it)
* Install dependencies into it ```pip3 install -r requirements.txt``` or ```python -m pip install -r requirements.txt```.
* Check out to develop branch.
* Make sure if you are using virtual environment, you have all dependencies installed (mentioned in ```requirements.txt```). ```python3 manage.py migrate --run-syncdb ``` [read here](https://stackoverflow.com/a/37799885/10127204) (p.s. all migration files are being ignored, see .gitignore) , ```python3 manage.py makemigrations``` and ```python3 manage.py migrate```. This will update database with tables as we describe in models.py. Then ```python3 manage.py runserver``` and play around testing what all has been developed.
use ```python3 manage.py createsuperuser``` to create admin credentials and then go to ```localhost:8080/admin``` after ```python3 manage.py runserver``` to log-in as admin. Create some user accounts/ profile pages/ question tags etc and play along with them, logging in from ```localhost:8080``` (you may use credentials of user you just created, but make sure you've created his/her profile as well from admin pannel).
###### Make sure you create tags before adding questions.

<details>
  <summary> ER diagram </summary>
  <img src="https://user-images.githubusercontent.com/46635452/99381606-56988e80-28f1-11eb-9f04-16f83ba68df0.png" alt="Entity Relationship Diagram"></img>

</details>


<details>
  <summary> Screenshots : </summary>
    <img src="https://user-images.githubusercontent.com/46635452/78997198-b2cd5000-7b63-11ea-9a2a-6942958f3ed8.png" alt="user profile"></img>
    <img src="https://user-images.githubusercontent.com/46635452/78997236-ca0c3d80-7b63-11ea-835d-ecfcd8d53fd5.png" alt="proble statement"></img>
    <img src="https://user-images.githubusercontent.com/46635452/78996997-6bdf5a80-7b63-11ea-972f-25a303eeaf90.png" alt="submission code"></img>
    <img src="https://user-images.githubusercontent.com/46635452/78996675-b3b1b200-7b62-11ea-8032-68bd97240ef6.png" alt="new post"></img>
    <img src="https://user-images.githubusercontent.com/46635452/78400079-ae5ce080-7613-11ea-8394-f35e26adb7b1.png" alt="code editor"></img>

</details>

#### Further Reading :
* [Writing tests](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing)
