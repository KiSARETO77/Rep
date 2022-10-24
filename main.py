import aminofix,samino
from aminofix import Client as Ç
from samino import Client as C
from samino import Local as S
PP={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"}
Ç=Ç(proxies=PP)
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
			if userId=="ecc5df17-3042-4a78-9e68-d409fee1912c":
				if chatId=="0029e51c-6490-480c-9205-b70e262a16d1":
					try:
						C=C(proxies=PP)
						C.login("au-@digdig.org","GOKU12")
						S=S(comId=comId,proxies=PP)
						X=S.get_video_rep_info(chatId=chatId).json
						C.login("K-HzT@wwjmp.com","GOKU12")
						S=samino.Local(comId=comId,proxies=PP)
						S.join_chat(chatId=chatId)
						S.send_message(chatId=chatId,message=f"Rep : {X['availableReputation']}",replyTo=MSGID)
					except Exception as F:
						print(F)
						pass
