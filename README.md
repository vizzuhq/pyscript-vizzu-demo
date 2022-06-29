# How to use Vizzu charts in PyScript

This how-to describes the steps to use the [Vizzu](https://github.com/vizzuhq/vizzu-lib) JavaScript charting library in [PyScript](https://pyscript.net/).

Working example: https://vizzuhq.github.io/vizzu-pyscript-example/.

Source code: https://github.com/vizzuhq/vizzu-pyscript-example/blob/main/docs/index.html

![Example chart](https://vizzuhq.github.io/vizzu-lib-doc/readme/example.gif)

## HTML

### Import map

Vizzu library's URL should be set in the HTML file using an import map.

```html
<script type="importmap">
  {
    "imports": {
      "Vizzu": "https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js"
    }
  }
</script>
```

### Container HTML element

Create an HTML element for the chart:

```html
<div id="myVizzu" style="width:500px; height:350px;"></div>
```
## PyScript 

Add a new `<py-script>` tag to the HTML file for the PyScript code:

```html
<py-script>
  ...
</py-script>
```

### Importing dependencies

The Vizzu library has to be imported into the PyScript source. `to_js` from `pyodide` and `Object` from `js` are also required to convert the Python dictionaries into JavaScript objects. 

```Python
from pyodide import to_js
from js import Object
import Vizzu
```

### Initializing Vizzu

A new Vizzu object is created by passing the container HTML element's id to its constructor.

```Python
chart = Vizzu.default.new("myVizzu")
```

### Creating a chart

In the following example, the data and the chart configuration object are passed to Vizzu. For further info on using Vizzu, check 
the [tutorial](https://lib.vizzuhq.com/latest/#chapter-0.0). 
Please note that the Python dictionary has to be manually converted into a JS object, as the auto conversion doesn't work because it would create JS maps instead of JS objects. `to_js` also needs to be set in a way that it creates JS objects, by passing a converter in the second parameter.

```Python
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
```

### Animating the chart

From this point, repeatedly calling the `animate` method will transform the chart. We suggest that you check the [tutorial](https://lib.vizzuhq.com/latest/#chapter-0.0) and the [examples](https://lib.vizzuhq.com/latest/#animated-charts) to get a sense of how to build animated charts and data stories with Vizzu.

```Python
chart.animate(to_js({
  "color": "Foo", 
  "x": "Baz",
  "geometry": "circle"
}, dict_converter=Object.fromEntries))
```

**Have fun animating charts with Vizzu and PyScript and let us know if you build something cool with them. 😊📈🚀**
