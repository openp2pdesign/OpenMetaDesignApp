# -*- coding: utf-8 -*-
#
# Open MetaDesign 0.1
#
# Author: Massimo Menichinelli
# Website:
# http://openmetadesign.org
# http://openp2pdesign.org
#
# License: GPL v.3
#
#
# Social analysis of an Organization repository in GitHub
#
# Requisite: 
# install pyGithub with pip install PyGithub
# install NetworkX with pip install networkx
#
# PyGitHub documentation can be found here: 
# https://github.com/jacquev6/PyGithub
#

from github import Github
import networkx as nx
from classes import *

#from analysis import analyse_repo

def analyse_repo(repository,graph): 
    issue = {}
    issue = {0:{"author":"none", "comments":{}}}
    commits = {0:{"commit","sha"}}
    repos = {}
 
    # Add owner
    graph.add_node(str(unicode(repository.owner.login)),owner="Yes")
    
    # Add watchers
    for i in repository.get_stargazers():
        if i != None:
            if i.login not in graph:
                graph.add_node(str(unicode(i.login)),watcher="Yes")
            else:
                graph.node[i.login]["watcher"]="Yes"
        else:
            graph.node["None"]["watcher"]="Yes"

    # Add collaborators
    for i in repository.get_collaborators():
        if i != None:
            if i.login not in graph:
                graph.add_node(str(unicode(i.login)),collaborator="Yes")
            else:
                graph.node[i.login]["collaborator"]="Yes"
        else:
            graph.node["None"]["collaborator"]="Yes"
    
    # Check issues..
    if repository.has_issues == True:
        for i in repository.get_issues(state="open"):
            if i.user != None:
                issue[i.number]= {}
                issue[i.number]["comments"]= {}
                issue[i.number]["author"] = i.user.login
            else:
                issue[i.number]= {}
                issue[i.number]["comments"]= {}
                issue[i.number]["author"] = "None"
            if i.assignee != None:
                graph.add_edge(str(i.user.login),str(i.assignee.login))
            else:
                graph.add_edge(str(i.user.login),"None")
                
            # Check issue comments
            for j,f in enumerate(i.get_comments()):
                if f.user != None:
                    issue[i.number]["comments"][j] = f.user.login
                else:
                    issue[i.number]["comments"][j] = "None"     

        # Check closed issues
        for i in repository.get_issues(state="closed"):
            if i.user != None:
                issue[i.number]= {}
                issue[i.number]["comments"]= {}
                issue[i.number]["author"] = i.user.login
            else:
                issue[i.number]= {}
                issue[i.number]["comments"]= {}
                issue[i.number]["author"] = "None"
            if i.assignee != None:
                graph.add_edge(str(i.user.login),str(i.assignee.login))
            else:
                graph.add_edge(str(i.user.login),"None")
            
            # Check comments of the closed issues
            for j,f in enumerate(i.get_comments()):
                if f.user != None:
                    issue[i.number]["comments"][j] = f.user.login
                else:
                    issue[i.number]["comments"][j] = "None"  
              
    # Check contributors
    for i in repository.get_contributors():
        if i.login != None:
            if i.login not in graph:
                    graph.add_node(str(unicode(i.login)),contributor="Yes")
            else:
                graph.node[i.login]["contributor"]="Yes"
        else:
            graph.node["None"]["contributor"]="Yes"

    # Check commits and interactions among them    
    repos[0]={0:""}
    for k,i in enumerate(repository.get_commits()):
        if i.committer != None:
            repos[0][k]=i.committer.login
        else:
            repos[0][k]="None"
       
    # Check the attributes of every node, and add a "No" when it is not present, in order to let Gephi use the attribute for graph partitioning
    for i in graph.nodes():
        if "owner" not in graph.node[i]:
            graph.node[i]["owner"] = "No"
        if "contributor" not in graph.node[i]:
            graph.node[i]["contributor"] = "No"               
        if "collaborator" not in graph.node[i]:
            graph.node[i]["collaborator"] = "No"
        if "watcher" not in graph.node[i]:
            graph.node[i]["watcher"] = "No"
                 
    # Add an edge from a commiter to a previous one,
    # i.e. if you are committing after somebody has commited,
    # you are interacting with him/her
    for h in repos[0]:
        if h < len(repos[0])-1:
            # Adding an edge from: repos[0][h] to previous committer: repos[0][h+1]
            graph.add_edge(str(repos[0][h]),str(repos[0][h+1]))
    
    # Creating the edges from the commits and their comments.
    # Each comment interacts with the previous ones,
    # so each user interacts with the previous ones that have been creating the issue or commented it    
    comm = {}
    
    for k,i in enumerate(repository.get_commits()):
        comm[k]= {}
        comm[k]["comments"]= {}
        
        for m,f in enumerate(i.get_comments()):
            comm[k]["comments"][m] = f.user.login
            # Adding an edge from f.user.login to i.author.login
            graph.add_edge(str(f.user.login),str(i.author.login))
            
            for l in range(m):
                # Adding an edge from f.user.login to comm[k]["comments"][l]
                graph.add_edge(str(f.user.login),str(comm[k]["comments"][l]))
    
    # Creating the edges from the issues and their comments.
    # Each comment interacts with the previous ones,
    # so each user interacts with the previous ones that have been creating the issue or commented it
    
    for a,b in enumerate(issue):
        for k,j in enumerate(issue[a]["comments"]):
            # Adding an edge from issue[a]["comments"][k] to issue[a]["author"]
            graph.add_edge(str(issue[a]["comments"][k]),str(issue[a]["author"]))

            for l in range(k):
                # Adding an edge from: issue[a]["comments"][k] to issue[a]["comments"][l]
                graph.add_edge(str(issue[a]["comments"][l]),str(issue[a]["comments"][l]))
    
    #print "FORKS"
    #print ""
    #for f,i in enumerate(repository.get_forks()):
    #    print i.name
    #    print "ANALYSING A FORK, number",f
    #    print ""
    #    analyse_repo(i,f+1)
    #    print ""
    #print "-----"
    
    # Check pull requests
    for i in repository.get_pulls():
        if i.assignee != None:
            one = i.assignee.login
        else:
            one = "None"
        if i.user != None:
            two = i.user.login
        else:
            two = "None"
        
        # Adding an edge from: one to: two
        graph.add_edge(str(one),str(two))
        
        # We should look at the comments on the pull request, but a pull request is automatically translated
        # as an issue, so we are already looking at the issue comments
    return


