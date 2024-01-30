import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


st.set_page_config(page_title='R Cheat Sheet', layout='wide', page_icon="R_logo.svg.png", initial_sidebar_state='auto')

st.image("R_logo.svg.png", width=200)

st.sidebar.image("R_logo.svg.png", width=50)
st.sidebar.title("R Cheat Sheet")
st.sidebar.caption("by asahcvulas made in streamlit")

with st.sidebar.expander("GETTING HELP"):
    st.subheader("Accesing the help files")
    st.code("?mean")
    st.caption("Get help of a particular function")
    st.code("help.search(‘weighted mean’)")
    st.caption("Search for help on a particular topic")
    st.code("help(package = ‘dplyr’)")
    st.caption("Get help on a particular package")

    st.subheader("More About an Object")
    st.code("str(iris)")
    st.caption("Get a summary of an object’s structure. ")
    st.code("class(iris)")
    st.caption("Find the class an object belongs to.")

with st.sidebar.expander("USING LIBRARIES"):
    st.code("install.packages(‘dplyr’)")
    st.caption("Download and install a package from CRAN")
    st.code("library(dplyr)")
    st.caption("Load the package into the session, making all its functions available to use.")
    st.code("dplyr::select")
    st.caption("Use a particular function from a package.")
    st.code("data(iris)")
    st.caption("Load a built-in dataset into the environment. ")

with st.sidebar.expander("WORKING DIRECTORY"):
    st.code("getwd()")
    st.caption("Get the current working directory")
    st.code("setwd(‘/Users/username/Documents’)")
    st.caption("Set the current working directory")
    st.markdown("`Use projects in RStudio to set the working directory to the folder you are working in.`")


    

st.title("R Cheat Sheet")
cols = st.columns(2)

def st_code_block(caption=None, code=None):
    st.caption(f"{caption}")
    st.code(code, language="r",line_numbers=True)


def vectors():
    st.header("Vectors")
    creating_vectors, vectors_functions, selecting_vector_elements = \
    st.tabs(["Creating Vectors", "Vectors Functions", "Selecting Vector Elements"])

    with creating_vectors:
        data = {
            'syntax' : ['c(2, 4, 6)', '2:6', 'seq(2, 3, by=0.5)',  'rep(1:2, times=3)', 'rep(1:2, each=3)'],
            'output' : ['2 4 6', '2 3 4 5 6', '2.0 2.5 3.0 3.5', '1 2 1 2 1 2', '1 1 1 2 2 2'],
            'Description' : ['Create a vector of numbers.', 'Create a vector of numbers from 2 to 6.', 'Create a vector of numbers from 2 to 3 in increments of 0.5.', 'Repeat the vector 1:2 three times.', 'Repeat each element of the vector 1:2 three times.']
        }
        df = pd.DataFrame(data)
        st.table(df)

    with vectors_functions:
        st_code_block("Return x sorted.", "sort(x)")
        st_code_block("Return x reversed.", "rev(x)")
        st_code_block("See counts of values.", "table(x)")
        st_code_block("Return unique values.", "unique(x)")
    
    with selecting_vector_elements:
        st.subheader("by position")
        position = {
            'syntax' : ['x[1]', 'x[-4]', 'x[2:4]', 'x[-(2:4)] ', 'x[c(1, 5)]'],
            'Description' : ['The fourth element.', 'All but the fourth.', 'Elements two to four', 'All elements except two to four', 'Elements one and five.']
        }

        df_position = pd.DataFrame(position)
        st.table(df_position)

        st.subheader("by value")
        value = {
            'syntax' : ['x[x == 10]', 'x[x < 0]', 'x[x %in% c(1, 2, 5)]'],
            'Description' : ['Elements which are equal to 10', 'All elements less than zero.', 'Elements in the set 1, 2, 5.']
        }

        df_value = pd.DataFrame(value)
        st.table(df_value)


def programming():
    st.subheader("Programming")
    for_loop, while_loop, if_statement, functions, condition = \
    st.tabs(["For Loop", "While Loop", "If Statement", "Functions", "Condition"])

    with for_loop:
        st_code_block("For loop", 
                      """
                for (variable in sequence){
                    Do something 
                }
                  """)
        st_code_block("example",
                      """
                    for (i in 1:4){
                        j <- i + 10 
                        print(j) 
                    }
                     """)
    with while_loop:
        st_code_block("While loop", 
                      """
                    while (condition){
                        Do something 
                    }
                  """)
        st_code_block("example",
                      """
                    while (i < 5){
                        print(i) 
                        i <- i + 1 
                    }
                     """)
    with if_statement:
        st_code_block("If statement", 
                      """
                    if (condition){ 
                        Do something 
                    } else { 
                        Do something different 
                    }

                  """)
        st_code_block("example",
                      """
                    if (i > 3){ 
                        print(‘Yes’) 
                    } else { 
                        print(‘No’) 
                    }
                     """)
    with functions:
        st_code_block("Functions", 
                      """
                    function_name <- function(arg1, arg2){
                        Do something 
                        return(something) 
                    }
                  """)
        st_code_block("example",
                      """
                    sum <- function(x, y){
                        result <- x + y 
                        return(result) 
                    }
                     """)
    with condition:
        condition = {
            'syntax' : ['a == b', 'a != b', 'a > b', 'a < b', 'a >= b', 'a <= b', 'is.na(a)', 'is.null(a)'],
            'Description' : ['a equals b', 'a does not equal b', 'a is greater than b', 'a is less than b', 'a is greater than or equal to b', 'a is less than or equal to b', 'a is NA', 'a is NULL']
        }

        df_condition = pd.DataFrame(condition)
        st.table(df_condition)


