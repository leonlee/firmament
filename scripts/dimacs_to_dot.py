#!/usr/bin/python

import sys, re

if len(sys.argv) < 2:
  print "usage: dimacs_to_dot.py <input>"
  sys.exit(1)

inputfile = sys.argv[1]

def dot_out(nodes, edges):
  # dot header
  print "digraph G {"
  print "\tgraph [center rankdir=LR]"
  # nodes
  print "\t{ node [shape=box]"
  print "\t",
  for n in nodes:
    print "%d " % (n['nid']),
  print "\t}"
  # edges
  print "\t{ edge [color=\"#ff0000\"]"
  print "\t",
  for e in edges:
    print "%d -> %d [ label = \"%d/%d/%d\" ];" % (e['src'], e['dst'],
                                                  e['cap_lb'], e['cap_ub'],
                                                  e['cost'])
  print "\t}"
  # dot footer
  print "}"

nodes = []
edges = []
for line in open(inputfile).readlines():
  fields = [x.strip() for x in line.split(" ")]
  if fields[0] == 'c':
    # comment, skip
    continue
  if fields[0] == 'p':
    # problem descr
    continue
  if fields[0] == 'n':
    # node
    node = { 'nid': int(fields[1]),
             'supp': int(fields[2]) }
    nodes.append(node)
  if fields[0] == 'a':
    # arc
    edge = { 'src': int(fields[1]),
             'dst': int(fields[2]),
             'cap_lb': int(fields[3]),
             'cap_ub': int(fields[4]),
             'cost': int(fields[5]) }
    edges.append(edge)

dot_out(nodes, edges)
