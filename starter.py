from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class VoiceoverDemo(VoiceoverScene):
    def construct(self):
        # Initialize speech synthesis using Azure's TTS API
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                #voice ="ko-KR-InJoonNeural",
                style="newscast-casual",  # global_speed=1.15
            )
        )

        code = Code(
            file_name="Shakespeare.py",
            insert_line_no=False,
            background="window",
            language="python",
        ).rescale_to_fit(12, 0)

        voice = self.add_voiceover_text(
            """English"""
        )
        self.play(FadeIn(code.background_mobject), run_time=voice.duration)

        # with self.voiceover(
        #     text="""As you can see, Manim started playing this voiceover,
        #         right as the code object started to be drawn.
        #         Let's see some more examples."""
        # ):
        #     pass

        