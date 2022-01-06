#!/usr/bin/python3
#test_rectangle.py
"""Defines unittest for models/rectangle.py"""
import sys
from io import StringIO
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittest for testing the initialization of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(2, 3), Base)
    def test_no_args(self):
         with self.assertRaises(TypeError):
            Rectangle()

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_two_args(self):
        r1 = Rectangle(2, 3)
        r2 = Rectangle(5, 6)
        self.assertEqual(r1.id, r2.id - 1)

    def test_four_args(self):
         r1 = Rectangle(2, 3, 6, 9)
         r2 = Rectangle(5, 6, 4, 2)
         self.assertEqual(r1.id, r2.id - 1)

    def test_five_args(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r1.id, 6)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 3, 4, 5, 6, 7)
       
    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(2, 3, 4, 5, 6).__width)

    def test_height_private(self):
       with self.assertRaises(AttributeError):
           print(Rectangle(2, 3, 4, 5, 6).__height)

    def test_x_private(self):
       with self.assertRaises(AttributeError):
           print(Rectangle(2, 3, 4, 5, 6).__x)

    def test_y_private(self):
       with self.assertRaises(AttributeError):
           print(Rectangle(2, 3, 4, 5, 6).__y)


    def test_width_setter(self):
        r1 = Rectangle(1, 1)
        r1.width = 5
        self.assertEqual(r1.width, 5)
        
    def test_height_setter(self):
        r1 = Rectangle(1, 1)
        r1.height = 5
        self.assertEqual(r1.height, 5)

    def test_x_setter(self):
        r1 = Rectangle(1, 1)
        r1.x = 5
        self.assertEqual(r1.x, 5)

    def test_y_setter(self):
        r1 = Rectangle(1, 1)
        r1.y = 5
        self.assertEqual(r1.y, 5)

    def test_width_getter(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r1.width, 2)

    def test_height_getter(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r1.height, 3)

    def test_x_getter(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r1.x, 4)

    def test_y_getter(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(r1.y, 5)


class TestRectangle_width(unittest.TestCase):
    """Unittest for testing initialization of Rectangle width attribute."""

    def test_width_is_int(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertIsInstance(r1.width, int)

    def test_width_as_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("9", 3, 4, 5, 6)

    def test_width_as_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 3, 4, 5, 6)

    def test_width_less_than_zero(self):
         with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-8, 3, 4, 5, 6)

    def test_width_as_None(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 3, 4, 5, 6)

    def test_width_as_complex(self):
         with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(2), 3, 4, 5, 6)

    def test_width_as_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 3, 4, 5, 6)

    def test_width_as_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 3, 4, 5, 6)


class TestRectangle_height(unittest.TestCase):
    """Unittest for testing initialization of Rectangle height attribute."""
    def test_height_is_int(self):
        r1 = Rectangle(2, 3, 4, 5, 6)
        self.assertIsInstance(r1.height, int)

    def test_height_as_str(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, "3", 4, 5, 6)

    def test_height_as_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0, 4, 5, 6)

    def test_height_less_than_zero(self):
         with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -3, 4, 5, 6)

    def test_height_as_None(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, None, 4, 5, 6)

    def test_height_as_complex(self):
         with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, complex(3), 4, 5, 6)

    def test_height_as_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('nan'), 4, 5, 6)

    def test_height_as_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, float('inf'), 4, 5, 6)


class TestRectangle_x(unittest.TestCase):
    """Unittest for testing initialization of Rectangle x attribute."""
    def test_x_is_int(self):
        r1 = Rectangle(2, 3, 4, 5)
        self.assertIsInstance(r1.x, int)
    
    def test_x_as_zero(self):
        r1 = Rectangle(2, 3, 0, 9, 6)
        r2 = Rectangle(4, 6, 0, 5, 6)
        self.assertEqual(r1.id, r2.id)

    def test_x_as_str(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(9, 3, "4", 5)

    def test_x_as_None(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, None, 5)

    def test_x_as_complex(self):
         with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, complex(4), 5)

    def test_x_as_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, float('nan'), 5)

    def test_x_as_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 3, float('inf'), 5)

    def test_x_as_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -3, 6)


