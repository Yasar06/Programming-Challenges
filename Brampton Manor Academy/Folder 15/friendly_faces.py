import csv
import codecs

def read_csv(path):
    with open(path) as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        csv_contents = []
        for row in csv_reader:
            csv_contents += row

    return csv_contents

def read_html(path):
    file = codecs.open(path, "r", "utf-8")
    contents = file.read()
    return contents

def process(csv, html):

    i = 0
    j = 0
    k = 0
    counter = 0
    newhtml = html
    while counter != 5:

        link_start = html.find("link",i)
        link_end = html.find('"',link_start)
        url = csv[counter*3]
        newhtml = newhtml.replace(html[link_start:link_end], url)
        

        initials_start = html.find("initials",j)
        initials_end = html.find("<",initials_start)
        initials = csv[counter*3+1]
        newhtml = newhtml.replace(html[initials_start:initials_end], initials)
        
        name_start = html.find("name",k)
        name_end = html.find("<",name_start)
        name = csv[counter*3+2]
        newhtml = newhtml.replace(html[name_start:name_end], name)
        
        i = link_end
        j = initials_end
        k = name_end
        counter+=1
    
    return newhtml

def write_html(path,html):
    html_writer = open(path,"w")
    html_writer.write(html)
    html_writer.close()

if __name__ == "__main__":
    csv = read_csv(path="south.csv")
    html = read_html(path="south.html")
    html = process(csv=csv, html=html)
    write_html(path="south_final.html", html=html)
