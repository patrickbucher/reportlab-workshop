#!/usr/bin/env python3

from reportlab.pdfgen import canvas

def hello_world(c):
    c.drawString(100, 100, "Hello, World!")

if __name__ == '__main__':
    c = canvas.Canvas("hello_world.pdf")
    hello_world(c)
    c.showPage()
    c.save()
