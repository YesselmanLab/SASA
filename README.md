# Solvent Accessible Surfafce Area (SASA)

This code is primarily useful for calculating the solvent accessibility surface area (SASA) of N1 of Adenine (A) and N3 of Cytosine (C) because these are the atoms that will be methylated during chemical mapping with Dimethyl sulfate (DMS). 

Therefore, it will calculate SASA for N1 of A and N3 of C in an RNA. For G and U, the output will be zero.

## How to:
```shell
# to download this repository
git clone https://github.com/YesselmanLab/SASA.git
cd SASA
pip install -r requirements.txt
```
If you dont have pip installed use the link below;
[pip installation](https://pip.pypa.io/en/stable/installation/)

### how to run:
```shell
python SASA.py Example.pdb
# provide the path to the pdb file of interest as an argument
```

## Example:
```shell
python SASA.py Example.pdb

# Output
Nt  Nt_num      SASA
 A       3  4.760952
 A       4  0.340195
 A       5 12.659646
 G       6  0.000000
 C      11  2.610542
 G      12  0.000000
 A      13 12.317836
 U      14  0.000000
```

