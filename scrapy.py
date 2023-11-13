import requests
from bs4 import BeautifulSoup

cookies = {
    'l': '20',
    'p': '1',
    '_gid': 'GA1.3.1073689595.1699700228',
    'mode': 'r',
    'mail_addr': 'on',
    '_ga_CGYCXWR546': 'GS1.1.1699712707.4.1.1699712707.0.0.0',
    '_ga': 'GA1.1.1078906806.1699700228',
}

headers = {
    'authority': 'riss.ipa.go.jp',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # 'cookie': 'l=20; p=1; _gid=GA1.3.1073689595.1699700228; mode=r; mail_addr=on; _ga_CGYCXWR546=GS1.1.1699712707.4.1.1699712707.0.0.0; _ga=GA1.1.1078906806.1699700228',
    'pragma': 'no-cache',
    'referer': 'https://riss.ipa.go.jp/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}


def getInfo(ddNumber):
    params = {
        'r': '%06d' % ddNumber,
    }

    try:
        response = requests.get('https://riss.ipa.go.jp/r', params=params, cookies=cookies, headers=headers, timeout=0.01)
        response.raise_for_status()
    except requests.exceptions.ConnectionError as e:
        print("Connection error occurred.", e)
        return ''
    except requests.exceptions.Timeout as e:
        print("Timeout occurred.", e)
        return ''
    except requests.exceptions.RequestException as e:
        print("Request exception occurred.", e)
        return ''
    except requests.exceptions.HTTPError as e:
        print("HTTP Error occurred.", e)
        return ''
    except ValueError as e:
        print("Response value error occurred.", e)
        return ''

    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')

    name = "body > div.detail-wrap > dl > dd:nth-child(6)"
    dNo = "body > div.detail-wrap > dl > dd:nth-child(2)"
    content = "body > div.detail-wrap > dl > dd:nth-child(38)"

    a = soup.select(name)
    b = soup.select(dNo)
    c = soup.select(content)

    staffInfo = f'{ddNumber:06}, {a[0].text if len(a) > 0 else ""}, {b[0].text if len(b) > 0 else ""}, {c[0].text if len(c) > 0 else ""}\n'

    return staffInfo


def main():
    MAX_NUMBER = 27018
    result = ''
    for i in range(MAX_NUMBER):
        txt = getInfo(i + 1)
        if not txt.isspace():
            result += txt

        if i % 1000 == 0: print(f'Processing {i}...')

    if not result.isspace():
        fo = open("./scrapy.txt", 'w', encoding="utf-8")
        fo.write(result)
        fo.close()


if __name__ == '__main__':
    main()
