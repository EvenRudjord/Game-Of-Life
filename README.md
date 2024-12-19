# Game of Life

A Python implementation of Conway's Game of Life, developed as a school project for the IN1000 course at the University of Oslo (UiO).

## Overview

Conway's Game of Life is a cellular automaton devised by mathematician John Conway. It consists of a grid of cells, where each cell can either be alive or dead. The state of each cell evolves over time based on a set of simple rules. This project implements the Game of Life, allowing users to explore how patterns emerge and evolve.

## Features

- **Customizable grid size**: Set the dimensions of the grid to your preference.
- **Initial configuration**: Start with random patterns or predefined configurations.
- **Simulation controls**: Play, pause, and step through the simulation.
- **Visualization**: See the grid update dynamically as generations evolve.

## Rules

The Game of Life operates on the following rules:
1. A live cell with fewer than 2 live neighbors dies (underpopulation).
2. A live cell with 2 or 3 live neighbors survives.
3. A live cell with more than 3 live neighbors dies (overpopulation).
4. A dead cell with exactly 3 live neighbors becomes alive (reproduction).

## How to Run

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd game-of-life
