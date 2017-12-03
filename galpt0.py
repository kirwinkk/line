# -*- coding: utf-8 -*-
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json, codecs, threading, glob, subprocess, webbrowser, ConfigParser
import base64, mechanize, tweepy

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

galpt = ["uc772a6893813833e0e990044f6cac302"]
odim = ["uec041f0014147d4fc405d4473219d25e"]
gojaj = ["ua217af62cac6bea67a954a50e33d2467"]
pije = ["u00a6fde34d6ead9de4e67b5b81d4a1de"]
babori = ["u1ffd9a4ea001ba26dbbc18eb14eba497"]
saorej = ["u192b4dab6ca0077b74cb3f866f732bb6"]
amri = ["ud8c0a304522704b36e502e9e52c6aa0d"]
henkubik = ["uf8eb3d02fa19a4add5acf25cee675d48"]

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    	mes = Message()
    	mes.to, mes.from_ = to, profile.mid
    	mes.text = text
    	mes.contentType, mes.contentMetadata = contentType, contentMetadata
    	if to not in messageReq:
        	messageReq[to] = -1
    	messageReq[to] += 1
	client._client.sendMessage(messageReq[to], mes)

def NOTIFIED_ADD_CONTACT(op):
    try:
        sendMessage(op.param1, client.getContact(op.param1).displayName + " 1")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ADD_CONTACT\n\n")
        return

tracer.addOpInterrupt(5,NOTIFIED_ADD_CONTACT)

def NOTIFIED_ACCEPT_GROUP_INVITATION(op):
    #print op
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + " 1")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_ACCEPT_GROUP_INVITATION\n\n")
        return

tracer.addOpInterrupt(17,NOTIFIED_ACCEPT_GROUP_INVITATION)

def NOTIFIED_KICKOUT_FROM_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param3).displayName + " 1")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_KICKOUT_FROM_GROUP\n\n")
        return

tracer.addOpInterrupt(19,NOTIFIED_KICKOUT_FROM_GROUP)

def NOTIFIED_LEAVE_GROUP(op):
    try:
        sendMessage(op.param1, client.getContact(op.param2).displayName + " 1")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return

tracer.addOpInterrupt(15,NOTIFIED_LEAVE_GROUP)

