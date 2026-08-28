10
Basic Optics Techniques and Hardware
Walter F. Smith
CONTENTS
10.1 Laser Safety.................................................................................................................................. 228
10.2 Lasers ........................................................................................................................................... 229
10.3 Optical Hardware......................................................................................................................... 229
Optical Tables and Breadboards................................................................................................... 229
Posts, Postholders, and Pedestals ................................................................................................. 230
10.4 Optical Elements.......................................................................................................................... 232
Lenses........................................................................................................................................... 233
Mirrors.......................................................................................................................................... 234
Neutral Density Filters ................................................................................................................. 235
Beamsplitters................................................................................................................................ 235
Polarizers and Waveplates............................................................................................................ 236
10.5 Beam Expanders .......................................................................................................................... 238
10.6 Alignment..................................................................................................................................... 238
10.7 Protection, Storage, and Cleaning................................................................................................ 240
10.8 Organization................................................................................................................................. 241
Labeling........................................................................................................................................ 241
Storage.......................................................................................................................................... 242
Tools Organization ....................................................................................................................... 242
Lab 10A The Quantum Eraser, Simple Version.................................................................................. 242
10A.1 Introduction.......................................................................................................................... 242
Classical Polarization and Interference............................................................................... 242
Quantum Polarization and Interference .............................................................................. 243
10A.2 Precision Optical Alignments .............................................................................................. 243
Walking the Beam............................................................................................................... 243
Aligning a Laser with the Grid of Holes............................................................................. 243
10A.3 Mach-Zender Interferometer and the Quantum Eraser........................................................244
Insert Polarizing Beam Splitter Cube and Align the Beam with the Table.........................244
Insert Mirrors 3 and 4, and Align the Beams ...................................................................... 244
Insert NPBS cube and Align the Beams with the Table...................................................... 245
Adding the Final Polarizer .................................................................................................. 245
Understanding Interference, and the “Quantum Eraser” .................................................... 246
227

228
Experimental Physics
10.1 Laser Safety
Lasers are widely used in current physics research because of the narrow range of wavelengths emitted
by the laser, the high intensity, the high degree of collimation, and the long coherence length.*
Depending on the power level, the hazard associated with a laser can be extreme or negligible. The
frst thing you should fnd out when using a laser is its class. Class 1, 1M, 2, and 2M lasers (classes I, II,
and IIa in the old system) are safe to use without protective eyewear, as long as you’re not viewing the
beam through optical instruments (e.g., a microscope or magnifying glass); your blink response is quick
enough to protect your eyes. You should never intentionally look into the beam. Class 3R lasers (class IIIa
in the old system) can technically be used without protective eyewear, so long as the wavelength is visible
and you’re not viewing the beam through optical instruments.† These lasers are “potentially hazardous
under some direct and specular refection viewing conditions if the eye is appropriately focused and
stable, but the probability of an actual injury is small.” Many consider it good practice to use protective
eyewear with class 3R lasers, especially when creating the setup; check with your instructor. For class 3B
and class 4 lasers (classes IIIb and IV in the old system), you must always use protective eyewear, as well
as protective barriers and curtains to prevent accident exposure to others. For class 4 and the high end of
class 3B lasers, you must also use skin protection. Make sure your protective eyewear is designed for the
wavelength of laser you’re using.
Concept test (answer below‡): If you’re using a blue laser, should your protective eyewear be blue or
orange?
In addition, you should adhere to the following standard practices. Accidental exposure to the laser is
most likely when you are creating your setup. So, if you are using anything above a class 2 or 2M laser,
you should do the setup using reduced beam power and/or with a flter directly in front of the laser. You
should block or turn off the laser before adding a new optical element. When at all possible, keep the
optical components close enough together that it’s not possible for someone to put their head between
them. (This is usually advantageous for optical reasons as well as for safety.) Arrange your setup so that
the beam is in a horizontal plane, well below eye level. Remove shiny jewelry from hands and wrists, to
avoid accidental refections. If you need to bend down (e.g., to pick up something you dropped), frst turn
off the laser or block it at the source.
When wearing eye protection, you’re usually unable to see the beam at all, since that wavelength is
completely fltered. So, to do the alignment, you should shine the beam onto a viewing card, which you
can purchase from most optics supply companies (e.g., ThorLabs); make sure you have one that’s appro­
priate for the wavelength you’re using. For blue lasers, the fuorescence shifts the wavelength emitted
from the card to red, so that you can see it through your eyewear. The cards are less effective for red
lasers, since fuorescence can only shift the emitted light to longer wavelengths. However, you can usu­
ally still see the spot on the card. If you don’t have the special fuorescent card, a piece of white paper is
often adequate; the paper is treated with fuorescent chemicals to make it appear “whiter than white.” In
some cases, fuorescent index cards can work well.
Another method is to set up a low power laser that is collinear with the higher power laser, and at a
different wavelength, so that you can easily see it while wearing the eye protection suited for the higher
power laser. It’s important to be as scrupulous as possible about arranging the collinearity, and even
* The coherence length can be thought of as the length of a photon. It is important in applications involving interference.
For example, to observe interference in a setup where the laser is split into two beams which are then brought back
together, the path lengths must be equal to within a coherence length. For gas lasers (e.g., HeNe lasers), the coherence
length is typically tens of cm. For diode lasers (e.g., those used in a laser pointer), the coherence length is less than a mm.
Both of these can be dramatically extended by frequency stabilization techniques, so that coherence lengths of tens or
thousands of meters are possible. The coherence length for non-laser sources is a fraction of a mm. As you can show in
Problem 10.1 (available on ExpPhys.com), the coherence length x is related to the range of wavelengths emitted by the
laser by Δλ ≅ λ2/Δx, and to the range of frequencies Δf emitted by Δf ≅ c/Δx.
† ANSI Z136.1-2014 American National Standard for Safe Use of Lasers.
‡ Blue glasses transmit blue light, so would be totally ineffective in protecting against a blue laser. Orange glasses absorb
blue light.

