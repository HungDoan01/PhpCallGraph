'''
Created on Nov 21, 2014

@author: dth1v_000
'''
import urllib.request

class FunctionNode(object):
    '''
    classdocs
    '''
    def __init__(self, index, functionName, url):
        self.index = index
        self.functioName = functionName
        self.url = url
        
    def getFunctionName(self):
        return self.functioName
    
    def getInputs(self):
        initialPath = 'file:///C:/CallGraphOutput/3.9/html/'
        inputVariables = ["$_POST", "$_GET", "$_REQUEST", "$_FILES", "$_COOKIE"]
        resultInputs = []
        if (self.url is not ""):
            try:
                url = self.url.split("#")
                response = urllib.request.urlopen(initialPath + url[0])
                html = response.read()
                from htmldom import htmldom
                 
                dom = htmldom.HtmlDom().createDom(str(html))
                element = dom.find("a#" + url[1]).next("div.memitem")
                elementStr = element.html()
                for inputVariable in inputVariables:
                    if (elementStr.find(inputVariable) != -1):
                        resultInputs.append(inputVariable)
            except ValueError:
                print("error")
            
        return resultInputs
            
            
        
        
        