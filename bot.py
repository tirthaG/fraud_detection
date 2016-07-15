black=0 #some value above which ips, users are said to be blacklisted
grey=0 #some value above which ips, users are said to be grey listed.

class IP:
	level=0
	def incGreylevel(val):
		print "ip->def incGreylevel():"
		self.level+=(val/2)

	def getGreylevel():
		print "ip->def getGreylevel():"

class User:
	level=0
	def incGreylevel(val):
		print "ip->def incGreylevel():"
		self.level+=val
	def getGreylevel():
		print "ip->def getGreylevel():"

class Session:
	ip=Ip()
	#info related to current session 
	#or any other ds to represent it
	def getIp():
		print "	def getIp():"
	def getUser():
		print "	def getUser():"
	def getUname():
		print "	def getUname():"
	def get Pwd():
		print "	def get Pwd():"

class BotDetect:
	lastP=""
	lastU=""
	currentP=""
	currentU=""

	lastDiff=0
	user=User()
	ip=Ip()
	
	def difference():
		print "	def difference():"
		#find difference between the last uname&pwd pair and the current one.
		diff=0
		#logic		
		return diff		
		
	def validate(Session T)
		self.ip=T.getIp()
		ipLevel=self.ip.getGreylevel()
	
		if ipLevel>=black:
			self.sendManualVerification()
		elif ipLevel>=grey:
			self.sendCaptcha() #as case 1			
		else:
			self.proceed(T)
			self.user=T.getUser()
			userLevel= self.user.getGreyLevel()
			if userLevel>=black:
				self.sendManualVerification()
			elif userLevel>=grey:
				self.sendCaptcha() #as case 2.1
			else:
				self.validateAttempt(T)

	def validateAttempt(Session T):
 		print "	def validateAttempt():"
		#listen to every failed attempt at login		
		#change prameters in T according to attempts (uname, pwd) pair	
		#for every attempt do the following
		transLevel=0
		self.currentU=T.getUname()		
		self.currrentP=T.getPwd()
		
		diff=self.difference()
		#build pattern with diff and lastDiff
		#change value "transLevel"	

		if transLevel>=black:
			self.sendManualVerification()		
		elif transLevel>=grey:
			self.sendCaptcha()
		#iterate
		
		#if successful attempt do:
		self.user=T.getUser()
		self.user.incGreyLevel(transLevel)
		self.ip.incGreyLevel(transLevel)

	def sendManualVerification():
		print "	def sendManualVerification():"
		#send instruction to membership grp for manual verification 

	def sendCaptcha():
		print "	def sendCaptcha()"
		#login using captcha in two cases
		#1. if the ip itself is grey listed
		#2. if the user is grey listed 
		#2.1 in the current transaction
		#2.2 due to previous history (irrespective of correct pwd, uname entry)

	def proceed(Session T):
		print "	def proceed():"
		#initial ip verification is over
		#move on to taking user inputs on forms
		#add attributes into T to reflect user actions

#listen to sessions
#if new session:
#send for validation
s=Session()
botDetect=BotDetect()
botDetect.validate(s)


