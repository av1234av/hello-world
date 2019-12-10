class Song:
    def __init__(self, name):
        self.name = name
        self.next = None

    def next_song(self, song):
        self.next = song

    def is_repeating_playlist(self):
        """
        :returns: (bool) True if the playlist is repeating, False if not.
        """
        slow = self
        fast = self.next
        while slow and fast and fast.next:
            if slow.name == fast.name:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


if __name__ == "__main__":
    first = Song("Hello")
    second = Song("Eye of the tiger")
    third = Song("Final Countdown")
    fourth = Song("Spaceship")

    first.next_song(second)
    second.next_song(third)
    third.next_song(fourth)
    fourth.next_song(second)

    print(first.is_repeating_playlist())