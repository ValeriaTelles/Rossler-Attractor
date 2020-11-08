# Rössler Attractor 

The **Rössler attractor** is the attractor for the Rössler system, a system of three non-linear ordinary differential equations originally studied by the German biochemist Otto Eberhard Rössler:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/f7451e7dd713793059138195cd66af25a20fcc3c) 

with particular values of parameters a = 0.2, b = 0.2 and c = 5.7. 

The three-dimensional Rössler system was originally conceived as a simple model for studying chaos. With only one nonlinear term it can be thought of as a simplification of the well-known Lorenz system and as a minimal model for continuous-time chaos.

This program provides a simulation of a Rössler System with the same parameters that Rössler studied with and the following initial conditions: $(X_1, Y_1, Z_1) = (0.1, 0., 0.1)$ and $(X_2, Y_2, Z_2) = (0.1001, 0., 0.1001)$. To solve the ODEs we used Euler Method:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/0df686bb7caa953daf6e0495aa9e1703e1be0ec4)

## Variation of Parameters
Varying each parameter (a, b, and c) has a comparable effect by causing the system to converge toward a periodic orbit, fixed point, or escape towards infinity, however specific ranges and behaviours induced vary substantially for each parameter. 

## Requirements 
This program uses Python 3.7.1 and may need additional packages installed.

```pip install -r requirements.txt```

**Warning**: As per matplotlib's limitation on blitting, this code does not work with the OSX backend (but does work with other GUI backends on mac). This program runs fine on Windows. 

## How to Use

1. Install Python 3
2. Check the version with ```python --version```
3. Type ```python RosslerAttractor.py``` in your terminal 

## Output

![](https://media.giphy.com/media/OZuagOigdmnY6E8FD6/giphy.gif)
