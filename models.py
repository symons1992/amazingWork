#-*- coding:utf -*-


#TODO : 考虑是否要保留这个models
class People:
    def __init__(self, id):
        self.id   = id
        self.homepage = ''
        self.name = ''
        self.age  = '' 
        self.contact = []  
        self.contact_ids = []
        self.rev_contact = []
        self.rev_contact_ids = []
        self.collection_article_title = []
        self.collection_article_url   = []
        self.group_joins = []

    def count_contact(self):
        return len(self.contact)

    def count_rev_contact(self):
        return len(self.contact)

