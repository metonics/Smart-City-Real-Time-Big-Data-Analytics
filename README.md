# Smart-City-Real-time-Big-Data-Analytics

Steps to run weather predictor

  1. Run batch file 'Run-Storm-Kafka-Cassandra.bat'
  2. Run batch file 'RunWeatherPredictor.bat'
  
Note
  - If all apache services are already running it is only neccessary to run the batch file 'RunWeatherPredictor.bat'.
  - To stop all apache services, the most simple way is to restart the server.
  - Before rerunning the WeatherPredictor the Topology must be killed. This can be done by navigating to localhost:8080 in
    a web browser, clicking the topology named 'PredictionTopology' and clicking kill. Alternatively it can be killed by
    opening the command line and executing the command 'storm kill PredictionTopology'.
