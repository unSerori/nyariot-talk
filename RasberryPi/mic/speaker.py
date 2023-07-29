import sounddevice as sd
import soundfile as sf

def speak():
	filepath = "./audio_file/from_server/nyariott.wav"

	sig, sr = sf.read(filepath, always_2d = True)
	sd.play(sig, sr)

	sd.wait()
	print("end")