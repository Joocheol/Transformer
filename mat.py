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

        m = setup_3()

        

        

        with self.voiceover(
            text="""
            <lang xml:lang="ko-KR">attention 이라는 단어를 생각해보겠습니다.</lang><bookmark mark='A'/>
            <lang xml:lang="ko-KR">만약 여기까지만 보이면</lang><bookmark mark='B'/>
            <lang xml:lang="ko-KR">우리는 다음 글자가 무엇일지를 짐작할 수가 있죠.</lang><bookmark mark='C'/>
            <lang xml:lang="ko-KR">인공지능은 어떻게 다음 글자를 알 수가 있을까요?</lang>"""
        ) as tracker:
            
            self.play(Write(m[0]))

            self.wait(10)


def setup_3():
    vg_1 = VGroup()
    vg_2 = VGroup()
    vg_3 = VGroup()

    box = Rectangle(height=0.4, width=1.2)

    text = "[START] je suis etudiant I am a student [END]".split()
    text = [Tex(i).scale(0.6) for i in text]

    for i in [0,1,2,3,-1]:
        temp = VGroup(text[i].copy(), box.copy())
        vg_1.add(temp)

    for i in [0,4,5,6,7]:
        temp = VGroup(text[i].copy(), box.copy())
        vg_2.add(temp)

    for i in [4,5,6,7,8]:
        temp = VGroup(text[i].copy(), box.copy())
        vg_3.add(temp)

    vg_1.arrange(DOWN, buff=0).rotate(PI/2)
    vg_2.arrange(DOWN, buff=0).rotate(PI/2)
    vg_3.arrange(DOWN, buff=0).rotate(PI/2)

    return vg_1, vg_2, vg_3

            