import subprocess

print("Transform dxf to shape file")
dxfFile = "downloads/finland_municipalities.dxf"
graphFile = "downloads/finland_municipalities.graph"
transformer = subprocess.run(
    [
        "depthmapXcli",
        "-m",
        "IMPORT",
        "-it",
        "drawing",
        "-f",
        dxfFile,
        "-o",
        graphFile,
    ],
    universal_newlines=True,
    capture_output=True,
    check=True,
)

print("stdout:", transformer.stdout)
print("stderr:", transformer.stderr)

import asyncio


async def run(cmd: str, description="Running command"):
    print(description, cmd)
    proc = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await proc.communicate()

    print(f"[{cmd!r} exited with {proc.returncode}]")
    if stdout:
        print(f"[stdout]\n{stdout.decode()}")
    if stderr:
        print(f"[stderr]\n{stderr.decode()}")


async def axial():
    axial_map_file = "downloads/axial-map.graph"
    await run(
        f"depthmapXcli -m MAPCONVERT -f {graphFile} -o {axial_map_file} -p -co axial -con axialMap",
        "Converting to axial map",
    )
    axial_analysis_file = "downloads/axial-analysis.graph"
    await run(
        f"depthmapXcli -m AXIAL -f {axial_map_file} -o {axial_analysis_file} -p -xa 3,n",
        "Performing axial analysis",
    )
    axial_shapefile_mif = "downloads/shapegraph-map.axial.mif"
    await run(
        f"depthmapXcli -m EXPORT -f {axial_analysis_file} -o {axial_shapefile_mif} -em shapegraph-map-mif",
        "Exporting axial analysis to mif",
    )


async def segment():
    print("This operation may take longer than 25 minutes to complete!!!")
    segment_map_file = "downloads/segment-map.graph"
    await run(
        f"depthmapXcli -m MAPCONVERT -f {graphFile} -o {segment_map_file} -p -co segment -con segmentMap",
        "Converting to segment map",
    )
    segment_analysis_file = "downloads/segment-analysis.graph"
    await run(
        f"depthmapXcli -m SEGMENT -f {segment_map_file} -o {segment_analysis_file} -p  -st metric -sr 200,400,1600",
        "Performing segment analysis",
    )
    segment_shapefile_mif = "downloads/shapegraph-map.segment.mif"
    await run(
        f"depthmapXcli -m EXPORT -f {segment_analysis_file} -o {segment_shapefile_mif} -em shapegraph-map-mif",
        "Exporting segment analysis to mif",
    )


async def main():
    await asyncio.gather(axial(), segment())


asyncio.run(main())
