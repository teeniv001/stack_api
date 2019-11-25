import requests
from bs4 import BeautifulSoup
import json

res = requests.get("https://stackoverflow.com/questions")

#print (res.text)

soup = BeautifulSoup(res.text,"html.parser")
#print (soup)

questions_data = {
    "questions" : [] 
}
questions = soup.select(".question-summary")
#print (questions[2].select_one(".question-hyperlink").getText())

for que in questions:
    q = que.select_one(".question-hyperlink").getText()
    vote_count = que.select_one(".vote-count-post").getText()
    views = que.select_one(".views").attrs['title']
    #print (views)
    questions_data['questions'].append({
        "questions" : q,
        "views" : views,
        "vote_count" : vote_count
    })

json_data = json.dumps(questions_data,indent=4)
print (json_data)