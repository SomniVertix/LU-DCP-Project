import requests

## 2015 - 2016 : https://www.liberty.edu/media/1270/dcps/1516/
## 2016 - 2019 : https://www.liberty.edu/media/1270/
base_url = "https://www.liberty.edu/media/1270/"
pdf = '.pdf'
def download_pdf(my_url, file_name):
    r = requests.get(my_url, stream=True)
    with open('PDF/DCP 2018 - 2019/' + file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024): 
                if chunk:
                    f.write(chunk)

with open("2018 - 2019 PDF.txt", 'r') as pdf_list:
    lines = pdf_list.readlines()
    for line in lines:
        if pdf in line:
            index = line.index('.pdf') + 4
            file_name = line[0:index]
            my_url = base_url + file_name
            download_pdf(my_url, file_name)