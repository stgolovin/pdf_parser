from pdfrw import PdfReader
import pdfplumber
import pdfreader
import psycopg2
import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker
from models import create_table, Years
from pdfreader import PDFDocument, SimplePDFViewer
from itertools import islice
from PIL import Image
from pprint import pprint


pdf_path = './test.pdf'
LOGIN = 'postgres'
PASSWORD = 'MPuzo1920'
DB_NAME = 'orm_test'

DSN = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{DB_NAME}'
engine = sqla.create_engine(DSN)
create_table(engine)
Session = sessionmaker(bind=engine)
session = Session()

def pdfreader():
    fd = open('./test.pdf', "rb")
    viewer = SimplePDFViewer(fd)
    viewer.navigate(1)
    viewer.render()
    markdown = viewer.canvas.text_content
    # print(markdown)
    engine_num = markdown.split('(Год изготовления)', 1)[1].split('(', 1)[1].split(')', 1)[0]
    print(engine_num)


def db():
    session.add(Years(id=1, text='2018'))
    session.commit()

subq = session.query(Years).subquery()
print(Years)

session.close()

def pdfrw_test():
    x = PdfReader(pdf_path)
    print('Size of the file is {}'.format(len(x.pages)))


def pdfplumber_test():
    with pdfplumber .open(pdf_path) as pdf:
        page = pdf.pages[2]
        tables = page.extract_tables()
        text = page.extract_text()
        print(text)

def main():
    # pdfrw_test()
    # pdfplumber_test()
    # pdfreader()
    db()


if __name__ == "__main__":
    main()
