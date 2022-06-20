from pyodide import to_js
from js import Object
import Vizzu

chart = Vizzu.default.new("myVizzu")

chart.animate(to_js({
	"data" : {
		"series": [
		  { "name": "Foo", "values": ["Alice", "Bob", "Ted"] },
		  { "name": "Bar", "values": [15, 32, 12] },
		  { "name": "Baz", "values": [5, 3, 2] }
		]
	},
	"config": {
		"x": "Foo",
		"y": "Bar"
	}
}, dict_converter=Object.fromEntries))

chart.animate(to_js({
  "color": "Foo", 
  "x": "Baz",
  "geometry": "circle"
}, dict_converter=Object.fromEntries))
