from utils import randbool
class Clouds:
  def __init__(self, width, height):
    self.width = width
    self.height = height
    self.cells = [[0 for i in range(width)] for j in range(height)]

  def update(self, threshold=1, max_random=20, threshold_g = 1, max_random_g = 10):
    for i in range(self.height):
      for j in range(self.width):
        if randbool(threshold, max_random):
          self.cells[i][j] = 1
          if randbool(threshold_g, max_random_g):
            self.cells[i][j] = 2
        else:
          self.cells[i][j] = 0

  def export_data(self):
    return {
      "cells": self.cells
    }  

  def import_data(self, data):
    self.cells = data["cells"] or [[0 for i in range(self.width)] for j in range(self.height)]