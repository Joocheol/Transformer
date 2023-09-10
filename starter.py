from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.azure import AzureService


class VoiceoverDemo(VoiceoverScene):
    def construct(self):
        # Initialize speech synthesis using Azure's TTS API
        self.set_speech_service(
            AzureService(
                voice="en-US-AriaNeural",
                style="newscast-casual",  # global_speed=1.15
            )
        )

        demo_code = Code(
            file_name="Shakespeare.py",
            insert_line_no=False,
            background="window",
            language="python",
        ).rescale_to_fit(12, 0)

        tracker = self.add_voiceover_text(
            """AI generated voices have become realistic
                enough for use in most content. Using neural
                text-to-speech frees you from the painstaking
                process of recording and manually syncing
                audio to your video."""
        )
        self.play(Write(demo_code), run_time=tracker.duration)

        with self.voiceover(
            text="""As you can see, Manim started playing this voiceover,
                right as the code object started to be drawn.
                Let's see some more examples."""
        ):
            pass

        