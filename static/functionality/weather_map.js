console.log("Map script loaded.");





// initder Heatmap
var map_heat = L.map('map_heat').setView([51.505, -0.09], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map_heat);

var temperatureLayer = L.tileLayer(`https://tile.openweathermap.org/map/temp_new/{z}/{x}/{y}.png?appid=${api_key}`, {
    maxZoom: 19,
    opacity: 0.8
}).addTo(map_heat);




//init rest
var map_rest = L.map('map_rest').setView([51.505, -0.09], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map_rest);

var precipitationLayer = L.tileLayer(`https://tile.openweathermap.org/map/precipitation_new/{z}/{x}/{y}.png?appid=${api_key}`, {
    maxZoom: 19,
    opacity: 0.8
});

var cloudLayer = L.tileLayer(`https://tile.openweathermap.org/map/clouds_new/{z}/{x}/{y}.png?appid=${api_key}`, {
    maxZoom: 19,
    opacity: 0.5
});

var windLayer = L.tileLayer(`https://tile.openweathermap.org/map/wind_new/{z}/{x}/{y}.png?appid=${api_key}`, {
    maxZoom: 19,
    opacity: 0.5
});

var baseLayersRest = {
    "Precipitation": precipitationLayer,
    "Clouds": cloudLayer,
    "Wind": windLayer
};




//button
L.control.layers({"Temperature": temperatureLayer}).addTo(map_heat);
L.control.layers(baseLayersRest).addTo(map_rest);
