<h1 class="gap">0x04. AirBnB clone - Web framework</h1>

<h2>Learning Objectives</h2>

<p>At the end of this project, you are expected to be able to <a href="/rltoken/kGCHY64UciygJ4I0ANPGCA" title="explain to anyone" target="_blank">explain to anyone</a>, <strong>without the help of Google</strong>:</p>

<h3>General</h3>

<ul>
<li>What is a Web Framework</li>
<li>How to build a web framework with Flask</li>
<li>How to define routes in Flask</li>
<li>What is a route</li>
<li>How to handle variables in a route</li>
<li>What is a template</li>
<li>How to create a HTML response in Flask by using a template</li>
<li>How to create a dynamic template (loops, conditions…)</li>
<li>How to display in HTML data from a MySQL database</li>
</ul>

<h2 class="gap">Tasks</h2>

<h4 class="task">
    0. Hello Flask!
</h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.0-hello_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000 ; echo "" | cat -e
Hello HBNB!$
guillaume@ubuntu:~$ 
</code></pre>

<h4 class="task">
    1. HBNB
</h4>

  

  <!-- Progress vs Score -->

  <!-- Task Body -->
  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.1-hbnb_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/hbnb ; echo "" | cat -e
HBNB$
guillaume@ubuntu:~$ 
</code></pre>



<h4 class="task">
    2. C is fun!
</h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/&lt;text&gt;</code>: display “C ” followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.2-c_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/is_fun ; echo "" | cat -e
C is fun$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c/cool ; echo "" | cat -e
C cool$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/c
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>


  <h4 class="task">
    3. Python is cool!
  </h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/&lt;text&gt;</code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.3-python_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/is_magic ; echo "" | cat -e
Python is magic$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ curl -Ls 0.0.0.0:5000/python/ ; echo "" | cat -e
Python is cool$
guillaume@ubuntu:~$ 
</code></pre>

  <h4 class="task">
    4. Is it a number?
  </h4>

  <p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/&lt;text&gt;</code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display “<code>n</code> is a number” <strong>only</strong> if <code>n</code> is an integer</li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.4-number_route
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/89 ; echo "" | cat -e
89 is a number$
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/8.9 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number/python 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>


  <h4 class="task">
    5. Number template
  </h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/&lt;text&gt;</code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display “<code>n</code> is a number” <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: “Number: <code>n</code>” inside the tag <code>BODY</code> </li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.5-number_template
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/89 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/8.9 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_template/python 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>


  <h4 class="task">
    6. Odd or even?
  </h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>Routes:

<ul>
<li><code>/</code>: display “Hello HBNB!”</li>
<li><code>/hbnb</code>: display “HBNB”</li>
<li><code>/c/&lt;text&gt;</code>: display “C ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)</li>
<li><code>/python/(&lt;text&gt;)</code>: display “Python ”, followed by the value of the <code>text</code> variable (replace underscore <code>_</code> symbols with a space <code></code>)

<ul>
<li>The default value of <code>text</code> is “is cool”</li>
</ul></li>
<li><code>/number/&lt;n&gt;</code>: display “<code>n</code> is a number” <strong>only</strong> if <code>n</code> is an integer</li>
<li><code>/number_template/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: “Number: <code>n</code>” inside the tag <code>BODY</code></li>
</ul></li>
<li><code>/number_odd_or_even/&lt;n&gt;</code>: display a HTML page <strong>only</strong> if <code>n</code> is an integer: 

<ul>
<li><code>H1</code> tag: “Number: <code>n</code> is <code>even|odd</code>” inside the tag <code>BODY</code></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ python3 -m web_flask.6-number_odd_or_even
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/89 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 89 is odd&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/32 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;Number: 32 is even&lt;/H1&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/number_odd_or_even/python 
&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN"&gt;
&lt;title&gt;404 Not Found&lt;/title&gt;
&lt;h1&gt;Not Found&lt;/h1&gt;
&lt;p&gt;The requested URL was not found on the server.  If you entered the URL manually please check your spelling and try again.&lt;/p&gt;
guillaume@ubuntu:~$ 
</code></pre>

  <h4 class="task">
    7. Improve engines
  </h4>

