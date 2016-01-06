import curses
import time
import os


def timer(window):
    window.addstr('Hola! I will track how much time you spent coding or any other job you do.\n \n Just tell me when to start \n \n \n All I understand is, \n \t r - Resume/start timer \n \t p - Pause timer \n \t s - Stop timer & exit')
    
    if not os.path.exists('timer.txt'):
        a = open('timer.txt','w')
        a.write('0')
        a.close()
        
    f = open('timer.txt','r')
    u = 0
    j = 0
    
    f.seek(0)
    i =int(f.read())
    f.close()
    
    while(u == 0):
        hrs = str(i//(60*60))
        minu = str((i%(60*60))//60)
        sec = str((i%60))
    
        time1 = hrs+' : '+minu+' : ' +sec
        i+=1
        window.addstr(12, 30,time1+'\n\n\n> ')
        
        
        if(j != 0):
            window.nodelay(True)
        else:
            j = 1 
        
        
        l = open('timer.txt','w')
        l.truncate()
        l.write(str(i))
        l.close()
        
        curses.curs_set(0)
        k = window.getch()
        
        if(k in range(65, 90) or k in range(97, 122)):
            window.addstr(15, 2,unichr(k))
        
        
        if(k == 112):
            while(k != 114 or k != 115):
                window.nodelay(False)
                k = window.getch()
                                    
                if(k in range(65, 90) or k in range(97, 122)):
                    window.addstr(15, 2,unichr(k))
                if(k == 115 or k == 114):
                    break
               

        if (k == 115):
            f = open('timer.txt','w')
            f.truncate()
            f.write(str(i))
            f.close()
            u = 1
            print("\nWish you could stay a bit longer. See you soon!")
            time.sleep(2)
            
        time.sleep(1)
        
    
    

#if(os.name == 'nt'):
#    p = os.popen('attrib +h', 'timer.txt')

curses.wrapper(timer)
