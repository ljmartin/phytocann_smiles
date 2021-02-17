import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from IPython.display import SVG

df = pd.read_csv('./phytocannabinoids.tsv', sep='\t')
smiles = list(df['smiles'])
names = list(df['name'])
l = 30
#names = [n if len(n)<l else n[:l-3]+'...' for n in names]

mols = [Chem.MolFromSmiles(i) for i in smiles]

shortsvg = Draw.MolsToGridImage(mols, molsPerRow=16, legends=names, useSVG=True)
longsvg = Draw.MolsToGridImage(mols, molsPerRow=8, legends=names, useSVG=True)

f = open('phytos_long.svg', 'w')
f.write(longsvg)
f.close()

f = open('phytos_short.svg', 'w')
f.write(shortsvg)
f.close()

names = [n if len(n)<l else n[:l-3]+'...' for n in names]
f = open('phytos.svg', 'w')
f.write(longsvg)
f.close()