229
Basic Optics Techniques and Hardware
when you’ve aligned things optimally with the low power laser, some fne tuning will be needed with
the high power laser.
Before turning on a laser, you should check with your instructor about whether you need to complete
additional laser safety training.
10.2 Lasers
You are most likely to encounter two types of lasers in physics research: gas lasers and diode lasers. The
decision between types is usually based on the desired wavelength. Gas lasers (e.g., HeNe) inherently
have good coherence length (tens of cm), a very narrow band of emitted wavelengths (with a “linewidth”
Δλ less than 10 pm), and excellent collimation. They are available in polarized and “randomly polarized”
versions. Unfortunately, the randomly polarized version is not “unpolarized” (meaning a superposition
of all possible polarizations), but instead has a polarization that often varies over timescales of tens of
seconds as the laser warms up. Full warm-up requires an hour or more, and even them the polarization
may be affected by changes in room temperature. Therefore, I recommend you purchase only polarized
lasers, which are usually about the same price.
Diode lasers are available in standard and frequency-stabilized versions. The standard versions are
much less expensive than gas lasers. The linewidth is a few nm, with correspondingly short coherence
length (a few tenths of a mm at best). The central wavelength can vary by a few nm between nominally
identical units and depends somewhat on room temperature (about 0.2 nm/°C). When possible, purchase
a “laser module,” which includes optics to produce a fairly well collimated beam; however, often the
beam profle is elliptical rather than circular.
The best frequency-stabilized diode lasers (“external cavity diode lasers”) are much more expensive
than low-end gas lasers, but have linewidths of less than 1 fm and can be tuned over a small range (typi­
cally about 0.1 nm).
Concept test (answer below*): What is the coherence length (essentially the length of a photon) for a
laser with a 1 fm linewidth and a wavelength of 633 nm?
10.3 Optical Hardware
Optical Tables and Breadboards
Optics setups are usually constructed either on an optical “breadboard” (a metal plate with an array
of tapped (i.e., threaded) holes), or an optical table (a table with an array of tapped holes in the top
surface). Optical tables and breadboards provide three functions: (1) the precision array of tapped
holes allows convenient mounting of optical elements. (2) Tables and breadboards have a high ratio
of stiffness to mass, so that if there are vibrations, everything moves together as much as possible,
resulting in little relative motion. (3) Tables and breadboards provide some isolation from vibrations
in the foor.
The choice between a table and the various types of breadboards involves a tradeoff between cost
and the other desirable aspects. The least expensive option is a breadboard made from solid aluminum.
This has the lowest stiffness-to-mass ratio and is also the most strongly affected by thermal expansion.
However, it is adequate for all but the most demanding experiments; more costly options are usually only
needed when data must be taken over periods of days, so that thermal expansion becomes critical, or
when a laser beam must remain focused on the same spot over several hours to a tolerance of less than
100 µm, or for experiments that are extremely sensitive to vibrations. (For all the experiments described
in this book, a solid aluminum breadboard is fne.) Aluminum breadboards have the advantage that
they can be easily moved. You can easily get some isolation of the breadboard from building vibrations
by putting an array of “Sorbothane” disks between the breadboard and the table it is placed on; this
* Δλ ≅ λ2/Δx ⇔Δx ≅ λ2/Δλ = 400 m.

230
Experimental Physics﻿
elastomer is engineered for use in vibration isolation applications.* It’s essential to put the breadboard
on a very sturdy table.
The next step up is breadboards made from steel with an internal honeycomb construction, which
enhances stiffness. These have significantly less thermal expansion. The thicker the breadboard, the
higher the stiffness-to-mass ratio, but the heavier (and so harder to move) it is. The high-end choice is
optical tables, which can include pneumatic legs for the best possible vibration isolation.
In all cases, to minimize the effects of vibrations and thermal expansion, it’s best to make optics
setups as compact and close to the breadboard/table surface as possible. For example, if two parts
of an interferometer are located only 10 cm away from each other, the distance between them will
be changed by thermal expansion by half as much as if they were separated by 20 cm, and they will
vibrate in unison at least twice as well. However, it’s important not to drive yourself crazy by making
things so close together or so low down
near the table surface that it causes
headaches with installing additional
components or making adjustments. For
the vertical positioning, it’s worthwhile
to think ahead and consider which com-
ponent in your setup will require the
largest vertical distance from the table-
top to the center of that component (e.g.,
a large sample mount, or something that
must be mounted on a stage that rotates
in the horizontal plane), then set every-
thing else to that height.
When purchasing the table or bread-
board, you must make the fateful decision
between imperial (inch-based) threads on
the holes and spacings between the holes,
or metric (cm-based). It’s best to stick
with one system or the other as much as
you can.
Posts, Postholders, and Pedestals
The most common method of mount-
ing optics is the post/postholder system
shown in Figure 10.1. This allows con-
venient adjust of height. The posts and
postholders are each available in a wide
range of heights. Each optic element is
held in a mount, which is attached to the
top of the post using a small diameter
(8–32 or M4) screw. In some cases, this
is a “setscrew,” i.e., a screw with no head,
but instead with a hexagonal socket for an
Allen wrench on one end. In other cases,
the mount is attached with a “capscrew,”
i.e., a screw with an Allen head.
* I recommend 1 inch diameter, 0.5 inch thick disks, with a durometer rating of 30. These can be obtained with stick-on
adhesive from IsolateIt.com. You can determine how many disks to use using the desired weight of about 1 kg per disk.
However, avoid positioning them more than 40 cm apart, since this will lead to “drumhead” behavior. If necessary, you
can cut them in half to avoid this.
lens in
mount
setscrew
post
cap
screw
post-
holder
pedestal
adapter
mirror in mount
(back surface shown)
post
“pitch”
adjust
“yaw” adjust
“pitch”
adjust
“yaw”
adjust
mirror
front
surface
FIGURE 10.1 Post and postholder system. Top left: some optics
attach to the post via a setscrew. Bottom left: assembled version. Top
right: other optics attach via a cap (Allen head) screw. The mirror
mount allows adjustment of the forward/backward tilt (“pitch”) and the
left/right azimuthal angle (“yaw”). Bottom right: assembled version.

