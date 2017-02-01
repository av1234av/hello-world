from unittest import TestCase


class TestMergesort(TestCase):
    def test_mergesort(self):
        from mergesort import mergesort
        ll=mergesort([4,7,1,8,33])
        self.assertListEqual(ll,[1,4,7,8,33])