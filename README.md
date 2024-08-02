# PdfScanner

Scans all the PDFs in a path to find any with more pages than expected.

```
pip install virtualenv
python -m venv env
.\env\Scripts\Activate
pip install -r requirements.txt
```

PDF Scanner
```
python -m pdfscan -p ../../Applications
Summary: Total Files(1413) Total With More Pages(8)
    ../../Applications\Folder\Processed\Applications.pdf
    ../../Applications\Folder\Processed\Applications SIGNED - 2 of 2.pdf
```

PDF FirstPage Extractor
```
python -m pdfseparatefirstpage -s .\TestSource\ -d .\TestDestination\
Summary: Total Files(1413) Total With More Pages(8)
    ../../Applications\Folder\Processed\Applications.pdf
    ../../Applications\Folder\Processed\Applications SIGNED - 2 of 2.pdf
```