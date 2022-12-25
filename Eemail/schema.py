
import graphene 
from graphene_django import*
from Eemail.graphapi.resolvers import resolve_Welcome,resolve_sendmail
from Eemail.graphapi.mutation import CreateMessageMutation

class Query(graphene.ObjectType):
    Welcome=graphene.String()
    def resolve_Welcome(self,info,**kwargs):
        return resolve_Welcome(self,info,**kwargs)

    sendmail=graphene.String()
    def  resolve_sendmail(self,info,**kwargs):
        return resolve_sendmail (self,info,**kwargs)   
class Mutation:
    compose=CreateMessageMutation.Field()
    # deletemessage=DeleteemailMutation.Field()

    
