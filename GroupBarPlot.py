import pylab as pl
import numpy as np

DATAPATH = '/Users/mac/PycharmProjects/ClickAnalysis'
dayslice = ['24/07','25/07','26/07','27/07','28/07','29/07','30/07','31/07','1/08 ','2/08','3/08','4/08','5/08',
'6/08', '7/08','8/08','9/08','10/08','11/08','12/08','13/08','14/08','15/08','16/08','17/08','18/08']
#colormap = ['darkblue','mediumblue','blue','dodgerblue','deepskyblue','lightskyblue','lightcyan']
activities = ['Projects', 'Lecture & Tutorial', 'Materials', 'View Announcements', 'Assessment', 'Problem Solving', 'Workshop Templates', 'Question & Help', 'Staff meetings', 'Library Links', 'Group Pages', 'MOOCchat', 'Reflection Tool']
colormap = ['cyan','springgreen','orange','yellow','red','magenta','grey']
colorarr = ['cyan','springgreen','skyblue','pink','cornsilk','gold','lightblue','peachpuff','orange','lightgreen','yellow','magenta','lime']
file_object = open('Groups for ProjectA.txt','rU')

group = dict()
key = ''
for line in file_object:
    if 'P0' in line:
        key = line.rstrip('\n')
    else:
        if line == '\n':
            continue
        else:
            if key in group.keys():
                group[key].append(line.rstrip('\n'))
            else:
                l = list()
                l.append(line.rstrip('\n'))
                group[key] = l


file_object.close()
#print(group)
def readuser(uid):
    fobj = open(DATAPATH+'/UsersData/' + uid, 'rU')
    matrix = []
    for line in fobj:
        s = line.rstrip('\n')
        t = s.split(',')
        numarr = []
        for word in t:
            numarr.append(int(word))
        matrix.append(numarr)
    #print({uid:matrix})
    return {uid:matrix}

def readgroup(groupname):
    fobj = open(DATAPATH+'/GroupsData/' + groupname, 'rU')
    matrix = []
    for line in fobj:
        s = line.rstrip('\n')
        t = s.split(',')
        numarr = []
        for word in t:
            numarr.append(int(word))
        matrix.append(numarr)
    #print({uid:matrix})
    return {groupname:matrix}

def DailySum(matrix):
    daily = []
    for i in range(0,len(matrix)):
        if daily == []:
            daily = matrix[i]
        else:
            for j in range(0,len(matrix[i])):
                daily[j] += matrix[i][j]
    return np.array(daily)
def easybarplot():
    width = 0.8
    for groupname in group.keys():
        #groupname = 'P04 - Elastomer'
        print(groupname)
        gsum = DailySum(readgroup(groupname)[groupname])
        x = range(0, 26)
        bottom = np.zeros(26)
        pl.figure(figsize=(27, 12), dpi=80)
        pl.xlim(-1, 26)
        pl.title('Clustered Stack of Overall Click Count from Group ' + groupname)
        pl.xlabel('Date (d/m)')
        pl.ylabel('Click Count')
        pl.xticks(x, dayslice)
        count = 0
        for username in group[groupname]:
            y = DailySum(readuser(username)[username])
            for i in range(0,len(y)):
                a = y[i] / gsum[i] * 100
                pl.text(x[i],y[i]/2+bottom[i],str(float('%.1f'%a))+'%',horizontalalignment='center',verticalalignment='center',fontsize=15)
            pl.bar(x,y,width=width,bottom=bottom,align = 'center',color= colormap[count],label='Student '+username[0:4])
            pl.legend(loc='upper left', numpoints=1)
            bottom += y
            count += 1
        for i in range(0,len(gsum)):
            pl.text(x[i],gsum[i],str(gsum[i]),horizontalalignment='center',fontsize=15)
        #pl.show()
        pl.savefig(DATAPATH + '/GroupsPlot/' + groupname + '/Overall Click Stack.png')
        pl.close()

easybarplot()
def difficultplot():
    weekdivide =[[0,1,2,3,4],[5,6,7,8,9,10,11],[12,13,14,15,16,17,18],[19,20,21,22,23,24,25]]
    weekcount = 1
    for dayperoid in weekdivide:
        print(dayperoid)
        sumday = len(dayperoid)
        for groupname in group.keys():
            print(groupname)
            #groupname= 'P04 - Elastomer'
            member = len(group[groupname])
            usercount = 0
            width = 1
            pl.figure(figsize=(27, 12), dpi=80)
            pl.xlim(0,(member+1)*sumday)
            pl.title('Clustered Stack of Daily Click Count for all Students in Group ' + groupname+' from '+dayslice[dayperoid[0]]+' to '+dayslice[dayperoid[-1]]+'(Week'+str(weekcount)+')')
            pl.xlabel('Date (d/m)')
            pl.ylabel('Click Count')
            l = []
            for i in range(0,sumday):
                l.append(i)
            days = np.array(l)
            pl.xticks(days*(member+1)+(member+1)/2, dayslice[dayperoid[0]:dayperoid[-1]+1])
            for username in group[groupname]:
                uSum = DailySum(readuser(username)[username])
                bottom = np.zeros(sumday)
                usercount+=1
                umatrix = readuser(username)[username]
                realmatrix = np.array(umatrix)
                for type in range(0,len(umatrix)):
                    daycount = 0
                    for day in dayperoid:
                        daycount += 1
                        if uSum[day]!=0:
                            a = umatrix[type][day]/uSum[day] * 100
                        else:
                            a = 0
                        pl.bar(usercount+(daycount-1)*(member+1),umatrix[type][day],bottom=bottom[daycount-1],width=width,align = 'center',color=colorarr[type])
                        if a != 0:
                            pl.text(usercount+(daycount-1)*(member+1),bottom[daycount-1]+umatrix[type][day]/2,str(float('%.1f'%a))+'%',horizontalalignment='center',verticalalignment='center',fontsize=15)
                        bottom[daycount - 1] += umatrix[type][day]
                        #pl.legend(loc='upper left', numpoints=1)
                        if type == len(umatrix)-1:
                            pl.text(usercount+(daycount-1)*(member+1),uSum[day],'S'+str(usercount)+'\n'+str(uSum[day]),horizontalalignment='center',fontsize=20)
                            #pl.text(usercount+(daycount-1)*(member+1),-5,'S'+str(usercount),horizontalalignment='center',fontsize=15)
            pl.savefig(DATAPATH+'/GroupsPlot/'+groupname+'/Week'+ str(weekcount)+' Clustered Stack.png')
            pl.close()
        weekcount += 1

            #pl.show()



'''
x = range(0,26)
y = DailySum(readgroup('P06 - Silicon')['P06 - Silicon'])
pl.figure(figsize=(27,12),dpi=80)
pl.bar(x,y,align = 'center')
pl.xlim(-1,26)
pl.title('Clustered Stack of Overall Click Count from Group '+'P06 - Silicon' )
pl.xlabel('Date (d/m)')
pl.ylabel('Click Count')
pl.xticks(x,dayslice)
pl.show()
'''