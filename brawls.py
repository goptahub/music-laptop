import cfg
import pygame

class Brawls:

    sounds:         dict[str, pygame.mixer.Sound] = {}
    keyboard:       dict[str, int] = {}
    marked_sounds:  dict[int, pygame.mixer.Sound] = {}
    active_sounds:  dict[int, pygame.mixer.Channel] = {}
    fadeout_time    = 600  # ms

    def __init__(self) -> None:
        pygame.mixer.init()

        '''upload tracks'''
        track_dir = cfg.tracks_dir + '/' + cfg.subdirs[0] + '/'
        track_path = ""
        for track in cfg.tracks:
            try:
                track_path = track_dir + track
                sound = pygame.mixer.Sound(track_path)
                note = track[:track.rindex('.')]
                self.sounds[note] = sound
            except:
                print(f"[-] failed to upload track {track_path}")
                return
            
        '''fill suproutine structs'''
        for i in range(len(cfg.notes)):
            note = cfg.notes[i]
            key = cfg.keys[i]
            self.keyboard[note] = key
            self.marked_sounds[key] = self.sounds[note]


        # print(self.sounds)
        # print(self.marked_sounds)
        # print(self.keyboard)


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                elif event.type == pygame.KEYDOWN:
                    event_key = event.key
                    if event_key in self.active_sounds:
                        continue
                    # print('hi')
                    sound = self.marked_sounds.get(event_key, None)
                    if not sound:
                        continue          

                    channel = sound.play()
                    self.active_sounds[event_key] = channel

                    
                elif event.type == pygame.KEYUP:
                    event_key = event.key
                    if event_key not in self.active_sounds:
                        continue
                    # print('buy')
                    self.active_sounds[event_key].fadeout(self.fadeout_time)
                    del self.active_sounds[event_key]
