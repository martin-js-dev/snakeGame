import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox
 
class cube(object):
    rows = 20
    w = 500
   
 
       
    def move(self, dirnx, dirny):
        
 
    def draw(self, surface, eyes=False):
        
 
      
       
 
 
 
class snake(object):
    body = []
    turns = {}
    def __init__(self, color, pos):
        
 
    def move(self):
        
 
    def reset(self, pos):
        
 
 
    def addCube(self):
        
       
 
    def draw(self, surface):
        
 
def drawGrid(w, rows, surface):
   
       
 
def redrawWindow(surface):
    
 
def randomSnack(rows, item):
 
    positions = item.body
 
    
       
    
 
 
def message_box(subject, content):
    
 
 
def main():
    global width, rows, s, snack
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))
    s = snake((255,0,0), (10,10))
    snack = cube(randomSnack(rows, s), color=(0,255,0))
    flag = True
 
    clock = pygame.time.Clock()
   
    
 
           
        redrawWindow(win)
 
       
    
 
 
 
main()
