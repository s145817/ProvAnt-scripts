import csv
import pyperclip

with open(r'C:\Users\PAUBOJE\OneDrive - Provincie Antwerpen\Python\Python-SSH\CP-URL\lijst.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        # Aangezien er maar één kolom is, printen we het eerste element
        var = (f'dst:"{row[0]}"\n')
        print(var)

        pyperclip.copy(var)
        vraag = input("Druk op Enter voor de volgende rij... q voor Quit\n")
        if vraag == "q" or vraag == "Q":
            break
        else:
            continue


