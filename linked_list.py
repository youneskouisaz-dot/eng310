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

    def remove_track(self, track):
        node = self.head

        while node is not None:
            if node.track == track:
                if node.prev is not None:
                    node.prev.next = node.next
                else:
                    self.head = node.next

                if node.next is not None:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev

                if self.current == node:
                    self.current = node.next if node.next is not None else node.prev

                if self.head is None:
                    self.current = None

                return True

            node = node.next

        return False

    def next_track(self):
        if self.current is not None and self.current.next is not None:
            self.current = self.current.next

        return self.get_current_track()

    def previous_track(self):
        if self.current is not None and self.current.prev is not None:
            self.current = self.current.prev

        return self.get_current_track()

    def get_current_track(self):
        if self.current is None:
            return None

        return self.current.track

    def get_tracks(self):
        tracks = []
        node = self.head

        while node is not None:
            tracks.append(node.track)
            node = node.next

        return tracks

    def move_up(self, track):
        node = self.head

        while node is not None:
            if node.track == track:
                if node.prev is None:
                    return False

                previous = node.prev
                before_previous = previous.prev
                after_node = node.next

                if before_previous is not None:
                    before_previous.next = node
                else:
                    self.head = node

                node.prev = before_previous
                node.next = previous

                previous.prev = node
                previous.next = after_node

                if after_node is not None:
                    after_node.prev = previous
                else:
                    self.tail = previous

                return True

            node = node.next

        return False

    def move_down(self, track):
        node = self.head

        while node is not None:
            if node.track == track:
                if node.next is None:
                    return False

                next_node = node.next
                before_node = node.prev
                after_next = next_node.next

                if before_node is not None:
                    before_node.next = next_node
                else:
                    self.head = next_node

                next_node.prev = before_node
                next_node.next = node

                node.prev = next_node
                node.next = after_next

                if after_next is not None:
                    after_next.prev = node
                else:
                    self.tail = node

                return True

            node = node.next

        return False
