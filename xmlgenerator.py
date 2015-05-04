plik = open('listaludzi', 'r')
xml = open('listaludzi.xml', 'w')

xml.write('<?xml version="1.0"?> \n')
xml.write("<data> \n")

pole = { 0: "person", 1:"name", 2:'surname', 3:'sex', 4:'dateofbirth', 5:'number'}

for i in range(50):
    xml.write(4*' '+'<osoba id="'+str(i)+'"> \n')
    for w in range(1,5):
        xml.write(8*' '+'<'+pole[w]+'>'+plik.readline().rstrip('\n')+'</'+pole[w]+'>\n')
    for w in range(int(plik.readline().rstrip('\n'))):
        xml.write(8*' '+'<'+pole[5]+'>'+plik.readline().rstrip('\n')+'</'+pole[5]+'>\n')
    plik.readline()
    xml.write(4*' '+"</osoba> \n")




xml.write("</data>")
xml.close()
plik.close()
