# gcs_objects_access
This is a python code using Django framework to access objects inside a google cloud storage. (Google bucket))

Setup steps:
1) Make a pull of this code.
2) Make a virtual environment
3) Run requirements.txt
4) Run migrations
5) Goto cloud_storage app -> views.py -> get_bucket_data() function
6) Replace your google generated client_id and secret_id
7) Run the python server
8) Goto http://127.0.0.1/accounts/login URL
9) Click sign in with google
10) Follow the procedure
11) After logging in hit https://127.0.0.1/
12) You will get the bucket objects as a response. 
