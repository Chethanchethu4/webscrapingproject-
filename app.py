import requests
from bs4 import BeautifulSoup

#URL="https://www.amazon.in/realme-Space-Purple-Storage-Medium/dp/B09G6D3QMF/ref=sr_1_24?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&qsid=262-5865631-5293367&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-24&sres=B099SJHHQL%2CB09FKDB27R%2CB09FKDH6FS%2CB09FK8MBMJ%2CB09FKD67CS%2CB099SF5X1W%2CB09FKGDJNC%2CB09G69ZB2B%2CB09DY6NWPK%2CB09FY5N6Q1%2CB094Y495LQ%2CB0999NNBPV%2CB08LZH4FYQ%2CB091GDFM2W%2CB07XMFDHSG%2CB08G28Z33M%2CB081ZD3BZS%2CB097KM3Z16%2CB0913H9RFQ%2CB08225158Y&srpt=CELLULAR_PHONE"
#URL="https://www.amazon.in/Samsung-Galaxy-Blue-128GB-Storage/dp/B09CGJFY5N/ref=sr_1_14_sspa?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-14-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUxFUUVHM1VEMEFWJmVuY3J5cHRlZElkPUEwNjU2MDYwWjdQRE80WjJZUzNXJmVuY3J5cHRlZEFkSWQ9QTA0MDM0MzcxN0UwUlBZRTJOMjdLJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
#URL="https://www.amazon.in/realme-narzo-Racing-128GB-Storage/dp/B099SJHHQL/ref=sr_1_1?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&qsid=262-5865631-5293367&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-1&sres=B099SJHHQL%2CB09FKDB27R%2CB09FKDH6FS%2CB09FK8MBMJ%2CB09FKD67CS%2CB099SF5X1W%2CB09FKGDJNC%2CB09G69ZB2B%2CB09DY6NWPK%2CB09FY5N6Q1%2CB094Y495LQ%2CB0999NNBPV%2CB08LZH4FYQ%2CB091GDFM2W%2CB07XMFDHSG%2CB08G28Z33M%2CB081ZD3BZS%2CB097KM3Z16%2CB0913H9RFQ%2CB08225158Y&srpt=CELLULAR_PHONE"
#URL="https://www.amazon.in/Samsung-Galaxy-Slate-Black-Storage/dp/B09CGLRLYM/ref=sr_1_1_sspa?crid=1Z0WLGCWQWA65&keywords=samsung&qid=1636185340&s=electronics&sprefix=samsu%2Celectronics%2C452&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOEZWMU0xQU1YQ01FJmVuY3J5cHRlZElkPUEwMTk3ODc5UlpDRDJaVFNJMEJYJmVuY3J5cHRlZEFkSWQ9QTA0MzIwNzJMRlFSS0VWTU9UUVImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"
#URL="https://www.amazon.in/Realme-Cyber-Black-128GB-Storage/dp/B0913H9RFQ/ref=sr_1_22?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&qsid=262-5865631-5293367&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-22&sres=B099SJHHQL%2CB09FKDB27R%2CB09FKDH6FS%2CB09FK8MBMJ%2CB09FKD67CS%2CB099SF5X1W%2CB09FKGDJNC%2CB09G69ZB2B%2CB09DY6NWPK%2CB09FY5N6Q1%2CB094Y495LQ%2CB0999NNBPV%2CB08LZH4FYQ%2CB091GDFM2W%2CB07XMFDHSG%2CB08G28Z33M%2CB081ZD3BZS%2CB097KM3Z16%2CB0913H9RFQ%2CB08225158Y&srpt=CELLULAR_PHONE"