def github_mining(project,userlogin,password,path):
    graph = nx.MultiDiGraph()
    issue = {}
    issue = {0:{"author":"none", "comments":{}}}
    commits = {0:{"commit","sha"}}
    repos = {}
    
    # Read the repository from the repo url
    urlparts = project.repo.split('/')    
    githubusername = urlparts[3]
    githubrepo = urlparts[4]

    g = Github( userlogin, password )
    
    try:
        # If successfull and type = User, the username exists and is a single user
        a = g.get_user(githubusername).type
    except:
        # Not found
        pass
    
    try:
        # If successfull, the username is an organization
        a = g.get_organization(githubusername).type
    except:
        # Not found
        pass
    
    # Load repository for analysis
    b = g.get_user(githubusername).get_repo(githubrepo)
        
    # Analyse the repo
    analyse_repo(b,graph)
    
    # Getting rid of the node "None", it was used to catch the errors of users that are NoneType
    graph.remove_node('None')
    
    # Converting multiple edges to weighted edges..."   
    graph2 = nx.DiGraph()
    
    for j in list(graph.nodes_iter(data=True)):
        # copying all the nodes with their attributes
        graph2.add_node(j[0],collaborator=j[1]["collaborator"],contributor=j[1]["contributor"],owner=j[1]["owner"],watcher=j[1]["watcher"])
        
    
    for j in list(graph.edges_iter(data=True)):
        subject_id = j[0]
        object_id = j[1]
        if graph.has_edge(subject_id, object_id) and graph2.has_edge(subject_id, object_id):
            graph2[subject_id][object_id]['weight'] += 1
        elif graph.has_edge(subject_id, object_id) and not graph2.has_edge(subject_id, object_id):
            graph2.add_edge(subject_id, object_id, weight=1)
    
    # Save the network as .graphml. When there will be no bugs with .gexf in networkx, save it as .gexf        
    nx.write_graphml(graph2, path+"_github_social_interactions_analysis.graphml")

    return
    
    
if __name__ == "__main__":
    a = project()
    a.load("test2.meta")
    github_mining(a,"","", "/")