from flask import Flask, request
import requests
import json
from bs4 import BeautifulSoup as bs
app = Flask(__name__)

@app.route('/api/v1/uva',  methods=["GET"])
def uvasolvecout():
    req_data = request.get_json()

    usernameReq = requests.get('https://uhunt.onlinejudge.org/api/uname2uid/'+str(req_data['username']))
    userId = usernameReq.text

    allSubmission = requests.get('https://uhunt.onlinejudge.org/api/subs-user/'+str(userId))
    submissionList = allSubmission.json()['subs']
    count = 0
    mapProblemId = {}
    for submission in submissionList:
        
        try:
            if(submission[2]==90):
                try:
                    if(mapProblemId[submission[1]] == True):
                        pass
                    else:
                        pass
                except:
                    count+=1
                mapProblemId[submission[1]] = True
            else:
                pass
        except:
            pass
        
    print(count)
    return {"Totall AC": count}

@app.route('/api/v1/cf',  methods=["GET"])
def codeforcessolvecout():
    req_data = request.get_json()

    allSubmission = requests.get('http://codeforces.com/api/user.status?handle='+str(req_data['username']))
    submissionList = allSubmission.json()

    xx = submissionList['result']
    count = 0
    mapProblemId = {}
    for submission in xx:
        try:
            if(submission['verdict']=="OK"):
                try:
                    if(mapProblemId[submission['problem']['name']] == True):
                        pass
                    else:
                        pass
                except:
                    count+=1
                    #print(submission['problem']['name'])
                mapProblemId[submission['problem']['name']] = True
            else:
                pass
        except:
            pass
    print(count)
    return {"Totall AC": count}
    
@app.route('/api/v1/lightoj',  methods=["GET"])
def lightojsolvecout():
    req_data = request.get_json()

    allSubmission = requests.get('https://lightoj.com/user/'+str(req_data['username']))
    soup = bs(allSubmission.content,'html.parser')

    soup = soup.find("div", class_ = "page-counts")
    soup = soup.find_all("span")[0]
    print(soup.text)
    return {"Totall AC": soup.text}


@app.route('/api/v1/uri',  methods=["GET"])
def urisolvecout():
    req_data = request.get_json()

    allSubmission = requests.get('https://www.urionlinejudge.com.br/judge/en/profile/'+str(req_data['username']))
    soup = bs(allSubmission.content,'html.parser')

    soup = soup.find("ul", class_ = "pb-information")
    soup = soup.find_all("li")[5]
    x = str(soup.text).split()

    return {"Totall AC": x[1]}

@app.route('/api/v1/timus',  methods=["GET"])
def timussolvecout():
    req_data = request.get_json()

    allSubmission = requests.get('https://acm.timus.ru/author.aspx?id='+str(req_data['username']))
    soup = bs(allSubmission.content,'html.parser')

    soup = soup.find_all("td", class_ = "author_stats_value")[1]

    x = str(soup.text).split()
    print(x)

    return {"Totall AC": x[0]}


@app.route('/api/v1/spoj',  methods=["GET"])
def spojsolvecout():
    req_data = request.get_json()

    allSubmission = requests.get('https://www.spoj.com/users/'+str(req_data['username']))
    soup = bs(allSubmission.content,'html.parser')

    soup = soup.find_all("dd")[0]

    x = str(soup.text)
    print(soup)

    return {"Totall AC": x}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)