class Node:
    def __init__(self, track):
        self.track = track
        self.next = None
        self.prev = None


class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_track(self, track):
        new_node = Node(track)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.current = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def get_tracks(self):
        tracks = []
        current_node = self.head

        while current_node is not None:
            tracks.append(current_node.track)
            current_node = current_node.next

        return tracks
