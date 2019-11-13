import requests
from bs4 import BeautifulSoup
import webbrowser
import sys

web_amount = 0

def reduce_list(list_, amount):
    entry = []

    if len(list_) <= amount:
        return list_

    for element in list_:
        if amount > 0:
            entry.append(element)
            amount -= 1
        else:
            break
    
    return entry

def find(target):
    total = 0

    url = "https://google.com/search?q=" + str(target)

    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36"})

    soup = BeautifulSoup(response.content, "lxml")

    links = []

    for div in soup.find_all("div", attrs={"class": "r"}):
        a = div.find("a")

        if a:
            links.append(a.attrs["href"])
            total += 1

    links = reduce_list(links, web_amount)

    num = 0

    print("---------RESULTS:------------")


    for web in links:  
        print("{}) {}".format(num+1, web))
        webbrowser.open(web)

        num += 1 

    print("-----------------------------")

    print(f"Found {num} result(s),\nFound {total} total result(s),\nWebsite Input: {web_amount} (User Input)")

    print("-----------------------------\n")

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            web_amount = int(sys.argv[1])
            target = str(sys.argv[2])

            print("\nFormat: <Input Count> \"<Target>\"")

            if not web_amount <= 0 and target:
                print("\nFinding...\n")

                find(target)

            sys.exit()

        target = str(input("\nTarget: "))
        web_amount = int(input("Input Count: "))

        if not web_amount <= 0 and target:
            print("\nFinding...\n")

            find(target)

        sys.exit()
    except Exception as e:
        print("\nSomething went wrong, please try again!\nError: " + str(e))

