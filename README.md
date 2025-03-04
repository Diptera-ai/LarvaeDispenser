# Larvae Dispenser <img src="docs/images/logo/Diptera_logo_small.png?raw=true" height="50" align="right" alt="">
 
The larvae dispenser was developed by [Diptera.ai](https://diptera.ai "Diptera.ai's Homepage") to achieve fast and reliable mosquito larvae aliqouting.

<br/>

<details open="open">
<summary>Table of Contents</summary>

- [Overview](#Overview)
    - [Machine](#Machine)
    - [Program](#Program)
- [Protocol](#Protocol)  
    [1. Larvae Preparation](#Larvae-Preparation)  
    [2. System Preparation](#System-Preparation)  
    [3. Aliquot](#Aliquot)  
    [4. Finish](#Finish)  
- [Q&A](#Q&A)

</details>

<br/>

<a name="Overview"></a>
## Overview

<br/>

<a name="Machine"></a>
### Machine

<img src="docs/images/photos/machine_v1_annotated.jpeg?raw=true" height="500" align="center" alt="">

1. Larvae collecting cup
2. Larvae water bottle
3. Bottle cap
4. Bottle connectors cap
5. Computer connections: HDMI, USB, LAN
6. Power/computer box
7. Power cable


<br>

<a name="Program"></a>
### Program

<img src="docs/images/photos/gui/1_basic.png?raw=true" height="500" align="center" alt="">

The program allows you to control, monitor, and analyze the aliquoting.  
The window is split to the control panel on the left, and info panel to its right.  
- On the control panel, from top to bottom: input box for target number of larvae, basic operation buttons for start/stop/wash/calibrate, and system pressure switch.  
- On the info panel, first is the live count readout. Below it, framed under the label of 'plot', a display of the day's runs' data. To the right of the graph, you can set the sensitivity threshold to account for debris in the water causing inaccuracies (more information below in the work protocol).  

<br>

<a name="Protocol"></a>
## Protocol
   
<br>

<a name="Larvae-Preparation"></a>
### 1. **Larvae Preparation**

For the most accurate results, make sure the sample, and the system itself, are as clean as possible.

   1. Separate larvae from debris by using a 30-mesh strainer. Clean the strainer from the debris and repeat a couple of times.
   2. Before putting larvae into the bottle, make sure that the bottle is clean from larvae or debris. 

<br>

<a name="System-Preparation"></a>
### 2. **System Preparation**
   
   1. Add lukewarm (~25C) water with larvae to the bottle. Do not fill the bottle above the marked line.  
   
   > 
   > **Larvae density should be around 10,000 larvae per liter of water.**  
   
   2. Connect the bottle to the system, make sure it is closed tightly.
   3. Place the larvae collecting cup.
   4. With the bottle and cup in place, open the LarvaeDispenser program (double-click the icon on the desktop).\
   Upon start-up, the bottle will be pressurised and initial calibration will take place - the **calibration** button will show green while calibration is still ongoing. See screenshot below.\
   During the calibration, the system fills its tubes with water from the bottle. A small amount will be poured to the cup, remember to empty it before starting any count. 
   
   <br/>
   <img src="docs/images/photos/gui/0_start_up.png?raw=true" height="500" align="center" alt="">
   <small>Program at start-up</small>
   <br/>
   <br/>
   

<br>

<a name="Aliquot"></a>
### 3. **Aliquot** 
   At This point the bottle should be in place, and pressurised, and the larvae collecting cup empty and ready too - as seen in the image above in the [machine overview](#Machine).
   1. Set the **Target #Larvae**.
   2. Press **Start**. The system will begin running larvae from the bottle to the cup and automatically stop when it reaches the target number of events detected. The **Start** button will show green while the system is running (i.e. counting), and the live count is updated simultaneously.\
      You may also press the **Stop** button at any time during the run, if need be. Note, this will stop the current run without option to resume it.
   
   <br>
   <img src="docs/images/photos/gui/2_start.png?raw=true" height="500" align="center" alt="">
   <small>While running a count, the start button shows green</small>
   <br>
   <br>
   
   3. Once finished, the plot will be updated with a **histogram of the events' signal magnitudes**. A big larva will be detected as a high magnitude event, and vice versa - a small debris will show as a low magnitude event.\
      The legend depicts different runs by their initiation timestamps.\
   Below, for example, a screenshot of the program after two runs, the most recent one in blue.
   
   <br>
   <img src="docs/images/photos/gui/3_finished_count.png?raw=true" height="500" align="center" alt="">
   <small>Once the count finished, the plot is updated with the events' signal histogram</small>
   <br>
   <br>
   
   4. Set the **sensitivity threshold**, and press **Apply New Threshold** to get a new reading of the total updated count. The higher the threshold, more events will be included in the count. Lowering the sensitivity threshold correctly allows you to remove from the count events that were probably caused by debris.
      >
      > **A good rule of thumb is to set the sensitivity threshold to the first minima to the left of the significant curve. This, basically, removes events caused by remaining debris.**
   
      In the example below, resetting the threshold to *0.25* updated the count to 918. 
   
   <br>
   <img src="docs/images/photos/gui/4_sensitivity_th_moved.png?raw=true" height="500" align="center" alt="">
   <small>Setting a new sensitivity threshold to remove events probably caused by debris</small>
   <br>
   <br>
    

   5. Make sure the water level in the bottle does not go below the lower markings, as this will make the count inaccurate and may cause errors.\
   If water level reaches the lower marking, add water to the bottle. 
   > **Do not open the bottle when the system is pressurised. See [here](#open-bottle).**

<br/>

<a name="Finish"></a>
### 4. **Finish**
   It is important to wash the system thoroughly after use.
   1. Open the bottle (remember to depressurise first, see [here](#open-bottle)).
   2. Remove remaining larvae in the bottle, and clean the bottle thoroughly.
   3. Fill the bottle with clean water (or use the second clean water bottle with the blue connectors cap) and close it tightly.
   4. Place an empty collecting cup.
   5. Switch to **Pressure On** and press **Wash**. Repeat wash 3 times.

<br/>

<a name="Q&A"></a>
## Q&A

<br/>

<a name="open-bottle"></a>
- How to open the bottle when the system is pressurised?
   - Switch to **Pressure Off**.
   - Wait 20 seconds or so for pressure to relieve.
   - Unscrew - just a little - the bottle cap (clear plastic).
   - Pop the connectors cap (black plastic).
   
<br/>
     
- How to detect and remove a system blockage:
  - If water runs slowly (droplets instead of a steady stream) while the bottle is ok (there's enough water, caps are closed tightly and pressure is on), then there might be a blockage in the system tubes.
  - To remove a blockage, start a count, or a wash operation, if it is not already ongoing. Fill a 50ml syringe with water and connect a tip to it. Connect the tip to the end of the tube (above the larvae collection cup) and press the syringe to run water backwards through the system, to clear the blockage back to the bottle. 
  - Open the bottle (see above how to open a pressurised bottle) and remove the debris that caused the blockage.

