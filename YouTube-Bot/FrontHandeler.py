import json

def jsonFileReader():
    with open('demo.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        items = data.get('items', [])
        dataPrinter(items, data)
        # if items:
        # title = items[0]['snippet'].get('title')
        # if title:
        #     print(print_bold(title))
        # else:
        #     print("Title not found.")
        # else:
        #     print("No items found in the JSON file.")

def dataPrinter(items, data):
    title = items[0]['snippet'].get('title')
    description = items[0]['snippet'].get('description')
    count = 1
    if title:
        for item in data['items']:
            title = item['snippet']['title']
            print(print_bold(title, True, count))
            if description:
                description = item['snippet']['description']
                print(print_bold(description, False, count) + "\n")
                count += 1

            else:
                print("Description Not Found")
    else:
        print("Title not found.")




def print_bold(text, isText, count):
    if isText == True:
        bold_text = "\033[1m" + f"{count}. Title:- " + text + "\033[0m"
        return bold_text

    else:
        bold_text = "Description:- " + text
        return bold_text
def main():
    jsonFileReader()

if __name__ == "__main__":
    main()
