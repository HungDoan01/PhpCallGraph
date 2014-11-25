import re
import networkx as nx
from CallGraph.PhpCallGraph import PhpCallGraph
import urllib.request
from htmldom import htmldom
# import matplotlib.pyplot as plt
 
initialPath = 'file:///C:/CallGraphOutput/3.9/html/'
callGraphObject = PhpCallGraph("cgraph.dot", "icgraph.dot", initialPath)

print(callGraphObject.getInputFunctions())

# var = callGraph.getInputFunctions()
# print(var)
print("done")
# fd = open("icgraph.dot", 'r')
# data = fd.read()
# fd.close()
 
#nodeStrList = re.findall(r'[N][o][d][e]\d*\s\[[l][a][b][e][l][=]["]\w*["]', data)
# nodeStrList = re.findall(r'Node\d*\s\[label="[A-Za-z\\_0-9]*"', data)
# nodeStrList = re.findall(r'Node\d*\s\[label=".*[;]', data)
# functions = {}
# functionsUrl = {}
# for line in nodeStrList:
#     nodeIndex = re.search(r'Node(\d*) ', line)
#     nodeName = re.search(r'label="(.*?)"',line)
#     nodeUrl = re.search(r'URL="\$(.*?)"\]', line)
#             
#     if nodeIndex and nodeName:
#         functions[nodeIndex.group(1)] = nodeName.group(1).replace("\l","").replace("\\\\","\\") 
#         functionsUrl[nodeName.group(1)] = nodeUrl
#            
# G = nx.DiGraph()
# for key in functions.keys():
#     G.add_node(functions[key])
#           
# nodePathStrList = re.findall(r'Node\d*\s[-][>]\s[N][o][d][e]\d{1,3}', data)
#             
# for line in nodePathStrList:
#     nodeIndex1 = re.search('Node(\d*) ->', line)
#     nodeIndex2 = re.search('-> Node(\d*)', line)
#           
#     G.add_edge(functions[nodeIndex2.group(1)], functions[nodeIndex1.group(1)])
    
# for node in G.nodes():
#     inputVariables = node.getInputs()
#     if (len(inputVariables) > 0):
#         print(node.getFunctionName(), inputVariables)

        

#print(G.edges())
#print(nx.shortest_path(G, "wp_ajax_update_widget", "get_instance_hash_key"))
        

#          
#      
# nx.draw(G)
# plt.show()
           
           
# import urllib.request
# import urllib.parse 
# print('running...')
# response = urllib.request.urlopen('file:///C:/CallGraphOutput/Wordpress/html/includes_2upgrade_8php.html#a913d174175f69bd5da3dba3288acc2b1')
# html = response.read()
# from htmldom import htmldom
#  
# dom = htmldom.HtmlDom().createDom(str(html))
# element = dom.find("a#a913d174175f69bd5da3dba3288acc2b1").next("div.memitem").find("div.fragment")
# print (element.html())
# print(element.len, ' Done!')

    
    


