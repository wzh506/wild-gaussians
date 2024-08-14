from read_and_write_model import read_images_text
import csv

if __name__ == "__main__":
    colmap_text_path = "/gpfs/dataset/imw_yanxu/qinghuayuan_240/undistorted_colmap/dense/colmap_text/images.txt"
    images = read_images_text(colmap_text_path)
    #// how to write a .tsv file, it has four columns, first is filename, second is image_id, third is split, fourth is dataset
    print(images)
    split = "train"
    dataset = "brandenburg"

    # Path to the .tsv file
    file_path = "output.tsv"

    # Writing to the .tsv file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["filename", "image_id", "split", "dataset"], delimiter='\t')
        
        # Write the header
        writer.writeheader()
        
        # Write the rows

        
        for key, value in images.items():
            
        #for image in images:
            row = {
                "filename": value[4],
                "image_id": value[3],
                "split": split,
                "dataset": dataset
            }
            writer.writerow(row)    
    