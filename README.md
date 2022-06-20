# How to use Vizzu charts in PyScript

This howto describes the steps to use [Vizzu](https://github.com/vizzuhq/vizzu-lib) JavaScript charting library in [PyScript](https://pyscript.net/).

See working example here: https://vizzuhq.github.io/vizzu-pyscript-example/

See full source code here: https://github.com/vizzuhq/vizzu-pyscript-example/blob/main/docs/index.html

![Example chart](https://vizzuhq.github.io/vizzu-lib-doc/readme/example.gif)

## Import map

We should set the vizzu library URL in our HTML file using an import map. 

```html
<script type="importmap">
  {
    "imports": {
      "Vizzu": "https://cdn.jsdelivr.net/npm/vizzu@latest/dist/vizzu.min.js"
    }
  }
</script>
```

## Container HTML element

We create an HTML element for containing the chart:

```html
<div id="myVizzu" style="width:500px; height:350px;"></div>
```
## PyScript 

We add a new `<py-script>` to our HTML file for our PyScript code:

```html
<py-script>
  ...
</py-script>
```

### Importing dependencies

We import the Vizzu library into our PyScript source. We will also need `to_js` from `pyodide` and 
`Object` from `js` to convert our Python dictionaries into JavaScript objects. 

```Python
from pyodide import to_js
from js import Object
import Vizzu
```

### Initializing Vizzu

We can create a new Vizzu object passing the container HTML element's id to it's constructor.

```Python
chart = Vizzu.default.new("myVizzu")
```

### Creating a chart

Here we pass the data and the chart configuration object to Vizzu. For further info on how to use Vizzu see
(Vizzu tutorial)[https://lib.vizzuhq.com/latest/]. Note, that we have to convert the Python dictionary into JS object
manually, since auto conversion won't work, because it would create JS maps instead of JS objects. We also have 
to set for `to_js` that it should create JS objects passing a converter in the second parameter.

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

### Modifying the chart

From this point we can repeat the `animate` calls and transform our chart.

```Python
chart.animate(to_js({
  "color": "Foo", 
  "x": "Baz",
  "geometry": "circle"
}, dict_converter=Object.fromEntries))
```


