---
title:  "Start to learn Jekyll"
date:   2017-09-03 14:26:01 +0930
categories: bar
---

My First Post
=======
**I love coding!**

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

```chuck```

~~~
Man chuck;
chuck = new Man();
~~~

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

![GitHub](/img/selfie20170903.jpg "GitHub,Social Coding")

<h4>Category</h4>
<ul>
    //这里使用了 Jekyll 语法，会被编译，所以加多个"\"
    {\% for category in site.categories %\}
    <li><a href="/categories/{\{ category | first }\}/" title="view all
posts">{\{ category | first }\} {\{ category | last | size }\}</a>
    </li>
    {\% endfor %\}
</ul>

