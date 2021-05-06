import requests
import re
from bs4 import BeautifulSoup

class SimplePageRank:
    maxpages=0
    def __init__(self, url):
        self.url=url
        self.page_ranks={}
        return

    def startPageRank(self, url='_'):
        if self.maxpages>100:
            return
        print("current ranks", self.page_ranks, "current url", url)
        if url=='_':
            url=self.url
        request=requests.get(self.url)
        if request.ok:
            soup=BeautifulSoup(request.text, 'html.parser')
            urls=[]
            for link in soup.find_all(attrs={'href':re.compile("http")}):
                newurl=link.get('href')
                newurl=newurl.split("?")[0]
                if newurl in self.page_ranks.keys():
                    pass
                else:
                    urls.append(newurl)
            for url in urls:
                if url in self.page_ranks.keys():
                    self.page_ranks[url]+=1
                else:
                    self.page_ranks[url]=1
                self.maxpages+=1
                self.startPageRank(url)
        else:
            if url in self.page_ranks.keys():
                self.page_ranks[url]-=1
        return
    
    def printPageRankInfo(self, ascending=False):
        if self.page_ranks=={}:
            print("\n","Run Page Rank first.")
            return
        print("\nPage Ranks\n")
        if not ascending:
            resultDict=dict(sorted(self.page_ranks.items(), key=lambda item: item[1], reverse=True))
        else:
            resultDict=self.page_ranks
        for i in resultDict:
            print("\n\t",i,"\t\t",resultDict[i])
        return

    def getPageRankInfo(self, ascending=False):
        if self.page_ranks=={}:
            return {}
        if not ascending:
            return dict(sorted(self.page_ranks.items(), key=lambda item: item[1], reverse=True))
        else:
            return self.page_ranks

if __name__=="__main__":
    pagerank=SimplePageRank(input("Enter url: "))
    pagerank.startPageRank()
    pagerank.printPageRankInfo()
