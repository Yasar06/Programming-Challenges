import urllib.request

url = "https://www.officialcharts.com/charts/singles-chart"

def scrape(url):
    fp = urllib.request.urlopen(url)
    mybytes = fp.read()
    mystr = mybytes.decode("utf8")
    fp.close()
    return mystr

def pos_finder(newstring):
    pos_lookingfor = '"position">'
    pos_start = newstring.find(pos_lookingfor)
    pos_end = newstring.find('</', pos_start)
    return (newstring[pos_start+len(pos_lookingfor):pos_end])

def name_finder(newstring):
    name_lookingfor = newstring.find('<a href')
    name_start = newstring.find('/">', name_lookingfor)
    name_end = newstring.find("</a>",name_start)
    return (newstring[name_start+3:name_end])

def artist_finder(newstring):
    artist_lookingfor = newstring.find('<div class="artist">')
    artist_start = newstring.find('/">', artist_lookingfor)
    artist_end = newstring.find("</a>", artist_start)
    return (newstring[artist_start+3:artist_end])

def table():
    i = 0
    num = 0
    print(f'{"Position:"}{"Name:":>31}{"Artist:":>43}')
    while num != 10:
        open_tr = html.find('<tr>', i)
        close_tr = html.find("</tr>", open_tr)
            
        newstring = html[open_tr:close_tr]

        pos = pos_finder(newstring)
        name = name_finder(newstring)
        artist = artist_finder(newstring)
        
        print(f'{pos:35}{name:40}{artist:80}')

        i = close_tr
        num += 1
        
        
      
if __name__ == "__main__":
    html = scrape(url)
    table()
