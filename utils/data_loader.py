from glob import glob 
import pandas as pd

def load_subtitles_dataset(dataset_path):
    subtitles_paths = glob(dataset_path+'/*.ass')
    scripts = []
    episode_num = []
    for path in subtitles_paths:
        try:
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                lines = lines[27:]
                lines = [",".join(line.split(',')[9:]) for line in lines]
            lines = [line.replace("\\N", " ") for line in lines]
            script = " ".join(lines)
            episode = int(path.split("\\")[-1].split("_")[0])
            
            scripts.append(script)  
            episode_num.append(episode)
        except Exception as e:
            print(f"Error processing file {path}: {str(e)}")
            continue
    
    df = pd.DataFrame.from_dict({"episode": episode_num, "script": scripts})
    return df