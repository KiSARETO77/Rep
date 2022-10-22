import aminofix,samino
PP={"https":"http://dimatjasko10:KWJYs68q@185.112.13.43:2831"}
Ç=aminofix.Client(proxies=PP)
Ç.login("K-HzT@wwjmp.com","GOKU12")
print("Ready")
@Ç.event("on_text_message")
def on_text_message(data: aminofix.objects.Event):
		MSG=data.message.content
		if ("!REP") in MSG:
			C=samino.Client(proxies=PP)
			C.login("zx-@digdig.org","GOKU12")
			S=samino.Local(comId=3434136,proxies=PP)
			X=S.get_video_rep_info(chatId="59e378d4-1897-4e21-ab42-63861568727f").json
			SUB=aminofix.SubClient(comId=3434136,profile=Ç.profile)
			SUB.send_message(chatId="59e378d4-1897-4e21-ab42-63861568727f",message=f"{X['availableReputation']}")
