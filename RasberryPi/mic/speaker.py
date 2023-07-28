import pygame.mixer

def speak():
  pygame.mixer.init()
  wav_sound = pygame.mixer.Sound('./audio_file/from_server/nyariott.wav')
  wav_sound.play()
  while pygame.mixer.get_busy():
      pass