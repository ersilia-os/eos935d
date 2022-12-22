import argparse
from utils import *
import os

##  it prepares the molecules for translation: it canonicalizes SMILES and then tokenizes them. The data are stored in a txt file
## -input_file: the input molecules in a csv ot txt file
## -output_file: the filename where the tokenised data will be saved 

def main(opt):
	input_file = opt.input_file
	output_file = opt.output_file
	count_invalid = 0
	outfile = open(output_file,'w')
	lines = open(input_file).read().split('\n')
	for i in range(0,len(lines)-1):
		if i!=0:
			mol_id, smiles, can_smile= lines[i].split(',')
			if not check_smile(smiles):
				print('invalid SMILES: ', smiles)
				count_invalid = count_invalid + 1
				continue
			smiles = canonicalise_smile(smiles)
			smiles_tok = smi_tokenizer(smiles)
			if i<len(lines)-2:
				outfile.write(smiles_tok + '\n')
			else:
				outfile.write(smiles_tok)
		
	outfile.close() 
	if count_invalid>0:
		print(count_invalid, 'invalid SMILES removed.')


root = os.path.dirname(os.path.abspath(__file__))
code_dir = os.path.abspath(os.path.join(root, "..", "..", "framework/code"))
test_molecules_source= os.path.join(code_dir, "processed_data.txt")


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-input_file', type=str,
                       help='Input File')
	parser.add_argument('-output_file', type=str, default=test_molecules_source,
                       help='Output File')
	opt = parser.parse_args()
	main(opt)