231
Basic Optics Techniques and Hardware
FIGURE 10.2 Top images: screwing a postholder into the optical table. Bottom row: After disassembly, if the screw
was put with the Allen head up (toward the post holder), it can be easily removed whether it winds up in the table or in the
postholder.
The postholder has a large diameter (1/4–20 or M6 thread) threaded hole at the bottom. Often, this is
used to secure the postholder directly to the tabletop, using a setscrew, as shown in Figure 10.2. Screw
the setscrew partway into the postholder, then screw this assembly into the tabletop. When you are ready
to disassemble things, you unscrew the assembly from the tabletop; it’s essentially random whether the
setscrew will wind up partly screwed into the tabletop or partly screwed into the postholder. Note that
the setscrew has a hexagonal (Allen) socket on one end only. This should go on the end that screws into
the postholder, not on the end that screws into the table. That way, when you unscrew the postholder from
the tabletop, if the screw remains partly screwed into the tabletop, you can use an Allen key to remove it.
If instead it remains partly screwed into the postholder, you can reach with an Allen key through the top
of the postholder to remove the screw.
Screwing the postholder directly into the tabletop makes it easy to align optics in straight, perpen­
dicular, or 45° lines. However, in many cases, one needs more fexibility with positioning in the hori­
zontal plane. Of the various ways to attach something to a tabletop, the clamping fork system shown
in Figure 10.3 gives the most fexibility and is the fastest. It’s best to purchase the fork with a “captive
screw,” since this saves time hunting for the screw.
In some cases, such as when a large object must be supported or when working in a lab that doesn’t
use the clamping fork system, it’s better to use a base with a larger footprint. In this case, frst attach the

232
Experimental Physics
FIGURE 10.3 Clamping fork system, including captive screw and base adapter for postholder.
FIGURE 10.4 Attaching a postholder via a base.
base to the postholder by putting a screw through
the recessed area on the base, then screw the base
to the tabletop, as shown in Figure 10.4.
An alternative to the post and postholder sys­
tem is to use a pedestal, as shown in Figure 10.5.
These provide more rigidity, and so are preferred
for applications that are very sensitive to vibra­
tions such as interferometers. However, the height
adjustment is limited. One can purchase vari­
ous heights of pedestals, and usually the critical
elements are all mounted on the same height.
However, some additional adjustability is available
via spacer rings, which can be purchased in a few
different thicknesses.
pedestals
spacer
fork
FIGURE 10.5 Left: pedestal system. Middle: assem­
bly including spacer ring; note long setscrew. Right: fully
assembled with spacer ring.
10.4 Optical Elements
A recurring theme when dealing with optical elements such as lenses and flters is the need for labeling.
In some cases, an expensive optical element can become almost useless if it is not labeled. For example,

233
Basic Optics Techniques and Hardware
if you fnd an unlabeled round piece of something that looks like transparent glass, it could be a quarter
or half waveplate (you’ll learn more about those later in this chapter), but determining which wavelength
it’s designed for requires multiple tests. So, the mount for the optical element should be clearly labeled,
including the wavelength or range of wavelengths the element is designed for. If the element is removed
from the mount, it should immediately be placed into a labeled container or a labeled small cloth bag.
(It is helpful to keep the containers for the optics elements you’re using in a box which is kept near your
optics table or breadboard.) When labeling a mounted optic, it’s best to use a label printer; handwritten
labels rub off too quickly. (It’s adequate to use handwritten labels for storage bags or containers, since
these are handled less.) It requires signifcant discipline to adhere to these practices, but it pays off hugely.
Lenses
The most important parameter for a lens is the focal length, i.e., the distance beyond the lens at which an
incident parallel beam (such as a laser) is brought to a focus. The next most important parameter is the
range of wavelengths the lens is intended for; this is determined by the material the lens is made from
(e.g., fused silica lenses are needed for ultraviolet), and the anti-refective coating.
However, you may need to deal with unlabeled lenses. If you need an accurate value for the focal
length f, you can accurately measure the distance s from a source to the lens, and the distance i from the
lens to the image, and use the “thin lens equation”:
1
1
1
=
+
(10.1)
f
s
i
However, often an estimate for f is all that’s needed. You can roughly determine the focal length by fnd­
ing the distance from the lens at which an image of the overhead lights is formed.
Concept Test (answer below*): Does this give an overestimate or an underestimate of the focal
length?
The “power” of a lens is defned as the inverse of the focal length, and has units of diopters, where
one diopter equals an inverse meter. If one lens is positioned just after another (so that the two are “in
series”), the total power is approximately equal to the sum of the individual powers.
To bring a parallel incident beam to the minimum diameter focus, the lens should have a hyperboloid
shape.† One can purchase such “aspheric” lenses, but they are expensive, especially for large diameters.
It’s less costly to make lenses with a spherical surface, so almost all lenses have this shape. However, it
has the drawback that rays parallel to the optic axis but far from it are brought to a focus at a different
point than rays close to the optic axis; this is called “spherical aberration.”
Lenses can of course be used to form images; for such applications, double convex lenses (curved on
both sides) are often best. However, the main use of lenses in this book is for controlling the diameter
of laser beams. For such applications, it is best to use plano-convex lenses. To minimize spherical aber­
ration, the lens should be oriented so that parallel rays enter or exit the lens on the curved side. (See, for
example, Figure 10.11.)
One can purchase pre-mounted lenses, which have the advantages of being pre-labeled, easier to han­
dle, and easier to combine with other optical elements by screwing them together. However, they’re about
40% more expensive than unmounted lenses. It is not diffcult to put an unmounted lens into a mount.
The mount has a thin lip on one side. Place the lens into the mount, so that it rests against the lip. The lens
is held in place with a retaining ring, which should be tightened with a “spanner” (a special wrench), as
shown in Figure 10.6. Avoid using improvised tools (such as tweezers) to tighten the retaining ring, since
this leads to frustration and occasionally a scratched lens.
* Since the overhead lights are not actually infnitely far away, the light from them is somewhat divergent at the position of
the lens, so this measurement is an overestimate of the focal length.
† Optics, Third Edition by E. Hecht (Addison-Wesley, 1998)

