# Larvae Dispenser <img src="docs/images/logo/Diptera_logo_small.png?raw=true" height="50" align="right" alt="">
 
Diptera.ai's larvae dispenser was developed to achieve fast and reliable mosquito larvae aliqouting.

<br/>

<details open="open">
<summary>Table of Contents</summary>

- [API reference](#API-reference)
  - [Board utilities](#Board-utilities)
    - [Board](#Board)
    - [Low-Level Utilities](#Low-Level-Utilities)
    - [High-Level Utilities](#High-Level-Utilities)
  - [Running Units](#Running-Units)
- [Usage Example](#Usage-Example)
- [Miscellaneous](#Miscellaneous)

</details>

<br/>

[sorting unit]:https://miro.com/app/board/o9J_l2clY7A=/ 

## Machine parts

<img src="docs/images/photos/machine_v1.jpg?raw=true" height="500" align="center" alt="">

Following is a (very brief and **very partial**) description of all major players in the game.
Full details in the code.

### Board utilities

Board utilities are building blocks for electronic hardware components, meant to abstract away the actual Jetson GPIO 
(or other libraries e.g. i2c communication) syntax. 

#### Board 

The [Board] class is to be instantiated once and prepared with its low-level utilities. 
After that, we can start adding high-level utilities. 

```yaml
class Board:
  - pin_map
  - set_btn_kwargs
  - set_valve_kwargs
  - set_led_kwargs
  - add_a2d
  - add_d2a
  - add_expander
  - add_commandPin
  - add_button
  - add_valve
  - add_led
  - add_ls
```



[comment]: <> (| Class     | Main methods      | Description         |)

[comment]: <> (| :-------- | :---------------- | :-----------------  |)

[comment]: <> (| [Board]   | pin_map           | mapping from GPIO.BOARD to GPIO.TEGRA_SOC |)

[comment]: <> (|           | set_btn_kwargs    | set the default button configs |)

[comment]: <> (|           | set_valve_kwargs  | set the default valve configs |)

[comment]: <> (|           | set_led_kwargs    | set the default LED configs |)

[comment]: <> (|           | add_a2d           | add an A2D to the board       |)

[comment]: <> (|           | add_d2a           | add a D2A to the board       |)

[comment]: <> (|           | add_expander      | add an expander to the board       |)

[comment]: <> (|           | add_commandPin    | add an &#40;output&#41; commandPin to the board       |)

[comment]: <> (|           | add_button        | add an &#40;input&#41; Button to the board       |)

[comment]: <> (|           | add_valve         | add an &#40;output&#41; Valve to the board       |)

[comment]: <> (|           | add_led           | add an &#40;output&#41; Led to the board       |)

[comment]: <> (|           | add_ls            | add an &#40;input&#41; LightSensor to the board       |)

[comment]: <> (| [Board]   | - a <br> - a <br> - a <br> - a <br> - a <br> - a <br> - a <br> |)




[Board]: https://github.com/roei-yehuda/Diptera_Jetson/blob/bc08c4da799d6d4b86e4bebedcde9007f168bf27/utils/gpio.py#L393

#### Low-level Utilities

Low level utilities refer to electrical components, such as a DAC, which expand the capability of the 
Jetson Nano board, but are, in essence, "just" a means to a target (the target being the high-level utilities, described 
next). These are meant to be added to a Board, and that's it, i.e., not to be used directly from outside but only from 
within the Board and its high-level utilities.\
The classes [A2D], [D2A] and [expander] are API (abstract) classes, where the 
classes [MCP3008], [MCP4728] and [MCP23008] inherit them, respectively.

```yaml
class A2D:
  - alloc_new_channel
  - read_raw
  - read_volt
class D2A:
  - alloc_new_channel
  - set_raw
  - set_volt
class expander:
  - add_commandPin
  - add_valve
  - add_led
  - enable_interupts
  - add_button
```

[A2D]: https://github.com/roei-yehuda/Diptera_Jetson/blob/93cf2b8c722af0b1830c208b4f58e4ee0e7fc7c7/utils/PCB/A2D.py#L6
[D2A]: https://github.com/roei-yehuda/Diptera_Jetson/blob/93cf2b8c722af0b1830c208b4f58e4ee0e7fc7c7/utils/PCB/D2A.py#L7
[expander]: https://github.com/roei-yehuda/Diptera_Jetson/blob/93cf2b8c722af0b1830c208b4f58e4ee0e7fc7c7/utils/PCB/expander.py#L57
[MCP3008]: https://github.com/roei-yehuda/Diptera_Jetson/blob/93cf2b8c722af0b1830c208b4f58e4ee0e7fc7c7/utils/PCB/A2D.py#L49
[MCP4728]: https://github.com/roei-yehuda/Diptera_Jetson/blob/93cf2b8c722af0b1830c208b4f58e4ee0e7fc7c7/utils/PCB/D2A.py#L46
[MCP23008]: https://github.com/roei-yehuda/Diptera_Jetson/blob/93cf2b8c722af0b1830c208b4f58e4ee0e7fc7c7/utils/PCB/expander.py#L762 

#### High-Level Utilities

High level utilities refer to elements in the system used directly in the sorting unit's operation 
protocols: [CommandPin], [Led], [Valve], [Button], [LightSensor].\
A very simple inheritance tree exists between them:
```
                 Pin
       ___________|_________
      |           |         |
  CommandPin    Valve     Button
      |                     |
     Led                LightSensor
```
*(Should've had Valve inherit CommandPin :facepalm: ... todo.)*\
Note that **a child class inherits its parent's methods**.
```yaml
class CommandPin(Pin):
  - on
  - off
  - on_future
class Led(CommandPin):
  - flash
  - strobe
class Valve(Pin):
  - open
  - close
  - open_future
  - is_open
  - is_closed
  - get_latest_opening
  - get_latest_closing
class Button(Pin):
  - is_High
  - is_Low
  - add_event_callback
  - get_latest_event_time
  - wait_for_edge
class LightSensor(Button):
  - read_volt
  - set_comp_th
  - auto_calibrate
```

[CommandPin]: https://github.com/roei-yehuda/Diptera_Jetson/blob/2e51d37d2ee2ed768f07576f24ff8d11442d68be/utils/gpio.py#L150
[Led]: https://github.com/roei-yehuda/Diptera_Jetson/blob/2e51d37d2ee2ed768f07576f24ff8d11442d68be/utils/gpio.py#L195
[Valve]: https://github.com/roei-yehuda/Diptera_Jetson/blob/2e51d37d2ee2ed768f07576f24ff8d11442d68be/utils/gpio.py#L221
[Button]: https://github.com/roei-yehuda/Diptera_Jetson/blob/2e51d37d2ee2ed768f07576f24ff8d11442d68be/utils/gpio.py#L292
[LightSensor]: https://github.com/roei-yehuda/Diptera_Jetson/blob/2e51d37d2ee2ed768f07576f24ff8d11442d68be/utils/gpio.py#L345



### Running Units

A running unit is a class with a `_run_loop()` method which runs (in a loop) in a new Thread.\
The classes [RunningUnit] and [SortingUnit] are API (abstract) classes, setting rules for [TankerUnit] and [LinearSortingUnit].     
Here too we have a simple inheritance tree:
```
              RunningUnit
             ______|______
            |             |
        TankerUnit    SortingUnit
                          |
                   LinearSortingUnit
```

Following is the main API methods: 
```yaml
class RunningUnit:
  - _pre_run
  - _run_loop
  - _post_run
  - run
  - stop
  - pause
  - resume
  - is_alive
class TankerUnit(RunningUnit):
  - _close_all_valves
  - _check_water_levels
  - _check_elapsed_time
  - fill
  - raise_error
class SortingUnit(RunningUnit):
  - flush
  - wash
  - auto_calibrate
class LinearSortingUnit(SortingUnit):
  - _open_all_valves
  - _close_all_valves
  - _set_sorter_to
  - _set_bouncer_to
  - _set_flow
  - _wait_for_larva
  - _classify_larva
  - _cls_activate_bypass
  - _sorter_watch_for_duplicates
  - _sorter_watch_for_output
  - raise_error
```

[RunningUnit]: https://github.com/roei-yehuda/Diptera_Jetson/blob/ee8ef21ee7d076cc4c686792c08aadf06123ecff/RunningUnit.py#L8
[SortingUnit]: https://github.com/roei-yehuda/Diptera_Jetson/blob/ee8ef21ee7d076cc4c686792c08aadf06123ecff/SortingUnit.py#L4
[TankerUnit]: https://github.com/roei-yehuda/Diptera_Jetson/blob/ee8ef21ee7d076cc4c686792c08aadf06123ecff/TankerUnit.py#L10
[LinearSortingUnit]: https://github.com/roei-yehuda/Diptera_Jetson/blob/ee8ef21ee7d076cc4c686792c08aadf06123ecff/LinearSortingUnit.py#L9

## Usage Example

```python
from utils.log import *
from utils.utils import *  # this imports configs dictionary
from utils.gpio import Board
from LSU.TankerUnit import TankerUnit
from LSU.LinearSortingUnit import LinearSortingUnit

### setup board
board = Board()

# set default parameters for buttons, valves, ...
board.set_btn_kwargs(configs.btn)
board.set_led_kwargs(configs.led)
board.set_valve_kwargs(configs.valve)

# add low-level utilities
board.add_a2d(a2d_class=MCP3008, init_kwargs=configs.a2d)
board.add_d2a(d2a_class=MCP4728, init_kwargs=configs.d2a_0)
board.add_expander(expander_class=MCP23008, init_kwargs=configs.expander_0)

# add high-level utilities
UI_led_g = board.add_led(
  **configs.pins.o.UI_led_g.to_dict(),
  **configs.led
)
UI_btn_0 = board.add_button(
  **configs.pins.i.UI_btn_0.to_dict(),
  **configs.btn,
  callback_funcs=[UI_led_g.flash]
)

# setup running units
tanker = TankerUnit(board=board)
lsu = LinearSortingUnit(board=board)

# run
tanker.run()
lsu.run()
```


## Miscellaneous

- Start up:\
  Upon rebooting the Nano, go to the project's directory and activate the virtual environment, 
  by running (in the terminal):
  ```bash
  cd ~/Diptera_Jetson/
  pipenv shell
  ```
  The above is aliased by a `diptera` command, i.e. you can alternatively run in the terminal:
  ```bash
  diptera
  ```
  Then, run:
  ```bash
  python3 -i main.py
  ```

- Configs:\
  Many parameters are to be pre-configured in the configs.py file.
  To do that on the Nano, run:
  ```bash
  gedit configs.py &
  ```

- Run log:\
  A new log file is generated in every run (once `utils.log` is imported) and saved to the `log\` directory.
  
- A2D check:\
  To get a live reading from the A2D:
  ```bash
  python3 utils/PCB/A2D.py
  ```




