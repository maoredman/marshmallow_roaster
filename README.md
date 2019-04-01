# marshmallow_roaster

We made an automatic marshmallow roaster in two days during the 2019 [MakeNTU hackathon](https://www.facebook.com/makentu.ntuee/), and won 2 awards: Best Creativity (chosen from 50 teams) and Highest Popularity (we received 40 votes)!

## How we made our roaster

### Heat source
After visiting several stores that sold electronic materials, we still couldn't find one that sold heating elements (preferable nichrome wire). However, hackers use whatever resources they can find, and one of our teammates came up with the clever idea of tearing down nichrome wire from a toaster machine, so we spent around $12 on a cheap toaster to get the goodies inside. We put some space between the nicrome wire, and raised them with wooden blocks to match the height of marshmallows on sticks. The result looked like this:

![](https://i.imgur.com/WkXyGBB.jpg)

We did some testing to ensure that the temperature was indeed high enough to roast marshmallows, which it was (phew!), and got that nice brown coating without much effort :D

### Automatic roasting tray

If you've roasted marshmallows over a fire before, you know that it's hard work -- your hands get uncomfortably hot, and the marshmallows burn very easily :'( 

We came up with the idea of designing something mechanical to turn the marshmallow sticks for us, which would both enable more control over the roasting process and save people the inconvenience of having to continuously turn and watch over those needy little marshies.

To implement this, we connected four stepper motors and a button to a Raspberry Pi. The motors turned the sticks after a button-press, and stopped turning when the button was pressed again. We could also code the turning duration into the Pi if we wanted. Because heat **rises** and all the circuitry lay **below** the nichrome wire, we were fairly confident that the electric components wouldn't be exposed to high temperature, but just to be on the safe side, we added a temperature sensor to monitor the circuitry surroundings. During all our roasting sessions, the temperature never exceeded 35&deg;C, which is slightly colder than the human body (very safe). Here's what the tray looked like:

![](https://i.imgur.com/Vi2rhvW.jpg)

