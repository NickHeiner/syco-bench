# Advances in Joint CTC-Attention based End-to-End Speech Recognition with a Deep CNN Encoder and RNN-LM

**Authors:** Takaaki Hori, Shinji Watanabe, Yu Zhang, William Chan

**arXiv:1706.02737** (cs.CL; cs.SD; eess.AS) — Submitted 8 Jun 2017

## Abstract

We present a state-of-the-art end-to-end Automatic Speech Recognition (ASR) model. We learn to listen and write characters with a joint Connectionist Temporal Classification (CTC) and attention-based encoder-decoder network. The encoder is a deep Convolutional Neural Network (CNN) based on the VGG network. The CTC network sits on top of the encoder and is jointly trained with the attention-based decoder. During the beam search process, we combine the CTC predictions, the attention-based decoder predictions and a separately trained LSTM language model. We achieve a 5-10% error reduction compared to prior systems on spontaneous Japanese and Chinese speech, and our end-to-end model beats out traditional hybrid ASR systems.

Subjects: Computation and Language (cs.CL); Sound (cs.SD); Audio and Speech Processing (eess.AS).
