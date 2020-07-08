import webbrowser
import schedule
import time
import datetime
import sys


#Register the webbrowser u want to open the url in
webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
         


class subject:
    def __init__(self,sub,url,day,time):
        self.url = url
        self.day = dayofweek(day)
        self.time = time
        self.subject = sub

        print('CLASS :',self.subject ,"\n URL: ", self.url, "\n DAY:", self.day , "\n TIME:", self.time)


    #schedule the class to open the url at the specified time  
    def timetable(self):

        print("TODAY'S CLASS: ",self.subject, "AT TIME " ,self.time)
        schedule.every().day.at(self.time).do(self.openurl,self.url)
            
    #function to open the url
    def openurl(self,url):
        webbrowser.get('chrome').open(self.url)


# returns the integer value of the given day 
# int value is required as datetime module returns only int value for day
def dayofweek(day):
    days = {
            'monday':0,
            'tuesday':1,
            'wednesday':2,
            'thursday':3,
            'friday':4,
            'saturday':5,
            'sunday':6
        }
    return days[day.lower()]


#function to exit since scheduler is in infinite loop
def exit():
    print("COMPLETED ALL CLASSES FOR THE DAY")
    sys.exit()



def main():
    if __name__== "__main__" :

        #all the urls for respective subjects

        sna_url = 'https://meet.google.com/lookup/ftoxsbb3wr'
        gta_url = 'https://meet.google.com/lookup/apdnv7fyah'
        rmt_url = 'https://meet.google.com/lookup/gq5gtnrujk'
        cns_url = 'https://meet.google.com/lookup/cth44zanx3'
        da_url = 'https://meet.google.com/lookup/htv3hncc5a'


        #the timetable
        classes = [['sna', sna_url , 'wednesday', '14:25'],
        ['sna',sna_url,'tuesday','11:40'],
        ['sna',sna_url,'thursday','09:20'],
        ['da',da_url,'tuesday','09:20'],
        ['da',da_url,'thursday','11:40'],
        ['da',da_url,'friday','14:25'],
        ['rmt',rmt_url,'monday','14:25'],
        ['rmt',rmt_url,'wednesday','11:40'],
        ['rmt',rmt_url,'friday','09:20'],
        ['gta',gta_url,'monday','11:40'],
        ['gta',gta_url,'wednesday','09:20'],
        ['gta',gta_url,'thursday','14:25'],
        ['cns',cns_url,'monday','09:20'],
        ['cns',cns_url,'tuesday','02:25'],
        ['cns',cns_url,'friday','11:40']]

        #this is not needed if default user is permitted into classroom
        user = '?pli=1&authuser=1'

        
        #creates the object only for classes of that day
        for c in classes:
            if datetime.datetime.now().weekday() == dayofweek(c[2]):
                class_ = subject(c[0],c[1]+user,c[2],c[3])
                class_.timetable()

        #exit()

        #scheduling the exit at 2:30pm everyday
        schedule.every().day.at('14:30').do(exit)

        #calls the scheduler
        while True:
            schedule.run_pending()
            time.sleep(1)

main()