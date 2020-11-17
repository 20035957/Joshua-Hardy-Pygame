# Shooter By Joshua Hardy

A small script made too show of Python and Pygame for my Application Scripting Class.

## Table of Contents

 1. Revision History 
 2. Introduction
 3. Design Goals.
 4. Requirements for the code to run.
 5. Pseudo Code write out
 6. Logical View of the code 
 7. Screenshots of the code within context to the design decision. 
 8. Final Source Code 
 
## Revision History 
Revision 0.0.8 - Code named - Keyboard 
- Drawn shapes follows user input from keyboard 
- Keyboard movement includes continued movement in 1 direction with speed control 

Revision 0.1.0 - Code named - Images 
- drawn images are replaced with loaded image sprites  
- Sprites follow mouse cursor rather than keyboard movement 

Revision 0.1.1 - Code named – Collision (Current Revision) 
- target sprite is added and loaded at random location 
- player is assigned fire role, when mouse is clicked and player and target occupies the same area of the screen the target sprite is   “killed” (removed) and respawns in another random location 

## Introduction
## Design Goals
### Aims of this script. 

This code is written with the intent of using Pygame python library Modules to demonstrate python's flexibility as a scripting language and its ability to quickly transition from one task too another through the import function of Modules. As stated, before this document uses the Pygame Library Modules too turn python into an efficiently written and altered gaming development platform. 

### Design priorities. 

The design priorities were to keep everything as simple as possible by only using standard & simple Python Syntax and as little python Modules as possible. The code was also designed with the intent of variability for not only human readability but also alteration.  

## Requirements

“Shooter” is written in Python it is not compiled and is simply just a Script so in order to be run Python “binaries” must be present and called to run the script.  The script itself uses very few Python Modules as of (revision 0.0.3a) it only imports 2 modules “Sys” and “Pygame”, These modules must also be installed before the script is installed. I have included a requirements.txt alongside the script that can be run by python's pip binary too install the required modules.

### How too get it running

1. Python 3 
  - Windows 
    Python 3 can be installed by downloading the latest installer file from https://www.python.org/downloads/ and then running the downloaded file too install.
  - Linux
    apt install python3 (replace apt with your distros package manager.) 

2. (Recommended) Python will also be installed alongside the Python IDE Thonny.
  You can Download the latest stable version from the – Github Release page 
  Or through your Linux package manager – apt install thonny 

  The rest of this guide will assume you are using the Recommended method of installing Thonny, however I suggest you do both and then follow the Thonny guide.  
  
    Once Thonny is installed we need to install the Modules that “Shooter” 
    will need to run. 
  
    Sys Module – Allows “shooter” too easily talk to the Operating system 
    and use its devices, “shooter” uses the Sys module too access user inputs. 
    You're in luck if you installed python or thonny you already have Sys 
    as it is a default python library.
    
    Random Module - Allows Shooter too generate Ranadom numbers for variables 
    that are based on randomness
    You're in luck if you installed python or thonny you already have 
    Sys as it is a default python library.
    
    Pygame  Module – Adapts python too be a very easily used as a 
    gaming development language. This is the base that “shooter” is 
    almost entirely built on. 
    Launch Thonny and then step through the first time setup process 
    after that click on “Tools” in Thonny’s Toolbar a Drop down will appear 
    then click on. “Manage plug-ins...”
    
    A window will appear titled “Thonny plug-ins” You will notice a search box inside 
    that window. Click on it and type in “pygame” and then press the “Enter” key 
  
    Under the Search box you should now see the Words pygame and under that 
    information about the Pygame Module. In the lower left you will see an “install” 
    button click on it and a dialogue box will appear and install pygame for you, 
    when it finishes you will have successfully installed pygame. 

## Pseudo Code 

    Player 1’s sprite is loaded from a file named player1.png 
    Player 1’s variable coordinates equal X 100 and Y 100 
    Player 1’s size is set too equal X 80 and Y 60 Pixels 
    Player 1's image, Coordinates and Size are now equal too variable named player1Image  

    The Targets sprite is loaded from a file named target.png 
    The Target sprite is given variable coordinates of X 500 and Y 500 
    The Targe is given the image size X 80 and Y 60 
    Variables size and coordinates and sprite are combined into one variable 
    Variable fireLock is set too equal 0 

    If the event MOUSEBUTTONDOWN is set, then
        fireLock is changed too equal 1 

    Screen is drawn with colour black defined by RGB code 0,0,0
        Variable mousePosition is pulled from Pygame 
        Variable newXPosition is pulled from pygame and fit too screen dimensions 
        Variable newYPosition is pulled from pygame and fit too screen dimensions 
        Variable player1XY is set as equal to the variables newX and newY 
        player1 sprite is now drawn with mousePosition pulled from above variable player1XY) 
        Target sprite is now loaded with image at coordinates from variable TargetXY 

       if pygame detects that both sprites are equal to the same area and firelock is set too 1 then  
       Target sprite will have a random new coordinate set 
            and fireLock will be set back too 0 

## Logical View

   Insert Image Here
  
## Screenshots with Context

   Insert Images here

## Final Code

   Insert Final Code here

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Author

* **Joshua Hardy** - [20035957](https://github.com/20035957)

## License

This project is licensed under the GNU General Public License v2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* My Lectures
* My Classmates
