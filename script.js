function sendRequest(url, retriesLeft) {
  const xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4) {
      if (this.status == 200) {
        const response = JSON.parse(this.responseText);
        if(response == "error"){
          document.getElementById("result").innerHTML = "Error: Failed to send request.";
        }
        else{
        document.getElementById("result").innerHTML = "tg(F(x)) = "+ response;
        }
      } else if (retriesLeft > 0) {
        // Retry the request after 1 second if there are retries left
        setTimeout(() => {
          sendRequest(url, retriesLeft - 1);
        }, 1000);
      } else {
        // Display an error message if the request failed after all retries
        document.getElementById("result").innerHTML = "Error: Failed to send request.";
      }
    }
  };
  xhttp.open("GET", url);
  xhttp.send();
}

function returnValue() {
  let func_v = document.getElementById("func_s").value;
  let point_v = document.getElementById("point_v").value;
  point_v = parseInt(point_v);
  const encoded_func_v = encodeURIComponent(func_v);
  const port = document.getElementById("server_port").value;
  const url = `http://localhost:${port}/api_?func_v=${encoded_func_v}&point_v=${point_v}`;

  sendRequest(url, 4);
}