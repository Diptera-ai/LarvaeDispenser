# Larvae Dispenser <img src="docs/images/logo/Diptera_logo_small.png?raw=true" height="50" align="right" alt="">
 
The larvae dispenser was developed by [Diptera.ai](https://diptera.ai "Diptera.ai's Homepage") to achieve fast and reliable mosquito larvae aliqouting.

<br/>

<details open="open">
<summary>Table of Contents</summary>

- [Overview](#Overview)
    - [Machine](#Machine)
    - [Program](#Program)
- [Protocol](#Protocol)  
    [1. New Day / Program Startup](#NewDay)  
    [2. New Bottle](#NewBottle)  
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

<img src="docs/images/gui/0_general.png?raw=true" height="500" align="center" alt="">

The program allows you to control, monitor, and analyze the aliquoting.  
The window is split to the control panel on the left, and info panel to its right.  
- On the control panel, from top to bottom: input box for target number of larvae, basic operation buttons for start/stop/wash/calibrate, and system pressure switch.  
- On the info panel, first is the live count readout. Below it, framed under the label of 'plot', a display of the day's runs' data. To the right of the graph, you can set the sensitivity threshold to account for debris in the water causing inaccuracies (more information below in the work protocol).  

<br>

<a name="Protocol"></a>
# Protocol
   
<br>


<a name="NewDay"></a>
## 1. **New Day / Program Startup**

At the beginning of a new day, or when starting the program, perform a wash and calibration with clean water. 

1. Connect a bottle with **clean** water, make sure it is closed tightly. 
2. Place a collecting cup.
3. Start the LarvaeDispenser program (double-click the icon on the desktop).
- Upon startup, the program tries to update itself so make sure there is **internet connection**.  
- Once up and running, the bottle will be pressurised. 
4. Press **Wash**. 
4. Press **Calibrate**.
   
<br/>
<img src="docs/images/gui/1_start_up.png?raw=true" height="500" align="center" alt="">
<small>Program at start-up. The Start button will appear gray, indicating a calibration is required.</small>
<br/>
<br/>

<br/>
<img src="docs/images/gui/2_cal.png?raw=true" height="500" align="center" alt="">
<small>It is necessary to do a calibration at the start of a new day. When pressing Calibrate, the program will remind you to wash with clean water before proceeding.</small>
<br/>
<br/>

<a name="NewBottle"></a>
## 2. **New Bottle**

When loading a new bottle with larvae, it is important to run one aliquot to set the sensitivity threshold according to the larvae population in the new bottle. 

1. Prepare larvae according to [this](#prep-larvae) and fill a new bottle.
> 
> **Larvae density should be around 10,000 larvae per 1 liter of water.**


2. Connect the new bottle to the system: 
- If another bottle is already connected, remember to turn off the pressure before disconnecting it. 
- Connect the new bottle. Make sure it is closed tightly. Turn the pressure on.
3. Place a clean collecting cup.
4. Press **Wash**. The purpose of this wash is to fill the tubes with larvae water and rid of any bubbles. 
- Once you see larvae in the cup, you can stop the wash.
- Empty the cup.
5. Set the **Target #Larvae**.  
   For the purpose of setting the sensitivity threshold, it is recommended to aliquot at least 500 larvae.
6. Press **Start**. \
   The system will begin running larvae from the bottle to the cup and automatically stop when it reaches the target number of events detected. The **Start** button will show green while the system is running (i.e. counting), and the live count is updated simultaneously.

<br>
<img src="docs/images/gui/3_start.png?raw=true" height="500" align="center" alt="">
<small>While running a count, the start button shows green.</small>
<br>
<br>

7. Once finished, the plot will be updated with a **histogram of the events' signal magnitudes**. A big larva will be detected as a high magnitude event, and vice versa - small debris will show as low magnitude events.\
   The legend depicts different runs by their initiation timestamps.
   The most recent measurement is the one in thick blue line, previous runs will appear in dashed lines. \
   Below, for example, a screenshot of the program after the first run.

<br>
<img src="docs/images/gui/4_finished_count.png?raw=true" height="500" align="center" alt="">
<small>Once the count finished, the plot is updated with the events' signal histogram</small>
<br>
<br>

8. Set the **sensitivity threshold**, and press **Set new threshold** to get a new reading of the total updated count. 
- The sensitivity threshold is 0.0 by default. This means that all events are counted as larvae. However, typically, larvae water contain certain amounts of debris smaller than the larvae. This debris will show in the histogram as noise, or a (small) peak of the curve on the leftmost side of the histogram.  \
Examining the histogram and setting the sensitivity threshold to the first minima to the left of the significant curve, let's call it the debris-larvae minima, allows you to remove from the count events that were probably caused by debris.
- Using the horizontal scale below the plot, you may test new sensitivity thresholds (marked by a red vertical line) and see how applying it affects the count. 
In the example below, resetting the sensitivity threshold to *0.071* updated the count to 795. \
Pressing **Set new threshold** will apply the change and keep that threshold for later runs too (now the line appears black).

- This step is usually required only after the **first** aliquot with a new bottle. Consecutive aliquots from the same bottle typically share the same sizes distribution and therefore the same debris-larvae minima.
- Note that the total number of larvae for this cup is jeopardised. In the example below, you can expect there to be only 795 larvae in the cup, not 1000 as the given target. This is because, of course, the sensitivity threshold was set to 0.0 for this measurement - in the next ones, as described [here](#Aliquot), that is not the case.

<br>

>
> **A new sensitivity threshold should be set after each bottle replacement. A good rule of thumb is to set the threshold to the first minima to the left of the significant curve. This, basically, removes events caused by debris.**

<br>

<a name="sens-th-example-0"></a>
<img src="docs/images/gui/5_sensitivity_th_moved_red.png?raw=true" height="500" align="center" alt="">
<small>Trying a new sensitivity threshold to remove events probably caused by debris</small>
<br>
<br>
<img src="docs/images/gui/6_sensitivity_th_moved_black.png?raw=true" height="500" align="center" alt="">
<small>After pressing **Set new threshold**, the newly selected sensitivity threshold is applied and saved for future runs.</small>
<br>
<br>

- More examples for sensitivity threshold applications can be found below, [here](#sens-th-example-1).

<a name="Aliquot"></a>
## 3. **Aliquot** 
In a consecutive run from the same bottle, the count is updated according to the new sensitivity threshold (black vertical line).

1. Set the **Target #Larvae**. \
It is recommended to aliquot at least 250 larvae every time.
2. Place an empty collecting cup.
3. Press **Start**. \
The system will begin an aliquot, running larvae from the bottle to the cup and automatically stop when it reaches the target number of events detected - AFTER applying the sensitivity threshold. I.E., smaller events than the threshold will be ignored.
- You may press the **Stop** button at any time during the run, if need be. Note, this will stop the ongoing aliquot without an option to resume it.
- Repeat.
  
<br>
<img src="docs/images/gui/7_finished_second_count.png?raw=true" height="500" align="center" alt="">
<small>A consecutive run from the same bottle usually shares the same debris-larvae minima.</small>
<br>
<br>

4. Make sure the water level in the bottle does not go below the lower markings, as this will make the count inaccurate and may cause errors.\
If water level reaches the lower marking, add water to the bottle. 
> **Do not open the bottle when the system is pressurised. See [here](#open-bottle).**

<br/>

<a name="Finish"></a>
## 4. **Finish**
It is important to wash the system thoroughly after use.

1. Open the bottle (remember to depressurise first, see [here](#open-bottle)).
2. Remove remaining larvae in the bottle, and clean the bottle thoroughly.
3. Fill the bottle with clean water (or use the second clean water bottle with the blue connectors cap) and close it tightly.
4. Place a collecting cup.
5. Switch to **Pressure On** and press **Wash**. Repeat wash 3 times.
6. Pressing **Save daily report** will generate a csv file with the day's counts at the daily_reports directory on the desktop.
7. When you exit, the program will send system logs to Diptera.ai. Please make sure that you have internet connection.


<br/>

<a name="Q&A"></a>
## Q&A

<br/>

<a name="prep-larvae"></a>
- How to prepare larvae for aliquoting?
    - For the most accurate results, make sure the sample is as clean as possible. Separate larvae from debris by using a 30-mesh strainer. Clean the strainer from the debris and repeat a couple of times.
    - Before putting larvae into the bottle, make sure that the bottle is clean from larvae or debris.
    - Add lukewarm (~25C) water with larvae to the bottle.  
    - Do not fill the bottle above the marked line.
    - Larvae density should be around 10,000 larvae per 1 liter of water.

<a name="open-bottle"></a>
- How to open the bottle when the system is pressurised?
   - Switch to **Pressure Off**.
   - Wait 10 seconds or so for pressure to relieve.
   - Pop the connectors cap (black plastic).
   - (if needed to fill/empty the bottle) unscrew the bottle cap (clear plastic).

 
- How to detect and remove a system blockage:
  - If water runs slowly (droplets instead of a steady stream) while the bottle is ok (there's enough water, caps are closed tightly and pressure is on), then there might be a blockage in the system tubes.
  - To remove a blockage, start a count, or a wash operation, if it is not already ongoing. Fill a 50ml syringe with water and connect a tip to it. Connect the tip to the end of the tube (above the larvae collection cup) and press the syringe to run water backwards through the system, to clear the blockage back to the bottle. 
  - Open the bottle (see above how to open a pressurised bottle) and remove the debris that caused the blockage.

<br/>

<a name="sens-th-example-1"></a>
### Sensitivity Thresholds Examples

<br>
<img src="docs/images/gui/8_sensitivity_th_moved_black_example-2.png?raw=true" height="500" align="center" alt="">
<small>Compared with the example above, this sample was cleaner and so setting the sensitivity threshold to the debris-larvae minima at 0.105 resulted in updated count of 979 larvae.</small>
<br>
<br>
