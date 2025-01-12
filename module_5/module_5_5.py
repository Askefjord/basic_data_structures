class User:
    users_dict = {}
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = password
        self.age = age

class Video:
    video_dict = {}
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = False

class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = User.users_dict
        self.videos = Video.video_dict
        self.current_user = None

    def log_in(self, nickname, password):
        pass

    def register(self, nickname, password, age):
        pass

    def log_out(self):
        pass

    def add(self, *videos):
        pass

    def get_videos(self, search_word):
        pass

    def watch_video(self, video_name):
        pass

