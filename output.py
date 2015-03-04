# The output module

import os
import sys
sys.path.append('./pymedia-1.3.7.3')

import pymedia.audio.sound as sound
import time
import wave

class Output:

	def __init__(self):
		self.bar = []
		self.loc = "/home/kazimierz/kazamc/wavfiles/"

	def play_wav(self, filename, length):
		f = wave.open(filename, 'rb')
		sampleRate = f.getframerate()
		channels = f.getnchannels()
		format = sound.AFMT_S16_LE
		snd1 = sound.Output(sampleRate, channels, format)

		s = ' '
		if length == 0: # Play all
			while len(s):
				s = f.readframes(1000)
				snd1.play(s)

			while snd1.isPlaying():
				time.sleep(0.05)

		else:
			x = 0
			y = length * 50
			while x < y:
				x += 1
				s = f.readframes(1000)
				snd1.play(s)

			while snd1.isPlaying():
					time.sleep(0.05)

	def process(self, bar):
		ret = []
		for x in xrange(2):
			half = bar[x]
			for beat in xrange(len(half)):
				tempo = len(half[beat])
				tempo = 10 / tempo
				for note in xrange(len(half[beat])):
					if half[beat][note] != 'extend':
						ret.append([half[beat][note], tempo])
					else:
						ret[(len(ret) - 1)][1] += tempo
				ret.append(['new_beat', 0])
			ret.append(['new_halfbar', 0])
		return ret

	def run(self, bar):
		for x in self.process(bar):
			if x[0] == 'new_beat':
				time.sleep(0.2)
			elif x[0] == 'new_halfbar':
				time.sleep(0.1)
			else:
				#self.play_wav((self.loc + x[0] + '.wav'), x[1])
				self.play_wav((self.loc + 'time.wav'), x[1])

		return 1
