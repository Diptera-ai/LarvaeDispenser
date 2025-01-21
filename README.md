# Larvae Dispenser <img src="docs/images/logo/Diptera_logo_small.png?raw=true" height="50" align="right" alt="">
 
The larvae dispenser was developed by [Diptera.ai](https://diptera.ai "Diptera.ai's Homepage") to achieve fast and reliable mosquito larvae aliqouting.

<br/>

<details open="open">
<summary>Table of Contents</summary>

- [Overview](#Overview)
  - [Machine](#Machine)
  - [Program](#Program)
- [Protocol](#Protocol)
- [Notes](#Notes)

</details>

<br/>

## Overview

<br/>

### Machine

<img src="docs/images/photos/machine_v1.jpg?raw=true" height="500" align="center" alt="">

1. bla
2. bla bla


<br>

### Program

<img src="docs/images/photos/gui/1_basic.png?raw=true" height="500" align="center" alt="">

blaaaaaa

<br>

## Protocol
   
<br>

1. **Larvae and system preperation**\
For the most accurate results, make sure the sample and the system itself are as clean as possible.

   1. Collect larvae using 30-mesh strainer and transfer to a 0.5L tray.
   2. Use light treatment to move larvae to the edge of the tray so the larvae are separated from debris (remnants of food and eggs).
   3. Collect larvae that congregate at the edge of the tray and run another light treatment.
   4. After collecting the majority of the larvae in the tray, kill the rest of the larvae left in the tray (which should be a negligible amount compared to the number of larvae hatched).
   5. Before putting larvae into the bottle, make sure that the bottle is clean from larvae or debris. Add lukewarm water to the bottle, and then the larvae. Do not fill the bottle above the marked line.
   
   <br/>
   
   > 
   > Larvae density should be around 80,000 larvae per liter of water.
   
   6. Place the collecting cup.
   7. Connect the bottle to the system, make sure it is closed tightly.
   
<br>

2. **Aliquoting**

   1. Open the LarvaeDispenser program (double-click the icon on the desktop).\
   Upon startup, the bottle will be pressurised and initial calibration will take place - the **calibration** buttom will show green while calibration is still ongoing.
   
   <br>
   <img src="docs/images/photos/gui/0_start_up.png?raw=true" height="500" align="center" alt="">
   <br>
   
   2. Set the **Target #Larvae**
   3. Press **Start**. The system will begin running larvae from the bottle to the cup and automatically stop when it reaches the target number. The **Start** button will show green while the system is running (i.e. counting), and the live count is updated simultaneously. You may also press the **Stop** button at any time during the run, if need be.\
   
   <br>
   <img src="docs/images/photos/gui/2_start.png?raw=true" height="500" align="center" alt="">
   <br>
   
   4. Once finished, the plot will be updated with a **histogram of the events' signal magnitudes**. The legend depicts different runs by their initiation timestamps.\
   Below, for example, a screenshot of the program after two runs, the most recent one in blue.
   
   <br>
   <img src="docs/images/photos/gui/3_finished_count.png?raw=true" height="500" align="center" alt="">
   <br>
   
   5. Set the **sensitivity threshold**, and press **Apply New Threshold** to get a new reading of the total updated count. The higher the threshold, more events will be included in the count. Lowering it correctly can remove noise.\
   In the example below, resetting the threshold to *0.75* updated the count to 918. 
   
   <br>
   <img src="docs/images/photos/gui/4_sensitivity_th_moved.png?raw=true" height="500" align="center" alt="">
   <br>
   <br>
    
   >
   > A good rule of thumb is to set the sensitivity threshold to one of the first minimas from the right. This removes noise, basically events caused by remaining debris.
   
   9. Make sure the bottle doesn’t run out of water and does not reach the bottom line marked on the bottle.
   10. Once you reach the end of the larvae, you can add water to the bottle (see below, in *Notes*, how to open the bottle) which will dilute the density of the larvae but will allow you to continue counting them without reaching the bottom line of the bottle.

<br/>

3. **Finish up**\
It is important to wash the system thoroughly after use.
   1. Open the bottle (see below in *Notes*).
   2. Remove remaining larvae in the bottle, and clean the bottle thoroughly.
   3. Fill the bottle with lukewarm clean water close it tightly like before.
   4. Place an empty collecting cup.
   5. Turn the **Pressure On** and press **Wash**. At the end of day, it is advisable to run **Wash** a couple of times.

<br/>

## Notes

<br/>

- Opening a pressurised bottle:
   - Switch to **Pressure Off**.
   - Unscrew - just a little bit - the bottle cap (clear plastic) to relieve the pressure.
   - Pop the connectors cap (black plastic).
- Detecting a blockage:
  - When you hear a loud sound from the dispenser it could be one of two things: there is a blockage in the tubes of the dispenser or the pressure went up to 30. 
  - When the water runs slowly without noise: there is a blockage in the tubes of the dispenser or the cap is not closed tightly enough.

