import lesson_7_task_2
import unittest


class Lesson7Test(unittest.TestCase):
    def test_result_lesson6(self):
        self.assertEqual(lesson_7_task_2.convertor_for_temperatures(32, "Celsius"), (305.15, 89.6))


if __name__ == "__main__":
    unittest.main()