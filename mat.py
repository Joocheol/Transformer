from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService

class VoiceoverDemo(VoiceoverScene):
    def construct(self):
        # Initialize speech synthesis using Azure's TTS API
        self.set_speech_service(
            AzureService(
                voice="en-US-JennyMultilingualNeural",
                style="newscast-casual",
            )
        )

        chars = Text("attention")
        chars_1 = Text("attentio?")
        # rect = Rectangle(color=YELLOW).set_fill(YELLOW, opacity=1.0).next_to(chars)
        

        with self.voiceover(
            text="""
            <lang xml:lang="ko-KR">attention 이라는 단어를 생각해보겠습니다.</lang><bookmark mark='A'/>
            <lang xml:lang="ko-KR">만약 여기까지만 보이면</lang><bookmark mark='B'/>
            <lang xml:lang="ko-KR">우리는 다음 글자가 무엇일지를 짐작할 수가 있죠.</lang><bookmark mark='C'/>
            <lang xml:lang="ko-KR">인공지능은 어떻게 다음 글자를 알 수가 있을까요?</lang>"""
        ) as tracker:
            
            self.play(
                Write(chars), run_time=tracker.time_until_bookmark("A", limit=1)
            )
            self.wait_until_bookmark("A")

            self.play(
                FadeOut(chars[-1]), run_time=tracker.time_until_bookmark("B", limit=1)
            )
            self.wait_until_bookmark("B")
            
            self.play(
                ReplacementTransform(chars[-1], chars_1[-1]), run_time=tracker.time_until_bookmark("C", limit=1)
            )
            self.wait_until_bookmark("C")

            for i in range(len(chars)):
                self.play(Transform(chars[i], chars[-1]), run_time=0.5)
            