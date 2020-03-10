function reqListener () {
  console.log(this.responseText);
}

var oReq = new XMLHttpRequest();

// data is not in the reponse
oReq.addEventListener("load", reqListener);

function transferComplete(evt) {
    console.log("The transfer is complete.");
  }
  
  function transferFailed(evt) {
    console.log("An error occurred while transferring the file.");
  }
  
  function transferCanceled(evt) {
    console.log("The transfer has been canceled by the user.");
  }

// Last true is for async
oReq.open("GET", "http://www.example.org/example.txt", true);
oReq.send();