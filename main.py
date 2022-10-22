import aminofix,samino
PP={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"}
comId,chatId=3434136,"59e378d4-1897-4e21-ab42-63861568727f"
Ç=aminofix.Client(proxies=PP)
Ç.login("K-HzT@wwjmp.com","GOKU12")
print("Ready")
@Ç.event("on_text_message")
def on_text_message(data: aminofix.objects.Event):
		MSG=data.message.content
		if ("!REP") in MSG:
			try:
				C=samino.Client(proxies=PP)
				C.login("zx-@digdig.org","GOKU12")
				S=samino.Local(comId=comId,proxies=PP)
				X=S.get_video_rep_info(chatId=chatId).json
				SUB=aminofix.SubClient(comId=comId,profile=Ç.profile)
				SUB.send_message(chatId=chatId,message=f"{X['availableReputation']}")
			except Exception as F:
				print(F)
				pass