234
Experimental Physics
lens
mount
lens
retaining
ring
spanner
lens
mount
with
lens
inside
notch in
retaining ring
tooth on
spanner
FIGURE 10.6 How to mount a lens. Left: parts. Center: engaging the spanner with the retaining ring. Right: fully
assembled.
FIGURE 10.7 Flip mirror.
Mirrors
Most mirrors have a refective surface made from aluminum (about 90% refectance for visible wave­
lengths) or silver (about 97% refectance). Aluminum mirrors withstand high humidity and accidental
fngerprints better than silver mirrors. The price is about the same. In most cases, the mirror is coated
with a thin transparent flm, such as SiO2, to limit tarnishing and reduce the effect of scratching. Mirrors
are installed in mounts that allow fne adjustment of the angle around a vertical and a horizontal axis, as
shown in Figure 10.1c,d.
Occasionally, it’s useful to use a “fip mirror,” which can be folded down to allow the beam to pass
over it, or folded up to direct the beam in a different direction, as shown in Figure 10.7. Unfortunately,
the angle adjustment screws for such mirrors are not very precise, so you should arrange for the primary

235
Basic Optics Techniques and Hardware
path to be the one that’s used when the mirror is fipped down. An alternative that is bulkier, but more
precise, is to combine a conventional mirror mount with a fip adapter.
Neutral Density Filters
Neutral density flters reduce the power of light. For example, this allows the experimenter to explore a
range of powers that varies over a few orders of magnitude, a broader range than is usually possible using
the electrical power adjustment on the laser (if there is one).
They are rated by the “optical density,” or OD, where
Power in
OD
= 10
(10.2)
Power out
Concept test (answer below*): An OD 1 flter and an OD 2 flter are placed back to back. What is the
ratio of the output power to the input power for this assembly?
The power reduction is achieved either by refecting or absorbing part of the light. The absorptive type
of flter is preferred in most cases.† For these, the ratio of input to output power varies by about 10% over
the range of optical wavelengths. They can be purchased with or without anti-refective coating,
The mounting system for flters is the same as for lenses. Filters can be purchased mounted or
unmounted, with the mounted version costing signifcantly more. However, one often wishes to combine
flters by screwing them together, which is much easier with mounted flters.
Beamsplitters
It is often necessary to split a laser beam, most frequently to create two paths for an interferometer or for
sensing the laser power. One can purchase plate beamsplitters, in which one side of a glass plate is coated
with a partially refecting layer, or cube beamsplitters (see Figure 10.8).
Both types absorb little of the incident power, but conventional cube beamsplitters absorb up to 15%.
Therefore, for high power applications, “laser line” cube beamsplitters (which absorb very little at a spec­
ifed wavelength) or plate beamsplitters are preferred. Plate beamsplitters are more diffcult to mount,
and are more easily damaged, so the cube type is usually preferred.
Both types are available in “non-polarizing” and “polarizing” varieties. For polarizing beamsplitter
cubes, the transmitted beam is horizontally polarized to a very high degree, while the refected beam
is primarily vertically polarized, but may contain up to 5% horizontally polarized light. The transmit­
ted beam of the non-polarizing type has only a modest effect on the polarization of the beam; for cube
beamsplitters, the ratio between vertically and horizontally polarized light is altered by at most 7%.
However, the polarization of the refected beam can be substantially changed. The intensity ratio of
refected horizontal and vertical polarizations is very similar to that in the incident beam, but the phase
between them can be changed. For example, incident light that is polarized at 45° relative to the horizon­
tal will have a transmitted beam that is also 45°, but the refected beam may well be elliptically polarized.
* The OD 1 flter reduces the power by a factor of 101 = 10, and the OD 2 flter reduces it by another factor of 100, for a total
reduction of a factor of 1000. Note that the OD of the combination is simply the sum of the individual ODs.
† Refective neutral density flters are more diffcult to use, in part because the refective surface is unprotected, so that they
are easily scratched by being touched. Also, the refected beam carries much of the power, leading to annoyance and also
safety concerns. (One safe way to deal with the refected beam is to direct it into a “beam stop,” an object that can safely
absorb all the laser power, by orienting the flter at an angle slightly away from perpendicular to the beam.) However, these
flters are more uniform in the ratio by which the power is reduced as wavelength is varied; the ratio is constant to within a
few percent over the range of optical wavelengths. They are somewhat better for high power applications, since absorbing
the power in the flter can lead to damage or thermal expansion (and associated beam distortion) of the flter. However,
the advantage over absorptive flters is only about a factor of two. Ordinary refective neutral density flters should not be
stacked immediately adjacent to each other, since refections amongst the various surfaces can lead to undesired interfer­
ence effects and also to surprising changes in the OD of the stacked assembly. However, for no increase in price one can
purchase “wedged” flters, in which the refective surface is slightly angled relative to the mount, eliminating these issues.

236
Experimental Physics
dot indicates
the half of the cube
where light should enter
FIGURE 10.8 Cube beamsplitters. Left: some are clearly marked with the intended beam path. Center and right: for oth­
ers, the half of the cube on which the beam should enter is shown by a dot. The cube is held in a kinematic prism mount.
(See Section 11.2 for the explanation of elliptical polarization.) The effect on the polarization of the
refected beam depends on the type of beamsplitter, so it is best to test experimentally.
Because of subtleties with anti-refection coatings, the incident beam should come in on the side
marked with a dot or with an incoming arrow, as shown in Figure 10.8. Beamsplitter cubes are usually
mounted on prism mounts, which provide angle adjustments similar to those in a mirror mount. To hold
the cube onto the mount, loosen the clamp on the clamping arm, lower the arm until the nylon-tipped
setscrew just touches the cube, then tighten the clamp. Finally, gently tighten the nylon-tipped setscrew
by a half-turn or so; overtightening can bend the support post for the clamping arm, and cause stress in
the cube which impairs its performance.
Polarizers and Waveplates
Control of polarization is essential for many physics experiments and applications. Polarization is con­
trolled with beamsplitters (see above), polarizers, and waveplates.
The ideal polarizer only transmits light that is polarized along the transmission axis. Real polarizers
are quantifed with the “extinction ratio.” This is defned, assuming a polarized input beam, as the ratio
of maximum transmission power (transmission axis aligned with input polarization) to minimum trans­
mission power (transmission axis perpendicular to input beam). For most applications, flm polarizers
(the least expensive kind) are adequate; their extinction ratio is at least 100 and is more than 500 over
most of the visible range.
As with lenses, flm polarizers are mounted using retaining rings. However, excess stress can impair
the performance of the polarizer. So, they should be mounted using a “stress-reducing retaining ring,”
which incorporates an elastomer O-ring. The retaining ring should be tightened only until it is slightly
snug – enough to keep the polarizer from moving, but no more.
Waveplates are used to convert between linear and circular polarization, and to change the angle of
polarization. As with polarizers, they have a unique axis that is perpendicular to the laser direction, and
which determines their action; for waveplates, this is called the “fast axis.” See Section 11.2 for more
details. Waveplates are more sensitive to stress than polarizers, so I recommend purchasing the pre­
mounted version, even though it is a little more costly.
The transmission axis (for polarizers) and the fast axis (for waveplates) is marked by the manufacturer,
often by a line on the edge of the optic. However, the marking for a particular polarizer or waveplate
can be off by as much as 5°. Therefore, when mounting the optic, it’s important to determine the actual
transmission or fast axis experimentally. For polarizers, you can roughly check the transmission axis
by observing light refected off the foor, e.g., from the window (see Figure 10.9). This light is partly
polarized parallel to the foor, so that you should see the least refected light when the polarization axis

