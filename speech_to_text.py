import speech_recognition as sr

r=sr.Recognizer()

t=0

with sr.Microphone() as source:
	print('Speak English :')
	
	while t==0:
		audio =r.listen(source)
		try:
			text =r.recognize_google(audio)
			print('you said :{}'.format(text))
			t=1

		except:
			print('Not understable')
			print('Try again')
			t==0


	