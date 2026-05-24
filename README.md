Current Progress
Got a clean 500x500 window up and running.
Hardcoded a custom alien sprite using basic shapes (`ellipse`, `circle`, `line`).
Fixed the main game loop and window-closing events (sorted out indentation bugs).
Created all characters: Dockalien, planet

Dev Log & Troubleshooting 2026/5/17
GitHub Codespaces issue**: Cloud servers have no physical display, so running the code here completely freezes the terminal and spikes the CPU to 100%.
Fix: Write and manage the code here, but connect via **local VS Code (Remote)** to actually launch and test the game window.

Todo/fixed  list
Need to add stars at background  (fixed)
Make Aliendock move by keyboard.  (fixed)
fixed tuple division error in screen.get_size()
ixed infinite loop by mergining while loops
Unified character position variables
Added movment logic for UP,DOWN,RIGHT,LEFT key.

Summary
A lightweight space shooting game built using python and pygame. 
It uses geometric character designs and custom math and is built with a clean loop.
