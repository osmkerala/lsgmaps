import urllib.request as urllib2
import csv
def main():
    with open('bpdpid.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(str(row[0]))
            download_file(str(row[0]))


def download_file(download_url):
    url="http://sec.kerala.gov.in/images/maps/"
    response = urllib2.urlopen(url+download_url+".pdf")
    file = open(download_url+".pdf", 'wb')
    file.write(response.read())
    file.close()
    print("Completed")

if __name__ == "__main__":
    main()
