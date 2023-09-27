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

        ba = Code(code=code_ba, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        ca = Code(code=code_ca, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        gsa = Code(code=code_gsa, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)
        csa = Code(code=code_csa, insert_line_no=False, background="window", language="python").rescale_to_fit(12,0)

        v = VGroup(ba.copy(), ca.copy(), gsa.copy(), csa.copy()).arrange(RIGHT).scale(0.2).to_edge(UP)

        self.add(v)

        self.play(ReplacementTransform(v[0].copy().background_mobject, csa.background_mobject))




        self.wait()




code_ba = """
class BaseAttention(tf.keras.layers.Layer):
  def __init__(self, **kwargs):
    super().__init__()
    self.mha = tf.keras.layers.MultiHeadAttention(**kwargs)
    self.layernorm = tf.keras.layers.LayerNormalization()
    self.add = tf.keras.layers.Add()




sample_csa = CausalSelfAttention(num_heads=2, key_dim=512)
    # continued                                                                .
"""

code_ca = """
class CrossAttention(BaseAttention):
  def call(self, x, context):
    attn_output, attn_scores = self.mha(
        query=x,
        key=context,
        value=context)

    x = self.add([x, attn_output])
    x = self.layernorm(x)
    return x

    # continued                                                                .
"""

code_gsa = """
class GlobalSelfAttention(BaseAttention):
  def call(self, x):
    attn_output = self.mha(
        query=x,
        value=x,
        key=x)

    x = self.add([x, attn_output])
    x = self.layernorm(x)
    return x

    # continued                                                                .
"""

code_csa = """
class CausalSelfAttention(BaseAttention):
  def call(self, x):
    attn_output = self.mha(
        query=x,
        value=x,
        key=x,
        use_causal_mask = True)
    x = self.add([x, attn_output])
    x = self.layernorm(x)
    return x

    # continued                                                                .
"""