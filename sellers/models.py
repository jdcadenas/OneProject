from django.db import models
from treebeard.mp_tree import MP_Node


class Seller(MP_Node):
    name = models.CharField(max_length=50)

    node_order_by = ["name"]

    def __str__(self):
        return "Seller: {} ".format(self.name)
