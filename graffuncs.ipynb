# DEFINING FUNCTIONS

def plot2D(x_points):
    # I find where the letter X is in my equation text and replace by placeholders {}
    number_of_placeholders = equation.value.count('X')
    decomposed_equation = equation.value.replace('X', '{}')
    y = []
    for point in x_points:
        dicti = {i: point for i in range(number_of_placeholders)}
        decomposed_eq = decomposed_equation.format(*dicti.values())   
        # WARNING: couldn't figure out any other way, let me know if you know
        exec("""global res
res = {}""".format(decomposed_eq))
        y.append(res)
    plt.plot(x_points, y)
    plt.show()


def plot3D(X, Y, Z):
    options = {
        "width": "100%",
        "style": "surface",
        "showPerspective": True,
        "showGrid": True,
        "showShadow": True,
        "keepAspectRatio": False,
        "height": "600px"
        }
     # LOADING DATA
    data = [ {"x": X[y,x], 
              "y": Y[y,x], 
              "z": Z[y,x]} for y in range(Y.shape[0]) for x in range(Y.shape[1]) ]  
    visual_code = r"""
       <link href="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.css" type="text/css" rel="stylesheet" />
       <script src="https://cdnjs.cloudflare.com/ajax/libs/vis/4.21.0/vis.min.js"></script>
       <div id="pos" style="top:0px;left:0px;position:absolute;"></div>
       <div id="visualization"></div>      
       <script type="text/javascript">
        var data = new vis.DataSet();
        data.add(""" + json.dumps(data) + """);
        var options = """ + json.dumps(options) + """;
        var container = document.getElementById("visualization");
        var graph3d = new vis.Graph3d(container, data, options);
        // setting the camera position initial
        graph3d.setCameraPosition({horizontal:0.8197963, vertical:0.945, distance:1.988})
        graph3d.on("cameraPositionChange", function(evt)
        {
            elem = document.getElementById("pos");
            elem.innerHTML = "Horizontal: " + evt.horizontal + "<br>Vertical: " + evt.vertical + "<br>Camera Distance: " + evt.distance;
        });
       </script>
    """
    html= "<iframe srcdoc='"+visual_code+"' width='50%' height='600px' style='border:10;' scrolling='no'> </iframe>"
    display(HTML(html))
