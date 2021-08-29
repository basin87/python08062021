import lesson_11_task_2
import unittest


class Lesson11Test(unittest.TestCase):
    def test_result_lesson6(self):
        name_list = ["ШАЛАШ", "КАЗАК", "ДЕД", "ДОХОД", "13231"]
        self.assertEqual(lesson_11_task_2.check_name(name_list), name_list)


if __name__ == "__main__":
    unittest.main()