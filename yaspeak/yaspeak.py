import requests

class YaSpeak:
    def __getattr__(self, speaker):
        return lambda *data: self.say(speaker, *data)
        
    def say(self, speaker, text="hello", file="out.mp3"):
        data = {"text": text}
        if speaker != "yandex": data.update({"speaker": speaker})
        output = requests.get("https://station.aimylogic.com/generate", data=data)
        with open(file, 'wb') as f:
            f.write(output.content)