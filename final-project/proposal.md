## Final Project Proposal

#### Codeable Bookends

*Modularity, Design System, Generative / Manual Twins*

This project is strongly inspired by this work:

[Codeable Objects](http://highlowtech.org/?p=2254)

The aim is to create a modular bookend based on radial symmetry. Bookends consist of two components: (1) a base -- this part resembles a block with the books on one side and notches on the other -- and (2) fans -- these can be 3d printed or handcrafted and fit into the notches on the base radially (resembling an open book).

The user would leverage a design system that helps generatively create a series of fans based on a sketch from the user. Mirroring and symmetry are used to determine the output. The user can then create fans using selected designs to create 3d printable fans using additive manufacturing or export designs / riff on them / create something wholly original for each fan.

The opportunity for modular assembly introduces the possibility of engaging with manual creation. My goal would be to create an interlocking system as well as experiment with material constraints to create hybrid objects.

My concerns with this project are as follows:
- It is too similar to codeable objects
- There won't be time to create a unified interface and to use the design system the user will have to go between tools
- This will require experimentation with hand-crafting and physical materials that I don't have on hand. Delays in acquiring these materials might make it hard to complete the project as intended given the quick turnaround. One workaround is to use paper cutouts and 3d print frames to assemble these as fans.

#### Music Votives

*Design System*

This project is inspired by this work:

[Gaudiesque Stackable Candle Masks](https://www.instructables.com/id/Gaudiesque-Stackable-Candle-Masks/)

One of my growing research interests in linked media and finding ways to translate expression across mediums. Listening to [Appalachian Spring by Aaron Copland](https://www.youtube.com/watch?v=8e3rVcSy3IQ) I was thinking of [Martha Graham's choreography](https://www.youtube.com/watch?v=XmgaKGSxQVw) to this piece (which can be read as memory) and reflecting on the sculptural aspects of the dance.

I'm interested in creating a design system that translates a piece of music into a vase or votives (perhaps stackable -- see below). The user would be able to control mappings between sound and form to create and explore emergent behavior. In general, creating design systems that allow users to edit mappings that dictate form are more interesting to me than ones that allow for direct editing.

I also found this web app to create stl files for 3d-printable QR codes -- [QR2STL](https://flxn.de/qrcode2stl/) -- that could be printed on the bottom or inside surface of the base of the design. These could provide links to media that includes this audio (the source of inspiration) or the audio source itself. One challenge is that we have single nozzle extruders so I would have to manually swap out filament or maybe use 3d printed QR code as a stamp.

If the designs were stackable, then it QR codes could provide links to different parts of a video (for example) to create a closer correlation between the input and output of the system.

My concerns with this work are as follows
- It is too similar to the Stackable Candle Masks work
- PLA will melt. Candle votives might not make sense as a design objective
- The user might have to interface with multiple systems to generate elements that contribute to the final design
- I have very little experience working with audio

#### GCode Gardening

*Design System, Creative Performance*

This work is partly inspired by Madeline Gannon's work:
[Atonaton](https://atonaton.com/)

And while I came up with this idea before finding this work I would now like to incorporate elements inspired by it in my project:
[John Edmark Golden Angle](http://www.johnedmark.com/#/phi/)
<!-- https://www.youtube.com/watch?v=B5p2A5mazEs -->

This idea is very experimental and would be an extension of our assignment to generate GCode from scratch. Instead of designing a slicer, this system would leverage the printer's behavior in a more organic fashion. Slicers generally work layer by layer building up the final structure. In this project, individual "plants" would grow with sequential motion including budding leaves and flowers.

The user would specify a seed. The seed would be the first item to print. Its formal properties would dictate the structure of the plant that would then be printed. The user would be able to manipulate these mappings and also adjust settings that would control the overall characteristics of the garden.

Plants would grow by first printing a seed, sprouting (a small print), generating a sapling (stage 2 print), and then growing over the years. Plants would be diverse from small wildflowers to large trees.

I would like to generate a means to capture the garden as it grows at each stage. While I think the time constraints prevents automating photography, the goal is to create a stopmotion video showcasing the printing of the garden along with video clips showing the garden growing overtime. The GCode would include interrupts where the observer could picture the garden. I am not sure if it would be possible to introduce some kind of manual control (resume print) to facilitate this process.

I'll most likely begin by extending my course assignment to simulate the behavior of a spirograph (and a spirograph within a spirograhp! See [hypercycles](https://shop.momath.org/gift-hypercycles.html)).

My concerns with this project are as follows:
- This work is too experimental
- The design system (mappings or exposing them) seems underdeveloped
- Intersections between the nozzle and printed garden to date (while not costly) might be challenging to avoid
- The output will likely look nothing like a garden. What would be the right way to evaluate this project?

#### Modular Origami

*Modularity, Generative / Manual Twins*

Modular origami involves the assembly of small individual folded components to create larger geometric superstructures. I think it would be compelling to experiment with designing a means to print modular units. The challenge would be in replicating creases and folds so that the final design is flexible enough to be manipulable so that it can be assembled accordingly.

Furthermore, the modularity of these units introduces the possibility of intermixing different materials. I would mix the 3d printed units with paper folded units to create structures that involve a high degree of manual craft.

While I think it will be challenging to reach this stage, I think it would be neat if the overall system could suggest ways and forms that could be assembled using the interlocking forms that would be printed.

This would be a more exploratory and open-ended project.

My concerns with this project are as follows:
- There would be a high degree of manual assembly involved that might be time consuming and not very interesting
- The generative aspect of this system is minimal
- The materiality in these objects (along with the geometry and precision) shapes their overall effect. Printed components might not be visually interesting.
