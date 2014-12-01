'''
Created on Nov 23, 2014

@author: dth1v_000
'''
import networkx as nx
import re
import urllib.request
from htmldom import htmldom
from _overlapped import NULL
class PhpCallGraph(object):
    '''
    classdocs
    '''
    inputVariables = ["$_POST", "$_GET", "$_REQUEST", "$_FILES", "$_COOKIE"]

    def __init__(self, callGraphFile = "", calledByGraphFile = "", initialPath = ""):

        #Build The Call Graph
        self.inputFunctions = {}
        if (not callGraphFile == ""):
            
            fd = open(callGraphFile, 'r')
            data = fd.read()
            fd.close()   
            
            self.callGraph, self.callGraphFunctionsUrl = self.getCallGraph(data)               
            for function in self.callGraphFunctionsUrl.keys():
                inputs = self.getInputVariables(function, self.callGraphFunctionsUrl[function], initialPath)          
                if (len(inputs) > 0):
                    self.inputFunctions[function] = inputs
        
        #Build The Called By Graph            
        if (not calledByGraphFile == ""):
            fd = open(calledByGraphFile, 'r')
            data = fd.read()
            fd.close()   
            self.calledByGraph, self.calledByGraphFunctionUrl = self.getCallGraph(data)
            for function in self.calledByGraphFunctionUrl.keys():
                inputs = self.getInputVariables(function, self.calledByGraphFunctionUrl[function], initialPath)          
                if (len(inputs) > 0):
                    self.inputFunctions[function] = inputs
                    
        
                    
    def getCallGraph(self, data):
        nodeStrList = re.findall(r'Node\d*\s\[label=".*[;]', data)
        functions = {}
        functionsUrl = {}
        for line in nodeStrList:
            
            nodeIndex = re.search(r'Node(\d*) ', line)
            nodeName = re.search(r'label="(.*?)"',line)
            nodeUrl = re.search(r'URL="\$(.*?)"\]', line)
                    
            if nodeIndex and nodeName:
                name = nodeName.group(1).replace("\\l\\\\", "\\").replace("\\\\","\\").replace("\\\\","\\")
                
                if (nodeIndex.group(1) == "1"):
                    self.firstNode = name
                    print(self.firstNode)
                
                
                functions[nodeIndex.group(1)] = name
                
                if (nodeUrl):
                    functionsUrl[name] = nodeUrl.group(1)
                   
        G = nx.DiGraph()
        for key in functions.keys():
            G.add_node(functions[key])
                  
        nodePathStrList = re.findall(r'Node\d*\s[-][>]\s[N][o][d][e]\d{1,3}', data)
                    
        for line in nodePathStrList:
            nodeIndex1 = re.search('Node(\d*) ->', line)
            nodeIndex2 = re.search('-> Node(\d*)', line)
                  
            G.add_edge(functions[nodeIndex2.group(1)], functions[nodeIndex1.group(1)])
            
        return G, functionsUrl
        
    def getInputVariables(self, function = "", urlStr = "", initialPath = ""):   
        resultInputs = []     
        url = urlStr.split("#")
        response = urllib.request.urlopen(initialPath + url[0])
        html = response.read()        
        dom = htmldom.HtmlDom().createDom(str(html))
        element = dom.find("a#" + url[1]).next("div.memitem")
        elementHtml = element.html().replace("\n","")
        
        codeLines = re.findall(r'<div class="line">(.*?)</div?', elementHtml)
        
        elementStr = ""
        for codeLine in codeLines:   
            elementStr +=  codeLine + "\n"

        for inputVariable in PhpCallGraph.inputVariables:
            if (elementStr.find(inputVariable) != -1):
                resultInputs.append(inputVariable)
                
        
        return resultInputs
   
    def printShortestPathLenFromInput(self):
        for inputFunction in self.inputFunctions.keys():   
            if (self.callGraph.has_node(inputFunction)):     
                print(nx.shortest_path(self.callGraph, inputFunction, self.firstNode), nx.shortest_path_length(self.callGraph, inputFunction, self.firstNode))
            if (self.calledByGraph.has_node(inputFunction)):     
                print(nx.shortest_path(self.calledByGraph, inputFunction, self.firstNode), nx.shortest_path_length(self.calledByGraph, inputFunction, self.firstNode))
        
    def getInputFunctions(self):
        return self.inputFunctions;
    
    def getFunctionsUrl(self):
        return self.callGraphFunctionsUrl
    
    def getGraph(self):
        return self.callGraph