import os
import downloader

class queue:
    def __init__(self, file_array, loop_when_done_playing):
        self.full_file_array = file_array
        self.file_array = self.full_file_array
        self.loop_when_done_playing = loop_when_done_playing
    
    # Returns the name of the current song in the queue
    def get_current_song(self):
        return downloader.DownloadMp3FromUrl(self.file_array[0])
    
    # Restarts the playlist
    def loop(self):
        self.file_array = self.full_file_array
    
    # Clears the playlist
    def clear(self):
        self.file_array = []
        self.full_file_array = []

    # Goes to the next song OR loops
    def goto_next_song(self):
        del self.file_array[0]

        if len(self.file_array) <= 0 and self.loop_when_done_playing:
            self.loop()
    
    # Adds a new song to the queue
    def add_to_queue(self, filenname):
        
        self.file_array.insert(len(self.file_array), filenname)

        return f"Successfully added {filenname} to the queue."

    # Returns a string containing every song in the playlist
    def list_queue(self):
        liststr = "Queue:\n"
        for index, item in enumerate(self.file_array):
            liststr = liststr + f"{str(index)}. {item},\n"
        return liststr