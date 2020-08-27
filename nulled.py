from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request
from urllib.parse import urlparse




def download_files(page):
    headers1 = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.11 (KHTML, like Gecko) '
                              'Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

    reg_url = 'http://www.nulled-scripts.xyz/page/'+str(page)+'/'



    t = urlparse(reg_url)
    if t.path:
        file = t.path.split("/")[2]
    else:
        file = '0'

    req = Request(url=reg_url, headers=headers1)
    html = urlopen(req).read()


    filename = file + ".csv"
    f = open(filename, "w")

    headers = "Category_Name,Title,About,Imag_Src,Demo_link,Download_link\n"
    f.write(headers)

    page_soup = soup(html, "html.parser")
    containers = page_soup.find_all("article")
    for container in containers:
        a = container.find("a")
        catena = container.find("span", {"class": "meta-category"}).text

        # print(catena)
        # exit()
        link = a["href"]
        alt = a["title"]

        page_url = link

        req = Request(url=page_url, headers=headers1)
        htmlpage = urlopen(req).read()

        page_soup_view = soup(htmlpage, "html.parser")
        category = page_soup_view.find("a", {"class": "herald-cat-2"})
        div = page_soup_view.find("div", {"class": "herald-section container"})
        title = div.find("h1", {"class": "entry-title h1"})
        text1 = div.find("div", {"class": "entry-content"})
        categoryname = catena

        titlename = title.text
        about = text1.p.text
        imgsrc = text1.img["src"]
        Allpara = text1.findAll("p")

        demolink = Allpara[1].code.text
        downloadlink = Allpara[2].code.text



        f.write(catena + "," + titlename.replace(",", "|") + "," + 'No Data' + "," + imgsrc.replace(",", "|") + "," + demolink.replace(",", "|") + "," + downloadlink.replace(",", "|") + "\n")
    f.close()

    newpage = int(page)+1
    download_files(newpage)

download_files(2)