<p>Before using Flask to display our HBNB data, you will need to update some part of our engine:</p>

<p>Update <code>FileStorage</code>: (<code>models/engine/file_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>reload()</code> method for deserializing the JSON file to objects</li>
</ul>

<p>Update <code>DBStorage</code>: (<code>models/engine/db_storage.py</code>)</p>

<ul>
<li>Add a public method <code>def close(self):</code>: call <code>remove()</code> method on the private session attribute (<code>self.__session</code>) <a href="/rltoken/O2mDvznV40mXE9dvTT3LJw" title="tips" target="_blank">tips</a> or <code>close()</code> on the class <code>Session</code> <a href="/rltoken/Vdh9u26tfc9fObUOb9NFzw" title="tips" target="_blank">tips</a></li>
</ul>

<p>Update <code>State</code>: (<code>models/state.py</code>) - If it’s not already present</p>

<ul>
<li>If your storage engine is not <code>DBStorage</code>, add a public getter method <code>cities</code> to return the list of <code>City</code> objects from <code>storage</code> linked to the current <code>State</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 
&gt;&gt;&gt; from models import storage
&gt;&gt;&gt; from models.state import State
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # Time to insert new data!
</code></pre>

<p>At this moment, in another tab:</p>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ echo 'INSERT INTO `states` VALUES ("421a55f1-7d82-45d9-b54c-a76916479545","2017-03-25 19:42:40","2017-03-25 19:42:40","Alabama");' | mysql -uroot -p hbnb_dev_db
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ 
</code></pre>

<p>And let’s go back the Python console:</p>

<pre><code>&gt;&gt;&gt; # Time to insert new data!
&gt;&gt;&gt; len(storage.all(State))
5
&gt;&gt;&gt; # normal: the SQLAlchemy didn't reload his `Session`
&gt;&gt;&gt; # to force it, you must remove the current session to create a new one:
&gt;&gt;&gt; storage.close()
&gt;&gt;&gt; len(storage.all(State))
6
&gt;&gt;&gt; # perfect!
</code></pre>

<p>And for the getter <code>cities</code> in the <code>State</code> model:</p>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ cat main.py
#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.city import City

"""
 Objects creations
"""
state_1 = State(name="California")
print("New state: {}".format(state_1))
state_1.save()
state_2 = State(name="Arizona")
print("New state: {}".format(state_2))
state_2.save()

city_1_1 = City(state_id=state_1.id, name="Napa")
print("New city: {} in the state: {}".format(city_1_1, state_1))
city_1_1.save()
city_1_2 = City(state_id=state_1.id, name="Sonoma")
print("New city: {} in the state: {}".format(city_1_2, state_1))
city_1_2.save()
city_2_1 = City(state_id=state_2.id, name="Page")
print("New city: {} in the state: {}".format(city_2_1, state_2))
city_2_1.save()


"""
 Verification
"""
print("")
all_states = storage.all(State)
for state_id, state in all_states.items():
    for city in state.cities:
        print("Find the city {} in the state {}".format(city, state))

guillaume@ubuntu:~/AirBnB_v2$ 
guillaume@ubuntu:~/AirBnB_v2$ rm file.json ; HBNB_TYPE_STORAGE=fs ./main.py 
New state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509954), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510256), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
New city: [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510797), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511437), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state: [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
New city: [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511873), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state: [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}

Find the city [City] (e3e36ded-fe56-44f5-bf08-8a27e2b30672) {'name': 'Napa', 'id': 'e3e36ded-fe56-44f5-bf08-8a27e2b30672', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510953), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510791)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (12a58d70-e255-4c1e-8a68-7d5fb924d2d2) {'name': 'Sonoma', 'id': '12a58d70-e255-4c1e-8a68-7d5fb924d2d2', 'state_id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511513), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511432)} in the state [State] (5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45) {'name': 'California', 'id': '5b8f1d55-e49c-44dd-ba6f-a3cf8489ae45', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510038), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 509950)}
Find the city [City] (a693bdb9-e0ca-4521-adfd-e1a93c093b4b) {'name': 'Page', 'id': 'a693bdb9-e0ca-4521-adfd-e1a93c093b4b', 'state_id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 512073), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 511869)} in the state [State] (a5e5311a-3c19-4995-9485-32c74411b416) {'name': 'Arizona', 'id': 'a5e5311a-3c19-4995-9485-32c74411b416', 'updated_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510373), 'created_at': datetime.datetime(2017, 12, 11, 19, 27, 52, 510252)}
guillaume@ubuntu:~/AirBnB_v2$ 
</code></pre>

  <h4 class="task">
    8. List of states
  </h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states_list</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: “States”</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/fid5cMJKYMaRJqL60PlUew" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/p5i5_Ny-0wL2JhPKvnLEnA" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.7-states_list
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states_list ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

        &lt;/UL&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>


  <h4 class="task">
    9. Cities by states
  </h4>

