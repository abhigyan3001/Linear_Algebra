# vectors.py
import math

class Vector:
    def __init__(self, values):
        self.values = values

    def __len__(self):
        return len(self.values)

    def dot(self, other):
        return sum(self.values[i] * other.values[i] for i in range(len(self)))

    def norm(self, type="l2"):
        if type == "l2":
            return math.sqrt(sum(v ** 2 for v in self.values))
        elif type == "l1":
            return sum(abs(v) for v in self.values)
        elif type == "inf":
            return max(abs(v) for v in self.values)
        else:
            raise ValueError("Unsupported norm type")

    def normalize(self):
        n = self.norm()
        return Vector([v / n for v in self.values])

    def angle(self, other):
        numerator = self.dot(other)
        denominator = self.norm() * other.norm()
        return math.acos(numerator / denominator)
