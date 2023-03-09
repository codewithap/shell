from flask import Flask,request
import subprocess

app = Flask(__name__)

@app.route("/")
def start():
  
  return """
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
  </head>
  <body>
   <input type="text">
    <a href="#"><button>run</button></a>
    <br><br>
    <div id="demo">
    
    </div>
    <script>
    let inp = document.querySelector("input")
    
    
    document.querySelector("button").addEventListener("click",()=>{
      var xhttp = new XMLHttpRequest();
      xhttp.onreadystatechange = function() {
          if (this.readyState == 4 && this.status == 200) {
             // Typical action to be performed when the document is ready:
             document.getElementById("demo").innerHTML += xhttp.responseText+"<br>";
          }
      };
      xhttp.open("GET",  "/res?cmd="+inp.value, true);
      xhttp.send();
    })
    </script>
  </body>
  </html>
 
  """
  
@app.route("/res")
def res(): 
  cmd = request.args.get("cmd")
  out = subprocess.getoutput(cmd)
  return f"{out}"

app.run(host = "0.0.0.0")