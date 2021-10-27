# Sanitizy
This is a simple and very light weight python package to help securing python web applications in general especially Falsk apps since they lack security !!

# Usage:

<h3> XSS:</h3>
<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">import sanitizy
<br>sanitizy.XSS.escape('&lt;h1&gt;')# produces: '&#x26;lt;h1&#x26;gt;' : </pre></div>
<h3> SQL-Injection:</h3>
<div style="background: #f8f8f8; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">import sanitizy
<br>sanitizy.SQLI.escape("' or 1=1 or '")# produces: '"\\' or 1=1 or \\'"' : </pre></div>
