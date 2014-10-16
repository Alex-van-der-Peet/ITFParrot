itf_parrot
==========

itf_parrot takes anything that comes in on /itf_listen and republishes it on /itf_talk. Intended for testing purposes.

Prerequisites
-------------

Works with ROS Hydro, shouldn't need anything else by itself for manual publishing / listening. To have it work you'll need the itf_talk and itf_listen projects, which state their own prerequisites in their own README files.

Usage
-----
Clone into your catkin workspace, to run:

rosrun itf_parrot itf_parrot.py

Notes
-----
None.
