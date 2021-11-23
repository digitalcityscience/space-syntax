[![CI Pipeline](https://github.com/digitalcityscience/space-syntax/actions/workflows/ci-pipeline.yml/badge.svg)](https://github.com/digitalcityscience/space-syntax/actions/workflows/ci-pipeline.yml)

## Space Syntax
For creating depthmap axial and segment analysis on maps.

Based on:
  - [osmnx](https://github.com/gboeing/osmnx) for openstreat map downloading
  - [geopandas](https://geopandas.org) for conversion
  - [depthmapX](https://www.ucl.ac.uk/bartlett/architecture/research/space-syntax/depthmapx) for spatial analysis

Algorithm pseudocode:
1. download map from OSM as an ESRI shapefile
1. convert the ESRI shapefile to DXF
1. transform DXF to a shape file GRAPH
1. convert the shape file into an axial map
    1. performing axial analysis
    1. exporting axial analysis to MIF
    1. transform the MIF to SHAPE
    1. transform the MIF to GeoJSON
1. convert the shape file into a segment map
    1. performing segment analysis
    1. exporting segment analysis to MIF
    1. transform the MIF to SHAPE
    1. transform the MIF to GeoJSON
