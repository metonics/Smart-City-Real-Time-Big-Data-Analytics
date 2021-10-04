
from flask import Flask, render_template
import os
import urllib2
app = Flask(__name__)
from cassandra.cluster import Cluster
cluster = Cluster(['127.0.0.1'])
session = cluster.connect('test')

TEMPLATE_DIR = os.path.abspath('templates')
STATIC_DIR = os.path.abspath('static')
app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

@app.route('/index.html')
def hello_name():
  return render_template('index.html')

@app.route('/')
def hello_name3():
  return render_template('index.html')

@app.route('/main.js')
def hello_name1():
  return render_template('main.js')

@app.route('/prediction.html')
def prediction_test():
  html = '''<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name ="website" content="frontend">
        <meta http-equiv="X-UA-Compatible" content="ie-edge">
        <title>Weather Website</title>
        <link rel= "stylesheet" type= "text/css" href= "/static/main.css">
    </head>
    <body>
        <div class="app-wrap">
            <nav>
                <label class="logo">SEPA6</label>
                <ul>
                    <li><a href="index.html">Status</a></li>
                    <li><a href="prediction.html">Fog And HAze</a></li>
                </ul>
            </nav>
           <header>
               <h1>FOG AND HAZE PREDICTION</h1>
            </header>
            <main>
             <div id="container">
                 <form>
                     <select id="select">
                         <option value="Melbourne, au">Melbourne</option>
                         <option value="Sydney">Sydney</option>
                         <option value="Canberra">Canberra</option>
                         <option value="Darwin">Darwin</option>
                         <option value="Brisbane">Brisbane</option>
                         <option value="Adelaide">Adelaide</option>
                         <option value="Hobart">Hobart</option>
                         <option value="Perth">Perth</option>
                     </select>
                     <button id="btn">Get the Selected city</button>
                 </form>
                 </div>
 
                <section class="location">
                    <div class="city">Melbourne, AU</div>
                    <div class="date">Saturnday 29 August 2021</div>
                </section>
               <div class= "prediction">
                <table id="table1">
                    <theadh>
                    <tr>
                      <th id="tabletitle">FOG PREDICTION</th>
                      <th id="tabletitle">HAZE PREDICTION</th>
                    </tr>
                </theadh>
                <tbody>
                    <tr>
                      <td id="mainprd">fogvalue1</td>
                      <td id="mainprd">hazevalue1</td>
                    </tr>
                </tbody>
                  </table>

                <table id="table2">
                    <theadh>
                        <tr>
                        <th id="tabletitle2">TIME</th>
                          <th id="tabletitle2">FOG PREDICTION</th>
                          <th id="tabletitle2">HAZE PREDICTION</th>
                        </tr>
                    </theadh>
                    <tbody>
                        <tr>
                          <td>time2</td>
                          <td>fogvalue2</td>
                          <td>hazevalue2</td>
                        </tr>
                        <tr>
                            <td>time3</td>
                            <td>fogvalue3</td>
                            <td>hazevalue3</td>
                        </tr>
                        <tr>
                            <td>time4</td>
                            <td>fogvalue4</td>
                            <td>hazevalue4</td>
                        </tr>
                        <tr>
                            <td>time5</td>
                            <td>fogvalue5</td>
                            <td>hazevalue5</td>
                        </tr>
                        <tr>
                            <td>time6</td>
                            <td>fogvalue6</td>
                            <td>hazevalue6</td>
                        </tr>
                        <tr>
                            <td>time7</td>
                            <td>fogvalue7</td>
                            <td>hazevalue7</td>
                        </tr>
                    </tbody>
                </table>
               </div>
           </main>
        </div>
        <script src="main.js"></script>
    </body>
</html>'''

  data = session.execute('SELECT toTimestamp(timeuuid) as timestamp, haze_prediction, fog_prediction FROM predictions WHERE city_id = 1 ORDER by timeuuid DESC limit 10;')
  count = 0
  for each in data:
      count = count + 1
      html = html.replace('fogvalue'+str(count), str(each.fog_prediction))
      html = html.replace('hazevalue'+str(count), str(each.haze_prediction))
      if (count > 1):
        html = html.replace('time'+str(count), str(each.timestamp).split(' ')[1][:5])
  
  return html


if __name__ == '__main__':
  app.run()
  