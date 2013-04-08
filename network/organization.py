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

from analysis import analyse_repo


def github_mining(userlogin,password):
    
    graph = nx.MultiDiGraph()
    issue = {}
    issue = {0:{"author":"none", "comments":{}}}
    commits = {0:{"commit","sha"}}
    repos = {}

    g = Github( userlogin, password )
    
    print "ORGANIZATIONS:"
    for i in g.get_user(userlogin).get_orgs():
        print "-", i.login
    print ""
    
    org_to_mine = raw_input("Enter the name of the Organization you want to analyse: ")
    print ""
    
    org = g.get_organization(org_to_mine)
    
    print org.login,"has",org.public_repos, "repositories."
    
    print ""
    
    for repo in org.get_repos():
        print "-",repo.name
    
    print ""
    
    repo_to_mine = raw_input("Enter the name of the repository you want to mine: ")
    b = org.get_repo(repo_to_mine)
    analyse_repo(b,graph)
    
    # Getting rid of the node "None", it was used to catch the errors of users that are NoneType
    graph.remove_node('None')
    
    print ""
    print "NODES..."
    print graph.nodes()
    print ""
    print "EDGES..."
    print graph.edges()
    print ""
    
    print "Converting multiple edges to weighted edges..."
    print ""
    
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
            
    print "EDGES..."
    print graph2.edges()
    print ""

    print "Saving the network..."
    nx.write_gexf(graph2, username+"_"+repo_to_mine+"_social_interactions_analysis.gexf")
    print "Done. Saved as "+username+"_"+repo_to_mine+"_social_interactions_analysis.gexf"
    
    return
    
    
if __name__ == "__main__":
    pass