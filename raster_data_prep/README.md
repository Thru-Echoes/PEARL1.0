# Raster data preperation

This folder contains raster data preparation utilities function. Before doing anything, please unzip the `pearl_data.zip` file.

## Requirements

This utility function requires `gdal` and `R` with library `raster`. The reason why `R` is needed is because the raw data are `R rasters`.

To use these data, I need to use `R` to convert the data to `GeoTIFF` first, and then use `gdal` for further preparation.

**Note:** *sample data can be found in the zip files. The code here takes grd data and turns them into tile map data structures for fast web visualization rendering of the distribution maps.*

**Note:** *sample .grd files that can be converted into tile maps can be found in the /grd/ folder (one level up from this README)*

**Note:** *sample tile maps can be found in /static/pearl-tiles/* 


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
  install.packages('raster')
  install.packages('rgdal')
```

### 1.2 Ubuntu (*or other OS using apt-get*)

Do the following in **a Python 2 environment on a Ubuntu machine!**

This is a dev installation for Ubuntu:

```bash

	sudo add-apt-repository ppa:ubuntugis/ppa && sudo apt-get update
	sudo apt-get install gdal-bin

```

To verify installation of gdal:

```bash

	ogrinfo

```

```bash

	sudo apt-get install libgdal1-dev
  sudo apt-get install python-gdal

```

**Note:** you may need to add the **-H** flag (after *sudo*) to set the security policy for the installing package. The **-H (HOME)** flag will set the HOME environment variable to the home dir.

Then, install `rpy2` for `R` connection in `python`:

```bash
  pip install rpy2
```

To install `R`, go to this [link](https://www.r-project.org/).

Start a root R session command line:

```bash
  sudo -i R
```

When `R` is installed, in R, type:

```R
  install.packages('raster')
  install.packages('rgdal')
```

## 2 Create tile maps

When you have all the dependencies installed, use:

```bash
  python raster_translation_18proj.py
```

Once the script is finished, the tile maps are in `/pearl_data/tile_maps/`, you can put all the tile maps to the `../static/data/`.

# Please Note!

Although this script runs in parallel, the running time is still every long because of the tile map creation. The `gdal` package might cause various problems.

## Error Notice
Some of the species folders in the origin has missing .grd or .gri files.
Implemented try and except function to filter out erroneous folders in raster_translation_18proj.py
