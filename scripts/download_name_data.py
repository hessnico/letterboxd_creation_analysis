import sys
sys.path.append("../")
import modules.download_name_module as dnd

if __name__ == "__main__":
    to_download = 'name.basics.tsv.gz'
    dnd.start_download(to_download)



