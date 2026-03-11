# imports
import os
import csv
import sys
import subprocess
import tempfile
import shutil

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
# checkpoints directory
checkpoints_dir = os.path.abspath(os.path.join(root, "..", "..", "checkpoints"))

code_dir = os.path.abspath(os.path.join(root, "..", "..", "framework/code"))
process_data_path= os.path.join(code_dir, "prepare_input_file.py")

tmp_dir = tempfile.mkdtemp()
src_file_tokenise_input = os.path.join(tmp_dir, "processed_data.txt")
predictions_folder = os.path.join(tmp_dir, "predictions")
os.makedirs(predictions_folder)
STORE = predictions_folder + "/"  # directory for output files

#list the models.pt from checkpoints
with os.scandir(checkpoints_dir) as models_pretrained:
    models_pretrained=[ model_pretrained.name for model_pretrained in models_pretrained if model_pretrained.name.endswith('.pt')]

translate_file= os.path.join(code_dir, "translate.py")

process_predictions_file= os.path.join(code_dir, "process_predictions.py")

# model to be run
def my_model():
    # name_env_model= "eos935d"
    # python_path_env= getPythonPath_env(name_env_model)

    cmd1 = '{} {} -input_file {} -output_file {}'.format(sys.executable, process_data_path, input_file, src_file_tokenise_input)
    subprocess.Popen(cmd1, shell=True).wait()

    BEAM=5  # beam size
    MIN=5   # minimum length of predicted sequence (in SMILES)
    MAX=120  # maximum length of predicted sequences (in SMILES)
    for model_id in [1,2,3,4,5,6]:
        MODEL_FILE= '{}/model_{}.pt'.format(checkpoints_dir,model_id)
        OUT_NAME='model{}_beam{}.txt'.format(model_id,BEAM)
        OUT_FILE='{}{}'.format(STORE,OUT_NAME)

        cmd2 = '{} {} -model {} -src {} -output {} -n_best {} -beam_size {}  -verbose -min_length {} -max_length {}'.format(sys.executable, translate_file,MODEL_FILE,src_file_tokenise_input,OUT_FILE,BEAM,BEAM,MIN,MAX)
        subprocess.Popen(cmd2, shell=True).wait()

    cmd3 = '{} {} -input_file {} -output_file {} -predictions_dir {}'.format(sys.executable, process_predictions_file, input_file, output_file, predictions_folder)
    subprocess.Popen(cmd3, shell=True).wait()

my_model()
shutil.rmtree(tmp_dir)