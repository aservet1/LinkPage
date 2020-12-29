from sys import argv

'''----------------------------------------------------------------------'''

def make_html_list(data,i):
	htmlcode = list()

	htmlcode.append("<ul>")

	data = [ d.strip() for d in data.split('\n') ]
	title = data[0]
	items = list()
	for d in data[1:]:
		if d.strip() == '': continue
		if '::' in d:
			d = d.split('::')
			name = d[0]
			link = d[1]
			items.append(f"<b><a href=\'{link}\'>{name}</a></b>")
		else: items.append(d.strip())
	htmlcode.append(f"<h4 id=\"{i}\">{title}</h4>")
	htmlcode.append("<ul>")
	for i in items:
		htmlcode.append(f"<li>{i}</li>")
	htmlcode.append("</ul>")

	htmlcode.append("</ul>")

	return htmlcode

'''----------------------------------------------------------------------'''

def generate_top_menu_nav(data):

	titles = [ x.split()[0] for x in [ d.split('\n')[0] for d in data ] ]
	titles = [ f"<a href=#{i}>{titles[i]}</a>" for i in range(len(titles)) ]
	return "<b>" + ' |::| '.join(titles) + "</b>"

def generate_htmlcode(data):

	data = [ d.strip() for d in data.split('<$>') ]
	data = list(filter(lambda x : x != '', data))
	title = data[0]
	data = data[1:]

	htmlcode = list()

	htmlcode.append("<html>\n<body>")
	htmlcode.append(f"<link rel=\"stylesheet\" href={argv[1].replace('.source','.css')}>")

	htmlcode.append(f"<div style=\"text-align:center\">{generate_top_menu_nav(data)}</div>")
	htmlcode.append(f"<h2>{title}</h2>")
	for i in range(len(data)):
		htmlcode.append("<hr>")
		htmlcode.extend(make_html_list(data[i],i))
	htmlcode.append("</body>\n</html>")

	return htmlcode

'''----------------------------------------------------------------------'''

def write_to_file(htmlcode, htmlfile):
	with open(htmlfile,'w') as fh:
		fh.write('\n'.join(htmlcode))

'''----------------------------------------------------------------------'''

sourcefile = argv[1]
htmlfile = sourcefile.replace('.source','.html')

src = open(sourcefile,'r'); data = src.read(); src.close()
htmlcode = generate_htmlcode(data)
write_to_file(htmlcode, htmlfile)
