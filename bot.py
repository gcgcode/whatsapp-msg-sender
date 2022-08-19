
import requests
from bs4 import BeautifulSoup
 
def count_words(url, the_word):
    r = requests.get(url, allow_redirects=False)
    soup = BeautifulSoup(r.content, 'lxml')
    words = soup.find(text=lambda text: text and the_word in text)
    print(words)
    return len(words)
 
 
def main():
    url = 'https://python-forum.io/thread-8147.html'
    word = 'code'
    count = count_words(url, word)
    print('\nUrl: {}\ncontains {} occurrences of word: {}'.format(url, count, word))
    print('hey')
    print('funciona')
 
if __name__ == '__main__':
    main()
