import sys, os

res = input("Resize Percentage: ")
for x in sys.argv[1:]:
	os.system("mkdir tmp")
	os.system("unzip \"" + x +"\" -d tmp")
		
	for filename in os.listdir("tmp"):
		os.system("mogrify -verbose -resize "+res+ "% tmp/\"" + filename + "\" ")
		
	os.system("zip -r \"" + x.split(".")[0]+"\"_min.cbz tmp/")
	os.system("rm -rf tmp")