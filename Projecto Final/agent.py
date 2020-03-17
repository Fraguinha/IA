#!/usr/bin/env python
# encoding: utf8
# Artificial Intelligence, UBI 2019-20
# Modified by: Carolina Silva and João Fraga

# ---------------------------------------------------------------
# Custom Libraries
import networkx as nx
import math
import time

# ---------------------------------------------------------------
# Libraries
import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

# ---------------------------------------------------------------
# Global variables
x_ant = 0
y_ant = 0

obj_ant = ''
room_ant = 1

time_start = None

# ---------------------------------------------------------------
# Data structures

rooms = [
    ((-15.6, -1.4), (3.6, -3.1)),
    ((-11.8, 5.1), (-9.6, -1.1)),
    ((-11.8, 7.3), (3.6, 5.4)),
    ((-4.0, 5.1), (-1.4, -1.1)),
    ((-15.6, 2.3), (-12.5, -0.8)),
    ((-15.6, 7.3), (-12.5, 3.0)),
    ((-15.6, 11.1), (-11.1, 7.9)),
    ((-10.6, 11.1), (-6.2, 7.9)),
    ((-5.6, 11.1), (-1.2, 7.9)),
    ((-0.6, 11.1), (3.6, 7.9)),
    ((-0.8, 4.8), (3.6, 2.0)),
    ((-0.8, 1.7), (3.6, -0.8)),
    ((-9.0, 4.8), (-7.1, -0.9)),
    ((-6.5, 4.8), (-4.5, -0.8))
]

corridors = [1, 2, 3, 4]

G = nx.Graph()
D = {}
T = {}


# ---------------------------------------------------------------
# odometry callback
def callback(data):
    global x_ant, y_ant, room_ant, corridors, D, T
    x = data.pose.pose.position.x-15
    y = data.pose.pose.position.y-1.5
    x_ant = x
    y_ant = y
    room = get_room(x, y)
    if room != room_ant and room != 0:
        G.add_edge(room, room_ant, weight=euclid(
            room_center(room), room_center(room_ant)))
        if room not in corridors and room_ant not in corridors:
            if (room_ant, "bed") in D:
                T[room_ant] = "suite"
        T[room] = "generic"
        room_ant = room


# ---------------------------------------------------------------
# object_recognition callback
def callback1(data):
    global obj_ant, room_ant, D, G
    obj = data.data
    if room_ant != 0 and obj != obj_ant and obj != "":
        print "object is %s" % obj
        l = obj.split(',')
        for item in l:
            category, name = tuple(item.split('_', 1))
            if (room_ant, category) in D:
                update = D[room_ant, category]
                if name not in update:
                    update.append(name)
                    D[room_ant, category] = update
            else:
                D[room_ant, category] = [name]
            if category == "bed":
                for n1, n2 in G.edges(room_ant):
                    if n2 not in corridors:
                        T[n1] = "suite"
                    elif len(D[n1, "bed"]) > 1:
                        T[n1] = "double"
                    else:
                        T[n1] = "single"
            if category == "table" or category == "chair":
                if (room_ant, "table") in D and len(D[room_ant, "table"]) == 1:
                    if (room_ant, "chair") in D and len(D[room_ant, "chair"]) > 1:
                        T[room_ant] = "meeting"
    obj_ant = obj


# ---------------------------------------------------------------
# questions_keyboard callback
def callback2(data):
    print "question is %s" % data.data
    if data.data == "1":
        question1()
    elif data.data == "2":
        question2()
    elif data.data == "3":
        question3()
    elif data.data == "4":
        question4()
    elif data.data == "5":
        question5()
    elif data.data == "6":
        question6()
    elif data.data == "7":
        question7()
    elif data.data == "8":
        question8()


# ---------------------------------------------------------------
# Answers
def question1():
    global D, G
    visited = 0
    occupied = 0
    for room in G:
        if room not in corridors:
            if(room, 'person') in D:
                occupied += 1
            visited += 1
    print "Of the %d rooms visited %d are not occupied." % (
        visited, visited - occupied)


def question2():
    global T
    suites = 0
    for room in T:
        if T[room] == "suite":
            suites += 1
    print "I found %d suites so far." % suites


