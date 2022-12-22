# imports
import os
import csv
#import joblib
import sys
#from rdkit import Chem
#from rdkit.Chem.Descriptors import MolWt
import subprocess

# parse arguments
input_file = sys.argv[1]
#output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# checkpoints directory
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

# read checkpoints (here, simply an integer number: 42)
ckpt = os.path.join(checkpoints_dir, "model_1.pt")

code_dir = os.path.abspath(os.path.join(root, "..", "..", "framework/code"))
process_data_path= os.path.join(code_dir, "prepare_input_file.py")

src_file_tokenise_input= os.path.join(code_dir, "processed_data.txt")

#list the models.pt from checkpoints
with os.scandir(checkpoints_dir) as models_pretrained:
    models_pretrained=[ model_pretrained.name for model_pretrained in models_pretrained if model_pretrained.name.endswith('.pt')]
    print (models_pretrained)
predictions_folder= os.path.join(code_dir, "predictions/")
STORE=predictions_folder  # directory for output files 

translate_file= os.path.join(code_dir, "translate.py")

# model to be run
def my_model():

    cmd1 = 'python {} -input_file {}'.format(process_data_path,input_file)
    subprocess.Popen(cmd1, shell=True).wait()

    BEAM=5  # beam size
    MIN=5   # minimum length of predicted sequence (in SMILES)
    MAX=120  # maximum length of predicted sequences (in SMILES)
#recorrer el directorio
    for model_id in {1,2,3,4,5,6}:
        MODEL_FILE= '{}/model_{}.pt'.format(checkpoints_dir,model_id)
        OUT_NAME='model{}_beam{}.txt'.format(model_id,BEAM)
        OUT_FILE='{}{}'.format(STORE,OUT_NAME)

        cmd2 = 'python {} -model {} -src {} -output {} -n_best {} -beam_size {}  -verbose -min_length {} -max_length {}'.format (translate_file,MODEL_FILE,src_file_tokenise_input,OUT_FILE,BEAM,BEAM,MIN,MAX)
        subprocess.Popen(cmd2, shell=True).wait()

    
# read SMILES from .csv file, assuming one column with header
'''with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader) # skip header
    smiles_list = [r[0] for r in reader]
'''
# run model
#outputs = my_model(smiles_list, ckpt)
my_model()

# write output in a .csv file
'''
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["value"]) # header
    for o in outputs:
        writer.writerow([o])
'''