import pandas as pd
from rdkit import Chem
from rdkit.Chem import Draw
from IPython.display import SVG

df = pd.read_csv('./phytocannabinoids.tsv', sep='\t')
smiles = list(df['smiles'])
names = list(df['name'])
l = 20
names = [n if len(n)<l else n[:l-3]+'...' for n in names]

mols = [Chem.MolFromSmiles(i) for i in smiles]

svg = Draw.MolsToGridImage(mols, molsPerRow=8, legends=names, useSVG=True)

f = open('phytos.svg', 'w')
f.write(svg)
f.close()

