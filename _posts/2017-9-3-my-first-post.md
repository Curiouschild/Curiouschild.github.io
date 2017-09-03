---
layout: post
title:  "My First Post"
date:   2017-09-03 14:26:01 +0930
---


My First Post
=======
**I love coding!**


```chuck```

~~~
Man chuck;
chuck = new Man();
~~~

* highlight code
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

* test: read data from member.yml in _data
-------------
{% for member in site.data.member %}
<ul>
  <li>{{ member.name }}</li>
</ul>
{% endfor %}

![GitHub](/img/formal-selfie.jpg "GitHub,Social Coding")