def r_w_data():
    st.header("Reading and Writing Data")
    r_w = {
        'reading' : ['df <- read.table(‘file.txt’)', 'df <- read.csv(‘file.csv’)', 'load(‘file.RData’)'],
        'writing' : ['write.table(df, ‘file.txt’)', 'write.csv(df, ‘file.csv’)', 'save(df, file=‘file.RData’)'],
        'Description' : ['Read and Write a text file.', 'Read and Write a CSV file.', 'Read and Write a binary file.']
    }

    df_r_w = pd.DataFrame(r_w)
    st.table(df_r_w)

def operator():
    st.subheader("Operators")
    arithmatic, logical, assignment, other = \
    st.tabs(["Arithmatic", "Logical", "Assignment", "Other"])

    with arithmatic:
        
        arithmatic = {
            'Operator' : ['x + y', 'x - y', 'x * y', 'x / y', 'x ^ y', 'x %% y', 'x %/% y'],
            'Description' : ['Addition', 'Subtraction', 'Multiplication', 'Division', 'Exponentiation', 'Modulo', 'Integer division']
        }
        df_arithmatic = pd.DataFrame(arithmatic)
        st.table(df_arithmatic)
    
    with logical:
        
        logical = {
            'Operator' : ['!', '&', '&&', '|', '||'],
            'Description' : ['Logical NOT', 'Element-wise Logical AND', 'Logical AND', 'Element-wise Logical OR', 'Logical OR']
        }
        df_logical = pd.DataFrame(logical)
        st.table(df_logical)
    with assignment:
        
        st_code_block("Assigns a variable to x",
                      """
                      x <- 5
                      x = 5
                      """)
    with other:
        
        other = {
            'Operator' : [' %in% ', '$', '%>%'],
            'Description' : ['Identifies whether an element belongs to a vector', 'Allows you to access objects stored within an object', 'Part of magrittr package, it’s used to pass objects to functions']
        }
        df_other = pd.DataFrame(other)
        st.table(df_other)

def math():
    st.subheader("Math Functions")
    math = {
        'Function' : ['log(x)', 'exp(x)', 'max(x)', 'min(x)', 'round(x, n) ', 'signif(x, n) ', 'cor(x, y)', 'sum(x)', 'rank(x) '],
        'Description' : ['Natural log', 'Exponentia', 'Largest element', 'Smallest element', 'Round to n decimal places', 'Round to n significant figures', 'Correlation.', 'Sum', 'Rank of elements']
    }
    df_math = pd.DataFrame(math)
    st.table(df_math)

def stat():
    st.subheader("📈Statistical Functions")
    stat = {
        'Function' : ['mean(x)', 'median(x)', 'sd(x)', 'var(x)', 'quantile(x, p)', 'scale(x)','lm(x ~ y, data=df)', 'glm(x ~ y, data=df)', 'summary', 't.test(x, y)', 'pairwise.t.test', 'prop.test', 'aov' ],
        'Description' : ['Mean', 'Median', 'Standard deviation', 'Variance', 'Quantiles',  'Standardize', 'Linear model', 'Generalised linear model', 'Get more detailed information out a model', 'Preform a t-test for difference between means.', 'Preform a t-test for paired data', 'Test for a difference between proportions', 'Analysis of variance']
    }
    df_stat = pd.DataFrame(stat)
    st.table(df_stat)

def data_types():
    st.subheader("Data Types")
    data_types = {
        'Type' : ['as.logical', 'as.numeric', 'as.character', 'as.factor'],
        'output' : ['TRUE, FALSE', '1, 2, 3', '‘a’, ‘b’, ‘c’', '‘a’, ‘b’, ‘c’'],
        'Description' : ['Convert to logical', 'Convert to numeric', 'Convert to character', 'Convert to factor']
    }
    df_data_types = pd.DataFrame(data_types)
    st.table(df_data_types)