product_to_track = [
    {
            "product_URL":"https://www.amazon.in/realme-Space-Purple-Storage-Medium/dp/B09G6D3QMF/ref=sr_1_24?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&qsid=262-5865631-5293367&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-24&sres=B099SJHHQL%2CB09FKDB27R%2CB09FKDH6FS%2CB09FK8MBMJ%2CB09FKD67CS%2CB099SF5X1W%2CB09FKGDJNC%2CB09G69ZB2B%2CB09DY6NWPK%2CB09FY5N6Q1%2CB094Y495LQ%2CB0999NNBPV%2CB08LZH4FYQ%2CB091GDFM2W%2CB07XMFDHSG%2CB08G28Z33M%2CB081ZD3BZS%2CB097KM3Z16%2CB0913H9RFQ%2CB08225158Y&srpt=CELLULAR_PHONE",
            "name":"mobile_one",
            "target_price":15000
    },
    {
            "product_URL":"https://www.amazon.in/Samsung-Galaxy-Blue-128GB-Storage/dp/B09CGJFY5N/ref=sr_1_14_sspa?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-14-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExQUxFUUVHM1VEMEFWJmVuY3J5cHRlZElkPUEwNjU2MDYwWjdQRE80WjJZUzNXJmVuY3J5cHRlZEFkSWQ9QTA0MDM0MzcxN0UwUlBZRTJOMjdLJndpZGdldE5hbWU9c3BfbXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==",
            "name":"mobile_two",
            "target_price": 15000
    },
    {
            "product_URL":"https://www.amazon.in/realme-narzo-Racing-128GB-Storage/dp/B099SJHHQL/ref=sr_1_1?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&qsid=262-5865631-5293367&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-1&sres=B099SJHHQL%2CB09FKDB27R%2CB09FKDH6FS%2CB09FK8MBMJ%2CB09FKD67CS%2CB099SF5X1W%2CB09FKGDJNC%2CB09G69ZB2B%2CB09DY6NWPK%2CB09FY5N6Q1%2CB094Y495LQ%2CB0999NNBPV%2CB08LZH4FYQ%2CB091GDFM2W%2CB07XMFDHSG%2CB08G28Z33M%2CB081ZD3BZS%2CB097KM3Z16%2CB0913H9RFQ%2CB08225158Y&srpt=CELLULAR_PHONE",
            "name":"mobile_three",
            "target_price": 15000
    },
    {
            "product_URL":"https://www.amazon.in/Samsung-Galaxy-Slate-Black-Storage/dp/B09CGLRLYM/ref=sr_1_1_sspa?crid=1Z0WLGCWQWA65&keywords=samsung&qid=1636185340&s=electronics&sprefix=samsu%2Celectronics%2C452&sr=1-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOEZWMU0xQU1YQ01FJmVuY3J5cHRlZElkPUEwMTk3ODc5UlpDRDJaVFNJMEJYJmVuY3J5cHRlZEFkSWQ9QTA0MzIwNzJMRlFSS0VWTU9UUVImd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl",
            "name":"mobile_four",
            "target_price": 15000
    },
    {
            "product_URL":"https://www.amazon.in/Realme-Cyber-Black-128GB-Storage/dp/B0913H9RFQ/ref=sr_1_22?crid=9Y5D7ZD88AGN&keywords=realme&qid=1636185310&qsid=262-5865631-5293367&s=electronics&sprefix=rea%2Celectronics%2C354&sr=1-22&sres=B099SJHHQL%2CB09FKDB27R%2CB09FKDH6FS%2CB09FK8MBMJ%2CB09FKD67CS%2CB099SF5X1W%2CB09FKGDJNC%2CB09G69ZB2B%2CB09DY6NWPK%2CB09FY5N6Q1%2CB094Y495LQ%2CB0999NNBPV%2CB08LZH4FYQ%2CB091GDFM2W%2CB07XMFDHSG%2CB08G28Z33M%2CB081ZD3BZS%2CB097KM3Z16%2CB0913H9RFQ%2CB08225158Y&srpt=CELLULAR_PHONE",
            "name":"mobile_five",
            "target_price": 15000
    }
]
def give_product_price(URL):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(id="priceblock_ourprice")
    if (product_price == None):
        product_price = soup.find(id="priceblock_outprice")

    return product_price.getText()

result_file = open('my_result_file','w')

try:
    for every_product in product_to_track:
        product_price_return = give_product_price(every_product.get("product_URL"))
        print(product_price_return + "-" + every_product.get("name"))

        my_product_price = product_price_return[1:]
        my_product_price = my_product_price.replace(",", '')
        my_product_price = int(float(my_product_price))

        print(my_product_price)
        if my_product_price < every_product.get("target_price"):
            print("available at your required price")
            result_file.write(every_product.get("name") + '- \t' + 'available at target price' + 'current price-' + str(my_product_price)+ '\n')

        else:
            print("still at current price")

finally:
    result_file.close()