<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/cities_by_states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: “States”</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/fid5cMJKYMaRJqL60PlUew" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code> + <code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
</ul></li>
</ul></li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/p5i5_Ny-0wL2JhPKvnLEnA" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.8-cities_by_states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/cities_by_states ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;
        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Akron&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Babbie&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Calera&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Fairfield&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Douglas&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Kearny&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Tempe&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Fremont&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Napa&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Francisco&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;San Jose&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;Sonoma&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Denver&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Miami&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Orlando&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;
                &lt;UL&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Honolulu&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Kailua&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Pearl city&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;
                &lt;UL&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Baton rouge&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Lafayette&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;New Orleans&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Saint Paul&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Jackson&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Meridian&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Tupelo&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;
                &lt;UL&gt;

                        &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Eugene&lt;/B&gt;&lt;/LI&gt;

                        &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Portland&lt;/B&gt;&lt;/LI&gt;

                &lt;/UL&gt;
            &lt;/LI&gt;

        &lt;/UL&gt;
    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>

<p><img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/9a7ae8155274b17881442200437e8793cf08de48.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20210119%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20210119T000115Z&amp;X-Amz-Expires=86400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=f6b2f5b8a3daf38ca8aecf88fc0dea05c5e241e60fc373edfad9ae2530e2e6ed" alt="" style=""></p>

 <h4 class="task">
    10. States and State
  </h4>


<p>Write a script that starts a Flask web application:</p>

<ul>
<li>Your web application must be listening on <code>0.0.0.0</code>, port <code>5000</code></li>
<li>You must use <code>storage</code> for fetching data from the storage engine (<code>FileStorage</code> or <code>DBStorage</code>) =&gt; <code>from models import storage</code> and <code>storage.all(...)</code></li>
<li>To load all cities of a <code>State</code>:

<ul>
<li>If your storage engine is <code>DBStorage</code>, you must use <code>cities</code> relationship</li>
<li>Otherwise, use the public getter method <code>cities</code></li>
</ul></li>
<li>After each request you must remove the current SQLAlchemy Session:

<ul>
<li>Declare a method to handle <code>@app.teardown_appcontext</code></li>
<li>Call in this method <code>storage.close()</code></li>
</ul></li>
<li>Routes:

<ul>
<li><code>/states</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li><code>H1</code> tag: “States”</li>
<li><code>UL</code> tag: with the list of all <code>State</code> objects present in <code>DBStorage</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z) <a href="/rltoken/fid5cMJKYMaRJqL60PlUew" title="tip" target="_blank">tip</a>

<ul>
<li><code>LI</code> tag: description of one <code>State</code>: <code>&lt;state.id&gt;: &lt;B&gt;&lt;state.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li><code>/states/&lt;id&gt;</code>: display a HTML page: (inside the tag <code>BODY</code>)

