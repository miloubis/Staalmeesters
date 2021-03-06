"""
load_orders.py
Staalmeester case

This is a test file to load an order into the class Order and do some experiments/tests with it
"""

from classes import *

orderlist = [
  ["Order1"],
  [190, 270],
  [90, 160],
  [120, 290],
  [110, 220],
  [160, 120],
  [90, 120],
  [200, 100],
  [110, 290],
  [120, 170],
  [100, 320],
  [90, 160],
  [190, 300],
  [170, 250],
  [180, 340],
  [170, 180],
  [90, 100],
  [110, 270],
  [70, 220],
  [40, 130],
  [140, 330],
  [130, 110],
  [40, 240],
  ["Order2"],
  [150, 150],
  [50, 110],
  [160, 270],
  [130, 270],
  [130, 130],
  [190, 160],
  [200, 190],
  [170, 240],
  [110, 220],
  [110, 140],
  [70, 230],
  [140, 170],
  [160, 240],
  [200, 130],
  [150, 100],
  [190, 220],
  [60, 150],
  [40, 240],
  ["order3"],
  [110, 100],
  [130, 240],
  [130, 220],
  [90, 160],
  [40, 100],
  [50, 140],
  [150, 250],
  [70, 200],
  [160, 120],
  [120, 120],
  [100, 190],
  [190, 240],
  [120, 270],
  [60, 130],
  [160, 230],
  [170, 170],
  [200, 170],
  [90, 210],
  [60, 190],
  [120, 180],
  [110, 190],
  [180, 270],
  [160, 120],
  [160, 100],
  ["Order4"],
  [90, 220],
  [110, 260],
  [80, 120],
  [80, 280],
  [50, 280],
  [80, 270],
  [160, 190],
  [40, 190],
  [90, 250],
  [180, 210],
  [180, 250],
  [110, 160],
  [170, 270],
  [140, 230],
  [110, 270],
  [80, 140],
  [100, 270],
  [140, 210],
  [120, 200],
  [120, 150],
  ["Order5"],
  [130, 240, "Type I"],
  [170, 190, "Type I"],
  [150, 150, "Type I"],
  [70, 160, "Type I"],
  [160, 210, "Type I"],
  [110, 140, "Type I"],
  [110, 170, "Type I"],
  [150, 170, "Type I"],
  [150, 230, "Type I"],
  [60, 120, "Type I"],
  [160, 150, "Type I"],
  [160, 240, "Type I"],
  [70, 160, "Type I"],
  [120, 230, "Type I"],
  [140, 120, "Type I"],
  [130, 240, "Type I"],
  [90, 180, "Type I"],
  [150, 230, "Type I"],
  [100, 150, "Type I"],
  [80, 180, "Type I"],
  [130, 180, "Type I"],
  [150, 210, "Type II"],
  [150, 150, "Type II"],
  [100, 230, "Type II"],
  [110, 110, "Type II"],
  [70, 240, "Type II"],
  [150, 230, "Type II"],
  [170, 220, "Type II"],
  [150, 190, "Type II"],
  [180, 210, "Type II"],
  [130, 120, "Type II"],
  [170, 230, "Type II"],
  [90, 200, "Type II"],
  [150, 230, "Type II"],
  [140, 190, "Type II"],
  [120, 130, "Type II"],
  [160, 150, "Type II"],
  [110, 100, "Type II"],
  [80, 190, "Type II"],
  [80, 230, "Type II"],
  [70, 180, "Type II"],
  [180, 100, "Type III"],
  [90, 130, "Type III"],
  [70, 180, "Type III"],
  [150, 120, "Type III"],
  [60, 200, "Type III"],
  [80, 200, "Type III"],
  [60, 240, "Type III"],
  [110, 160, "Type III"],
  [120, 240, "Type III"],
  [110, 170, "Type III"],
  [150, 230, "Type III"],
  ["Order6"],
  [130, 100, 205],
  [160, 180, 327],
  [100, 160, 211],
  [120, 200, 302],
  [120, 180, 286],
  [190, 180, 360],
  [190, 170, 343],
  [130, 140, 260],
  [160, 200, 343],
  [140, 180, 303],
  [200, 190, 380],
  [110, 190, 178],
  [100, 200, 284],
  [160, 150, 300],
  [120, 130, 240],
  [170, 180, 340],
  [170, 130, 278],
  [110, 130, 223],
  [130, 150, 261],
  [110, 120, 220],
  [180, 110, 220],
  [110, 140, 238],
  [150, 110, 234],
  [170, 180, 340],
  [160, 200, 343],
  [120, 150, 251],
  [160, 170, 320],
  [200, 160, 339],
  [180, 170, 340],
  [170, 110, 250],
  [140, 110, 220],
  [120, 140, 244],
  [140, 180, 305],
  [150, 190, 321],
  [150, 160, 300],
  [160, 130, 262],
  [130, 170, 278],
  [130, 140, 260],
  [110, 190, 178],
  [110, 110, 110],
  [200, 130, 266],
  [110, 100, 170]
]

order1 = Order(orderlist[1:23])
order2 = orderlist[24:42]
order3 = orderlist[43:67]
order4 = orderlist[68:88]
combinedOrders234 = order2 + order3 + order4
combinedOrders234 = Order(combinedOrders234)
order5 = Order(orderlist[89:141])
# order6 = Order(orderlist[142:185])



