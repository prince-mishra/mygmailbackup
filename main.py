import imaplib, getpass
def fetchMyMail():
	try:
		M = imaplib.IMAP4_SSL('imap.gmail.com',993)
		M.login('','')
		M.select()
		data = M.search(None, 'ALL')
		info = M.fetch(495, '(RFC822)')
		print info
		M.close()
		M.logout()
	except Exception, fault:
		raise fault
	return
if __name__=="__main__":
		try:
			print "hello"
			fetchMyMail()
		except Exception, fault:
			raise fault