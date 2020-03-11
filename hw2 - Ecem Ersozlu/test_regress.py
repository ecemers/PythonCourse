# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 06:24:50 2020

@author: Ecem
"""

import unittest
import regress
import numpy as np

class TestReg(unittest.TestCase):
    
    def test_vars(self):
        self.assertIsNotNone(x)
        self.assertIsNotNone(y)
        self.assertIn(x, df)
        self.assertIn(y, df)
        
    def test_dim(self):
        self.assertEqual(len(x), len(y))
        col1 = np.shape(x)
        col2 = np.shape(y)
        self.assertEqual(col1, col2)
        self.assertNotEqual(len(df), len(data))
        