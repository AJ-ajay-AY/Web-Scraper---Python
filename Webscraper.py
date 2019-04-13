"""

Code to Scrape a website using Python : Made use of Beautiful soup and Requests Library
    Data Scraped and Info Gathered :
        External files referenced or Links
        Images
        Css elements
        Html elements
        JS elements
"""

import time
import requests
import bs4

def links():
    """
    Function to get list of links and print number of links
    """
    link_list= [link.get("href") for link in soup.find_all('a') if link.get("href")]
    print("Number of links are ", len(link_list))
    return link_list

def images():
    """
    Function to get list of images and print number of images
    """
    img_list = [i.get('src') for i in soup.find_all('img') if i.get('src')]
    print("Number of images are ", len(img_list))
    return img_list

def css_elements():
    """
    Function to get a list of css element usage and number of css elements
    """
    css_elements_list =[css.get("class") for css in soup.find_all('div') if css.get("class")]
    print("Number of css elements are ", len(css_elements_list))
    return css_elements_list

def js_file():
    """
    Function to get number of JS files
    """
    js_file_lst=[i.get('src')for i in soup.find_all('script') if i.get('src')]
    print("Number of java script files are", len(js_file_lst))

def html_elements():
    """
    Function to get a number of HTML elements
    """
    tag_open = soup.find_all('html')
    print("number of Html elements %d" % len(tag_open))

def file_writer(list1,listdes):

    myfile.write("\n\n\n\nBELOW ARE THE LIST OF " + listdes +'\n')
    for i in list1:
        myfile.write('\n'+str(i))


if __name__ == '__main__':
    strurl = input("Please enter URL of Desired Site :")
    start = time.time()
    res = requests.get(strurl)
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    end = time.time()
    lnklist = links()
    imglist = images()
    cslist = css_elements()
    js_file()
    html_elements()
    print("time taken to Parse ", end - start)

    #Creating custom file name to prevent overwrite
    filename = strurl[12:30]+'.txt'
    print('\n **** Please check ' + filename + ' for list of links,images and CSS elements ****')

    """
    File Handling section
    """
    myfile=open(filename, 'a+')
    myfile.write("THIS IS THE OUTPUT AFTER PARSING %s" % strurl)
    myfile.write('\nTIME TAKEN TO PARSE '+ str(end-start))
    file_writer(lnklist, ":  LINKS")
    file_writer(imglist, "   IMAGES")
    file_writer(cslist, ":  CSS ELEMENTS")
    myfile.close()