def NOTIFIED_READ_MESSAGE(op):
    #print op
    try:
        if op.param1 in wait['readPoint']:
            Name = client.getContact(op.param2).displayName
            if Name in wait['readMember'][op.param1]:
                pass
            else:
                wait['readMember'][op.param1] += "\n・" + Name
                wait['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

tracer.addOpInterrupt(55, NOTIFIED_READ_MESSAGE)

def RECEIVE_MESSAGE(op):
    msg = op.message
    try:
        if msg.contentType == 0:
            try:
                if msg.to in wait['readPoint']:
                    if msg.from_ in wait["ROM"][msg.to]:
                        del wait["ROM"][msg.to][msg.from_]
               	else:
                   	pass
      	    except:
               	pass
        else:
            pass
	if msg.text == ".mid":
                sendMessage(msg.to, msg.to)
	if msg.text == ".m?":
                sendMessage(msg.to, msg.to)
        if msg.text == ".me":
                sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
        if msg.text == ".gift":
                sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
	if msg.text in [".time"]:
                sendMessage(msg.to, datetime.datetime.today().strftime(' %Y-%m-%d %H:%M:%S'))
	if (".enc " in msg.text):
		enc = msg.text.replace(".enc ","")
		enc0 = enc.encode('base64','strict')
		enc1 = enc0.encode('base64','strict')
		enc2 = enc1.encode('base64','strict')
		enc3 = enc2.encode('base64','strict')
		enc4 = enc3.encode('base64','strict')
		enc5 = enc4.encode('base64','strict')
		enc6 = enc5.encode('base64','strict')
		enc7 = enc6.encode('base64','strict')
		enc8 = enc7.encode('base64','strict')
		enc9 = enc8.encode('base64','strict')
		enc10 = enc9.encode('base64','strict')
		sendMessage(msg.to, "" + enc10)
	if (".dec " in msg.text):
		dec = msg.text.replace(".dec ","")
		dec0 = dec.decode('base64','strict')
		dec1 = dec0.decode('base64','strict')
		dec2 = dec1.decode('base64','strict')
		dec3 = dec2.decode('base64','strict')
		dec4 = dec3.decode('base64','strict')
		dec5 = dec4.decode('base64','strict')
		dec6 = dec5.decode('base64','strict')
		dec7 = dec6.decode('base64','strict')
		dec8 = dec7.decode('base64','strict')
		dec9 = dec8.decode('base64','strict')
		dec10 = dec9.decode('base64','strict')
		sendMessage(msg.to, "" + dec10)
	if msg.text == ".about":
		sendMessage(msg.to, "ABOUT\n======\nInstagram: gal.pt\n[https://www.instagram.com/gal.pt]\n======\nEmail: galih6juli@gmail.com")
	if msg.text == ".?":
		sendMessage(msg.to, "COMMANDS\n[.?]\n======\n\nPRIVATE\n======\n[.mid] ~ Show MID\n[.me] ~ Show your own contact\n[.gift] ~ Send a gift\n[.time] ~ Show current time\n[(dot)enc] ~ Encode text message\n[(dot)dec] ~ Decode text message\n[.about] ~ Show script's information\n[.?] ~ Show commands\n\nPUBLIC\n======\n[.mid] ~ Show your own MID\n[.gid] ~ Show the group's ID\n[.ginfo] ~ Show the group's info\n[.gname] ~ Change the group's name\n[.gurl] ~ Show the group's URL\n[.gopen] ~ Enable invite to group by URL\n[.gclose] ~ Disable invite to group by URL\n[.ginv] ~ Invite to group using MID\n[.gcancel] ~ Cancel all the group's pending invitations\n[.me] ~ Show your own contact\n[.show] ~ Show a contact by MID\n[.time] ~ Show current time\n[.gift] ~ Send a gift\n[.gtag] ~ Tag all the group's members\n[.about] ~ Show script's information\n[.s] ~ Set a ReadPoint to a group\n[.r] ~ Show reads using the last ReadPoint\n\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " {gal.pt}")
              	    else:
                   	pass
		else:
                    pass
	if msg.toType == 2:
        	if msg.contentType == 0:
                	if msg.text == ".mid":
                    		sendMessage(msg.to, msg.from_)
                	if msg.text == ".gid":
                    		sendMessage(msg.to, msg.to)
                	if msg.text == ".ginfo":
                    		group = client.getGroup(msg.to)
                    		md = "[Group Name]\n" + group.name + "\n\n[GID]\n" + group.id + "\n\n[Group Picture]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    		if group.preventJoinByTicket is False: md += "\n\nInvitation URL: Permitted\n"
                    		else: md += "\n\nInvitation URL: Refused\n"
                    		if group.invitee is None: md += "\nMembers: " + str(len(group.members)) + "\n\nInviting: 0"
                    		else: md += "\nMembers: " + str(len(group.members)) + "\nInvited: " + str(len(group.invitee)) + ""
                    		sendMessage(msg.to,md)
                	if (".gname " in msg.text):
				if msg.from_ in galpt:
					if msg.toType == 2:
						X = client.getGroup(msg.to)
						X.name = msg.text.replace(".gname ","")
						client.updateGroup(X)
					else:
						client.sendText(msg.to,"0")
                	if msg.text == ".gurl":
                    		sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to))
                	if msg.text == ".gopen":
                    		group = client.getGroup(msg.to)
                    		if group.preventJoinByTicket == False:
                        		sendMessage(msg.to, "0")
                    		else:
                        		group.preventJoinByTicket = False
                        		client.updateGroup(group)
                        		sendMessage(msg.to, "1")
                	if msg.text == ".gclose":
                    		group = client.getGroup(msg.to)
                    		if group.preventJoinByTicket == True:
                        		sendMessage(msg.to, "0")
                    		else:
                        		group.preventJoinByTicket = True
                        		client.updateGroup(group)
                        		sendMessage(msg.to, "1")
                	if ".k" in msg.text:
                    		if msg.from_ in galpt:
		    			nk0 = msg.text.replace(".k ","")
		    			nk1 = nk0.lstrip()
		    			nk2 = nk1.replace("@","")
		    			nk3 = nk2.rstrip()
		    			_name = nk3
		    			gs = client.getGroup(msg.to)
		    			targets = []
		    			for s in gs.members:
						if _name in s.displayName:
			    				targets.append(s.mid)
		    				if targets == []:
							pass
		    				else:
							for target in targets:
			    					try:
									client.kickoutFromGroup(msg.to,[target])
									print (msg.to,[g.mid])
			    					except:
									client.sendText(msg.to,"1")
                	if msg.text == ".gcancel":
                    		group = client.getGroup(msg.to)
                    		if group.invitee is None:
                        		sendMessage(op.message.to, "No one is inviting.")
                    		else:
                        		gInviMids = [contact.mid for contact in group.invitee]
                        		client.cancelGroupInvitation(msg.to, gInviMids)
                        		sendMessage(msg.to, str(len(group.invitee)) + " Done")
                	if ".ginv " in msg.text:
                    		key = msg.text[-33:]
                    		client.findAndAddContactsByMid(key)
                    		client.inviteIntoGroup(msg.to, [key])
                    		contact = client.getContact(key)
                	if msg.text == ".me":
                    		M = Message()
                    		M.to = msg.to
                    		M.contentType = 13
                    		M.contentMetadata = {'mid': msg.from_}
                    		client.sendMessage(M)
                	if ".show " in msg.text:
                    		key = msg.text[-33:]
                    		sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    		contact = client.getContact(key)
                    		sendMessage(msg.to, ""+contact.displayName+"'s contact")
                	if msg.text == ".time":
                    		sendMessage(msg.to, datetime.datetime.today().strftime(' %Y-%m-%d %H:%M:%S'))
			if msg.text == ".gift":
				sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
			if msg.text == ".gtag":
				group = client.getGroup(msg.to)
				nama = [contact.mid for contact in group.members]

				cb = ""
				cb2 = ""
				strt = int(0)
				akh = int(0)
				for md in nama:
		    			akh = akh + int(6)

		    			cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

		    			strt = strt + int(7)
		    			akh = akh + 1
		    			cb2 += "@nrik \n"

				cb = (cb[:int(len(cb)-1)])
				msg.contentType = 0
				msg.text = cb2
				msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

				try:
		    			client.sendMessage(msg)
				except Exception as error:
		    			print error
			if msg.text == ".about":
				sendMessage(msg.to, "ABOUT\n======\nInstagram: gal.pt\n[https://www.instagram.com/gal.pt]\n======\nEmail: galih6juli@gmail.com")
                	if msg.text == ".s":
                    		sendMessage(msg.to, "1")
                    		try:
                        		del wait['readPoint'][msg.to]
                        		del wait['readMember'][msg.to]
                    		except:
                        		pass
                    		wait['readPoint'][msg.to] = msg.id
                    		wait['readMember'][msg.to] = ""
                    		wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    		wait['ROM'][msg.to] = {}
                    		print wait
                	if msg.text == ".r":
                    		if msg.to in wait['readPoint']:
                        		if wait["ROM"][msg.to].items() == []:
                            			chiya = ""
                        		else:
                            			chiya = ""
                            			for rom in wait["ROM"][msg.to].items():
                                			print rom
                                			chiya += rom[1] + "\n"

                        		sendMessage(msg.to, "Read by %s\n\nSider(s)\n%s\nMarked:\n%s\n\nUpdated:\n" % (wait['readMember'][msg.to],chiya,setTime[msg.to]) + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
                    		else:
                        		sendMessage(msg.to, "0")
                	else:
                    		pass
        	else:
            		pass
    except KeyboardInterrupt:
	   sys.exit(0)
    except Exception as error:
        print error
        print ("\n\nRECEIVE_MESSAGE\n\n")
        return

tracer.addOpInterrupt(26, RECEIVE_MESSAGE)

global _delay
_delay = 5
delay = _delay

class AskFM1:
    def __init__(self, username, delay=5):
        self.username = username
        self.delay = delay

    def ask_question(self, q, count):
        n = 0
	eta = self.delay * int(count)
        print self.format_eta(eta)
        while n < int(count):
            br = mechanize.Browser()
            br.open("http://ask.fm/" + self.username)

            for form in br.forms():
                if form.attrs['id'] == "question_form":
                    br.form = form
                    break
            br.form['question[question_text]'] = q
            br.submit()	
	n += 1
        print "Question submitted."
        time.sleep(self.delay)

    def format_eta(self, eta):
        if eta > 60:
            return "ETA: " + str(eta / 60) + "m"
        else:
            return "ETA: " + str(eta) + "s"

class AskFM2:
    def __init__(self, username, delay=5):
        self.username = username
        self.delay = delay

    def ask_question(self, q, count):
        n = 0
        eta = self.delay * int(count)
        print self.format_eta(eta)
        while n < int(count):
            br = mechanize.Browser()
            br.open("http://ask.fm/" + self.username)

            for form in br.forms():
                if form.attrs['id'] == "question_form":
                    br.form = form
                    break
            br.form['question[question_text]'] = q
            br.submit()
	n += 1
        print "Question submitted."
        time.sleep(self.delay)

    def format_eta(self, eta):
        if eta > 60:
            return "ETA: " + str(eta / 60) + "m"
        else:
            return "ETA: " + str(eta) + "s"

def SEND_MESSAGE(op):
	global username
	global question
	global data
	global count
	msg = op.message
    	try:
        	if msg.toType == 0:
            		if msg.contentType == 0:
                		if msg.text == ".mid":
                    			sendMessage(msg.to, msg.to)
				if msg.text == ".m?":
                    			sendMessage(msg.to, msg.to)
                		if msg.text == ".me":
                    			sendMessage(msg.to, text=None, contentMetadata={'mid': msg.from_}, contentType=13)
                		if msg.text == ".gift":
                    			sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
				if msg.text == ".time":
                    			sendMessage(msg.to, datetime.datetime.today().strftime(' %Y-%m-%d %H:%M:%S'))
				if (".enc " in msg.text):
		   			enc = msg.text.replace(".enc ","")
					enc0 = enc.encode('base64','strict')
					enc1 = enc0.encode('base64','strict')
					enc2 = enc1.encode('base64','strict')
					enc3 = enc2.encode('base64','strict')
					enc4 = enc3.encode('base64','strict')
					enc5 = enc4.encode('base64','strict')
					enc6 = enc5.encode('base64','strict')
					enc7 = enc6.encode('base64','strict')
					enc8 = enc7.encode('base64','strict')
					enc9 = enc8.encode('base64','strict')
					enc10 = enc9.encode('base64','strict')
		   			sendMessage(msg.to, "" + enc10)
				if (".dec " in msg.text):
		   			dec = msg.text.replace(".dec ","")
					dec0 = dec.decode('base64','strict')
					dec1 = dec0.decode('base64','strict')
					dec2 = dec1.decode('base64','strict')
					dec3 = dec2.decode('base64','strict')
					dec4 = dec3.decode('base64','strict')
					dec5 = dec4.decode('base64','strict')
					dec6 = dec5.decode('base64','strict')
					dec7 = dec6.decode('base64','strict')
					dec8 = dec7.decode('base64','strict')
					dec9 = dec8.decode('base64','strict')
					dec10 = dec9.decode('base64','strict')
		   			sendMessage(msg.to, "" + dec10)
				if msg.text == ".askfm":
					sendMessage(msg.to, "FORMAT\n======\n[.u {username}] ~ Enter the username\n[.q {question}] ~ Enter the question to be asked\n[.qsend] ~ Send question\n[.chkfmt] ~ Check information")
				if msg.text == ".chkfmt":
					sendMessage(msg.to, "Username: @" + username + "\nQuestion: " + "" + question)
				if msg.text == ".chkfmt.":
					if msg.from_ in galpt:
						sendMessage(msg.to, "Username: @" + username + "\nQuestion: " + "" + question + "\nTotal: " + "" + count)
				if (".u. " in msg.text):
					if msg.from_ in galpt:
						username = msg.text.replace(".u. ","")
						data = AskFM1(username)
				if (".q. " in msg.text):
					if msg.from_ in galpt:
						question = msg.text.replace(".q. ","")
				if (".c. " in msg.text):
					if msg.from_ in galpt:
						count = msg.text.replace(".c. ","")
    				if msg.text == ".qsend.":
					if msg.from_ in galpt:
        					data.ask_question(question, int(count))
				if (".u " in msg.text):
					username = msg.text.replace(".u ","")
					data = AskFM2(username)
				if (".q " in msg.text):
					question = msg.text.replace(".q ","")
    				if msg.text == ".qsend":
        				data.ask_question(question)
				if msg.text == ".chk1":
					if msg.from_ in galpt:
						odim.sendMessage(msg.to, "ok")
				if msg.text == ".about":
					sendMessage(msg.to, "ABOUT\n======\nInstagram: gal.pt\n[https://www.instagram.com/gal.pt]\n======\nEmail: galih6juli@gmail.com")
				if msg.text == ".?":
					sendMessage(msg.to, "COMMANDS\n[.?]\n======\n\nPRIVATE\n======\n[.mid] ~ Show MID\n[.me] ~ Show your own contact\n[.gift] ~ Send a gift\n[.time] ~ Show current time\n[(dot)enc] ~ Encode text message\n[(dot)dec] ~ Decode text message\n[.about] ~ Show script's information\n[.?] ~ Show commands\n\nPUBLIC\n======\n[.mid] ~ Show your own MID\n[.gid] ~ Show the group's ID\n[.ginfo] ~ Show the group's info\n[.gname] ~ Change the group's name\n[.gurl] ~ Show the group's URL\n[.gopen] ~ Enable invite to group by URL\n[.gclose] ~ Disable invite to group by URL\n[.ginv] ~ Invite to group using MID\n[.gcancel] ~ Cancel all the group's pending invitations\n[.me] ~ Show your own contact\n[.show] ~ Show a contact by MID\n[.time] ~ Show current time\n[.gift] ~ Send a gift\n[.gtag] ~ Tag all the group's members\n[.about] ~ Show script's information\n[.s] ~ Set a ReadPoint to a group\n[.r] ~ Show reads using the last ReadPoint\n\n" + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S') + " {gal.pt}")
                		else:
                    			pass
            		else:
                		pass
        	if msg.toType == 2:
            		if msg.contentType == 0:
                		if msg.text == ".mid":
                    			sendMessage(msg.to, msg.from_)
                		if msg.text == ".gid":
                    			sendMessage(msg.to, msg.to)
                		if msg.text == ".ginfo":
                    			group = client.getGroup(msg.to)
                    			md = "[Group Name]\n" + group.name + "\n\n[GID]\n" + group.id + "\n\n[Group Picture]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    			if group.preventJoinByTicket is False: md += "\n\nInvitation URL: Permitted\n"
                    			else: md += "\n\nInvitation URL: Refused\n"
                    			if group.invitee is None: md += "\nMembers: " + str(len(group.members)) + "\n\nInviting: 0"
                    			else: md += "\nMembers: " + str(len(group.members)) + "\nInvited: " + str(len(group.invitee)) + ""
                    			sendMessage(msg.to,md)
                		if (".gname " in msg.text):
					if msg.from_ in galpt:
						if msg.toType == 2:
							X = client.getGroup(msg.to)
							X.name = msg.text.replace(".gname ","")
							client.updateGroup(X)
						else:
							client.sendText(msg.to,"0")
                		if msg.text == ".gurl":
                    			sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to))
                		if msg.text == ".gopen":
                    			group = client.getGroup(msg.to)
                    			if group.preventJoinByTicket == False:
                        			sendMessage(msg.to, "0")
                    			else:
                        			group.preventJoinByTicket = False
                        			client.updateGroup(group)
                        			sendMessage(msg.to, "1")
                		if msg.text == ".gclose":
                    			group = client.getGroup(msg.to)
                    			if group.preventJoinByTicket == True:
                        			sendMessage(msg.to, "0")
                    			else:
                        			group.preventJoinByTicket = True
                        			client.updateGroup(group)
                        			sendMessage(msg.to, "1")
                		if ".k" in msg.text:
                    			if msg.from_ in galpt:
		    				nk0 = msg.text.replace(".k ","")
		    				nk1 = nk0.lstrip()
		    				nk2 = nk1.replace("@","")
		    				nk3 = nk2.rstrip()
		    				_name = nk3
		    				gs = client.getGroup(msg.to)
		    				targets = []
		    				for s in gs.members:
							if _name in s.displayName:
			    					targets.append(s.mid)
		    					if targets == []:
								pass
		    					else:
								for target in targets:
			    						try:
										client.kickoutFromGroup(msg.to,[target])
										print (msg.to,[g.mid])
			    						except:
										client.sendText(msg.to,"1")
                		if msg.text == ".gcancel":
                    			group = client.getGroup(msg.to)
                    			if group.invitee is None:
                        			sendMessage(op.message.to, "No one is inviting.")
                    			else:
                        			gInviMids = [contact.mid for contact in group.invitee]
                        			client.cancelGroupInvitation(msg.to, gInviMids)
                        			sendMessage(msg.to, str(len(group.invitee)) + " Done")
                		if ".ginv " in msg.text:
                    			key = msg.text[-33:]
                    			client.findAndAddContactsByMid(key)
                    			client.inviteIntoGroup(msg.to, [key])
                    			contact = client.getContact(key)
                		if msg.text == ".me":
                    			M = Message()
                    			M.to = msg.to
                    			M.contentType = 13
                    			M.contentMetadata = {'mid': msg.from_}
                    			client.sendMessage(M)
                		if ".show " in msg.text:
                    			key = msg.text[-33:]
                    			sendMessage(msg.to, text=None, contentMetadata={'mid': key}, contentType=13)
                    			contact = client.getContact(key)
                    			sendMessage(msg.to, ""+contact.displayName+"'s contact")
                		if msg.text == ".time":
                    			sendMessage(msg.to, datetime.datetime.today().strftime(' %Y-%m-%d %H:%M:%S'))
				if msg.text == ".gift":
					sendMessage(msg.to, text="gift sent", contentMetadata=None, contentType=9)
				if msg.text == ".gtag":
					group = client.getGroup(msg.to)
					nama = [contact.mid for contact in group.members]

					cb = ""
					cb2 = ""
					strt = int(0)
					akh = int(0)
					for md in nama:
		    				akh = akh + int(6)

		    				cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

		    				strt = strt + int(7)
		    				akh = akh + 1
		    				cb2 += "@nrik \n"

					cb = (cb[:int(len(cb)-1)])
					msg.contentType = 0
					msg.text = cb2
					msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

					try:
		    				client.sendMessage(msg)
					except Exception as error:
		    				print error
				if msg.text == ".about":
					sendMessage(msg.to, "ABOUT\n======\nInstagram: gal.pt\n[https://www.instagram.com/gal.pt]\n======\nEmail: galih6juli@gmail.com")
                		if msg.text == ".s":
                    			sendMessage(msg.to, "1")
                    			try:
                        			del wait['readPoint'][msg.to]
                        			del wait['readMember'][msg.to]
                    			except:
                        			pass
                    			wait['readPoint'][msg.to] = msg.id
                    			wait['readMember'][msg.to] = ""
                    			wait['setTime'][msg.to] = datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                    			wait['ROM'][msg.to] = {}
                    			print wait
                		if msg.text == ".r":
                    			if msg.to in wait['readPoint']:
                        			if wait["ROM"][msg.to].items() == []:
                            				chiya = ""
                        			else:
                            				chiya = ""
                            				for rom in wait["ROM"][msg.to].items():
                                				print rom
                                				chiya += rom[1] + "\n"

                        			sendMessage(msg.to, "Read by %s\n\nSider(s)\n%s\nMarked:\n%s\n\nUpdated:\n" % (wait['readMember'][msg.to],chiya,setTime[msg.to]) + datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
                    			else:
                        			sendMessage(msg.to, "0")
                		else:
                    			pass
        		else:
            			pass
	
    	except Exception as e:
        	print e
        	print ("\n\nSEND_MESSAGE\n\n")
        	return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    	tracer.execute()
