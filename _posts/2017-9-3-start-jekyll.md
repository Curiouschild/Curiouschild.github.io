---
title:  "Start to learn Jekyll"
date:   2017-09-03 14:26:01 +0930
categories: Jekyll
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


<h4>Category</h4>
