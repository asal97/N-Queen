# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 22:31:07 2018

@author: 8.1
"""
import timeit
import numpy as np
import random
import matplotlib.pyplot as plt

time = []


# baraye random entekhab krdne jameye Ehtemali chn permutation hasho random migirim
# hmun 10 taye avalesho negah darim be javab reCdim

def getTenFirst(l):
    gTF = l[0:10]
    return gTF


# inja miyaym az majmue afradi k darim 3ta 3ta joda mikonim(hr seri 3ta index e random
# az kolmizanim va batavoj be tabe tedad Tahdid ke qablan hesab krdim miyam uni k beyne
# in 3ta tahdidesh az hame kmtare ro entekhab mikonim
# va be andaze 10 bar in azmayesho anjam midim
def Tournoment(lTahdid, l):
    start1 = timeit.default_timer()
    listOfMinTahdid = []
    for j in range(10):
        lTour = []
        for i in range(3):
            # entekhabe 3 nfr random
            lTour.append(random.randint(0, len(l) - 1))
            # peyda krdne min eshun tebqe meqdare az pish taEn shode
        minTahdid = min(lTahdid[lTour[0]], lTahdid[lTour[1]], lTahdid[lTour[2]])
        f = False
        for k in range(len(lTour)):
            if (lTahdid[lTour[k]] == minTahdid and f == False):
                # ezafe krdn e frde entekhab shode be liste kolle afrade entekhabie jamiat
                listOfMinTahdid.append(l[lTour[k]])
                f = True

        lTour = []
    finish1 = timeit.default_timer()
    time.append(finish1 - start1)
    return listOfMinTahdid


def PMX(l1, l2, ch1, ch2):
    p1 = random.randint(0, len(l1) - 1)
    p2 = random.randint(0, len(l1) - 1)
    while (p2 == p1):
        p2 = random.randint(0, len(l1) - 1)

    first = min(p1, p2)
    second = max(p1, p2)

    ch1[first:second + 1] = l1[first:second + 1]
    ch2[first:second + 1] = l2[first:second + 1]

    pmxC(l1, l2, first, second, ch1)
    pmxC(l2, l1, first, second, ch2)


def pmxC(p1, p2, first, second, ch):
    for i in p2[first:second + 1]:
        if (i not in ch):
            posf = p2.index(i)
            pos = p1[posf]
            insert(p1, p2, first, second, ch, i, pos)

    ch = fix(p1, p2, ch)


def insert(p1, p2, first, second, ch, item, pos):
    if (np.count_nonzero(ch) == len(ch)):
        return
    elif (ch[list(p2).index(pos)] != 0):
        insert(p1, p2, first, second, ch, item, p1[list(p2).index(pos)])
    else:
        ch[p2.index(pos)] = item
    return


def fix(p1, p2, ch):
    result = []
    for i in p2:
        if (not (i in ch)):
            result.append(i)
    j = 0
    for i in ch:
        if (i == 0):
            ch[list(ch).index(i)] = result[j]
            j = j + 1
    return ch


# ye random mizanim k bar asase un tasmim begirim ke ruye farzand mutation
# bezanim ya na va intorie k age randomemun kmtar az 0.1 umad miayam
# 2 ta index e random entekhab mikonim va mohtavshun ro swap mikonim

def mutation(l1):
    start3 = timeit.default_timer()
    p = random.random()
    print(p)
    if (p <= 0.1):
        p1 = random.randint(0, len(l1) - 1)
        p2 = random.randint(0, len(l1) - 1)
        copy = l1[p1]
        l1[p1] = l1[p2]
        l1[p2] = copy
        print(l1)
    finish3 = timeit.default_timer()
    time.append(finish3 - start3)


# baraye entekhabe 2taye behtarin,array tahdid ro sort mikonim un 2tayi ke kmtrin meqdaro
# daran ro var midarim(copy mikonim dar vaqe) va be array lElitism ezafe mikonim
def elitism(l, lTahdid, lElitism):
    start4 = timeit.default_timer()
    lTahdidS = np.sort(lTahdid)
    t = 0
    for i in range(len(l)):
        # migarde tak tak un zojE ke tedad tahdidashun mosavie min bud ro var midare
        if ((lTahdid[i] == lTahdidS[0] or lTahdid[i] == lTahdidS[1]) and t < 2):
            lElitism.append(l[i])
            t = t + 1
    print(lElitism)
    finish4 = timeit.default_timer()
    time.append(finish4 - start4)


# baraye peyda krdnw tahdid byd sotun o satr va qotre asli o farE ro check knim
# chn negah be in board besurate matrix e nemishe k az function E k baraye mohasebeye
# tahdid chromosome Stefade krdim bokonim ama manteq yki bude fqt Ddesh avaz mishe
def TahdidBackTrack(i, j, n):
    # check mikone k aya vaziri tuye un satr ya sotun vojud dare (tahdid e satri o sutuni)
    for k in range(0, n):
        # age tu un sotun ya satr qeire chizi k mikhay bezarim yeki bud tahdid ro true bargardun
        # yni emkane ja gozarish nis
        if board[i][k] == 1 or board[k][j] == 1:
            return True
    # baz kolle board ro byd bekhatere qotra check knim
    for k in range(0, n):
        for l in range(0, n):
            # agar dar qotre asli ya farE 1 e Dg E bud baz byd jolosh grfte she va true bargrdunde she
            if (k + l == i + j) or (k - l == i - j):
                if board[k][l] == 1:
                    return True
    return False


def BackTrack(found, n):
    # age found=0 bud yani inke jvbe masale peyda shode
    if found == 0:
        return True
    for i in range(0, n):
        for j in range(0, n):
            # miad tak take khune haro check mikone beBne mitune tushun vaziro bezare ya na
            # ba Stefade az function e tahdid!
            if (not (TahdidBackTrack(i, j, n))) and (board[i][j] != 1):
                board[i][j] = 1
                if BackTrack(found - 1, n) == True:
                    return True
                board[i][j] = 0


# function e check krdn tedad tahdid tu chromosome
def checkingTahdid(l, lTahdid):
    # chon darim az avalin radif shuru mikonim be jolo rftan
    # va tahdidasho ba hme check mikonim baraye harkudum Dg lazem nis samte chapesho
    # check knim chn tu qabliash hesab krdim
    for k in range(len(l)):
        t = 0;
        for i in range(n - 1):
            y = l[k][i]
            x = i
            yU = y
            yD = y
            for j in range(i, n - 1):
                x = x + 1;
                yU = yU + 1
                yD = yD - 1
                if (l[k][x] == yU or l[k][x] == yD):
                    t = t + 1
        lTahdid.append(t)
    return lTahdid
    return False


def analytical(n):
    # ye board e kamel sefr misazim baad bar asase formul haye mojud poresh mikonim
    start6 = timeit.default_timer()
    board = np.zeros((n, n))
    i = 0
    j = 0
    if (np.remainder(n, 2) == 1):
        board[n - 1][n - 1] = 1
        n = n - 1

    if (np.remainder(n, 2) == 0):
        if (np.remainder(n, 6) != 2):
            for i in range(int(n / 2)):
                j = 2 * i + 1
                board[i][j] = 1
            for i in range(int(n / 2), n):
                j = np.remainder(2 * i, n)
                board[i][j] = 1
        elif (np.remainder(n, 6) == 2):
            for i in range(int(n / 2)):
                j = np.remainder(int(n / 2) + (2 * i) - 1, n)
                board[i][j] = 1
            for i in range(int(n / 2), n):
                j = np.remainder(int(n / 2) + (2 * i) + 2, n)
                board[i][j] = 1
    print(board)
    finish6 = timeit.default_timer()
    time.append(finish6 - start6)


# vorudi migire :)
n = int(input("n? "))
l = []
lElitism = []
lTahdid = []
board = np.zeros((n, n))
# tolid e permutation e haye mokhtalef ta baad bar Asase ravesh haye nemune giri azsh jamiate
# avalie ro brdarim
for i in range(3 * n):
    a = np.random.permutation(n)
    l.append(a)
# tedad tahdid haro hesab mikonim
lTahdid = checkingTahdid(l, lTahdid)
print("kolle afrade tolid shode : ")
print(l)
print("kolle tahdid ha: ", lTahdid)
print("-----------------")
# jamiate random :
lRandom = getTenFirst(l)
print("jamiate avalie bar asase nemune bardari random")
print(lRandom)
print("kolle tahdid haye jamiate avalie: ", lTahdid[0:10])
print("-----------------")
print("pichidegie makanie ghesmate alef: ", n)
print("-----------------")
print("jamiate tolidie tournoment")
lTour = Tournoment(lTahdid, l)
print(lTour)
print("-----------------")
childs = []

print("ehtemale jahesh:")
tahdidChilds = checkingTahdid(childs, [])
print("-----------------")
l2 = [6, 2, 4, 5, 3, 1]
print("elitism : ")
elitism(l, lTahdid, lElitism)

print("-------------------")
board = np.zeros((n, n))
bl = n
start5 = timeit.default_timer()
BackTrack(n, bl)
finish5 = timeit.default_timer()
time.append(finish5 - start5)
print(board)
print("zamane lazem jahate rasme board ", finish5 - start5)
print("-------------------")
print("analytical solution")
analytical(n)
# PMX(l1,l2)
height = [time[0] * 1000, time[1] * 1000, time[2] * 1000, time[3] * 1000]
bars = ('A', 'B', 'C', 'D', 'E')
y_pos = np.arange(len(bars))
plt.bar(y_pos + 1, height, color=(0.2, 0.4, 0.6, 0.6))

# Custom Axis title
plt.xlabel('N-Queen', fontweight='bold', color='orange', fontsize='17', horizontalalignment='center')


