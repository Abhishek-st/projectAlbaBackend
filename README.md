# C3P

<h2>Demo Video Link : </h2>
https://drive.google.com/file/d/16n7UAJ72PVBOQFYIAqYZleJ-QxaLO5az/view?usp=sharing
<br>

<h2>Inatallation SetUp</h2>
<ul>
    <li> Create virtual environment in python  " python3 -m venv env"</li>
    <li> Activate Env "source env/bin/activate"</li>
    <li> Now run "pip install -r requirements.txt"</li>
    <li> Type command "python manage.py makemigrations"</li>
    <li> Type command "python manage.py migrate"</li>
    <li> Type command "python manage.py runserver"</li>
    <li> Now you are ready for testing the API"</li>
</ul>
<br><br>

<h2>EndPoints</h2>
<ul>
    <li>GET  http://127.0.0.1:8000/api/leaderBoard/   :  To get all Users data</li>
    <li>POST http://127.0.0.1:8000/api/postMarks/   :  To post a marks of a student <br> <br>
    <center>  data =   {
        "name": "String",
        "roll": Integer,
        "physics": float,
        "chemistry": float,
        "marks": float}
     </center><br><br></li>

</ul>
