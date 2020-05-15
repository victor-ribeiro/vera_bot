import twint as t
import os

class tweet_search(t.Config):

    def __init__(self, user_name_vera=None, terms=None, limit_vera=200, csv_bool=True,):
        super().__init__()
        self.user_name_vera=user_name_vera
        self.terms_vera=terms
        self.limit_vera=limit_vera
        self.csv_bool_vera=csv_bool,
    
    def get_google_terms(self, arq='query'):
        with open(arq) as query:
            terms_list = query.readlines()
            terms_list = [val.replace('\n', '') for val in terms_list]
            self.terms_vera = terms_list
            query.close()


    def add_term(self, *terms):
        self.terms_vera = self.terms_vera + list(terms)

    def search_by_terms(self):
        import twint as t
        from datetime import datetime
        import getpass
        import random

        try:
            self.get_google_terms()
        except:
            if os.path.isfile('query'):
                raise IOError('não foi possivel abrir o arquivo com os termos de busca')
            else:
                raise IOError("Arquivo 'query' não exite")

        self.Limit = self.limit_vera
        self.Search = random.sample(self.terms_vera, 2)
        self.Limit = self.limit_vera
        self.Store_csv = self.csv_bool_vera
        print('buscando por {}'.format(self.Search), end='\n\n')
        self.Output = 'data/{}_{}.csv'.format(getpass.getuser(), datetime.now().timestamp())
        t.run.Search(self)

if __name__ == "__main__":
    import time

    wait_time = 1
    while True:
        import time
        s = tweet_search()
        s.search_by_terms()
        print('busca por {} terminada'.format(s.Search), end='\t')
        print('aguardando {} segundo'.format(wait_time))
        time.sleep(wait_time)
        if wait_time < 129:
            wait_time += 1
        else:
            wait_time = 1