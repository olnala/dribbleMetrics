import math

def distancecor(filename):
    """This set of metrics should offer some insight into how defender
    velocity affects field goal percentage. It's expected that a higher distance translates
    to a higher field goal percentage."""
    #find max distance, then create a series of segments to create a fg% metric
    import csv
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile)
        next(reader,None) #skip the headers
        metriclist=[]
        checkmaxdistance=[]
        for row in reader:
            #filter out layups
            shotlocx=float(row[0])
            shotlocy=float(row[1])
            shotdist=((shotlocx**2)+(shotlocy**2))**(1/2)
            if shotdist>=6:
                distance=float(row[6])
                checkmaxdistance.append(distance)
                made=int(row[5])
                newline=[distance,made]
                metriclist.append(newline)

        #max distance sets the upper bound for the set of metrics
        maxdistance=max(checkmaxdistance)
        maxdistance=math.ceil(maxdistance)
        maxdistance+=1

        #distancecorlist will be the nested list of metrics that is written to the new CSV
        distancecorlist=[]
        for num in range(0,maxdistance):
            numsum=0
            madesum=0
            for metric in metriclist:
                if metric[0]<num and metric[0]>num-1:
                    madesum+=metric[1]
                    numsum+=1
            if numsum>0:
                fgp=madesum/numsum
                perfoot=[num,fgp,numsum]
                distancecorlist.append(perfoot)

        print(distancecorlist)
        """
        New metric row will have format:
        (Defender Distance Ceiling, FG%, Total Shots on Specified Distance Ceiling)
        """

    #Write these metrics to a separate CSV
    with open("distancecor.csv","w",newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(distancecorlist)


def anglecor(filename):
    """This set of metrics should offer some insight into how defender
    angle affects field goal percentage. Expected that as the angle approaches 0,
    field goal percentage should go down."""
    #segment by distance from 0; segmented by degrees of 5 in order to allow for fg% metric

    import csv
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile)
        next(reader,None) #skip the headers
        metriclist=[]
        checkmaxangle=[]
        for row in reader:
            #filter out layups
            shotlocx=float(row[0])
            shotlocy=float(row[1])
            shotdist=((shotlocx**2)+(shotlocy**2))**(1/2)
            if shotdist>=6:
                defangle=float(row[7])
                checkmaxangle.append(defangle)
                made=int(row[5])
                newline=[defangle,made]
                metriclist.append(newline)

        maxangle=max(checkmaxangle)
        maxangle=math.ceil(maxangle)
        maxangle+=1
        #print(maxangle)

        anglecorlist=[]
        for num in range(0,maxangle):
            numsum=0
            madesum=0
            for metric in metriclist:
                #Absolute value of the angle, because 1 degree and -1 degree with
                #the given metrics translate to practically the same positioning
                #of the defender in contesting the shot
                if abs(metric[0])<num and abs(metric[0])>num-1:
                    madesum+=metric[1]
                    numsum+=1
            if numsum>0:
                fgp=madesum/numsum
                perdegree=[num,fgp,numsum]
                anglecorlist.append(perdegree)
        print(anglecorlist)

        """
        New metric row will have format:
        (Defender Angle Ceiling, FG%, Total Shots on Specified Angle Ceiling)
        """

    #Write these metrics to a separate CSV
    with open("anglecor.csv","w",newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(anglecorlist)

def shootervelocitycor(filename):
    """This set of metrics should offer some insight into how shooter velocity
    affects field goal percentage. Expected that higher shooter velocity decreases
    field goal percentage"""
    import csv
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile)
        next(reader,None) #skip the headers
        metriclist=[]
        checkmaxvelocity=[]
        for row in reader:
            #filter out layups
            shotlocx=float(row[0])
            shotlocy=float(row[1])
            shotdist=((shotlocx**2)+(shotlocy**2))**(1/2)
            if shotdist>=6:
                shootervelocity=float(row[2])
                checkmaxvelocity.append(shootervelocity)
                made=int(row[5])
                newline=[shootervelocity,made]
                metriclist.append(newline)

        maxvelocity=max(checkmaxvelocity)
        maxvelocity=math.ceil(maxvelocity)
        maxvelocity+=1
        #print(maxvelocity)

        velocitycorlist=[]

        compnum=0
        while compnum<=maxvelocity:
            numsum=0
            madesum=0
            for metric in metriclist:
                if metric[0]<compnum+0.5 and metric[0]>compnum:
                    madesum+=metric[1]
                    numsum+=1
            if numsum>0:
                fgp=madesum/numsum
                perfps=[compnum,fgp,numsum]
                velocitycorlist.append(perfps)
            compnum+=0.5
        print(velocitycorlist)

        """
        New metric row will have format:
        (Shooter Velocity, FG%, Total Shots on Specified Distance Ceiling)
        """

    #Write these metrics to a separate CSV
    with open("shootervelocitycor.csv","w",newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(velocitycorlist)

def defendervelocitycor(filename):
    """This set of metrics should offer some insight into how defender velocity
    affects field goal percentage. Expected that lower defender velocity decreases
    field goal percentage, because this means the defender should already be in good
    position to guard the shot."""
    import csv
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile)
        next(reader,None) #skip the headers
        metriclist=[]
        checkmaxvelocity=[]
        for row in reader:
            #filter out layups
            shotlocx=float(row[0])
            shotlocy=float(row[1])
            shotdist=((shotlocx**2)+(shotlocy**2))**(1/2)
            if shotdist>=6:
                defendervelocity=float(row[8])
                checkmaxvelocity.append(defendervelocity)
                made=int(row[5])
                newline=[defendervelocity,made]
                metriclist.append(newline)

        maxvelocity=max(checkmaxvelocity)
        maxvelocity=math.ceil(maxvelocity)
        maxvelocity+=1
        #print(maxvelocity)

        velocitycorlist=[]

        compnum=0
        while compnum<=maxvelocity:
            numsum=0
            madesum=0
            for metric in metriclist:
                if metric[0]<compnum+0.5 and metric[0]>compnum:
                    madesum+=metric[1]
                    numsum+=1
            if numsum>0:
                fgp=madesum/numsum
                perfps=[compnum,fgp,numsum]
                velocitycorlist.append(perfps)
            compnum+=0.5
        print(velocitycorlist)

        """
        New metric row will have format:
        (Shooter Velocity, FG%, Total Shots on Specified Distance Ceiling)
        """

    #Write these metrics to a separate CSV
    with open("defendervelocitycor.csv","w",newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(velocitycorlist)


def dribblemetrics(filename):
    """This set of new metrics allows us to check the correlations between
    dribbles to FG%, dribbles to defender angle, and dribbles to defender distance.
    Previous set of metrics should offer some insight into how defender angle and
    defender distance should translate to field goal percentage.
    """
    import csv
    with open(filename,'r') as csvfile:
        reader=csv.reader(csvfile)
        next(reader,None) #skip the headers
        metriclist=[]
        checkmaxdribbles=[]
        for row in reader:
            #filter out layups
            shotlocx=float(row[0])
            shotlocy=float(row[1])
            shotdist=((shotlocx**2)+(shotlocy**2))**(1/2)
            if shotdist>=6:
                dribbles=int(row[4])
                checkmaxdribbles.append(dribbles)
                made=int(row[5])
                distance=float(row[6])
                angle=float(row[7])
                shovelocity=float(row[2])
                defvelocity=float(row[8])
                newline=[dribbles,made,distance,angle,shovelocity,defvelocity]
                metriclist.append(newline)
        maxdribbles=max(checkmaxdribbles)
        maxdribbles+=1
        #print(maxdribbles)

        finmetriclist=[]
        for num in range(0,maxdribbles):
            perdribblemetric=[]
            numsum=0
            madesum=0
            distancesum=0
            anglesum=0
            shovelocitysum=0
            defvelocitysum=0
            for metric in metriclist:
                if metric[0]==num:
                    madesum+=metric[1]
                    distancesum+=metric[2]
                    anglesum+=metric[3]
                    shovelocitysum+=metric[4]
                    defvelocitysum+=metric[5]
                    numsum+=1
            if numsum>0:
                fgp=madesum/numsum
                distance=distancesum/numsum
                angle=anglesum/numsum
                shovelocity=shovelocitysum/numsum
                defvelocity=defvelocitysum/numsum
                perdribblemetric=[num,fgp,distance,angle,shovelocity,defvelocity,numsum]
                finmetriclist.append(perdribblemetric)
        print(finmetriclist)

        """
        New metric row will have format:
        (Dribbles, FG%, Avg Defender Distance, Avg Defender Angle, Avg Shooter Velocity,
        Avg Defender Velocity, Total Shots on Specified Dribble #)
        """

    #Write these metrics to a separate CSV
    with open("newshots.csv","w",newline='') as csvfile:
        writer=csv.writer(csvfile)
        writer.writerows(finmetriclist)


"""
Uncomment the following function calls in order to create the new
CSV's, under the assumption that the file name is shots.csv.
"""

#anglecor("shots.csv")
#distancecor("shots.csv")
#shootervelocitycor("shots.csv")
#defendervelocitycor("shots.csv")
#dribblemetrics("shots.csv")
