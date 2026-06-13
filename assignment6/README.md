# Convolution performance
main.py for most code


* Components
-- Naive implementation of convolution
-- Better implementations of convolution using cache access concepts
-- Track energy usage
-- Tracker for gCO2 and use that to get real-time energy tracker

* Measure time and energy usage: 
-- Different images
-- Number of channels (greyscale / coloured)
-- Input size
-- Kernel size
-- Stride size
-- Padding off / padding on
-- Number of filters

Questions: 
* Plot performance/energy for optimal params for each, with graphs. Export the data, and discuss the shape of the graphs, and why they are that way.
* Look at the convolution algorithm and discuss how it is more optimised than the naive approach. 
* From the graphs, estimate the optimal hyperparams needed for the best performance and the best energy with turbostat.
* Using the data, weigh the energy usage + accuracy + time values from the five sets of graphs to get the best values for each, and test.
* How much does the images being greyscale/coloured (number of channels) affect the convolution performance?
* Do we get the same result when running the same number of keras? What makes keras different from our implementation? 