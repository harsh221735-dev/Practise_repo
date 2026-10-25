# Practise_repo
concepts lesarned:
1. logging to logg the outputs or error in a file or cmd using a formatter
2. yaml - same as json, "dvc repro" runs the entire "dvc.yaml" file contents as a pipeline and store results in "dvc.lock" with hash code for each file , dependecy, paramters which help to skip the file which are already run and only run files which have been chnaged (this will have different hash code , it conpares hash to know which file to run)
3. dvclive- to store the results and parameters of each ml model or file intsead of manuaaly writing