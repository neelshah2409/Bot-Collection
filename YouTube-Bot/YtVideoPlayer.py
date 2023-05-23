import vlc
import pafy

def main():
    url = "https://www.youtube.com/watch?v=hiuRBNCGpzU"
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.Instance.media_new(best.url)
    player = vlc.Instance.media_player_new()
    vlc.Media.get_mrl()
    player.set_media(media)
    player.play()
