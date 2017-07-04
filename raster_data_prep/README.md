# Raster data preperation

This folder contains raster data preparation utilities function. Before doing anything, please unzip the `pearl_data.zip` file.

## Requirements

This utility function requires `gdal` and `R` with library `raster`. The reason why `R` is needed is because the raw data are `R rasters`.

To use these data, I need to use `R` to convert the data to `GeoTIFF` first, and then use `gdal` for further preparation.

## To Do

-[x] check out how colors work :
	To change the colors with rgb values, change the color list into rgb values with space inbetween the triplets (ex. '230 34 145')
 
-[] find different colors to use for the maps


## 1 Installation

### 1.1 OS X

To install `gdal` for OSX:

```bash
  brew install gdal
```

Once it is done, install `gdal` python package using conda (recommended and easiest):

```bash
  conda install gdal
```

Then, install `rpy2` for `R` connection in `python`:

```bash
  pip install rpy2
```

To install `R`, go to this [link](https://www.r-project.org/). When `R` is installed, in R, type:

```R
  install.package('raster')
  install.package('rgdal')
```

### 1.2 Ubuntu (*or other OS using apt-get*)

Do the following in **a Python 2 environment on a Ubuntu machine!**

This is a dev installation for Ubuntu:

```bash

  sudo apt-get install gdal python-gdal

```

Then, install `rpy2` for `R` connection in `python`:

```bash
  pip install rpy2
```

To install `R`, go to this [link](https://www.r-project.org/). When `R` is installed, in R, type:

```R
  install.package('raster')
  install.package('rgdal')
```

## 2 Create tile maps

When you have all the dependencies installed, use:

```bash
  python raster_translation.py
```

Once the script is finished, the tile maps are in `/pearl_data/tile_maps/`, you can put all the tile maps to the `../static/data/`.

# Please Note!

Although this script runs in parallel, the running time is still every long because of the tile map creation. The `gdal` package might cause various problems.
