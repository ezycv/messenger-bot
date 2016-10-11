HTTP/1.1 500 INTERNAL SERVER ERROR
Connection: keep-alive
Server: gunicorn/19.6.0
Date: Tue, 11 Oct 2016 18:14:30 GMT
Transfer-Encoding: chunked
X-Frame-Options: SAMEORIGIN
Content-Type: text/html
Via: 1.1 vegur


<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="content-type" content="text/html; charset=utf-8">
  <meta name="robots" content="NONE,NOARCHIVE">
  <title>IndentationError at /facebook_auth</title>
  <style type="text/css">
    html * { padding:0; margin:0; }
    body * { padding:10px 20px; }
    body * * { padding:0; }
    body { font:small sans-serif; }
    body>div { border-bottom:1px solid #ddd; }
    h1 { font-weight:normal; }
    h2 { margin-bottom:.8em; }
    h2 span { font-size:80%; color:#666; font-weight:normal; }
    h3 { margin:1em 0 .5em 0; }
    h4 { margin:0 0 .5em 0; font-weight: normal; }
    code, pre { font-size: 100%; white-space: pre-wrap; }
    table { border:1px solid #ccc; border-collapse: collapse; width:100%; background:white; }
    tbody td, tbody th { vertical-align:top; padding:2px 3px; }
    thead th { padding:1px 6px 1px 3px; background:#fefefe; text-align:left; font-weight:normal; font-size:11px; border:1px solid #ddd; }
    tbody th { width:12em; text-align:right; color:#666; padding-right:.5em; }
    table.vars { margin:5px 0 2px 40px; }
    table.vars td, table.req td { font-family:monospace; }
    table td.code { width:100%; }
    table td.code pre { overflow:hidden; }
    table.source th { color:#666; }
    table.source td { font-family:monospace; white-space:pre; border-bottom:1px solid #eee; }
    ul.traceback { list-style-type:none; color: #222; }
    ul.traceback li.frame { padding-bottom:1em; color:#666; }
    ul.traceback li.user { background-color:#e0e0e0; color:#000 }
    div.context { padding:10px 0; overflow:hidden; }
    div.context ol { padding-left:30px; margin:0 10px; list-style-position: inside; }
    div.context ol li { font-family:monospace; white-space:pre; color:#777; cursor:pointer; }
    div.context ol li pre { display:inline; }
    div.context ol.context-line li { color:#505050; background-color:#dfdfdf; }
    div.context ol.context-line li span { position:absolute; right:32px; }
    .user div.context ol.context-line li { background-color:#bbb; color:#000; }
    .user div.context ol li { color:#666; }
    div.commands { margin-left: 40px; }
    div.commands a { color:#555; text-decoration:none; }
    .user div.commands a { color: black; }
    #summary { background: #ffc; }
    #summary h2 { font-weight: normal; color: #666; }
    #explanation { background:#eee; }
    #template, #template-not-exist { background:#f6f6f6; }
    #template-not-exist ul { margin: 0 0 0 20px; }
    #unicode-hint { background:#eee; }
    #traceback { background:#eee; }
    #requestinfo { background:#f6f6f6; padding-left:120px; }
    #summary table { border:none; background:transparent; }
    #requestinfo h2, #requestinfo h3 { position:relative; margin-left:-100px; }
    #requestinfo h3 { margin-bottom:-1em; }
    .error { background: #ffc; }
    .specific { color:#cc3300; font-weight:bold; }
    h2 span.commands { font-size:.7em;}
    span.commands a:link {color:#5E5694;}
    pre.exception_value { font-family: sans-serif; color: #666; font-size: 1.5em; margin: 10px 0 10px 0; }
  </style>
  
  <script type="text/javascript">
  //<!--
    function getElementsByClassName(oElm, strTagName, strClassName){
        // Written by Jonathan Snook, http://www.snook.ca/jon; Add-ons by Robert Nyman, http://www.robertnyman.com
        var arrElements = (strTagName == "*" && document.all)? document.all :
        oElm.getElementsByTagName(strTagName);
        var arrReturnElements = new Array();
        strClassName = strClassName.replace(/\-/g, "\-");
        var oRegExp = new RegExp("(^|\s)" + strClassName + "(\s|$)");
        var oElement;
        for(var i=0; i<arrElements.length; i++){
            oElement = arrElements[i];
            if(oRegExp.test(oElement.className)){
                arrReturnElements.push(oElement);
            }
        }
        return (arrReturnElements)
    }
    function hideAll(elems) {
      for (var e = 0; e < elems.length; e++) {
        elems[e].style.display = 'none';
      }
    }
    window.onload = function() {
      hideAll(getElementsByClassName(document, 'table', 'vars'));
      hideAll(getElementsByClassName(document, 'ol', 'pre-context'));
      hideAll(getElementsByClassName(document, 'ol', 'post-context'));
      hideAll(getElementsByClassName(document, 'div', 'pastebin'));
    }
    function toggle() {
      for (var i = 0; i < arguments.length; i++) {
        var e = document.getElementById(arguments[i]);
        if (e) {
          e.style.display = e.style.display == 'none' ? 'block': 'none';
        }
      }
      return false;
    }
    function varToggle(link, id) {
      toggle('v' + id);
      var s = link.getElementsByTagName('span')[0];
      var uarr = String.fromCharCode(0x25b6);
      var darr = String.fromCharCode(0x25bc);
      s.innerHTML = s.innerHTML == uarr ? darr : uarr;
      return false;
    }
    function switchPastebinFriendly(link) {
      s1 = "Switch to copy-and-paste view";
      s2 = "Switch back to interactive view";
      link.innerHTML = link.innerHTML == s1 ? s2: s1;
      toggle('browserTraceback', 'pastebinTraceback');
      return false;
    }
    //-->
  </script>
  
</head>
<body>
<div id="summary">
  <h1>IndentationError at /facebook_auth</h1>
  <pre class="exception_value">unexpected unindent (views.py, line 109)</pre>
  <table class="meta">

    <tr>
      <th>Request Method:</th>
      <td>POST</td>
    </tr>
    <tr>
      <th>Request URL:</th>
      <td>https://thawing-sands-52537.herokuapp.com/facebook_auth</td>
    </tr>

    <tr>
      <th>Django Version:</th>
      <td>1.7</td>
    </tr>

    <tr>
      <th>Exception Type:</th>
      <td>IndentationError</td>
    </tr>


    <tr>
      <th>Exception Value:</th>
      <td><pre>unexpected unindent (views.py, line 109)</pre></td>
    </tr>


    <tr>
      <th>Exception Location:</th>
      <td>/app/hellobot/urls.py in &lt;module&gt;, line 3</td>
    </tr>

    <tr>
      <th>Python Executable:</th>
      <td>/app/.heroku/python/bin/python</td>
    </tr>
    <tr>
      <th>Python Version:</th>
      <td>2.7.12</td>
    </tr>
    <tr>
      <th>Python Path:</th>
      <td><pre>[&#39;/app&#39;,
 &#39;/app/.heroku/python/bin&#39;,
 &#39;/app&#39;,
 &#39;/app/.heroku/python/lib/python27.zip&#39;,
 &#39;/app/.heroku/python/lib/python2.7&#39;,
 &#39;/app/.heroku/python/lib/python2.7/plat-linux2&#39;,
 &#39;/app/.heroku/python/lib/python2.7/lib-tk&#39;,
 &#39;/app/.heroku/python/lib/python2.7/lib-old&#39;,
 &#39;/app/.heroku/python/lib/python2.7/lib-dynload&#39;,
 &#39;/app/.heroku/python/lib/python2.7/site-packages&#39;,
 &#39;/app/.heroku/python/lib/python2.7/site-packages/setuptools-25.2.0-py2.7.egg&#39;,
 &#39;/app/.heroku/python/lib/python2.7/site-packages/pip-8.1.2-py2.7.egg&#39;]</pre></td>
    </tr>
    <tr>
      <th>Server time:</th>
      <td>Tue, 11 Oct 2016 18:14:30 +0000</td>
    </tr>
  </table>
</div>




<div id="traceback">
  <h2>Traceback <span class="commands"><a href="#" onclick="return switchPastebinFriendly(this);">Switch to copy-and-paste view</a></span></h2>
  
  <div id="browserTraceback">
    <ul class="traceback">
      
        <li class="frame django">
          <code>/app/.heroku/python/lib/python2.7/site-packages/django/core/handlers/base.py</code> in <code>get_response</code>

          
            <div class="context" id="c140598814242072">
              
                <ol start="80" class="pre-context" id="pre140598814242072"><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>        urlconf = settings.ROOT_URLCONF</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>        urlresolvers.set_urlconf(urlconf)</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>        resolver = urlresolvers.RegexURLResolver(r&#39;^/&#39;, urlconf)</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>        try:</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>            response = None</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>            # Apply request middleware</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>            for middleware_method in self._request_middleware:</pre></li></ol>
              
              <ol start="87" class="context-line"><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>                response = middleware_method(request)</pre> <span>...</span></li></ol>
              
                <ol start='88' class="post-context" id="post140598814242072"><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>                if response:</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>                    break</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre></pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>            if response is None:</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>                if hasattr(request, &#39;urlconf&#39;):</pre></li><li onclick="toggle('pre140598814242072', 'post140598814242072')"><pre>                    # Reset url resolver with a custom urlconf.</pre></li></ol>
              
            </div>
          

          
            <div class="commands">
                
                    <a href="#" onclick="return varToggle(this, '140598814242072')"><span>&#x25b6;</span> Local vars</a>
                
            </div>
            <table class="vars" id="v140598814242072">
              <thead>
                <tr>
                  <th>Variable</th>
                  <th>Value</th>
                </tr>
              </thead>
              <tbody>
                
                  <tr>
                    <td>response</td>
                    <td class="code"><pre>None</pre></td>
                  </tr>
                
                  <tr>
                    <td>resolver</td>
                    <td class="code"><pre>&lt;RegexURLResolver &#39;hellobot.urls&#39; (None:None) ^/&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>self</td>
                    <td class="code"><pre>&lt;django.core.handlers.wsgi.WSGIHandler object at 0x7fdfb77e8550&gt;</pre></td>
                  </tr>
                
                  <tr>
                    <td>urlconf</td>
                    <td class="code"><pre>&#39;hellobot.urls&#39;</pre></td>
                  </tr>
                
                  <tr>
                    <td>request</td>
                    <td class="code"><pre>&quot;&lt;WSGIRequest\npath:/facebook_auth,\nGET:&lt;QueryDict: {}&gt;,\nPOST:&lt;QueryDict: {}&gt;,\nCOOKIES:{},\nMETA:{&#39;CONTENT_LENGTH&#39;: &#39;274&#39;,\n &#39;CONTENT_TYPE&#39;: &#39;application/json&#39;,\n &#39;HTTP_ACCEPT&#39;: &#39;*/*&#39;,\n &#39;HTTP_CONNECTION&#39;: &#39;close&#39;,\n &#39;HTTP_CONNECT_TIME&#39;: &#39;0&#39;,\n &#39;HTTP_HOST&#39;: &#39;thawing-sands-52537.herokuapp.com&#39;,\n &#39;HTTP_TOTAL_ROUTE_TIME&#39;: &#39;0&#39;,\n &#39;HTTP_USER_AGENT&#39;: &#39;curl/7.47.0&#39;,\n &#39;HTTP_VIA&#39;: &#39;1.1 vegur&#39;,\n &#39;HTTP_X_FORWARDED_FOR&#39;: &#39;45.127.232.16&#39;,\n &#39;HTTP_X_FORWARDED_PORT&#39;: &#39;443&#39;,\n &#39;HTTP_X_FORWARDED_PROTO&#39;: &#39;https&#39;,\n &#39;HTTP_X_REQUEST_ID&#39;: &#39;2d9822cc-53d9-4abc-a2c0-f5e638efbfa4&#39;,\n &#39;HTTP_X_REQUEST_START&#39;: &#39;1476209670211&#39;,\n &#39;PATH_INFO&#39;: u&#39;/facebook_auth&#39;,\n &#39;QUERY_STRING&#39;: &#39;&#39;,\n &#39;RAW_URI&#39;: &#39;/facebook_auth&#39;,\n &#39;REMOTE_ADDR&#39;: &#39;10.179.164.130&#39;,\n &#39;REMOTE_PORT&#39;: &#39;11545&#39;,\n &#39;REQUEST_METHOD&#39;: &#39;POST&#39;,\n &#39;SCRIPT_NAME&#39;: u&#39;&#39;,\n &#39;SERVER_NAME&#39;: &#39;0.0.0.0&#39;,\n &#39;SERVER_PORT&#39;: &#39;28653&#39;,\n &#39;SERVER_PROTOCOL&#39;: &#39;HTTP/1.1&#39;,\n &#39;SERVER_SOFTWARE&#39;: &#39;gunicorn/19.6.0&#39;,\n &#39;gunicorn.socket&#39;: &lt;socket._socketobject object at 0x7fdfb66afb40&gt;,\n &#39;wsgi.errors&#39;: &lt;gunicorn.http.wsgi.WSGIErrorsWrapper object at 0x7fdfb6617050&gt;,\n &#39;wsgi.file_wrapper&#39;: &lt;class &#39;gunicorn.http.wsgi.FileWrapper&#39;&gt;,\n &#39;wsgi.input&#39;: &lt;gunicorn.http.body.Body object at 0x7fdfb6617250&gt;,\n &#39;wsgi.multiprocess&#39;: True,\n &#39;wsgi.multithread&#39;: False,\n &#39;wsgi.run_once&#39;: False,\n &#39;wsgi.url_scheme&#39;: &#39;https&#39;,\n &#39;wsgi.version&#39;: (1, 0)}&gt;&quot;</pre></td>
                  </tr>
                
                  <tr>
                    <td>middleware_method</td>
                    <td class="code"><pre>&lt;bound method CommonMiddleware.process_request of &lt;django.middleware.common.CommonMiddleware object at 0x7fdfb6a0acd0&gt;&gt;</pre></td>
                  </tr>
                
              