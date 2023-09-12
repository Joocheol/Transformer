from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class VoiceoverDemo(VoiceoverScene):
    def construct(self):
        # Initialize speech synthesis using Azure's TTS API
        self.set_speech_service(
            AzureService(
                #voice="en-US-AriaNeural",
                voice ="ko-KR-InJoonNeural",
                style="newscast-casual",  # global_speed=1.15
            )
        )


        rect = Rectangle(color=YELLOW).set_fill(YELLOW, opacity=1.0)
        self.play(Create(rect))

        self.wait()