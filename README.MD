# Load Test Example Project

A simple dockerized django rest framework api to demo https://locust.io 

## Quickstart
Ensure [docker compose](https://docs.docker.com/compose/install/) is installed 
Data can be added and inspected in the [admin panel](http://localhost:8000/admin)
g
username: `admin` password: `admin`

To run the locust command, when the server finishes building run the following command to bring start locust `docker exec -it load_test-web-1 locust`

Open you web browser to [locust.io ui](http://localhost:8089/) and start the load test