class TestRectangle_y(unittest.TestCase):
    """Unittest for testing initialization of Rectangle y attribute."""
    def test_y_is_int(self):
        r1 = Rectangle(2, 3, 4, 5)
        self.assertIsInstance(r1.x, int)

    def test_y_as_zero(self):
        r1 = Rectangle(2, 3, 0, 9, 6)
        r2 = Rectangle(4, 6, 8, 0, 6)
        self.assertEqual(r1.id, r2.id)

    def test_y_as_str(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(9, 3, 4, "5")

    def test_y_as_None(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, None)

    def test_y_as_complex(self):
         with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, complex(4))

    def test_y_as_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, float('nan'))

    def test_y_as_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 3, 4, float('inf'))

    def test_y_as_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 3, 4, -6)


class TestRectangle_area(unittest.TestCase):
    """Unittest for testing the area method of the Rectangle class."""
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_width_is_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 4)

    def test_large_area(self):
        r = Rectangle(999999999999999999, 99999999999999999)
        self.assertEqual(r.area(), 99999999999999998900000000000000001)

    def test_area_changes_attributes(self):
        r = Rectangle(2, 3)
        r.width = 4
        r.height = 6
        self.assertEqual(r.area(), 24)

    def test_area_with_an_arg(self):
        r = Rectangle(6, 7)
        with self.assertRaises(TypeError):
            r.area(42)


class TestRectangle_stdout(unittest.TestCase):
    """Unittest for testing __str__ and display method of the Rectangle Class."""
    
    # Test for the __str__ method
    def test_two_args(self):
        r = Rectangle(4, 6)
        self.assertEqual(str(r), "[Rectangle] ({}) 0/0 - 4/6".format(r.id))

    def test_three_args(self):
        r = Rectangle(4, 6, 3)
        self.assertEqual(str(r), "[Rectangle] ({}) 3/0 - 4/6".format(r.id))

    def test_four_args(self):
        r = Rectangle(4, 6, 3, 5)
        self.assertEqual(str(r), "[Rectangle] ({}) 3/5 - 4/6".format(r.id))

    def test_five_args(self):
        r = Rectangle(4, 6, 2, 5, 9)
        self.assertEqual(str(r), "[Rectangle] (9) 2/5 - 4/6")

    def test_larger_values(self):
        r = Rectangle(499999, 6999999, 299999, 599999)
        result = "[Rectangle] ({}) 299999/599999 - 499999/6999999".format(r.id)
        self.assertEqual(str(r), result)

    def test_str_method_change_attributes(self):
        r = Rectangle(4, 6, 2, 5, 9)
        r.width = 9
        r.height = 5
        r.x = 2
        r.y = 6
        r.id = 4
        self.assertEqual(str(r), "[Rectangle] (4) 2/6 - 9/5")

    #Test for the display method

    @staticmethod
    def capture_stdout(rect):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The Rectangle to print to stdout.

        Returns:
           The text printed to stdout.
        """
        # Create the in-memory "file"
        capture = StringIO()
        # Replace default stdout (terminal) with new stream
        sys.stdout = capture
        # This will go to the new memory stream:
        rect.display()
        
        # The original `sys.stdout` is kept in a special
        # dunder named `sys.__stdout__`. So restore
        # the original output stream to the default stdout - the terminal.

        sys.stdout = sys.__stdout__
        return capture

    def test_display_width_height(self):
        r = Rectangle(4, 6, 0, 0, 0)
        capture =  TestRectangle_stdout.capture_stdout(r)
        display = "####\n####\n####\n####\n####\n####\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_width_height_x(self):
        r = Rectangle(4, 6, 2, 0, 0)
        capture =  TestRectangle_stdout.capture_stdout(r)
        display = "  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_width_height_y(self):
        r = Rectangle(4, 6, 0, 2, 0)
        capture =  TestRectangle_stdout.capture_stdout(r)
        display = "\n\n####\n####\n####\n####\n####\n####\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_width_height_x_h(self):
        r = Rectangle(4, 6, 2, 2, 7)
        capture =  TestRectangle_stdout.capture_stdout(r)
        display = "\n\n  ####\n  ####\n  ####\n  ####\n  ####\n  ####\n"
        self.assertEqual(capture.getvalue(), display)

    def test_display_one_arg(self):
        r = Rectangle(4, 6, 0, 2, 8)
        with self.assertRaises(TypeError):
            r.display("all")
























     
