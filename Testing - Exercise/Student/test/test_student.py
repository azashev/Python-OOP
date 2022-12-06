from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("TestName")
        self.student_with_course = Student("TestName2", {"TestCourse": ["Note1"]})

    def test_correct_initialization(self):
        self.assertEqual("TestName", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"TestCourse": ["Note1"]}, self.student_with_course.courses)

    def test_enroll_with_existing_course_name_return_message(self):
        result = self.student_with_course.enroll("TestCourse", ["Note2", "Note3"])

        self.assertEqual(['Note1', 'Note2', 'Note3'], self.student_with_course.courses["TestCourse"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_with_new_course_name_and_add_course_notes_are_return_message(self):
        result = self.student.enroll("NewCourseName", "Yy", "Y")

        self.assertEqual('Yy', self.student.courses["NewCourseName"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_new_course_name_and_add_course_notes_is_empty_parameter_return_message(self):
        result = self.student.enroll("NewCourseName", "Yy", "")

        self.assertEqual('Yy', self.student.courses["NewCourseName"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_new_course_name_and_add_course_notes_are_not_y_or_empty_return_message(self):
        result = self.student.enroll("NewCourseName", "Note1", "Random")

        self.assertEqual([], self.student.courses["NewCourseName"])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_with_valid_course_name_and_return_message(self):
        result = self.student_with_course.add_notes("TestCourse", "Note2")

        self.assertEqual(['Note1', 'Note2'], self.student_with_course.courses["TestCourse"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_with_invalid_course_name_and_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("RandomCourse", "Note1")

        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_existing_course_name_and_return_message(self):
        result = self.student_with_course.leave_course("TestCourse")

        self.assertEqual({}, self.student_with_course.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_non_existing_course_name_and_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("RandomCourse")

        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