237
Basic Optics Techniques and Hardware
FIGURE 10.9 Roughly checking polarization axis. Left: the light from the overhead lights down the hall is refected off
the foor. The refected light is mostly horizontally polarized. The transmission axis of the polarizer is horizontal, so the
light gets through. Right: the transmission axis is vertical, so the light is blocked.
is vertical. To fnd the polarization axis more precisely, mount the polarizer on a breadboard or optical
table, and use a polarized laser or another polarizer with known transmission axis.
To fnd the true fast axis of a quarter wave plate (qwp), start with horizontally polarized light, and pass
it through the qwp with the marked fast axis at 45° above the horizontal. Put a linear polarizer after the
qwp and observe the strength of the transmitted beam as the linear polarizer is rotated. If the fast axis is
actually at 45°, the beam emerging from the quarter wave plate will be circularly polarized, so that the
strength of the beam transmitted through the linear polarizer is independent of the polarizer angle. If it
isn’t, make small adjustments to the angle of the qwp until the beam strength doesn’t vary as the linear
polarizer is rotated. The true fast axis of the qwp is now at 45°.
To fnd the true fast axis for a half wave plate (hwp), start with horizontally polarized light, and pass it
through the hwp with the marked fast axis at 45° above the horizontal. The light emerging from the hwp
should be linearly polarized, with the polarization refected about the fast axis. So, if the fast axis is truly
at 45°, the light emerging from the hwp should be polarized vertically. Use a linear polarizer after the
hwp to measure the actual polarization angle. The true fast axis is at half this angle.
Polarizers and waveplates should be installed in rotary mounts, so the angle of the transmission axis or
fast axis can be easily varied. It’s worth the small extra expense to purchase rotary mounts with adjust­
able zero, so that the transmission or fast axis can be easily and accurately aligned with the scale on the
mount.*
For most rotary mounts, the angle is read at the top, but usually one wants to measure the angle of the
transmission or fast axis relative to the horizontal (see Figure 10.10a). Therefore, you should mount the
optic with the transmission or fast axis aligned with the 90 degree mark of the rotary mount. Then, when
you read “0” degrees (at the top of the rotary mount), the axis is horizontal. IMPORTANT: although
this is the smart way to mount optics, many labs use the convention of aligning the transmission or
fast axis with the 0 degree mark on the rotary mount. If you’re using an optic that was mounted
by someone else, make sure you know what convention they used. If you mount the optic yourself,
* It is possible, with patience, to align the axis of the optic with the numerical scale on a rotary mount without adjustable
zero. First, make a tiny mark (about 1–2 mm long) with an extra fne point Sharpie on the front surface of the optic at the
position of the axis of the optic. Set the optic into the mount, with the Sharpie mark about 25° counterclockwise from the
desired orientation and tighten the retaining ring with the spanner. The Sharpie mark will likely still be too far counter­
clockwise. Loosen the retaining ring slightly while exerting as little downward pressure as possible with the spanner, then
retighten while exerting more downward pressure. You should fnd that the Sharpie mark has advanced a little clockwise.
Repeat until it’s at the desired position.

238
Experimental Physics
10o
fast axis
a
b
FIGURE 10.10 (a) Rotary mount marked at top, but angle measured relative to horizontal. (b) optic rotated by 10°.
mark the mount clearly, e.g., “fast axis aligned with 90 deg mark.” Also, you should orient the
mount so that the markings are on the “downstream” side of your setup, i.e., so that when you’re look­
ing at the markings you are looking back up toward the laser. This way, when you rotate the optic 10°
counterclockwise, the reading on the mount (read off the top of the mount) will be “10” degrees, and the
transmission or fast axis will be at 10° relative to the horizontal (see Figure 10.10b).
10.5 Beam Expanders
It is common to need to expand the beam to a larger but
still collimated beam (one having parallel rays). There
are two ways of doing this, as shown in Figure 10.11. The
version with the diverging lens is preferred, because it’s
more compact and avoids concentrating the beam to a
small volume. (For a high power beam, this can heat the
air to the extent of causing fuctuations in the beam path.)
However, for low power lasers such as those used in this
chapter and Chapter 11, one often uses the version with
converging lenses, since there are usually more focal
lengths available in a typical lab.
Concept test (answer below*): What is dout /din for
f
f
1
2
dout
din
a
f2
dout
din
-f1
b
FIGURE 10.11 (a) Keplerian beam expander. (b)
Galilean beam expander; note that f1 < 0.
the version in Figure 10.11a, in terms of the focal lengths? How about for the version of Figure 10.11b?
10.6 Alignment
As you’ll learn in Lab 10A.2 “Precision optical alignments,” good alignment of a laser requires two mir­
ror bounces. There are three common ways to arrange this, as shown in Figure 10.12; the choice between
them depends on where you need to ft the rest of your optics.
* Both parts: d /d
=
.
f f/
out
in
2
1

