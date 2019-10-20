# CBZ-Minimizer
A simple python script to shrink iamges inside a cbz file

## Dependencies
zip, unzip, imagemagick

## Usage
```
python CBZ Minimizer.py [file1] [file2] [file...]
```

Script takes files/ full file paths. 
It will extract the images to a tmp dir where the script is located. 
Shrink the images based on the percentage you input when asked.
Then output [filename]_min.cbz 
