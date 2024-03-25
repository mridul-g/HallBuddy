HallBuddy
==================================

This application was made as a course project of [CS253A](https://www.cse.iitk.ac.in/users/isaha/Courses/sdo22.shtml/): Software Development and Operations in spring 2024 under 
the guidance of [Dr. Indranil Saha](https://www.cse.iitk.ac.in/users/isaha/).

Hall Buddy is a merged platform designed for the residents of various halls at IITK to access day to day hall functionalities. This portal aims to 
digitalize various services provided by the hall that includes mess, canteen and various other services. 

Broadly, the application will support the following:

* Students can book the hall's guest room.
* Students can maintain a digital cleaning log of their rooms and the admin can export room-cleaning data
* Students can use the software's complaint management system to lodge complaints.
* Students can view their pending hostel-dues and pay these dues.
* Special permissions have been provided to the Hostel Manager to facilitate all these services.

## Group Details

| Name                   | Roll no. | Email Id                |
| ---------------------- | -------- | ----------------------- |
| Ritesh Hans            | 220893   | riteshhans22@iitk.ac.in |
| Mridul Gupta           | 220672   | mridulg22@iitk.ac.in    |
| Krutuparna Paranjape   | 210536   | krutuparna21@iitk.ac.in |
| Mrdul Agarwal          | 210632   | mrdula21@iitk.ac.in     |
| Apoorv Tandon          | 220192   | apoorvt22@iitk.ac.in    |
| Taneshq Zendey         | 221123   | taneshq22@iitk.ac.in    |
| Tanishq Maheshwari     | 221128   | tanishqm22@iitk.ac.in   |
| Ayush                  | 220259   | ayushs@iit.ac.in        |
| Samarpan Verma         | 220943   | samarpanv22@iitk.ac.in  |
| Rohan Batra            | 210868   | rohanb21@iitk.ac.in     |

## Deployment

The web app is deployed at: http://hallbuddyweb.pythonanywhere.com/

## How to run the software locally?

* Make sure you have python and pip installed in your system.

Clone the repository-

```
git clone https://github.com/mridul-g/HallBuddy
```

Run following commands to start the backend server-

```
cd HallBuddy_Website
```

```
pip install -r requirements.txt
```

```
python manage.py collectstatic
```
Use following commands to run the server locally : 
```
python manage.py makemigrations
```
```
python manage.py migrate
```

```
python manage.py runserver
```

Go on the localhost web address :http://127.0.0.1:8000/ which must have been printed on the terminal.



  
