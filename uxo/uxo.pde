// Criteria:
//
// Minefield
// - mine field size: 800px x 500px
// - The minefield has 500 mines when starting
// - 1 frame per second
// - Landmines are circular with a diameter of 5px
// - Once a landmine is disarmed it disappears from the minefield
// - The number of disarmed landmines are displayed on the canvas
// 
// Robot
// - Robot has to be in contact with a land mine for 5 seconds (5 frames) to disarm it
// - Robot can only disarm one landmine at a time
// - Landmine robot is rectangular 50px x 75px
//
// People
// - People are circular (different color from landmines) 25px in diameter
// - The number of people on the mine field is constant (nPeople). When a person dies a new person replaces him/her. When placed on the minefield people start at a radnom location.
// - People move randomly (Brownian motion) up to 5px in horizontal and/or vertical direction
// - A person dies when touching a landmine; the person and the landmine is removed from the minefield 
// - The number of casualties (number of people that have died) are keep track of using a counter displaued on the canvas
//
// Misc
// - The simulation runs for 1 minute. The goal is to disarm as many landmines as possible with as few casualities as possible.

// 1. Place mines
// 2. Add landmine clearing robot
// 3. Add interaction with people moving across the mine field and keeping track of the number of casualties
// 4. Explore different landmine clearing strategies 
// 5. Add a splash screen

// Physical Computer Extension
// Connect two breadboarded LEDs to GPIO pinsand have them light up when a mine is cleared (green LED) and when a person steps on a landmine (red LED). 
// Instructions for controlling GPIO pins from Processing: 
// - https://www.youtube.com/watch?v=mp5GzsSDH0s
// - https://hackaday.io/project/7008-fly-wars-a-hackers-solution-to-world-hunger/log/21899-controlling-raspberry-pi-gpio-pins-from-within-processing-environment

int nMines = 500; // Number of land mines placed
int nPeople = 10; // Number of people on the minefield at any given time

// Dimensions of the mine field (canvas size)
int h = 500;
int w = 800;
  
// Lists for keeping track of landmine coordinates
IntList x; 
IntList y; 

void setup(){
  size(800,500);
  background(255,255,255);
  
  // Generate list of landmine coordinates
  x = new IntList();
  y = new IntList();
  for (int i=0; i<nMines; i++){
    x.append(int(random(w)));
    y.append(int(random(h)));
  }
}

void draw() {
  for (int i=0; i<nMines; i++){
    ellipse(x.get(i), y.get(i), 5, 5);
    fill(255,0,0);
    noStroke();
  } 
}
