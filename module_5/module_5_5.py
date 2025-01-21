class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and password == hash(user.password):
                self.current_user = user

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

if __name__ == '__main__':
    x = UrTube()