239
Basic Optics Techniques and Hardware
3
2
1
reversal
z fold
ÿgure 4
FIGURE 10.13 The beam will pass through the left two
FIGURE 10.12 Three methods for achieving two mirror
elements before hitting the rightmost one. Install the far-
bounces.
thest downstream element (number 1) frst, then number
2, then number 3.
It is usually best to start with a beam that is
aligned with the grid holes (as instructed in Lab
10A.2 “Precision optical alignments”), and then position each new element along this beam, without
moving the beam itself. If there will be several optical elements in a row, start with the one that is farthest
“downstream,” i.e., farthest from the laser, as shown in Figure 10.13. That way, you have a clean beam for
alignment, one that is unaffected by upstream optics.
When you introduce a new optical element, you should center it on the beam. If the element is a 1-inch
circular optic, targets such as the one shown in Figure 10.14 make this easy.
Usually, you want to align an optical element exactly perpendicular to the beam. One way to do this is
by observing the small part of the beam that is back refected from the element. Align the element so that
the back refected beam goes straight back in the direction of the incident beam. Sometimes, it is helpful
to have the incident beam come through a card with a hole in it, so that the back refection can be seen
more easily, as shown in Figure 10.15.
FIGURE 10.14 A target can be hung on a one-inch circular optic for alignment.

240
Experimental Physics
back
re˜ection
hole
FIGURE 10.15 Back refection method of alignment, including card with hole.
10.7 Protection, Storage, and Cleaning
All optics are adversely affected by fngerprints, which scatter light and, over time, can actually etch the
optical surface. So, whenever handling unmounted optics (lenses, mirrors, etc.), you must wear gloves.
Some prefer disposable latex or nitrile gloves, because they provide better dexterity, while others prefer
cloth gloves because they’re reusable. You can handle mounted optics without gloves, as long as you’re
very careful not to touch the optical surfaces.
Despite your best efforts at avoiding fngerprints, it’s inevitable that you will need to clean optics.
There are two cardinal rules, which must never be violated:
1. Use a can of compressed gas or a rubber bulb to blow off the optic, removing all visible dust,
before applying other cleaning methods. Otherwise, the dust will act as an abrasive in later
cleaning stages, scratching the optic. Do not use your own breath to blow off the optic, as there
is always some chance of accidentally getting tiny droplets of spit on it. (Ick!) If using a can of
compressed gas, be sure to hold it within 15° of vertical; if you tip it further, liquid will come
out and stain your optic.
2. Use only lens paper, a clean cloth, or a cotton swab for cleaning. Other products, such as
KimWipes, are too scratchy. A previously used cloth may have abrasive particles embedded in
it.
To clean an optic (after blowing with air), the most commonly recommended method is the “tissue with
forceps” method: fold a piece of lens tissue into a wad, grab with a pair of locking forceps, and apply
a few drops of isopropanol. Shake any excess isopropanol off; if you have too much, it will get into the
threads of the mount, and draw dirt out from them. Wipe the tissue across the surface of the optic, rotat­
ing the lens tissue as you go so that a new part of the tissue is constantly coming into contact with the
optic; this prevents dust pickup up by one part of the tissue from scratching the optic. Discard and replace
the tissue as needed.
If the above doesn’t work, and the optic to be cleaned is a mirror that protrudes from its mount (the
usual case), you can try the “drop and drag” technique, which is described on ExpPhys.com.
If the above techniques are not effective, you have two options:

241
Basic Optics Techniques and Hardware
FIGURE 10.16 Cloth bag for storing optics elements, kept closed with paper clips.
(1) Remove the optic from its mount, and clean with the full immersion or “drop and drag” tech­
niques; see the link on ExpPhys.com for a full description of these techniques, which are very
gentle.
(2) In research, one must balance the need for getting things done quickly (which truly is quite
important) with the need to protect optics for decades of useful life. It takes a good deal of time
to remove the optic from its mount, clean it using one of the techniques above, remount it, and
re-align it. Therefore, if the optic is not expensive (e.g., a standard mirror with a protective
coating or a standard lens for optical wavelengths), you can clean it without removing it from
the mount by breathing on it with an open mouth (“Haaaaah”) to coat it with a thin layer of
moisture from condensation, then wiping it with a clean cloth (not your shirt!) or lens tissue,
just using your gloved fnger (rather than forceps) to move the cloth or tissue, similar to the way
you’d clean eyeglasses. Make sure you have observed cardinal rule 1 (blowing it off) before you
wipe it. If the optic is anything other than a basic inexpensive lens or mirror, you should spend
the time to remove it from the mount and clean it in one of the more gentle ways.
You should store optics elements in their original containers, or in labeled cloth bags, to prevent scratch­
ing. Small cloth bags are available for low cost from optics suppliers. Keep them closed with paper clips,
as shown in Figure 10.16.
10.8 Organization
More than in any other area of experimental physics, it is essential to keep your optics well organized.
I’ll be more than usually dictatorial here, to effciently impart lessons I’ve learned from bitter experience.
Each optical element or piece of hardware is a signifcant expense and put together the costs add up more
quickly than you can imagine. Without signifcant attention to organization, you will waste a great deal
of time and money.
Labeling
Unlike electronic components, optics elements are usually not labeled after you take them out of the box.
However, each one may be suited only to a limited wavelength range, and there is no way to tell this by
looking. There is no way to tell the difference between a quarter wave plate and a half wave plate just
by looking. Some more exotic optic elements look just like a quarter wave plate but have a completely
different function. Although you can re-measure the focal length of a lens, you waste time doing so. So,
you must label every optic element as soon as it is put in a mount, as shown for example in Figure 10.10.
The label must include the wavelengths for which the optic is designed; in the case of lenses, you can

