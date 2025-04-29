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
	predictions_directory = os.path.join(code_dir, "predictions/")
	#figures_directory = 'Figures/'
	models = [1,2,3,4,5,6]
	beam = 5
	max_metabolites = 15  # Set the maximum number of metabolites

	pred_lines = {}

	for num in range(0,len(models)):
		predictions_file = predictions_directory+'model'+str(models[num])+'_'+'beam'+str(beam)+'.txt'
		with open(predictions_file) as f_pred:  
			pred_lines[num] = [''.join(line.strip().split(' ')) for line in f_pred.readlines()]

	models_count = len(pred_lines.keys())
	'''
	if opt.visualise_molecules:
		if not os.path.exists(figures_directory):
			os.makedirs(figures_directory)'''

	molID2smiles = {}
	molID2metabolites = {}
	index = 0
	# read SMILES from .csv file, assuming one column with header
	with open(input_file, "r") as f:
		reader = csv.reader(f)
		next(reader)  # skip header
		smiles_list = [r[0] for r in reader]
	pred_counts = []
	for i in range(0, len(smiles_list)): 
		smiles = smiles_list[i]
		if not check_smile(smiles):
			continue
		smiles = canonicalise_smile(smiles)
		mol_id = f'molecule-{i}'  # Molecule numbering
		molID2smiles[mol_id] = smiles  # Store SMILES for the molecule
		predictions = set()
		for j in range(index, index + beam):
			for num in range(0, models_count):
				predictions.add(pred_lines[num][j])
		index = index + beam
		processed, invalid, invalid_count = process_predictions(predictions,smiles,0.25,0.25,False,True)
		pred_counts.append(len(processed))
		molID2metabolites[mol_id] = processed
		# drug = Chem.MolFromSmiles(smiles)
		# preds = [Chem.MolFromSmiles(pred_smiles) for pred_smiles in processed] 

# Convert the results to separate columns for each metabolite
	columns =[f'metabolite_{str(i).zfill(2)}' for i in range(max_metabolites)]
	data = []
	for mol_id in molID2metabolites.keys():
		metabolites = list(molID2metabolites[mol_id])  # Convert set to a listid]
		row = []
		for i in range(max_metabolites):
			if i < len(metabolites):
				row.append(metabolites[i])
			else:
				row.append("")  # Fill empty cells if there are fewer than max_metabolites predictions
		data.append(row)
	
	with open(output_file, 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(columns)
		for row in data:
			writer.writerow(row) 

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-input_file', type=str,help='Input File')
	parser.add_argument('-output_file', type=str, default='predicted_metabolites.csv',help='Processed Predictions File')
	parser.add_argument('-predictions_dir', type=str, default='predictions/',help='Predictions Directory')
	parser.add_argument('-beam_size', type=int, default=5,help='Beam Size')
	parser.add_argument('-visualise_molecules', type=bool, default=False,help='Visualise predicted metabolites')
	opt = parser.parse_args()
	main(opt)
