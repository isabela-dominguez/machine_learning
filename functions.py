from config import *

#functions 

#prepare data
def prepare_data(path): 
    #read values form pdf 
    pdf_path = path

    #separate data into pages 
    data = tabula.read_pdf(pdf_path, output_format= 'dataframe', pages = 'all', multiple_tables=True) 
    print(data[0].head()) 
    print(data[1].head())
    #print(data.dtype)
        

 

 


