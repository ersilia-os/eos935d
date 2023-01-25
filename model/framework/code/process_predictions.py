import argparse
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw
from utils import *
import os
import csv

## it reads the output of the models, un-tokenises the predicted sequences and filters out unlikely metabolites
## -input_file: the csv file that has the input molecules (molecule ID and SMILES representations)
## -output_file: the filename where the processed predictions will be saved. It's a csv file. 
## predictions_directory: the directory where the output of the models from the tranaslate_molecules script is saved
## -beam_size: the beam_size. It can be in [5,10,15,20]
## -visualise_molecules (boolean): it visualises all predicted metabolites if True. They are stored within the predictions directory.



def main(opt):
	input_file = opt.input_file
	output_file = opt.output_file
	root = os.path.dirname(os.path.abspath(__file__))
	code_dir = os.path.abspath(os.path.join(root, "..", "..", "framework/code"))
	predictions_directory = predictions_folder= os.path.join(code_dir, "predictions/")

	models = [1,2,3,4,5,6]
	beam = 5

	pred_lines = {}

	for num in range(0,len(models)):
		predictions_file = predictions_directory+'model'+str(models[num])+'_'+'beam'+str(beam)+'.txt'
		with open(predictions_file) as f_pred:  
			pred_lines[num] = [''.join(line.strip().split(' ')) for line in f_pred.readlines()]

	models_count = len(pred_lines.keys())

	molID2smiles = {}
	molID2metabolites = {}
	index = 0
	drug_lines = open(input_file).read().split('\n')
	pred_counts = []
	for i in range(0,len(drug_lines)-1):
		if i!=0:
			mol_id,smiles,can_smile = drug_lines[i].split(',')
			if not check_smile(smiles):
				continue
			smiles = canonicalise_smile(smiles)
			molID2smiles[mol_id] = smiles
			predictions = set()
			for j in range(index,index+beam):
				for num in range(0,models_count):
					predictions.add(pred_lines[num][j])
			index = index + beam
			processed, invalid, invalid_count = process_predictions(predictions,smiles,0.25,0.25,False,True)
			pred_counts.append(len(processed))
			molID2metabolites[mol_id] = processed
			drug = Chem.MolFromSmiles(smiles)
			preds = [Chem.MolFromSmiles(pred_smiles) for pred_smiles in processed]

	table = ['Molecule ID', 'SMILES', 'Metabolites']
	list_metabolites=[]
	for mol_id in molID2metabolites.keys():
		metabolites_str = ''
		smiles = molID2smiles[mol_id]
		metabolites = molID2metabolites[mol_id]
		for metabolite in metabolites:
			metabolites_str = metabolites_str + metabolite + ' '
		metabolites_str = metabolites_str[:-1]
		entry = [mol_id, smiles, metabolites_str]
		table = np.vstack((table,entry))

		list_metabolites.append(metabolites_str)


	with open(output_file, "w") as f:
		writer = csv.writer(f)
		writer.writerow(["Metabolites"]) # header
		for o in list_metabolites:
			writer.writerow([o])
			
if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-input_file', type=str,help='Input File')
	parser.add_argument('-output_file', type=str, default='predicted_metabolites.csv',help='Processed Predictions File')
	parser.add_argument('-predictions_dir', type=str, default='predictions/',help='Predictions Directory')
	parser.add_argument('-beam_size', type=int, default=5,help='Beam Size')
	parser.add_argument('-visualise_molecules', type=bool, default=False,help='Visualise predicted metabolites')
	opt = parser.parse_args()
	main(opt)