import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

import psycopg2
import sqlalchemy as sqla
from sqlalchemy.orm import sessionmaker

from models import create_table, Years

pdf_path = './test.pdf'
LOGIN = 'postgres'
PASSWORD = 'MPuzo1920'
DB_NAME = 'orm_test'

DSN = f'postgresql://{LOGIN}:{PASSWORD}@localhost:5432/{DB_NAME}'
engine = sqla.create_engine(DSN)
create_table(engine)
Session = sessionmaker(bind=engine)
session = Session()


def read_pdf():
    fd = open('./test.pdf', "rb")
    viewer = SimplePDFViewer(fd)
    viewer.navigate(1)
    viewer.render()
    markdown = viewer.canvas.text_content
    created_at = markdown.split("(Год изготовления)", 1)[1].split('(', 1)[1].split(')', 1)[0]
    color = markdown.split("(Цвет кузова \(кабины, прицепа\))", 1)[1].split('(', 1)[1].split(')', 1)[0]
    print("The year is %s. The color is %s." % (created_at, color))


def db():
    session.add(Years(id=1, text='2018'))
    session.commit()
    subq = session.query(Years)
    print(subq)
    session.close()


def main():
    read_pdf()
    # db()


if __name__ == "__main__":
    main()
