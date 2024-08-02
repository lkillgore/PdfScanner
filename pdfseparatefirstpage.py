import PyPDF2
import os, sys, getopt
import fnmatch

def createFirstPagePdf(source_path, dest_path):
    try:
        with open(source_path, 'rb') as pdfFile:
            pdfReader = PyPDF2.PdfReader(pdfFile)

            try:
                # Create a PdfWriter object for the new PDF
                output_pdf = PyPDF2.PdfWriter()

                # Add the first page from the original PDF to the new PDF
                output_pdf.add_page(pdfReader.pages[0])

                # Save the new PDF to a file
                with open(dest_path, "wb") as output_file:
                    output_pdf.write(output_file)
                return True
            except Exception as e:
                print(f"Failed to write PDF '{dest_path}' because '{e}'")
                return False

    except Exception as e:
        print(f"Failed to read PDF '{source_path}' because '{e}'")
        return False

def scan(source_path, dest_path):
    totalScanned = 0
    totalPdfsCreated = 0
    totalPdfsFailed = 0
    for root, dir, files in os.walk(source_path):
        for pdfPath in fnmatch.filter(files, "*.pdf"):
            totalScanned += 1
            fullPath = os.path.join(root, pdfPath)
            dest_pdf = os.path.join(dest_path, os.path.basename(pdfPath)) + '.' + str(totalPdfsCreated) + '.firstpage.pdf'
            if createFirstPagePdf(os.path.join(fullPath), dest_pdf):
                totalPdfsCreated += 1
                print(f"Created PDF {fullPath} {dest_pdf}")
            else:
                totalPdfsFailed += 1
                print(f"Failed to create {dest_pdf}")
    print(f'Summary: Total Files({totalScanned}) Total PDFs created ({totalPdfsCreated}) Total failed to create ({totalPdfsFailed})')

def main(argv):
    source = os.path.curdir
    dest = os.path.curdir
    try:
        opts, args = getopt.getopt(argv,"hs:d:",["source_path=", "destination_path="])
    except getopt.GetoptError:
        print('pdfseparatefirstpage.py -p <path> -l <page length>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('pdfseparatefirstpage.py -p <path> -l <page length>')
            sys.exit()
        elif opt in ("-s", "--source_path"):
            source = arg
        elif opt in ("-d", "--destination_path"):
            dest = arg
    print('Source Folder "', source, '"')
    scan(source, dest)

if __name__ == "__main__":
    main(sys.argv[1:])
