"""
     Visualize quadtree in separate window.
"""
from tkinter import Canvas, ALL, Toplevel
from tkinter.font import Font

from quadtree.draw_tree import DrawTree, layoutDrawTree

class VisualizationWindow:
    def __init__(self, master):
        self.master = master
        self.frame = Toplevel(width=1024, height=512)
        self.canvas = Canvas(self.frame, width=1024, height=512)        

        self.frame.title("QuadTree Visualization")
        self.canvas.pack()
        self.largeFont = None
        self.smallFont = None

    def clear(self):
        """Clear everything."""
        self.canvas.delete(ALL)

    def plot(self, tree):
        """Given DrawTree information, plot the quadtree."""
        dt = DrawTree(tree)
        dt = layoutDrawTree(dt)
        self.canvas.delete(ALL)
        if self.largeFont is None:
            self.largeFont = Font(family='Times', size='24')
            self.smallFont = Font(family='Times', size='14')
        dt.format(self.canvas, self.smallFont, self.largeFont, -1)