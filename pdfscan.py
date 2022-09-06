import PyPDF2
import os, sys, getopt
import fnmatch

def pageCountForPdf(pdfPath):
    try:
        with open(pdfPath, 'rb') as pdfFile:
            pdfReader = PyPDF2.PdfFileReader(pdfFile)
            return pdfReader.numPages if pdfReader.numPages else 0
    except Exception as e:
        print(f"Failed to read PDF '{pdfPath}' because '{e}'")
    return 0

def scan(path, pages):
    totalScanned = 0
    totalWithMorePages = 0
    allPaths = []
    for root, dir, files in os.walk(path):
        for pdfPath in fnmatch.filter(files, "*.pdf"):
            totalScanned += 1
            fullPath = os.path.join(root, pdfPath)
            if pageCountForPdf(os.path.join(fullPath)) > pages:
                totalWithMorePages += 1
                print(f"Found PDF {pdfPath} in folder {dir}")
                allPaths.append(fullPath)
    print(f'Summary: Total Files({totalScanned}) Total With More Than {pages} Pages({totalWithMorePages})')
    for path in allPaths:
        print(f'    {path}')

def main(argv):
    path = 'default'
    pages = 2
    try:
        opts, args = getopt.getopt(argv,"hp:l:",["path=", "length="])
    except getopt.GetoptError:
        print('test.py -p <path> -l <page length>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -p <path> -l <page length>')
            sys.exit()
        elif opt in ("-p", "--path"):
            path = arg
        elif opt in ("-l", "--length"):
            pages = arg
    print('Source Folder "', path, '"')
    scan(path, pages)

if __name__ == "__main__":
    main(sys.argv[1:])
