#!/bin/bash
echo "Transform dxf to shape file"
depthmapXcli -m IMPORT -it drawing -f downloads/finland_municipalities.dxf -o test.graph

echo "Converting to axial map"
depthmapXcli -m MAPCONVERT -f test.graph -o axial-map.graph -p -co axial -con axialMap

#echo "Converting to segment map"
#depthmapXcli -m MAPCONVERT -f test.graph -o segment-map.graph -p -co segment -con segmentMap

echo "Perform axial analysis"
depthmapXcli -m AXIAL -f axial-map.graph -o axial-analysis.graph -p -xa 3,n

#echo "Perform segment analysis"
#depthmapXcli -m SEGMENT -f segment-map.graph -o segment-analysis.graph -p  -st metric -sr 200,400,1600

echo "Exporting axial analysis to mif"
depthmapXcli -m EXPORT -f axial-analysis.graph -o axial.mif -em shapegraph-map-mif

echo "Exporting segment analysis to mif"
depthmapXcli -m EXPORT -f segment-analysis.graph -o segment.mif -em shapegraph-map-mif