242
Experimental Physics
use a shorthand for the type of anti-refective coating, as long as it will be understood clearly by others
working in your lab. If you remove the optic from the mount, you must immediately place it in a labeled
box or bag. You must use a label maker to create the labels; handwritten labels rub off quickly.
Storage
You should store optics elements and hardware in a storage cabinet with multiple small drawers. If you’re
the one setting this up, spend some time fguring out an organization scheme that makes sense to you,
or use the one recommended on ExpPhys.com. Have a cardboard box underneath your optics bench, and
as soon as you remove an optic element from its small box or bag, put the box or bag in the cardboard
box. That way, when it’s time to disassemble your setup, you have all the containers ready. Don’t delay in
returning the optics parts to the proper storage cabinets when you disassemble the setup.
Tools Organization
Mount a magnetic strip on or near your optics bench. Keep the most common Allen wrenches stuck to it.
Lab 10A The Quantum Eraser,* Simple Version†
Learning goals: Become familiar with research-grade mounting systems for optics and with
beam splitters.
Pre-lab reading: 10.1–10.8, plus the coverage of polarization of light in your intro physics book
Safety notes: You will be using a class 2 laser. Therefore, you do not need to use safety glasses
or other unusual precautions. Do not intentionally look into the beam or point it at people. You
should adhere to the other standard laser safety practices described in Section 10.1.
10A.1 Introduction
A central theme in quantum mechanics is the interplay between the behavior of a physical system and
experimentalists’ knowledge about the state of the system. The idea that the reality of a physical system
depends on the information about the system that can be measured with the apparatus takes some getting
used to, but one cannot understand quantum experiments without accepting this principle. The canoni­
cal example of this phenomenon is the two-slit experiment, in which the amplitudes for photons passing
through one slit or the other interfere and result in wavelike interference patterns – but only if it is not
possible even in principle to determine which slit a photon went through with the apparatus used.
Classical Polarization and Interference
As you’ve reviewed in your intro physics text, for light passing through a polarizer, only the component
of the electric feld parallel to the transmission axis gets through, i.e., Etransmitted
= Eincident cosq , where θ is
the angle between the incident polarization and the transmission axis. Since the intensity is proportional
to E2, we see that Intensity ˜ cos2q ; this is Malus’s Law.
In the classical view, the interference pattern observed on a screen is due to constructive or destructive
interference between the various electric (or magnetic) feld waves traveling via all possible paths from
the source to the point on the screen.
* Parts of this lab were written by Jacob Seely and David Colletta, and are used with their permission.
† You can do a more sophisticated version, using one photon at a time, in Lab 20C. That lab gives much deeper insights into
the quantum mechanics.

243
Basic Optics Techniques and Hardware
Quantum Polarization and Interference
In the quantum view, to understand the interaction of a photon with a polarizer, we resolve the incident
wavefunction into a new one expressed in the basis of the axes parallel and perpendicular to the transmis­
sion axis. Putting this anthropomorphically, the photon is required to “choose” whether it has polariza­
tion along the transmission axis (and so gets transmitted) or instead has polarization perpendicular to the
transmission axis (and so gets blocked). The probability amplitude Ψ of “choosing” to be parallel to the
transmission axis is proportional to cos θ, and the fraction of photons that gets through is proportional to
2
˜
2 ° cos q , in agreement with Malus’s Law.
In the quantum view, the interference pattern observed on a screen is due to constructive or destructive
interference between the various parts of the wavefunction Ψ traveling via all possible paths from the
source to the point on the screen. If there is a way to determine the path that the photon traveled, then the
multiple paths are collapsed to a single path, and there is no interference.
10A.2 Precision Optical Alignments
Walking the Beam
In many optical experiments, you need to get the beam
to go precisely through the centers of several optics ele­
ments. The procedure for doing so requires two mirrors,
and by the end of this exercise you’ll see why.
If you are planning to do 10A.3 “Mach-Zender
Interferometer and the Quantum Eraser,” you should use
a polarized laser* for this exercise, with the polarization
set at 45° relative to the horizontal. Use a linear polarizer
to check the polarization angle.
Create the setup shown in Figure 10.17, with mirror 1
mounted on a post and postholder and mirror 2 mounted
on a short pedestal. You are provided with two cards with
small holes in them, also mounted on short pedestals.
Position them so the beam refected off mirror 2 passes
through both holes, with the cards separated by about a half
meter along the beam direction; clamp everything in place.
Change the settings of both angle control knobs on both of the mirrors, so that the beam is nowhere
close to going through the holes. Now, use the combination of the four adjustments (two knobs on two
mirrors) to get the beam going back through both holes; you’re only allowed to adjust the mirrors – don’t
move the cards. Figure out and record the systematic procedure for making the adjustments. Why do we
need two mirrors to accomplish the task of getting the beam to go through both holes?
Before you go on, it’s important that you have a full understanding of the above questions, so please
check the “answers” on ExpPhys.com.
Aligning a Laser with the Grid of Holes
Many experiments require aligning the beam exactly (within a very small tolerance) parallel to the grid
of holes on the optical table or breadboard.
Your goal is to adjust the two mirrors so that the refection from mirror 2 is precisely parallel (hori­
zontally) to the rows of screw holes in the table, and also precisely parallel in the vertical direction to
* If a polarized laser is not available, you can use an unpolarized laser with a polarizer set to 45o in front of it. However, as
the laser warms up, the distribution of polarization modes changes, so the intensity of the beam emerging from the polar­
izer varies over periods of several seconds up to several minutes. For this lab, that’s okay, as long as you know to expect
it.
FIGURE 10.17 Initial setup.

