# CS612_N5 Release Note
This is a simple Python Flask RestApi web service exhibition project.

### How to Run
You can run this program locally by downloading the project and run restapp.py. Please make sure that your system has python3 and flask installed.

You may also run it in Docker by build a docker image with the Dockerfile provided here. 
(ex. sudo docker build -t restapi-flask-demo . )

For grading purpose, I have included a docker image export at /image. You can just take the .tar file and load it into Docker from your local system.
(ex. sudo docker load -i /home/usr/demoImage.tar )

### Narratives
This API processes the information requests for library management system. Each uniquely ID'd records correspond to a member of library and contains the current status of library books taken by them.

### Prep
A good amount of research was needed as there are many possible stacks to achive it, even with the limited scope given by the requirement specification. Ultimately, Flask web framework was chosen for being a popular tool and its ease of implementation.

### Design
This project was specifically for implementing RestApi endpoints, so using a static .json file as a datastore was allowed. The main module, which acts as an entry point of this application, would contain the view logic that deals with RestApi queries. It would return the query results based on four routes availale . If root level (/) is called, then it would bring up a simple test page that allows the user to click on buttons to query the sytem with pre-determined condition values. 

### Implementation
appserver.py would just loads up the json file and make its data model accessible. restapp.py sets the RestApi Routes and packages the query result into JSON output. Venv was set up to isolate the python dev environment locally but not for Docker image, as such complexity was not deemed necessary for this project (I'm aware that it is good practice to wrap that in as wel). Source files were isolated into a single folder in order to add other frameworks later in future.

### Afterwords
Needed much more information on selecting tech stacks.

