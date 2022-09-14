import freesasa
from biopandas.pdb import PandasPdb

name = input("Name of the pdb file?\n")

ppdb = PandasPdb()
ppdb.read_pdb(f'{name}')
ATOM = ppdb.df['ATOM']
resname = ATOM['residue_name']
atom = ATOM['atom_name']
resi_number = ATOM['residue_number']
length = len(ATOM.index)
print("Nt,Nt_num,SASA value")
for i in range(length):
    if atom[i] == 'N1':
        if (resname[i] == 'A'):
            structure = freesasa.Structure(f'{name}')
            result = freesasa.calc(structure, freesasa.Parameters({'algorithm' : freesasa.LeeRichards, 'probe-radius' : 2.0}))
            selection = freesasa.selectArea((f'n1,(name N1) and (resn A) and (resi {resi_number[i]}) ',f'n3, (name N3) and (resn C) and (resi {resi_number[i]})'), structure, result)
            sel1 = selection['n1']

            print(resname[i],resi_number[i],sel1)

        elif(resname[i] == 'C'):
            structure = freesasa.Structure(f'{name}')
            result = freesasa.calc(structure,
                                   freesasa.Parameters({'algorithm': freesasa.LeeRichards, 'probe-radius': 2.0}))
            selection = freesasa.selectArea((f'n1,(name N1) and (resn A) and (resi {resi_number[i]}) ',
                                             f'n3, (name N3) and (resn C) and (resi {resi_number[i]})'), structure,
                                            result)
            sel2 = selection['n3']

            print(resname[i],resi_number[i],sel2)
        else:
            print(resname[i],resi_number[i],0)
