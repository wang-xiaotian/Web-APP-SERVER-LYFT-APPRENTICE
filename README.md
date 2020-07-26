# Web-APP-SERVER-LYFT-APPRENTICE
- This application responses to POST request with argument 'string_to_cut'
- Requird packages: flask
- (Windows User)
- Execute Option 1 (debug mode=True): 
> python server.py
- Execute Option 2: 
> set FLASK_APP=server.py; flask run
- Client Input: curl -X POST --header "Content-Type: application/json" HTTP://127.0.0.1:5000/test --data {\"string_to_cut\":\"fdl!@#$%^&*()_+~ssygff26t322460872340\"}
- Client ouput: {"return_string" : "lyft2020" }
