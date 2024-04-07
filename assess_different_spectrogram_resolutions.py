from utils import save_wav_to_file, load_wav_file
import torch
import torchaudio
import random

DEVICE = "cpu"
genre = "classical"
random_i = random.randint(10, 99)
random_wav = "GTZAN/{}/{}.000{}.wav".format(genre, genre, random_i)
print("Loading {}...".format(random_wav))
wav = load_wav_file(random_wav)

GTZAN_SAMPLE_RATE = 22050
N_MELS = 256
N_FFTS = 2586 * 2
SPEC_TRANSFORM = torchaudio.transforms.MelSpectrogram(sample_rate=GTZAN_SAMPLE_RATE, n_mels=N_MELS, n_fft=N_FFTS)

print("Transforming to spec...")
spec = SPEC_TRANSFORM(wav).to(DEVICE)
if spec.shape[1] != 256 or spec.shape[2] != 256:
    print(spec.shape)
    exit()

print("Inverting Mel Scale...")
inverse_transform = torchaudio.transforms.InverseMelScale(n_mels=N_MELS, sample_rate=GTZAN_SAMPLE_RATE, n_stft=int((N_FFTS//2)+1)).to(DEVICE)
spec = inverse_transform(spec)
print("Converting to waveform...")
grifflim_transform = torchaudio.transforms.GriffinLim(n_fft=N_FFTS).to(DEVICE)
reconstructed_wav = grifflim_transform(spec)

reconstructed_wav = torch.unsqueeze(reconstructed_wav, dim=0)
print("Saving to file...")
save_wav_to_file(reconstructed_wav, "test_256x256.wav")


N_MELS = 512
N_FFTS = 2586
SPEC_TRANSFORM = torchaudio.transforms.MelSpectrogram(sample_rate=GTZAN_SAMPLE_RATE, n_mels=N_MELS, n_fft=N_FFTS)

print("Transforming to spec...")
spec = SPEC_TRANSFORM(wav).to(DEVICE)
if spec.shape[1] != 512 or spec.shape[2] != 512:
    print(spec.shape)
    exit()

print("Inverting Mel Scale...")
inverse_transform = torchaudio.transforms.InverseMelScale(n_mels=N_MELS, sample_rate=GTZAN_SAMPLE_RATE, n_stft=int((N_FFTS//2)+1)).to(DEVICE)
spec = inverse_transform(spec)
print("Converting to waveform...")
grifflim_transform = torchaudio.transforms.GriffinLim(n_fft=N_FFTS).to(DEVICE)
reconstructed_wav = grifflim_transform(spec)

reconstructed_wav = torch.unsqueeze(reconstructed_wav, dim=0)
print("Saving to file...")
save_wav_to_file(reconstructed_wav, "test_512x512.wav")



N_MELS = 1024
N_FFTS = 2586 // 2
SPEC_TRANSFORM = torchaudio.transforms.MelSpectrogram(sample_rate=GTZAN_SAMPLE_RATE, n_mels=N_MELS, n_fft=N_FFTS)

print("Transforming to spec...")
spec = SPEC_TRANSFORM(wav).to(DEVICE)
if spec.shape[1] != 1024 or spec.shape[2] != 1024:
    print(spec.shape)
    exit()

print("Inverting Mel Scale...")
inverse_transform = torchaudio.transforms.InverseMelScale(n_mels=N_MELS, sample_rate=GTZAN_SAMPLE_RATE, n_stft=int((N_FFTS//2)+1)).to(DEVICE)
spec = inverse_transform(spec)
print("Converting to waveform...")
grifflim_transform = torchaudio.transforms.GriffinLim(n_fft=N_FFTS).to(DEVICE)
reconstructed_wav = grifflim_transform(spec)

reconstructed_wav = torch.unsqueeze(reconstructed_wav, dim=0)
print("Saving to file...")
save_wav_to_file(reconstructed_wav, "test_1024x1024.wav")