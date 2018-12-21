# Overall driver for rounds of genetic experimentation on ptsne network


pass

# imports
import tools
from pathlib import Path
import os

# run the breeding for GENERATIONS with GENSIZE with TESTNAME in DIRNAME
def run_test(num_generations , gensize , testname , target_dir_name):
    # create the target directory if it doesn't exist
    current_dir = Path('.')
    target_dir = Path('.') / target_dir_name

    if target_dir not in [x for x in current_dir.iterdir() if x.is_dir()]:
        os.mkdir(str(target_dir))

    # create directory in target_dir named for this test, but quit if
    # this directory already exists as we don't want accidental overwrites

    #NOTE we don't care about overwrites now so this is commented out, uncomment when driver is finished
    test_dir = target_dir / testname
    '''
    if test_dir in [x for x in target_dir.iterdir() if x.is_dir()]:
        print("ERROR: a directory of this test name already exists, quitting to avoid potential overwrites...")
        quit()
    else:
        os.mkdir(str(test_dir))
    '''
    if test_dir not in [x for x in target_dir.iterdir() if x.is_dir()]:
        os.mkdir(str(test_dir)) # delete when the above lines are uncommented

    # create a file to sit in our test_dir that describes the sizes of the test,
    # for ease of future reading, this will be called 'test_specs'
    tools.write_test_specs(test_dir, num_generations, gensize)

    # for reasons of directory nomenclacture, we use 1 as our base index
    for generation in [i+1 for i in range(num_generations)]:
        generation_name = 'generation_' + str(generation)
        # create a directory for this generation
        gen_dir = test_dir / generation_name
        os.mkdir(str(gen_dir))
        # same thing with children
        for child in [k+1 for k in range(gensize)]:
            child_name = "child_" + str(child)
            # make a folder for the child
            child_dir = gen_dir / child_name
            os.mkdir(str(child_dir))

def train_child(generation_directory , child_name)

# for each generation, create a subfolder in dirname/testname
    # for each member of a generation create subfolder in DIRNAME/childname
        # in this folder create dummy.model, dummy.losslog dummy.dna
if __name__ == '__main__':
    run_test(1,1,'DELETE','DUMMY')