def question3():
    global G, D, corridors
    num_rooms = 0
    num_corridors = 0
    visited_rooms = 0
    visited_corridors = 0
    for room in G:
        if room in corridors:
            visited_corridors += 1
            if (room, 'person') in D:
                num_corridors += 1
        else:
            visited_rooms += 1
            if (room, 'person') in D:
                num_rooms += 1

    prob_rooms = 0
    prob_corridors = 0
    if visited_rooms > 0:
        prob_rooms = num_rooms / float(visited_rooms)
    if visited_corridors > 0:
        prob_corridors = num_corridors / float(visited_corridors)

    if prob_rooms > prob_corridors:
        print "It's more probable to find people in rooms."
    elif prob_rooms < prob_corridors:
        print "It's more probable to find people in corridors."
    else:
        print "It's equally probable to find people in rooms and corridors."


def question4():
    global D, T
    types = ["single", "double", "suite", "meeting", "generic"]
    count = [0, 0, 0, 0, 0]
    comp = [0, 0, 0, 0, 0]
    for room in T:
        t = T[room]
        i = types.index(t)
        count[i] += 1
        if (room, "computer") in D:
            comp[i] += 1

    prob_max = 0
    type_max = 4
    for i in range(5):
        prob = 0
        if count[i] > 0:
            prob = comp[i] / float(count[i])
        if prob > prob_max:
            prob_max = prob
            type_max = i
    if prob_max > 0:
        print "You should go to a %s room." % types[type_max]
    else:
        print "I've never seen a computer before."


def question5():
    global G, T, x_ant, y_ant
    l = []
    for room in T:
        if T[room] == "single":
            l.append(room)

    if l == []:
        print "No single rooms found yet."
    else:
        for n1, n2 in G.edges(room_ant):
            G.add_edge(-1, n2, weight=euclid((x_ant, y_ant), room_center(n2)))
        d = nx.shortest_path_length(G, source=-1, weight="weight")
        G.remove_node(-1)
        min_dist = 999999999
        min_room = 0
        for single in l:
            if d[single] < min_dist:
                min_dist = d[single]
                min_room = single

        print "The closest single room is room number %d." % min_room


def question6():
    path = nx.shortest_path(G, source=room_ant, target=1, weight="weight")

    for room, i in zip(path[1::], range(1, len(path)+1)):
        print "%d. From room %d go to room %d." % (i, path[i-1], room)

    print "%d. Your destination will be on the left" % (len(path))


def question7():
    global time_start, G, D, corridors
    total_rooms = 10
    t = time.time() - time_start

    visited = 0
    books = 0
    for room in G:
        if room not in corridors:
            visited += 1
            if (room, "book") in D:
                books += len(D[(room, "book")])

    if visited == total_rooms:
        print "I already visited all the rooms, I don't expect to find any more books... maybe I missed some"
    elif visited == 0:
        print "I still haven't visited any rooms, I don't know what to expect."
    elif books == 0:
        print "I've never seen a book before."
    else:
        rooms_sec = 0
        if t != 0:
            rooms_sec = total_rooms / t

        books_room = 0
        if visited != 0:
            books_room = float(books) / visited

        remaining_rooms = total_rooms - visited
        rooms_num = rooms_sec * 2 * 60

        if rooms_num > remaining_rooms:
            estimate = remaining_rooms * books_room
        else:
            estimate = rooms_num * books_room

        print "I estimate to find %d more books in the next 2 minutes" % round(
            estimate)


def question8():
    global G, D
    t_nb_c = 0
    nb_c = 0
    visited = 0
    p = 0
    for room in G:
        if room not in corridors:
            visited += 1
            if (room, "book") not in D and (room, "chair") in D:
                nb_c += 1
                if (room, "table") in D:
                    t_nb_c += 1

    if nb_c != 0:
        p = t_nb_c / float(nb_c)

    print "The probability is %.2f." % p


# ---------------------------------------------------------------
# Agent code
def agent():
    global time_start
    time_start = time.time()

    rospy.init_node('agent')

    rospy.Subscriber("questions_keyboard", String, callback2)
    rospy.Subscriber("object_recognition", String, callback1)
    rospy.Subscriber("odom", Odometry, callback)

    rospy.spin()


# ---------------------------------------------------------------
# Auxiliar functions
def get_room(x, y):
    global rooms
    alpha = 0.1

    for ((a, b), (c, d)), i in zip(rooms, range(1, 15)):
        if x >= a - alpha and x <= c + alpha and \
                y >= d - alpha and y <= b + alpha:
            return i
    return 0


def room_center(room):
    (x1, y1), (x2, y2) = rooms[room-1]
    x = (x2 - x1) / 2
    y = (y2 - y1) / 2
    return (x, y)


def euclid(point1, point2):
    global rooms
    (x1, y1) = point1
    (x2, y2) = point2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


# ---------------------------------------------------------------
# Entry point
if __name__ == '__main__':
    agent()
