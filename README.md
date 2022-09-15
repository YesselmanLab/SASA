# Solvent Accessible Surfafce Area (SASA)

A python code to calculate SASA for each A and C in an RNA. For G and U, the output will be zero. 

## How to:
```shell
# to download this repository
git clone https://github.com/YesselmanLab/SASA.git
```

### how to run:
```shell
python SASA.py Example.pdb
# provide the path to the pdb file of interest as an argument
```

## Example:
```shell
python SASA.py Example.pdb

# Output
Nt,Nt_num,SASA value
A 3 4.760952386380994
A 4 0.3401953785016046
A 5 12.659646235528148
G 6 0
C 11 2.61054168384766
G 12 0
A 13 12.317836337061284
U 14 0
```

