import lesson_15_task_2
import unittest


class Lesson15Test(unittest.TestCase):
    def test_result_lesson6(self):
        self.assertEqual(lesson_15_task_2.check_tel_number("380502852124"), "(+38) 050-285-21-24")


if __name__ == "__main__":
    unittest.main()