import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\n""Is loving as good as they say?", 0.05),
        ("Now I'm so lonely", 0.08),
        ("Oh, I wish I'd find a lover that could hold me", 0.06),
        ("Now I'm crying in my room", 0.07),
        ("So skeptical of love", 0.06),
        ("But still, I want it more, more, more""\n", 0.07),
    ]
    
    delays = [0.3, 3.8, 6.0, 10.5, 12.8, 16.0]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()