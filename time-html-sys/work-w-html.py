import html

html.escape("This HTML fragment contains a <script>script</script> tag.")
#  escape parses all the html formatted to harmless strings
# encoding to HTML5
html.unescape("I &hearts; Python's &lt;standard library&gt;.")
#coverts editted strings to html5 currently.
#encoding from html5
