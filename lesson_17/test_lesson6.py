import unittest
import lesson_6_task_1


class Lesson6Test(unittest.TestCase):
    def test_result_lesson6(self):
        self.assertEqual(lesson_6_task_1.join_var_into_dict("Bitcoin", "BTC"), {"Bitcoin": "BTC"})


if __name__ == "__main__":
    unittest.main()