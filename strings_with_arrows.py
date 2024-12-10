"""""
**************************************************************
The function string_with_arrows generates a 
visual representation of a section of text by marking a 
specified range (from pos_start to pos_end) with arrows (^). 
This is particularly useful for highlighting errors or 
specific parts of code, such as in compilers or interpreters.
This function visually pinpoints the range of text causing an issue,
making debugging easier. 
eg:
This is a test
        ^^^^

**************************************************************
"""""

def string_with_arrows(text, pos_start, pos_end):
    result = ''
    
    #calculate indices
    idx_start = max(text.rfind('\n', 0, pos_start.idx), 0) #searches for the last occurence of \n within range
    # ensures that idx_start is atleast 0
    idx_end = text.find('\n', idx_start + 1)
    if idx_end < 0: 
        idx_end = len(text)
        
    #Generate each line
    line_count = pos_end.ln - pos_start.ln + 1
    for i in range(line_count):
        #Calculate line columns
        line = text[idx_start:idx_end]
        col_start = pos_start.col if i == 0 else 0
        col_end = pos_end.col if i == line_count - 1 else len(line) -1
        
        #Append to result
        result += line + '\n'
        result += ' ' * col_start + '^' * (col_end - col_start)
        
        #Re-calculate indices
        idx_start = idx_end
        idx_end = text.find('\n', idx_start + 1)
        if idx_end < 0: idx_end = len(text)
        
    return result.replace('\t',')')