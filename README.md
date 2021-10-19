# Smart-City-Real-time-Big-Data-Analytics

Running weather predictor

Prerequisites

- Apache Zookeeper 3.4.6
- Apache Kafka 0.9.0.1
- Apache Storm 1.0.2
- Apache Cassandra 3.11
- Python 2.7
- JDK 8

Python Packages
  The file requirements.txt contains all required python packages. To install these packages use the command "pip install -r requirements.txt"


Steps

  1. Run batch file 'Run-Storm-Kafka-Cassandra.bat'
  2. Run batch file 'RunWeatherPredictor.bat'
  3. Run batch file 'StartWebApp.bat'

  The webapp can be accessed at 110.173.132.3:5000
  
Note
  - If all apache services are already running it is only neccessary to run the batch file 'RunWeatherPredictor.bat'.
  - To stop all apache services, the most simple way is to restart the server.
  - Before rerunning the WeatherPredictor the Topology must be killed. This can be done by navigating to localhost:8080 in
    a web browser, clicking the topology named 'PredictionTopology' and clicking kill. Alternatively it can be killed by
    opening the command line and executing the command 'storm kill PredictionTopology'.
    
Example Code Folder
  Contains example code used as building blocks to create the weather predictor
  
Weather Predictor Folder
  Contains all code for making weather predictions, the front end web application as well as tests and batch files to run the weather predictor.
  
  - BatchFiles Folder
      Contains BatchFiles used by the main batch files to run services, weather predictor and web app
  - Flask Folder
      ***#####BRIEF EXPLANATION OF CODE JULIAN#####***
  - Weather Data Producer
      Contains code to receive data from OpenWeatherMap API and produce this data to an Apache Kafka topic. Also contains unit tests to test it's ability to receive data from 
      the API and produce it to a topic.
  - Weather Prediction Topology
      Contains code to build Apache Storm Topology. The topology receives data from the Kafka topic and analyzes it in a Storm Bolt using pickle files generated using                 SvmClassifier.py to make predictions on fog and haze. These predictions are then stored in an Apache Cassandra database. 
  
SvmClassifier.py
  ***#####BRIEF EXPLANATION OF CODE SHRUTHI#####***
    

    
 
