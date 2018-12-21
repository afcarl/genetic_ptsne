# Overall driver for rounds of genetic experimentation on ptsne network


pass

# imports
import tools
from pathlib import Path
import os
import genetic_helpers as gh

# run the breeding for GENERATIONS with GENSIZE with TESTNAME in DIRNAME
def run_test(num_generations , gensize , testname , target_dir_name, test_data):
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

    # get our first batch of dna
    child_dna = gh.breed_generation(gensize)

    # for reasons of directory nomenclacture, we use 1 as our base index
    for generation in [i+1 for i in range(num_generations)]:
        generation_name = 'generation_' + str(generation)
        # create a directory for this generation
        gen_dir = test_dir / generation_name
        os.mkdir(str(gen_dir))
        # same thing with children
        for child_num, dna in [(i+1,j) for (i,j) in enumerate(child_dna)]:
            child_name = "child_" + str(child_num)
            # make a folder for the child
            child_dir = gen_dir / child_name
            os.mkdir(str(child_dir))
            train_child(child_dir , dna , test_data)

def train_child(child_dir_path , dna, test_data):
    # translate our dna
    # create a network of this name with our stats
    # train it on test_data
    # write out our loss history
    # save our model
    # write our dna
    tools.write_dna(child_dir_path , dna)



if __name__ == '__main__':
    run_test(1,1,'DELETE','DUMMY' , "")
