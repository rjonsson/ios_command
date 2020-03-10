function callApi(){
    var targetApi = 'http://10.100.1.112:5000/api/' + document.getElementById("inputHost").value
    
    var request = new XMLHttpRequest();
    request.open('GET', targetApi, true)

    request.onload = function() {
        var responseData = this.response
    
        if (request.status >= 200 && request.status < 400) {
            console.log(responseData)
            document.getElementById("outputPre").innerHTML = responseData
            document.body.appendChild(outputTarget)
        } else {
            console.log('error')
        }
    }
    request.send()
}

window.onload = function() {
    document.getElementById("okButton").onclick = callApi
}
