import urllib.request


def get_data(tik, page):
    print(tik)
    print(page)

    url_0 = 'http://regi.zju.edu.cn/redir.php?catalog_id=6&cmd=learning&tikubh='
    url_1 = '&page='

    try:
        response = urllib.request.urlopen(url_0+tik+url_1+str(page+1)).read()
    except:
        response = getdata(tik, page)

    return response


def main():
    tikubh = [1436, 1467, 1471, 1484, 1485, 1486]
    max_pages = [77, 37, 82, 27, 19, 12]
    tikubh = list(map(str, tikubh))

    file = open('question.html', 'wb')

    for idx, tik in enumerate(tikubh):
        for page in range(max_pages[idx]):
            response = get_data(tik, page)
            file.write(response)

    file.close()


if __name__ == '__main__':
    main()
