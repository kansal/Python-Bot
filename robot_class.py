class robot():
	pos=[[2,4],[3,4],[4,4],[5,4],[6,4],[7,4],[8,4],[2,5],[3,5],[4,5],[5,5],[6,5],[7,5],[8,5],[2,6],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[2,7],[3,7],[4,7],[5,7],[6,7],[7,7],[8,7]]
	mystr="  i i   [@ @] /|___|\\ d w b "
	def __init__(self,myscr):
		for i in range(28):
			myscr.addch(self.pos[i][1],self.pos[i][0],self.mystr[i])
			#pos1=pos
		
	def move_RIGHT(self,pos,myscr):
		for i in range(7):
			#curses.color_pair(random.randint(1,50))
			myscr.addch(pos[6-i][1],pos[6-i][0],' ')
			pos[6-i][0]+=1
			myscr.addch(pos[6-i][1],pos[6-i][0],self.mystr[6-i])
			myscr.addch(pos[13-i][1],pos[13-i][0],' ')
			pos[13-i][0]+=1
			myscr.addch(pos[13-i][1],pos[13-i][0],self.mystr[13-i])
			myscr.addch(pos[20-i][1],pos[20-i][0],' ')
			pos[20-i][0]+=1
			myscr.addch(pos[20-i][1],pos[20-i][0],self.mystr[20-i])
			myscr.addch(pos[27-i][1],pos[27-i][0],' ')
			pos[27-i][0]+=1
			myscr.addch(pos[27-i][1],pos[27-i][0],self.mystr[27-i])
		return pos
	def move_LEFT(self,pos,myscr):
		for i in range(7):	
			myscr.addch(pos[i][1],pos[i][0],' ')
			pos[i][0]-=1
			myscr.addch(pos[i][1],pos[i][0],self.mystr[i])
			myscr.addch(pos[7+i][1],pos[7+i][0],' ')
			pos[7+i][0]-=1
			myscr.addch(pos[7+i][1],pos[7+i][0],self.mystr[7+i])
			myscr.addch(pos[14+i][1],pos[14+i][0],' ')
			pos[14+i][0]-=1
			myscr.addch(pos[14+i][1],pos[14+i][0],self.mystr[14+i])
			myscr.addch(pos[21+i][1],pos[21+i][0],' ')
			pos[21+i][0]-=1
			myscr.addch(pos[21+i][1],pos[21+i][0],self.mystr[21+i])
		return pos
	def move_UP(self,pos,mysc):
		for i in range(28):
			mysc.addch(pos[i][1],pos[i][0],' ')
			pos[i][1]-=1
			mysc.addch(pos[i][1],pos[i][0],self.mystr[i])
		return pos
	def move_DOWN(self,pos,myscr):			
		for i in range(28):
			myscr.addch(pos[27-i][1],pos[27-i][0],' ')
			pos[27-i][1]+=1
			myscr.addch(pos[27-i][1],pos[27-i][0],self.mystr[27-i])
		return pos
	def check_code(self,myscr):
		count=0
		for i in range(100):
			for j in range(30):
				if myscr.inch(j,i) & 255 == ord('C'):
					count+=1
		return count
	def check_bomb(self,myscr):
		count=0
		for i in range(100):
			for j in range(30):
				if myscr.inch(j,i) & 255 == ord('B'):
					count+=1
		return count
	def check(self,myscr):
		x=self.check_code(myscr)
		y=self.check_bomb(myscr)
		if x!=0:
			if y==0:
				return 1
		return 0
#class robot1(robot):
#	def no_mines(self,myscr):
#		count=0
#		for i in range(60):
#			for j in range(20):
#				if myscr.inch(j,i) & 255 == ord("M"):
#					count+=1
		#return count
