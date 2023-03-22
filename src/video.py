from src.channel import Channel


class Video:

    def __init__(self, id_video: str) -> None:
        self.id_video: str = id_video
        self.__info: dict = Channel.get_video_info(self.id_video)
        self.name_video: str = self.__info['items'][0]['snippet']['title']
        self.link_to_video: str = f'https://www.youtube.com/watch?v={self.id_video}'
        self.number_of_views: str = self.__info['items'][0]['statistics']['viewCount']
        self.number_of_likes: str = self.__info['items'][0]['statistics']['likeCount']

    def __str__(self):
        return self.name_video


class PLVideo(Video):

    def __init__(self, id_video: str, id_playlist: str) -> None:
        super().__init__(id_video)
        self.id_playlist: str = id_playlist


