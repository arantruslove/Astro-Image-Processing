"""Module that contains project classes."""

class FitsBox:
    """Contains information for the region of a fits image."""
    def __init__(self, x_centre: float, y_centre: float, height: float, width: float):
        self.x_centre =  x_centre
        self.y_centre = y_centre
        self.height =  height
        self.width = width


class Object:
    """Contains information about an astronomical object."""
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

class CutoffRegion:
    """Specifies the coordinates of a region with the associated cutoff brightness."""
    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float,
                cutoff: float):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.cutoff = cutoff
