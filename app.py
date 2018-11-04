from kivy.app import App
from kivy.properties import StringProperty
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
import assistant
import texttospeech
import speechtotext
import recorder

class AssistantLayout(BoxLayout):
    user_text = StringProperty("cool")
    assistant_text = StringProperty("")

    def __init__(self, **kwargs):
        super(AssistantLayout, self).__init__(**kwargs)

    def speak(self):
        recorder.record_to_file("input.wav")
        print("recording finished: input.wav")
        self.user_text = speechtotext.listen("input.wav")
        print("speech to text: " + self.user_text)
        response = assistant.send_message(self.user_text)
        self.assistant_text = str(response[0])
        print("assistant responded: " + self.assistant_text)
        self.respond()

    def send(self):
        print(self.user_text)
        response = assistant.send_message(self.user_text)
        self.assistant_text = str(response[0])
        self.respond()

    def respond(self):
        texttospeech.speak(self.assistant_text)
        sound = SoundLoader.load('output.mp3')
        if sound:
            print("Sound found at %s" % sound.source)
            print("Sound is %.3f seconds" % sound.length)
            sound.play()

class AssistantApp(App):
    def build(self):
        assistant = AssistantLayout()
        #Clock.schedule_interval(assistant.update, 1.0)
        return assistant

AssistantApp().run()