<ul>
<li>If a <code>State</code> object is found with this <code>id</code>:

<ul>
<li><code>H1</code> tag: “State: <state.name>”</state.name></li>
<li><code>H3</code> tag: “Cities:”</li>
<li><code>UL</code> tag: with the list of <code>City</code> objects linked to the <code>State</code> <strong>sorted by <code>name</code></strong> (A-&gt;Z)

<ul>
<li><code>LI</code> tag: description of one <code>City</code>: <code>&lt;city.id&gt;: &lt;B&gt;&lt;city.name&gt;&lt;/B&gt;</code></li>
</ul></li>
</ul></li>
<li>Otherwise: 

<ul>
<li><code>H1</code> tag: “Not found!”</li>
</ul></li>
</ul></li>
</ul></li>
<li>You must use the option <code>strict_slashes=False</code> in your route definition</li>
<li>Import this <a href="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql" title="7-dump" target="_blank">7-dump</a> to have some data</li>
</ul>

<p><strong>IMPORTANT</strong></p>

<ul>
<li>Make sure you have a running and valid <code>setup_mysql_dev.sql</code> in your <code>AirBnB_clone_v2</code> repository (<a href="/rltoken/p5i5_Ny-0wL2JhPKvnLEnA" title="Task" target="_blank">Task</a>)</li>
<li>Make sure all tables are created when you run <code>echo "quit" | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db ./console.py</code></li>
</ul>

<pre><code>guillaume@ubuntu:~/AirBnB_v2$ curl -o 7-dump.sql "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/290/7-states_list.sql"
guillaume@ubuntu:~/AirBnB_v2$ cat 7-dump.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/AirBnB_v2$ HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python3 -m web_flask.9-states
* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
....
</code></pre>

<p>In another tab:</p>

<pre><code>guillaume@ubuntu:~$ curl 0.0.0.0:5000/states ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;States&lt;/H1&gt;
        &lt;UL&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479545: &lt;B&gt;Alabama&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479546: &lt;B&gt;Arizona&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479547: &lt;B&gt;California&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479548: &lt;B&gt;Colorado&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479549: &lt;B&gt;Florida&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479550: &lt;B&gt;Georgia&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479551: &lt;B&gt;Hawaii&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Illinois&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479553: &lt;B&gt;Indiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479554: &lt;B&gt;Louisiana&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479555: &lt;B&gt;Minnesota&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479556: &lt;B&gt;Mississippi&lt;/B&gt;&lt;/LI&gt;

            &lt;LI&gt;421a55f4-7d82-47d9-b54c-a76916479557: &lt;B&gt;Oregon&lt;/B&gt;&lt;/LI&gt;

        &lt;/UL&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/421a55f4-7d82-47d9-b54c-a76916479552 ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;State: Illinois&lt;/H1&gt;
        &lt;H3&gt;Cities:&lt;/H3&gt;
        &lt;UL&gt;
                &lt;LI&gt;521a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Chicago&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;561a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Joliet&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;541a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Naperville&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;531a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Peoria&lt;/B&gt;&lt;/LI&gt;

                &lt;LI&gt;551a55f4-7d82-47d9-b54c-a76916479552: &lt;B&gt;Urbana&lt;/B&gt;&lt;/LI&gt;
        &lt;/UL&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ curl 0.0.0.0:5000/states/holberton ; echo ""
&lt;!DOCTYPE html&gt;
&lt;HTML lang="en"&gt;
    &lt;HEAD&gt;
        &lt;TITLE&gt;HBNB&lt;/TITLE&gt;
    &lt;/HEAD&gt;
    &lt;BODY&gt;

        &lt;H1&gt;Not found!&lt;/H1&gt;

    &lt;/BODY&gt;
&lt;/HTML&gt;
guillaume@ubuntu:~$ 
</code></pre>
