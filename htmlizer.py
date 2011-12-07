#This is a project from Patrick Morgan.

import urllib

head = """
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html>
    <head>
    <title>Python-Generated Website</title>
    """
body = """
    </head>
    <body>
    """
bodyend = """
    </body>
    </html>
    """
begin = '<h2>Problem'
finish = '</div><br />'

def callpages(start, stop):
    content = ""
    for page in range(start, stop+1):
        loaded_page = urllib.urlopen("http://projecteuler.net/index.php?section=problems&id=%d" % page)
        source = loaded_page.read()
        #print source[:100]
        content += finder(begin, finish, source)
    document = file('webpage.html', 'w')
    document.write(pagebuild(content=content))



def pagebuild(head=head,metacontent="",body=body,content="",bodyend=bodyend):
    page = head + metacontent + body + content + bodyend
    return page

def finder(start, end, source):
    index = 0
    while start != source[index:index+len(start)]:
        index += 1
        if start == source[index:index+len(start)]:
            x = index

    #hacky section to skip over one divider
    while '</p>' != source[index:index+len('</p>')]:
        index += 1

            
    while end != source[index:index+len(end)]:
        index += 1
        if end == source[index:index+len(end)]:
            y = index
    return source[x:y]

callpages(23,50)
#just give it a start and end problem


