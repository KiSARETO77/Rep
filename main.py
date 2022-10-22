import aminofix,samino
PP={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"}
Ç=aminofix.Client(proxies=PP)
Ç.login("K-HzT@wwjmp.com","GOKU12")
print("Ready")
@Ç.event("on_text_message")
def on_text_message(data: aminofix.objects.Event):
		MSG=data.message.content
		comId=data.comId
		chatId=data.message.chatId
		MSGID=data.message.messageId
		userId=data.message.author.userId
		if ("!REP") in MSG:
			if userId=="6704eb09-1786-4891-b210-c5aafb0c038e":
				try:
					C=samino.Client(proxies=PP)
					C.login("zx-@digdig.org","GOKU12")
					S=samino.Local(comId=comId,proxies=PP)
					X=S.get_video_rep_info(chatId=chatId).json
					C.login("K-HzT@wwjmp.com","GOKU12")
					S=samino.Local(comId=comId,proxies=PP)
					S.send_message(chatId=chatId,message=f"Rep : {X['availableReputation']}",replyTo=MSGID)
				except Exception as F:
					print(F)
					pass
