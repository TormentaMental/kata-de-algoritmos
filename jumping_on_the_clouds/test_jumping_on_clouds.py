import unittest

from jumping_on_the_clouds.jumping_on_clouds import jumping_on_clouds


# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
class MyJumpingOnCloudsTests(unittest.TestCase):
    def test_it_works_for_a_complete_example(self):
        clouds = [0, 0, 1, 0, 0, 0, 1, 0]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(4, jumps)

    def test_it_should_make_no_jumps(self):
        clouds = [0]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(0, jumps)

    def test_it_makes_one_jump_when_providing_two_clouds(self):
        clouds = [0, 0]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(1, jumps)

    def test_it_makes_one_jump_when_three_good_clouds_provided(self):
        clouds = [0, 0, 0]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(1, jumps)

    def test_it_makes_minimum_number_of_jumps_for_four_consecutive_clouds(self):
        clouds = [0, 0, 0, 0]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(2, jumps)

    def test_it_makes_no_jumps_if_next_cloud_is_thunderhead(self):
        clouds = [0, 1]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(0, jumps)

    def test_it_makes_no_jumps_if_first_and_second_clouds_are_thunderheads(self):
        clouds = [0, 1, 1]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(0, jumps)

    def test_it_makes_one_jumps_with_one_bad_cloud(self):
        clouds = [0, 1, 0]
        jumps = jumping_on_clouds(clouds)
        self.assertEqual(1, jumps)
