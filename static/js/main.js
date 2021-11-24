  var map = L.map('map').
    setView([ -38.7333,-72.6667],
    10);
  
    L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
   
    maxZoom: 10,
    
    }).addTo(map);

    function Get_Mapa(data){
        console.log(data);
      
        var polyline=L.polyline(data,{color:'red'}).addTo(map);
        map.fitBounds(polyline.getBounds());
    }