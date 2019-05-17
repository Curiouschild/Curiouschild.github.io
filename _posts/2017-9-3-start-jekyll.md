---
title:  "Start to learn Jekyll"
date:   2017-09-03 14:26:01 +0930
categories: WebDevelpment
tags: Jekyll
---

It's the second week of this semester and a logic time to start building my personal blog. Now I'm begining with github pages and jekyll. This post is about tech issues of learning jekyll.

<!-- more -->

```java
	for(int i=1; i<5; i++){
	new chuck();
	}
```

//use raw to escape liquid syntax
{% raw %}
{{site.time}}
{% endraw %}

//use global variable site.time to output time

{{site.time}}

// use for loop to output all page.path in site.pages

{% for page in site.pages %}
<ul>
  <li>{{ page.path }}</li>
</ul>
{% endfor %}

```java
Man chuck;
chuck = new Man();
```

highlight code
---------

{% highlight ruby linenos %}
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
{% endhighlight %}

test: read data from member.yml in _data
-------------
//_data folder --> membe file
{% for member in site.data.membe %}
<ul>
  <li>{{ member.name }} : {{ member.age }}</li>
</ul>
{% endfor %}

<div id="mountNode" width="100%"></div>
<script>/*Fixing iframe window.innerHeight 0 issue in Safari*/document.body.clientHeight;</script>
<script src="https://gw.alipayobjects.com/os/antv/assets/g2/3.0.4/g2.min.js"></script>
<script src="https://gw.alipayobjects.com/os/antv/assets/data-set/0.8.5/data-set.min.js"></script>
<script src="https://gw.alipayobjects.com/os/antv/assets/lib/jquery-3.2.1.min.js"></script>
<script src="https://gw.alipayobjects.com/os/antv/assets/lib/lodash-4.17.4.min.js"></script>
<script>
    function getTextAttrs(cfg) {
        return _.assign({}, {
            fillOpacity: cfg.opacity,
            fontSize: cfg.origin._origin.size,
            rotate: cfg.origin._origin.rotate,
            text: cfg.origin._origin.text,
            textAlign: 'center',
            fontFamily: cfg.origin._origin.font,
            fill: cfg.color,
            textBaseline: 'Alphabetic'
        }, cfg.style);
    }

    // 给point注册一个词云的shape
    G2.Shape.registerShape('point', 'cloud', {
        drawShape(cfg, container) {
            const attrs = getTextAttrs(cfg);
            return container.addShape('text', {
                attrs: _.assign(attrs, {
                    x: cfg.x,
                    y: cfg.y
                })
            });
        }
    });
    $.getJSON('/assets/data/word_count.json', data => {
        const dv = new DataSet.View().source(data);
        const range = dv.range('value');
        const min = range[0];
        const max = range[1];
        dv.transform({
            type: 'tag-cloud',
            fields: ['x', 'value'],
            size: [window.innerWidth, window.innerHeight],
            font: 'Verdana',
            padding: 0,
            timeInterval: 5000, // max execute time
            rotate() {
                let random = ~~(Math.random() * 4) % 4;
                if (random == 2) {
                    random = 0;
                }
                return random * 90; // 0, 90, 270
            },
            fontSize(d) {
                if (d.value) {
                    return ((d.value - min) / (max - min)) * (80 - 24) + 24;
                }
                return 0;
            }
        });
        const chart = new G2.Chart({
            container: 'mountNode',
            width: 1000,
            height: 800,
            padding: 0,
        });
        chart.source(dv, {
            x: {nice: false},
            y: {nice: false}
        });
        chart.legend(false);
        chart.axis(false);
        chart.tooltip({
            showTitle: false
        });
        chart.coord().reflect();
        chart.point()
            .position('x*y')
            .color('category')
            .shape('cloud')
            .tooltip('value*category');
        chart.render();
    });
</script>
