<head>
<title>Document</title>
<link rel="stylesheet" href="style.css">
<script src="script.js"></script>
</head>

function temperature(){
    //To convert celcius to farenheit
    //(CEL * 9/5) + 32
    var c = document.getElementById("celsius").value;
    var f = (c * 9/5) + 32
    document.getElementById("fahrenheit").value = f
}
function weight(){
    //To convert KGs to Pounds
    // KG * 2.2
    var kg = document.getElementById("kilo").value;
    var p = kg * 2.2
    document.getElementById("pounds").value = p
}
function distance(){
    //To convert KMs to Miles
    // KM * 0.62137
    var km = document.getElementById("km").value;
    var m = km * 0.62137
    document.getElementById("miles").value = m
}

<fieldset>
    <legend>Temperature</legend>
    <label for="Temperature">Celsius</label> <br/>
    <input type="number" id="celsius"> <br/>
    <button id="temperature" onclick="temperature()"> Convert </button> <br/>
    <input type="number" id="fahrenheit"> <br/>
    <label for="Temperature">Fahrenheit</label>
</fieldset>

<fieldset>
    <legend>Weight</legend>
    <label for="Weight">KG</label> <br/>
    <input type="number" id="kilo"> <br/>
    <button id="weight" onclick="weight()"> Convert </button>  <br/>
    <input type="number" id="pounds">  <br/>
    <label for="Weight">Pounds</label>
</fieldset>

<fieldset>
    <legend>Distance</legend>
    <label for="Distance">KM</label> <br/>
    <input type="number" id="km">  <br/>
    <button id="distance" onclick="distance()"> Convert </button> <br/>
    <input type="number" id="miles">  <br/>
    <label for="Distance">Miles</label>
</fieldset>