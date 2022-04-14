from googleapiclient.discovery import build
import os
import json

GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']
CX_ID= os.environ['CX_ID']

def google_maps_search(query):
    page = 1
    start = (page - 1) * 10 + 1

    print(page)
    # service = build("customsearch", "v1", developerKey=GOOGLE_API_KEY)
    # res = service.cse().list(q=query, cx=CX_ID, gl=us, start=start).execute()

    f = open('res.json', 'r')
    data = json.load(f)


    res = data['items']
    return res


if __name__ == '__main__':

    queries = ['some', 'random', 'queries']
    start = 1
    for i in queries:
        res = google_maps_search(i)

        for item in res:
            title = item['title']
            maps_link = item['link']
            full_address = item['pagemap']['metatags'][0]['og:site_name']

            save_path = '/Users/ingari/Desktop/DESKTOP/Google-Search-API/'
            name_of_file = i

            completeName = os.path.join(save_path, name_of_file+".txt")   
            if not os.path.exists(completeName):
                open(completeName, 'w').close()
            file = open(completeName, "a")  

            file.write(" -------------- \n Result : " + str(start) + " \n Title: " + title + "\n Maps Link: " + maps_link + "\n Full Address: " + full_address + "\n -------------- \n")
            file.close()
            start += 1



  