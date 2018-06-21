def read_text(FILENAME):
    '''
        Read text from a file.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            FILENAME : [string] States the file name along with its path.
            
        returns:
            lines : [list] All lines from the text.
            
        example:
            lines = read_text("./blogs/test.txt")
    '''
    lines = list(open(FILENAME))
    return lines

def extract_info(lines):
    '''
        Extract blog title, date, place and author information.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] All lines from the text.
            
        returns: 
            [info, lines_body]:
                info : [list] Blog title, date, place and author information.
                lines_body : [list] All lines from the text with information extracted.
            
        example:
            [TITLE, DATE, PLACE, AUTHOR, lines_body] = extract_info(lines)
    '''
    TITLE = lines[0][0:-1]
    DATE = lines[2][0:-1]
    PLACE = lines[4][0:-1]
    AUTHOR = lines[6][0:-1]
    lines_body = lines[8:]
    info = [TITLE, DATE, PLACE, AUTHOR]
    return [info, lines_body]

def translate_header(lines):
    '''
        Translate titles to html headers.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] All lines from the text.
            
        returns:
            lines : [list] All lines from the text with headers translated.
            
        example:
            lines_h = translate_header(lines)
    '''
    i = 0
    for line in lines:
        if line[0] == '#':
            if line[1] == ' ':
                lines[i] = '<h2 style="font-family:courier;">' + line[2:-1] + '</h2>'
            elif line[1] == '#':
                if line[2] == ' ':
                    lines[i] = '<h4 style="font-family:courier;">' + line[3:-1] + '</h4>'
                else: raise ValueError("The header symbol should be '# 'or '## '!")
            else: raise ValueError("There should be a space between header symbol and text!")
        i = i + 1
    return lines

def translate_paragraph(lines):
    '''
        Translate paragraphs to html paragraphs.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] All lines from the text.
            
        returns:
            lines : [list] All lines from the text with paragraphs translated.
            
        example:
            lines_p = translate_paragraph(lines)
    '''
    i = 0
    for line in lines:
        if (line[0] != '#') & (line[0] != '$') & (line[0] != '<') & (line[0] != '>') & (line[0] != '\n'):
            lines[i] = '<p>' + line[0:-1] + '</p>'
        i = i + 1
    return lines

def translate_break(lines):
    '''
        Translate empty lines to html breaks.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] All lines from the text.
            
        returns:
            lines : [list] All lines from the text with breaks translated.
            
        example:
            lines_h = translate_break(lines)
    '''
    i = 0
    for line in lines:
        if line[0] == '\n':
            lines[i] = '<br>'
        i = i + 1
    return lines

def translate_quotations(lines):
    '''
        Translate quotations to html quotations.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] All lines from the text.
            
        returns:
            lines : [list] All lines from the text with quotations translated.
            
        example:
            lines_h = translate_quotations(lines)
    '''
    return lines

def translate_image(lines):
    '''
        Translate images filename to html images path.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] All lines from the text.
            
        returns:
            lines : [list] All lines from the text with images translated.
            
        example:
            lines_h = translate_image(lines)
    '''
    i = 0
    for line in lines:
        if (line[0] == '$') & (line[1] == ' '):
            lines[i] = '<img src="../../src/blogs/' + line[2:-1] + '" alt="' + line[2:-1] + '" style="height: 100%; width: 100%; object-fit: contain">'
        i = i + 1
    return lines

def link_html(info, lines, FOLDER):
    '''
        Link each part together to form a completed html text.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            info : [list] Blog title, date, place and author information.
            lines : [list] All lines from the translated text.
            FOLDER : [string] Indicate the blogs folder name.
            
        returns:
            lines_html : [list] Linked html text.
            
        example:
            lines_html = link_html(info, lines)
    '''
    import datetime
    TIME = str(datetime.datetime.now().time())[0:5]
    
    part1 = read_text("part1")
    part2 = read_text("part2")
    part3 = []
    part4 = read_text("part4")
    
    part1[10] = part1[10][0:-1] + FOLDER + ' - ' + info[0] + '</title>\n'
    part2[4] = part2[4][0:-1] + info[0] + '</h1>\n'
    part2[7] = part2[7][0:-1] + info[1] + ' <em>' + info[3] + '</em></h4>\n'
    for line in lines:
        part3.append(line + '\n')
    part4[1] = part4[1][0:-1] + info[2] + ' ' + TIME + ' (UTC+08:00)</p>\n'
    
    lines_html = part1 + part2 + part3 + part4
    
    return lines_html

def save_html(lines, FILENAME):
    '''
        Save text to html document.
        
        Author: Wenjie Chen 
        E-mail: wenjiechen@pku.edu.cn
        
        args:
            lines : [list] Linked html text.
            FILENAME : [string] States the file name along with its path.
            
        returns:
            null
            
        example:
            save_html("./blogs/test.html")
    '''
    import os
    try:
        os.remove(FILENAME)
        print(FILENAME + " exists. Overwriting now...")
    except:
        print(FILENAME + " does not exist. Creating now...")
    for line in lines:
        with open(FILENAME, 'a') as f:
            f.write(line)
    print("Successfully translated text to html blog.")
    return

    def text2html(FILENAME, FOLDER):
        '''
            Tanslate text to html blog.
            
            Author: Wenjie Chen 
            E-mail: wenjiechen@pku.edu.cn
            
            args:
                FILENAME : [string] States the file name along with its path.
                FOLDER : [string] Indicate the blogs folder name.
                
            returns:
                null
                
            example:
                text2html("./blogs/test.html", "Others")
        '''
        lines = read_text(FILENAME)
        [info, lines_body] = extract_info(lines)
        lines_h = translate_header(lines_body)
        lines_hp = translate_paragraph(lines_h)
        lines_hpbr = translate_break(lines_hp)
        lines_hpbri = translate_image(lines_hpbr)
        lines_html = link_html(info, lines_hpbri, FOLDER)
        save_html(lines_html, FILENAME[0:-3] + 'html')
        return