import curses,random
scr=curses.initscr()
curses.noecho()
curses.curs_set(0)
import robot_class
class robot1(robot_class.robot):
	def __init__(self,myscr):
		robot_class.robot.__init__(self,myscr)
	def no_mines(self,myscr):
		count=0
		for i in range(100):
			for j in range(30):
				if myscr.inch(j,i) & 255 == ord("M"):
					count+=1
		return count
curses.start_color()
cumscore=[0,0,0]
myscr=curses.newwin(30,100,0,0)
myscr.refresh()
myscr.border(0)
curses.init_pair(1,3,0)
curses.init_pair(2,4,0)
curses.init_pair(3,5,0)
curses.init_pair(4,1,0)
myscr.addstr(1,35,"ROBOT STRIKEv1.1",curses.color_pair(1))
myscr.addstr(3,3,"1.There is a robot, You can control it",curses.color_pair(2))
myscr.addstr(4,4,"with arrow keys",curses.color_pair(2))
myscr.addstr(5,3,"2.There are some defuse codes('C') which you")
myscr.addstr(6,4,"you need to collect before difusing bomb('B')")
myscr.addstr(7,3,"3.If you collect bomb before collecting ALL",curses.color_pair(2))
myscr.addstr(8,4,"the defuse codes bomb will explod",curses.color_pair(2))
myscr.addstr(9,3,"4.If your robot COLLIDES with the walls")
myscr.addstr(10,4,"game gets over and you loose")
myscr.addstr(11,3,"5.You get 10 points for collecting a defuse code",curses.color_pair(2))
myscr.addstr(12,3,"6.MIND IT... as LEVEL INCREASES game becomes more")
myscr.addstr(13,4,"difficult as there are more and more obstacles")
myscr.addstr(14,3,"7.If you touch these obstacles like MINES('M'), game gets over",curses.color_pair(2))
myscr.addstr(16,10," ARE TOU READY FOR THE ULTIMATE ACTION......",curses.color_pair(3))
myscr.addstr(17,10," PRESS ANY KEY TO START THE GAME",curses.color_pair(3))
myscr.addstr(19,3," AFTER LEVEL 1 LEVEL 2 WILL START IMMEDIATELY.... DON'T GET RELAXED ")
#myscr.addstr(30,35," DESIGNED BY KSHITIJ KANSAL ")
myscr.getch()
myscr.erase()
#curses.endwin()
level=1
#curses.color_pair(3)
while(level!=3):
	myscr=curses.newwin(30,100,0,0)
	myscr.refresh()
	myscr.nodelay(1)
	myscr.keypad(1)
	myscr.border(0)
	key=curses.KEY_RIGHT
	codes=4
	pos=[[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7]]
	mystr="  i i   [@ @] /|___|\\ d w b "
	pos1=pos
	if level==2:
		mines=3
		while mines!=0:
			c=[n for n in [random.randrange(1,99,1),random.randrange(1,29,1)] if n not in pos1]
			myscr.addch(c[1],c[0],'M')
			pos1.append(c)
			mines-=1
	while(codes!=0):
		c=[n for n in [random.randrange(1,99,1),random.randrange(1,29,1)] if n not in pos1]
		myscr.addch(c[1],c[0],'C',curses.color_pair(4))
		pos1.append(c)
		codes-=1
	c=[n for n in [random.randrange(1,99,1),random.randrange(1,29,1)] if n not in pos1]
	myscr.addch(c[1],c[0],'B')
	if level==1:
		robo=robot_class.robot(myscr)
	elif level==2:
		robo=robot1(myscr)
#	x=robo.check_code()
#	y=robo.check_bomb()
#	if x!=0:
#	 	if y==0:
#	 		break

	while key!=27:
		flag=0
	 	for_score=robo.check_code(myscr)
		myscr.addstr(0,2,"ScOrE: " + str((4-(for_score))*10))
		myscr.addstr(0,15,"DiFuSe cOdEs LeFt: " + str(for_score))
	#	x=robo.check(myscr)
		x=robo.check(myscr)
		y=robo.check_bomb(myscr)
		if x==1:
			#if y!=0:
			flag=1
			break
		if y==0:
			break
		z=robo.check_code(myscr)
		myscr.timeout(250+ ( (len(pos)-6) % 10- (len(pos)-6) ) * 3 )
		getkey=myscr.getch()
		if getkey==-1:
			key=key
		else :
			key=getkey
		if key==curses.KEY_RIGHT:
			if pos[6][0]+1==99:
				flag=1
				break
			if level==2:
				p=robo.no_mines(myscr)
				if p < 3:
					break
			pos=robo.move_RIGHT(pos,myscr)
		if key==curses.KEY_LEFT:
			if pos[0][0]-1==1:
				flag=1
		  		break
			if level==2:
				p=robo.no_mines(myscr)
				if p < 3:
					break
			pos=robo.move_LEFT(pos,myscr)
		if key==curses.KEY_UP:
			if pos[0][1]-1==1:
				flag=1
			    	break
			if level==2:
				p=robo.no_mines(myscr)
				if p < 3:
					break
			pos=robo.move_UP(pos,myscr)
		if key==curses.KEY_DOWN:
			if pos[27][1]+1==29:
				flag=1
				break
			if level==2:
				p=robo.no_mines(myscr)
				if p < 3:
					break
			pos=robo.move_DOWN(pos,myscr)
	cumscore[level]=(4-(for_score))*10
	if flag==1:
	  break
	level+=1
	
curses.endwin()
print
print "Game over"
print
print "Your score in level in" +" "+ str(1)+" : " + str(cumscore[1])
print 
print "Your score in level in"+" "+str(2)+ " : " + str(cumscore[2]) 
print 
print " $THANK YOU FOR PLAYING$ "
print "Designed by KSHITIJ KANSAL"
print 