244
Experimental Physics
the table surface. The technique you will learn
can be applied to a wide variety of optical setups.
Mount an iris mounted to a baseplate in such
a way that the height and horizontal position
can be continuously adjusted. Near the mirror
(i.e., mirror 2), put two screws in adjacent table
holes along the beam path, and screw them all
the way in. Put two more screws as far down the
table as possible. Roughly adjust the tilt and (if
needed) positions of both mirrors by hand so that
the beam appears parallel to the table and to the
rows of screw holes. Now place the base plate
used to support the iris with its edge fat against
the closest set of screws and adjust the position
of the iris so the beam goes through the iris. DO
NOT ADJUST THE MIRROR! (This is “step 2”
in Figure 10.18. Now move the iris to the farther
set of screws and use the fne angle adjustments
on the mirror to send the beam through the iris.
DO NOT ADJUST THE IRIS! (This is “step 3.”)
Now bring the iris back to the frst set of
screws and repeat this process a few times until
the beam goes through the iris at both positions
pair of screws
screwed into
holes on
optical table
FIGURE 10.18 Method for aligning beam with grid of
holes. Image courtesy of Prof. Enrique Galvez, who devel­
oped this method.
base for iris
touching both screws
Step 3: Far position:
adjust mirror re˜ection
Step 2: Near position:
adjust iris x and y
iris mounted on base
mirror
Laser beam
without any adjustment. If the beam hits the edge of the mirror as a result of this alignment, you must
adjust the placement of this mirror and redo the alignment.
Your beam should now be parallel to the screw holes (horizontally) and to the breadboard surface
(vertically). That’s an important accomplishment!
10A.3 Mach-Zender Interferometer and the Quantum Eraser*
Your goal is to create and align the version of a Mach-Zender interferometer shown in Figure 10.19.
This requires very precise alignment of all the components, so if you can get it to work you should be
proud of yourself! We assume this is the frst time you’ve created such a precise setup, so we’ll walk you
through it. The components you are adding should all be on short pedestals, held in place with “forks.”
Insert Polarizing Beam Splitter Cube and Align the Beam with the Table
The polarizing beam splitter (PBS) splits the beam with one of the exit beams polarized horizontally and
the other vertically. If the incident beam is polarized at 45°, then each of the exit beams has equal power.
Ensure the cube is placed in its holder so that light is not blocked by the holder and so the incident beam
hits the cube on the side with the black dot on it. The refected beam should roughly be parallel to a row
of holes. Using the iris and the same procedure as above, align the beam refected out of the cube with
the grid of holes.
Q1: Why isn’t the alignment of the transmitted beam affected by your adjustments to the PBS
cube’s tilt as you align the refected beam?
Insert Mirrors 3 and 4, and Align the Beams
Place one mirror in the path of the beam that is refected from the PBS cube and a second mirror in the
path of the beam that is transmitted. Tilt them so that they are both refecting the laser toward the spot
* This is adapted from a lab by Prof. Mark Beck of Reed College.

245
Basic Optics Techniques and Hardware
FIGURE 10.19 Mach-Zender interferometer for quantum eraser experiment.
where you will place the non-polarizing beam splitter (NPBS) cube. Using the iris technique, align the
beams that are refected from these mirrors with the grid of holes. Erect a screen in the path of each beam
just off the edge of the optical table. You will use these screens to align the beams from the two paths,
and eventually to observe the interference pattern.
Insert NPBS cube and Align the Beams with the Table
This is the trickiest part of the alignment, since it requires that both beams hit the inside of the cube at the
same place. First, roughly position and secure the cube so that the faces of the cube are perpendicular to
the beams coming from mirrors 3 and 4 and the beams appear to meet in the same place inside the cube.
It doesn’t matter which side the black dot is on, because the setup is symmetrical – beams are coming
from both sides. If you have correctly aligned the beams with the table, you should only need to adjust
the horizontal position of the beams so that they overlap inside the cube by changing the angles of the
mirrors, as they should be at the same vertical level already.
The goal is to have both pairs of beams coming out of the cube overlap so that you only see one spot on
each of the screens. More than likely, you will see two spots on the screen at this stage of the alignment.
This is because the beams that are transmitted through the cube are unaffected by the tilt of the cube, but
the refected beams are. Adjust the fne tilt on the NPBS cube mount until the spots are as close together
on the screens as you can get them. You may fnd that the spots no longer meet at the same point inside
the cube. In this case, the cube must be repositioned slightly and the tilt alignment must be repeated.
After a few iterations, both conditions for alignment (spots meet at the same place inside the cube, and
spots on the screens overlap) should be satisfed.
When the alignment seems good enough, put a diverging lens in the path of either beam after the cube.
On the screen placed after the diverging lens, you should see a large circular spot of laser light, without
any strong interference fringes.
Adding the Final Polarizer
Now, add a polarizer at 45° at the spot labeled “linear polarizer will go here” in Figure 10.19. (Don’t
screw it in place.) On the screen placed after the diverging lens, you should now see a “bull’s eye”

246
Experimental Physics
FIGURE 10.20 Bull’s eye interference pattern.
interference pattern, with alternating bright and dark interference fringes, as shown in Figure 10.20.
(In fact, you will likely only see part of it, as suggested by the small square in the fgure.) This occurs
because of angle-dependent path-length differences between the beam that bounces off mirror 3 and the
beam that bounces off mirror 4, in a manner very similar to the angle-dependent path-length differences
that occur in a two-slit interference experiment. In this case, there is circular symmetry around the laser
beam axis, so instead of getting a pattern of vertical interference lines (as in an experiment with two
vertical slits), you get the “bull’s eye” pattern. If you do not see the pattern or part of it, try making small
adjustments to the NPBS angles. If you still don’t see fringes, ask your instructor for help.
Make small adjustments to the NPBS angles until you’re seeing part of the pattern that is a little off
center, as suggested by the square in Figure 10.20. (This makes it easier to tell whether or not strong
fringes are present.)
Understanding Interference, and the “Quantum Eraser”
Now remove the polarizer you just added. Q2: What do you observe on the screen?
To understand what happened, we have to consider the effect of the polarizing beam splitter cube.
Q3: Using the linear polarizer, determine the polarization of both the transmitted and refected
beam after the PBS cube. Given the results of this exercise, and thinking in the classical picture,
why do we see no interference pattern when the polarizer is removed? Why do we see interference
when the polarizer is present?
Q4: Explain your results using the quantum mechanical picture. Hint: this experiment is very
similar to a two-slit interference experiment, with the beam that bounces off mirror 3 playing the role
of the light emerging from one of the slits, and the beam that bounces off mirror 4 playing the role
of the light that emerges from the other slit. As you know, for the two-slit experiment, if you do any
measurement that allows you to determine which slit the light went through, the interference pattern is
destroyed. So here, if there is even the possibility of doing such a measurement, the interference pattern
will be destroyed.
Q5: Why is this experiment called the quantum eraser? Hint: what is being erased when you add
the polarizer at 45°? Think in terms of whether a measurement would allow you to determine which path
a particular photon had followed.
Q6: Why was it important to use short pedestals when building this setup, rather than posts and
post holders?