def data_frames():
    st.subheader("Data Frames")
    st_code_block("Create a data frame","""

        df <- data.frame(x = 1:3, y = c('a', 'b', 'c'))""")
    st.caption("A special case of a list where all elements are the same length")

    st.write("The output")
    st.write(pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']}))
    st.caption("Nb: ignore the left row numbers")
    st_code_block("Understanding a data frame","""
                    view(df) # See the full data frame
                    head(df) # See the first six rows
                    tail(df) # See the last six rows
                    str(df) # See the structure of the data frame
                    summary(df) # See summary statistics
                    nrow(df) # Number of rows
                    ncol(df) # Number of columns
                    dim(df) # Dimensions of the data frame
                    """)

def matrix():
    st.subheader("Matrix")
    st_code_block("Matrixes","""
                m <- matrix(x, nrow = 3, ncol = 3) #Create a matrix from x.
                m[2, ] # Select a row
                m[, 2] # Select a column
                m[2, 2] # Select an element
                t(m) # Transpose
                m %*% n # Matrix multiplication
                solve(m) # Inverse
                  
                  """)

def plot():
    st.subheader("Plot")

    st.subheader("dot plot")
    st_code_block("", "plot(x, y, type = ‘p’)")
    st.caption('output')
    
    x = np.random.randn(100)
    y = np.random.randn(100)
    fig, ax = plt.subplots()
    ax.plot(x, y, 'o', color='blue')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Dot Plot')
    st.pyplot(fig)

    st.divider()

    st.subheader("line plot")
    st_code_block("", "plot(x, y, type = ‘l’)")
    st.caption('output')

    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, linestyle='-', color='blue')  # '-' untuk tipe garis
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_title('Line Plot')
    st.pyplot(fig)

    st.divider()

    st.subheader("bar plot")
    st_code_block("", "barplot(x,y)")
    st.caption('output')

    categories = ['A', 'B', 'C', 'D', 'E']
    values = np.random.randint(1, 10, size=len(categories))
    fig, ax = plt.subplots()
    ax.bar(categories, values, color='skyblue')
    ax.set_xlabel('Categories')
    ax.set_ylabel('Values')
    ax.set_title('Bar Plot')
    st.pyplot(fig)

    st.divider()

    st.subheader("histogram")
    st_code_block("", "hist(x)")
    st.caption('output')

    data = np.random.randn(1000)
    fig, ax = plt.subplots()
    ax.hist(data, bins=30, color='skyblue', alpha=0.7)
    ax.set_xlabel('Data')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram')
    st.pyplot(fig)

def distributions():
    st.subheader("Distributions")
    data = {
    'Distribution': ['Normal', 'Poisson', 'Binomial', 'Uniform'],
    'Random Variates': ['rnorm', 'rpois', 'rbinom', 'runif'],
    'Density Function': ['dnorm', 'dpois', 'dbinom', 'dunif'],
    'Cumulative Distribution': ['pnorm', 'ppois', 'pbinom', 'punif'],
    'Quantile': ['qnorm', 'qpois', 'qbinom', 'qunif']}

    df = pd.DataFrame(data)
    st.table(df)



left_column_defaults = ['Vectors', 'Reading and Writing Data', 'Math Functions', 'Data Types', 'Data Frames', 'Distributions']
right_column_defaults = ['Programming', 'Operators', '📈Statistical Functions', 'Matrix', 'Plot']
all_segments = left_column_defaults + right_column_defaults

def default_layout():
    st.session_state["layout_left_column"] = left_column_defaults
    st.session_state["layout_right_column"] = right_column_defaults

custom_layout = st.sidebar.expander("🧑‍🎨 Customize Layout")

with custom_layout:
    st.button("Default Layout", on_click=default_layout)
    side_left_col, side_right_col = st.columns(2)
    left_col_segments = side_left_col.multiselect("Left Column", 
                          options=all_segments, 
                          default=left_column_defaults,
                          key="layout_left_column")
                          
    right_col_segments = side_right_col.multiselect("Right Column", 
                          options=all_segments, 
                          default=right_column_defaults,
                          key="layout_right_column")

segment_dict= {
    "Vectors": vectors,
    "Programming": programming,
    "Reading and Writing Data": r_w_data,
    "Operators": operator,
    "Math Functions": math,
    "📈Statistical Functions": stat,
    "Data Types": data_types,
    "Data Frames": data_frames,
    "Matrix": matrix,
    "Plot": plot,
    "Distributions": distributions
}

with cols[0]:
    for seg in left_col_segments:
        segment_dict[seg]()
    

with cols[1]:
    for seg in right_col_segments:
        segment_dict[seg]()



                    

st.sidebar.info("""
    Note: This online cheatsheet for R is based on materials from the [Github pages](https://iqss.github.io/dss-workshops/R/Rintro/base-r-cheat-sheet.pdf) and [DataCamp](https://www.datacamp.com/cheat-sheet/getting-started-r). 
    The content and logo of R used in this application are the intellectual property of R Foundation. and are used here with proper attribution. 
    This cheatsheet is not affiliated with or endorsed by R Foundation Please refer to the official R documentation for detailed information and updates.

""")

st.sidebar.info("""
    This cheatsheet are referring to the [snowflake cheatsheet](https://snow-flake-cheat-sheet.streamlit.app/). Thanks to whoever make these cheatsheet, i inspired by them to make this cheatsheet in R languange.


""")


    