import random
import glob

def get_random_order():
    ordered_scenes = glob.glob('dialogue/*.txt')
    random.shuffle(ordered_scenes)

    for folder in glob.glob('dialogue/ordered/*'):
        f = sorted(glob.glob(folder + '/*.txt'))
        start_i, end_i = 0, len(ordered_scenes) - 4

        for filename in f:
            placement_i = random.randint(start_i, end_i)
            ordered_scenes.insert(placement_i, filename)

            start_i, end_i = placement_i + 1, end_i+2

    ordered_scenes.insert(0, 'dialogue/first/first_customer.txt')

    return ordered_scenes
        
if __name__ == "__main__":
    get_random_order()